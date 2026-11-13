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

EXCLUDE_KEYWORDS = ["Shop", "18+", "магазин"]
EXCLUDE_SPECIFIC = ["Тестовый канал"]
EXCLUDE_BY_GROUP = [('Turon Media (VPN)', 'Первый канал HD')]

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
                # ИСПРАВЛЕННАЯ СТРОКА - добавлены закрывающая кавычка и скобка
                current_block[0] = current_block[0].replace(f'group-title="{current_group}"', f'group-title="{new_group}"')
                current_group = new_group
                
        elif is_target:
            current_block.append(clean)
            if clean.startswith('http://') or clean.startswith('https://'):
                block_text = " ".join(current_block).lower()
                
                if any(kw.lower() in block_text for kw in EXCLUDE_KEYWORDS):
                    is_target = False
                    continue
                
                channel_name = current_block[0].split(',')[-1].strip()
                if channel_name.lower() in [name.lower() for name in EXCLUDE_SPECIFIC]:
                    is_target = False
                    continue
                
                if any(current_group == grp and channel_name.lower() == ch.lower() for grp, ch in EXCLUDE_BY_GROUP):
                    is_target = False
                    continue
                
                if clean in seen_urls:
                    is_target = False
                    continue
                
                seen_urls.add(clean)
                result.extend(current_block)
                is_target = False

with open('iptv.m3u', 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))

unique_count = len([line for line in result if line.startswith('#EXTINF')])
print(f"Готово! Добавлено уникальных каналов: {unique_count}")
