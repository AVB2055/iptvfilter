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
           
