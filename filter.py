import urllib.request

# СПИСОК исходных плейлистов
SOURCE_URLS = [
    "https://raw.githubusercontent.com/AVB2055/IPTV1/refs/heads/main/AVBTV.m3u8",
    "http://stream.mcquack.net/stream.mcquack.net.m3u",
    "https://raw.githubusercontent.com/Dimonovich/TV/refs/heads/Dimonovich/FREE/TV"
]

# Группы, которые нужно оставить (оставляем и старые, и новые названия для надежности)
TARGET_GROUPS = [
    'group-title="🇷🇺Федеральные"',
    'group-title="📻Радио"',
    'group-title="👁Информационные"',
    'group-title="🔎‍Познавательные"',
    'group-title="🤣Развлекательные"',
    'group-title="🎶Музыкальные"',
    'group-title="⛹🏿Спортивные"',
    'group-title="🧒Детские"',
    'group-title="🎦📺Фильмы 🔹 Сериалы"',
    'group-title="🎬Kinowalk TV  Not 24-7"',
    'group-title="Познавательные"',
    'group-title="Развлекательные"',
    'group-title="Музыкальные"',
    'group-title="Спорт"',
    'group-title="Детские"',
    'group-title="Кино"',
    'group-title="Rutube (VPN)"',
    'group-title="Квант-Телеком (VPN 🇷🇺)"',
    'group-title="Turon Media (VPN)"',
    'group-title="Uplink (VPN)"',
    'group-title="Оргтехсервис (VPN)"',
    'group-title="Internet42 LLC"'
]

# СЛОВАРЬ ПЕРЕИМЕНОВАНИЯ ГРУПП
# Формат: 'Старое название': 'Новое название с эмодзи'
GROUP_RENAMES = {
    "Познавательные": "🔎‍Познавательные",
    "Развлекательные": "🤣Развлекательные",
    "Музыкальные": "🎶Музыкальные",
    "Спорт": "⛹🏿Спортивные",
    "Детские": "🧒Детские",
    "Кино": "🎦📺Фильмы 🔹 Сериалы"
}

# 1. Глобальные исключения по ключевым словам
EXCLUDE_KEYWORDS = [
    "Shop",
    "18+",
    "магазин"
]

# 2. Точечные исключения по названию
EXCLUDE_SPECIFIC = [
    "Тестовый канал"
]

# 3. ИСКЛЮЧЕНИЯ ПО ГРУППАМ
EXCLUDE_BY_GROUP = [
    ('Turon Media (VPN)', 'Первый канал HD')
]

result = ["#EXTM3U"]

for url in SOURCE_URLS:
    print(f"Обработка: {url}")
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            text = response.read().decode('utf-8')
    except Exception as e:
        print(f"Ошибка скачивания {url}: {e}")
        continue
    
    lines = text.split('\n')
    current_block = []
    current_group = ""
    is_target = False
    
    for line in lines:
        clean = line.strip()
        if not clean:
            continue
            
        if clean.startswith('#EXTINF'):
            current_block = [clean]
            is_target = any(group in clean for group in TARGET_GROUPS)
            
            # Запоминаем название группы текущего канала
            current_group = ""
            if 'group-title="' in clean:
                start = clean.find('group-title="') + len('group-title="')
                end = clean.find('"', start)
                current_group = clean[start:end]
                
            # === НОВАЯ ЛОГИКА: Переименование группы на лету ===
            if current_group in GROUP_RENAMES:
                new_group_name = GROUP_RENAMES[current_group]
                # Заменяем старое название группы на новое прямо в строке #EXTINF
                current_block[0] = current_block[0].replace(f'group-title="{current_group}"', f'group-title="{new_group_name}"')
                # Обновляем переменную, чтобы дальнейшие проверки использовали новое имя
                current_group = new_group_name
            # ====================================================
                
        elif is_target:
            current_block.append(clean)
            if clean.startswith('http://') or clean.startswith('https://'):
                block_text = " ".join(current_block).lower()
                
                # Проверка 1: глобальные ключевые слова
                exclude_keywords_lower = [kw.lower() for kw in EXCLUDE_KEYWORDS]
                if any(kw in block_text for kw in exclude_keywords_lower):
                    is_target = False
                    continue
                
                # Проверка 2: глобальные точные названия
                channel_name = current_block[0].split(',')[-1].strip()
                exclude_specific_lower = [name.lower() for name in EXCLUDE_SPECIFIC]
                if channel_name.lower() in exclude_specific_lower:
                    is_target = False
                    continue
                
                # Проверка 3: точечные исключения по группе
                should_exclude = False
                for group_name, channel_to_exclude in EXCLUDE_BY_GROUP:
                    if current_group == group_name and channel_name.lower() == channel_to_exclude.lower():
                        should_exclude = True
                        break
                
                if should_exclude:
                    is_target = False
                    continue
                
                # Если все проверки пройдены — добавляем канал (уже с переименованной группой)
                result.extend(current_block)
                is_target = False

with open('iptv.m3u', 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))

print(f"Готово! Добавлено каналов: {len([line for line in result if line.startswith('#EXTINF')])}")
