import urllib.request

SOURCE_URLS = [
    "https://raw.githubusercontent.com/AVB2055/IPTV1/refs/heads/main/AVBTV.m3u8",
    "http://stream.mcquack.net/stream.mcquack.net.m3u",
    "https://raw.githubusercontent.com/Dimonovich/TV/refs/heads/Dimonovich/FREE/TV"
]

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

GROUP_RENAMES = {
    "Познавательные": "🔎‍Познавательные",
    "Развлекательные": "🤣Развлекательные",
    "Музыкальные": "🎶Музыкальные",
    "Спорт": "⛹🏿Спортивные",
    "Детские": "🧒Детские",
    "Кино": "🎦📺Фильмы 🔹 Сериалы"
}

# === ИСКЛЮЧЕНИЯ КАНАЛОВ ===
# Формат: ('название группы', 'название канала')
EXCLUDE_CHANNELS = [
    ('⛹🏿Спортивные', 'Eurosport 1'),
    ('⛹🏿Спортивные', 'Eurosport 2'),
    ('⛹🏿Спортивные', 'Setanta Sports UA'),
    ('⛹🏿Спортивные', 'Setanta Sports+'),
    ('⛹🏿Спортивные', 'Qazsport'),
    ('⛹🏿Спортивные', 'ОККО Спорт'),
    ('⛹🏿Спортивные', 'ОККО Футбол'),
    ('⛹🏿Спортивные', 'ОККО Прайм Спорт'),
    ('Internet42 LLC', 'ТНТ4'),
    ('Internet42 LLC', 'Театр'),
    ('Internet42 LLC', 'Телекафе'),
    ('Internet42 LLC', 'Cartoon Network'),
    ('Uplink (VPN)', 'Живи'),
    ('Turon Media (VPN)', 'Discovery Science'),
    ('Turon Media (VPN)', 'ТНТ Music'),
    ('Turon Media (VPN)', 'Globus Music'),
    ('Turon Media (VPN)', '1HD'),
    ('Rutube (VPN)', 'CGTN Русский'),  
    ('Rutube (VPN)', 'Плюс минус 16'),  
    ('Rutube (VPN)', 'РБК'),
    ('Rutube (VPN)', 'Илли ТВ'),
    ('Rutube (VPN)', 'ТОЛК'),
    ('Квант-Телеком (VPN 🇷🇺)', 'Big Planet'),
    ('Квант-Телеком (VPN 🇷🇺)', 'Моя планета'),
    ('Квант-Телеком (VPN 🇷🇺)', 'TV XXI'),
    ('Квант-Телеком (VPN 🇷🇺)', 'КИНОСЕРИЯ'),  
    ('Квант-Телеком (VPN 🇷🇺)', 'Индия'),  
    ('Квант-Телеком (VPN 🇷🇺)', 'МУЛЬТ'),  
    ('Квант-Телеком (VPN 🇷🇺)', 'Aiva')
]

# Исключения по ключевым словам (удаляют каналы ВЕЗДЕ)
EXCLUDE_KEYWORDS = [
    "Shop",
    "18+",
    "магазин",
    "test",
    "backup"
]

result = ["#EXTM3U"]
seen_urls = set()

for url in SOURCE_URLS:
    print(f"Обработка: {url}")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            text = response.read().decode('utf-8', errors='ignore')
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
            
            current_group = ""
            if 'group-title="' in clean:
                start = clean.find('group-title="') + len('group-title="')
                end = clean.find('"', start)
                current_group = clean[start:end]
                
            if current_group in GROUP_RENAMES:
                new_group = GROUP_RENAMES[current_group]
                current_block[0] = current_block[0].replace(f'group-title="{current_group}"', f'group-title="{new_group}"')
                current_group = new_group
                
        elif is_target:
            current_block.append(clean)
            if clean.startswith('http://') or clean.startswith('https://'):
                block_text = " ".join(current_block).lower()
                channel_name = current_block[0].split(',')[-1].strip()
                
                # Проверка 1: Ключевые слова
                if any(kw.lower() in block_text for kw in EXCLUDE_KEYWORDS):
                    is_target = False
                    continue
                
                # Проверка 2: Точечные исключения по группе
                if any(current_group == grp and channel_name == ch for grp, ch in EXCLUDE_CHANNELS):
                    is_target = False
                    continue
                
                # === Проверка 3: Дубликаты ссылок (С НОРМАЛИЗАЦИЕЙ HTTP/HTTPS) ===
                # Приводим ссылку к единому виду (https), чтобы http и https считались одним и тем же
                normalized_url = clean.replace('http://', 'https://')
                
                if normalized_url in seen_urls:
                    is_target = False
                    continue
                
                # Запоминаем нормализованную ссылку
                seen_urls.add(normalized_url)
                
                result.extend(current_block)
                is_target = False

with open('AVBTVfull.m3u', 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))

unique_count = len([line for line in result if line.startswith('#EXTINF')])
print(f"Готово! Добавлено уникальных каналов: {unique_count}")
