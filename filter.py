import urllib.request

# === НАСТРОЙКИ ДЛЯ КАЖДОГО ПЛЕЙЛИСТА ===
CONFIGS = [
    # ---------------------------------------------------------
    # ФАЙЛ 1: Основной полный плейлист
    # ---------------------------------------------------------
    {
        "output_file": "AVBTVfull.m3u",
        "sources": [
            "https://raw.githubusercontent.com/AVB2055/IPTV1/refs/heads/main/AVBTV.m3u8",
            "http://stream.mcquack.net/stream.mcquack.net.m3u",
            "https://raw.githubusercontent.com/Dimonovich/TV/refs/heads/Dimonovich/FREE/TV"
        ],
        "target_groups": [
            'group-title="🇷🇺Федеральные"', 'group-title="📻Радио"', 'group-title="👁Информационные"',
            'group-title="🔎‍Познавательные"', 'group-title="🤣Развлекательные"', 'group-title="🎶Музыкальные"',
            'group-title="⛹🏿Спортивные"', 'group-title="🧒Детские"', 'group-title="🎦📺Фильмы 🔹 Сериалы"',
            'group-title="🎬Kinowalk TV  Not 24-7"', 'group-title="Познавательные"', 'group-title="Развлекательные"',
            'group-title="Музыкальные"', 'group-title="Спорт"', 'group-title="Детские"', 'group-title="Кино"',
            'group-title="Rutube (VPN)"', 'group-title="Квант-Телеком (VPN 🇷🇺)"', 'group-title="Turon Media (VPN)"',
            'group-title="Uplink (VPN)"', 'group-title="Оргтехсервис (VPN)"', 'group-title="Internet42 LLC"'
        ],
        "group_renames": {
            "Познавательные": "🔎‍Познавательные", "Развлекательные": "🤣Развлекательные",
            "Музыкальные": "🎶Музыкальные", "Спорт": "⛹🏿Спортивные",
            "Детские": "🧒Детские", "Кино": "🎦📺Фильмы 🔹 Сериалы"
        },
        "exclude_channels": [
            ('⛹🏿Спортивные', 'Eurosport 1'), ('⛹🏿Спортивные', 'Eurosport 2'), ('⛹🏿Спортивные', 'Setanta Sports UA'),
            ('⛹🏿Спортивные', 'Setanta Sports+'), ('⛹🏿Спортивные', 'Qazsport'), ('⛹🏿Спортивные', 'ОККО Спорт'),
            ('⛹🏿Спортивные', 'ОККО Футбол'), ('⛹🏿Спортивные', 'ОККО Прайм Спорт'), ('Internet42 LLC', 'ТНТ4'),
            ('Internet42 LLC', 'Театр'), ('Internet42 LLC', 'Телекафе'), ('Internet42 LLC', 'Cartoon Network'),
            ('Uplink (VPN)', 'Живи'), ('Turon Media (VPN)', 'Discovery Science'), ('Turon Media (VPN)', 'ТНТ Music'),
            ('Turon Media (VPN)', 'Globus Music'), ('Turon Media (VPN)', '1HD'), ('Rutube (VPN)', 'CGTN Русский'),  
            ('Rutube (VPN)', 'Плюс минус 16'), ('Rutube (VPN)', 'РБК'), ('Rutube (VPN)', 'Илли ТВ'), ('Rutube (VPN)', 'ТОЛК'),
            ('Квант-Телеком (VPN 🇷🇺)', 'Big Planet'), ('Квант-Телеком (VPN 🇷🇺)', 'Моя планета'), ('Квант-Телеком (VPN 🇷🇺)', 'TV XXI'),
            ('Квант-Телеком (VPN 🇷🇺)', 'КИНОСЕРИЯ'), ('Квант-Телеком (VPN 🇷🇺)', 'Индия'), ('Квант-Телеком (VPN 🇷🇺)', 'МУЛЬТ'), ('Квант-Телеком (VPN 🇷🇺)', 'Aiva')
        ],
        "exclude_keywords": ["Shop", "18+", "магазин", "test", "backup"]
    },
    # ---------------------------------------------------------
    # ФАЙЛ 2: Объединенный кино-плейлист (ВАШ + DIMONOVICH)
    # ---------------------------------------------------------
    {
        "output_file": "AVBCinema.m3u8",
        "sources": [
            "https://raw.githubusercontent.com/AVB2055/IPTV1/refs/heads/main/AVBCinema.m3u8",
            "https://raw.githubusercontent.com/Dimonovich/TV/refs/heads/Dimonovich/FREE/FILMS.m3u"
        ],
        "target_groups": [
            'group-title="Новинки кино"',
            'group-title="Films_4k"',
            'group-title="Фильмы"',
            'group-title="Кино"',
            'Кинофильмы'  # <-- Ключевое добавление: поддерживает формат #EXTGRP:Кинофильмы
        ],
        "group_renames": {}, 
        "exclude_channels": [], 
        "exclude_keywords": ["Shop", "18+", "магазин", "test", "backup"]
    }
]

# === ОСНОВНАЯ ЛОГИКА (поддерживает оба формата групп) ===
for config in CONFIGS:
    print(f"\n{'='*50}")
    print(f"🚀 Начинаем сборку: {config['output_file']}")
    print(f"{'='*50}")
    
    result = ["#EXTM3U"]
    seen_urls = set()
    
    for url in config["sources"]:
