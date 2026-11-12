import urllib.request

# СПИСОК исходных плейлистов (можно добавлять сколько угодно)
SOURCE_URLS = [
    "https://raw.githubusercontent.com/Dimonovich/TV/refs/heads/Dimonovich/FREE/TV",
    "https://raw.githubusercontent.com/другой-автор/другой-репо/main/playlist.m3u",
    "https://example.com/еще-один-плейлист.m3u"
    # Добавляйте новые URL-ы сюда, каждый в кавычках и через запятую
]

# Группы, которые нужно оставить (работают для ВСЕХ источников)
TARGET_GROUPS = [
    'group-title="Квант-Телеком (VPN 🇷🇺)"',
    'group-title="Turon Media (VPN)"',
    'group-title="Uplink (VPN)"',
    'group-title="Оргтехсервис (VPN)"',
    'group-title="Internet42 LLC"'
]

# Черный список: слова для исключения каналов (работает для ВСЕХ источников)
EXCLUDE_KEYWORDS = [
    "Наше новое кино",
    "Shop",
    "18+"
]

# Начинаем с заголовка M3U
result = ["#EXTM3U"]

# Обрабатываем каждый исходный файл по очереди
for url in SOURCE_URLS:
    print(f"Обработка: {url}")
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            text = response.read().decode('utf-8')
    except Exception as e:
        print(f"Ошибка скачивания {url}: {e}")
        continue  # Пропускаем этот URL и переходим к следующему
    
    lines = text.split('\n')
    current_block = []
    is_target = False
    
    for line in lines:
        clean = line.strip()
        if not clean:
            continue
            
        if clean.startswith('#EXTINF'):
            current_block = [clean]
            is_target = any(group in clean for group in TARGET_GROUPS)
        elif is_target:
            current_block.append(clean)
            if clean.startswith('http://') or clean.startswith('https://'):
                block_text = " ".join(current_block).lower()
                exclude_keywords_lower = [kw.lower() for kw in EXCLUDE_KEYWORDS]
                
                if not any(kw in block_text for kw in exclude_keywords_lower):
                    result.extend(current_block)
                
                is_target = False

# Сохраняем объединенный результат
with open('iptv.m3u', 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))

print(f"Готово! Добавлено каналов: {len([line for line in result if line.startswith('#EXTINF')])}")
