CONFIGS = [
    {
        "output_file": "AVBtv.m3u",
        "sources": [
            "https://raw.githubusercontent.com/AVB2055/IPTV1/refs/heads/main/AVBTV.m3u8",
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
        },
        "exclude_channels": [
            ('Internet42 LLC', 'ТНТ4'), ('Internet42 LLC', 'Театр'), ('Internet42 LLC', 'Телекафе'),
            ('Internet42 LLC', 'Cartoon Network'), ('Uplink (VPN)', 'Живи'), 
            ('Uplink (VPN)', 'Новое телевидение'),
            ('Turon Media (VPN)', 'Discovery Science'), ('Turon Media (VPN)', 'ТНТ Music'),
            ('Turon Media (VPN)', 'Globus Music'), ('Turon Media (VPN)', '1HD'),
            ('Turon Media (VPN)', 'Fox News'), ('Квант-Телеком (VPN 🇷🇺)', 'Авто Плюс'),
            ('Turon Media (VPN)', 'Первый канал HD'), ('Rutube (VPN)', 'CGTN Русский'), ('Rutube (VPN)', 'Плюс минус 16'),
            ('Rutube (VPN)', 'РБК'), ('Rutube (VPN)', 'Илли ТВ'), ('Rutube (VPN)', 'ТОЛК'),
            ('Квант-Телеком (VPN 🇷🇺)', 'Big Planet'), ('Квант-Телеком (VPN 🇷🇺)', 'Моя планета'),
            ('Квант-Телеком (VPN 🇷🇺)', 'TV XXI'), ('Квант-Телеком (VPN 🇷🇺)', 'КИНОСЕРИЯ'),
            ('Квант-Телеком (VPN 🇷🇺)', 'Индия'), ('Квант-Телеком (VPN 🇷🇺)', 'МУЛЬТ'), 
            ('Квант-Телеком (VPN 🇷🇺)', 'Матч! Арена'), ('Квант-Телеком (VPN 🇷🇺)', 'MMA-TV.COM'),
            ('Квант-Телеком (VPN 🇷🇺)', 'KHL'), ('Квант-Телеком (VPN 🇷🇺)', 'Aiva')
        ],
        "exclude_url_keywords": [
            #"stream8.cinerama.uz",
            "31.210.208.171",
            "185.46.16.239"
        ],
        "exclude_keywords": ["Shop", "18+", "магазин", "test", "backup"]
    },
    {
        "output_file": "AVBfilms.m3u",
        "sources": [
            "https://raw.githubusercontent.com/AVB2055/IPTV1/refs/heads/main/AVBCinema.m3u8",
            "https://raw.githubusercontent.com/Dimonovich/TV/refs/heads/Dimonovich/FREE/FILMS.m3u"
        ],
        "target_groups": [
            'group-title="Новинки кино"',
            'group-title="Films_4k"',
            'group-title="Фильмы"',
            'group-title="Кино"',
            'group-title="Кинофильмы"'
        ],
        "group_renames": {},
        "exclude_channels": [
            ('Новинки кино', '🔺 INFO 🔺Посмотри!!!'),
            ('Фильмы', 'Властелин колец: Две крепости (2002)'),
            ('Фильмы', 'Ганга Дин (1939)'),
            ('Фильмы', 'Гарри Поттер и Дары Смерти. Часть 2 (2011)'),
            ('Фильмы', 'Джек Райан: Призрачная война (2026)'),
            ('Фильмы', 'Луна 44 (1990)'),
            ('Фильмы', 'Матрица: Перезагрузка (2003)'),
            ('Фильмы', 'Про Красную шапочку (1977)')
        ],
        "exclude_url_keywords": [],
        "exclude_keywords": ["Shop", "18+", "магазин", "test", "backup"]
    },
    {
        "output_file": "AVBvideo.m3u",
        "sources": [
            "https://raw.githubusercontent.com/AVB2055/IPTV1/refs/heads/main/AVBVideo.m3u8",
            "https://raw.githubusercontent.com/Dimonovich/TV/refs/heads/Dimonovich/FREE/FILMS.m3u"
        ],
        "target_groups": [
            'group-title="Девяностые"',
            'group-title="Следствие вели"',
            'group-title="Тайны нашего кино"',
            'group-title="Советские артисты"',
            'group-title="Жизнь на нашей планете (2023)"'
        ],
        "group_renames": {},
        "exclude_channels": [],
        "exclude_url_keywords": [],
        "exclude_keywords": []
    },
    {
        "output_file": "AVBcartoon.m3u",
        "sources": [
            "https://raw.githubusercontent.com/AVB2055/IPTV1/refs/heads/main/AVBCartoon.m3u8",
            "https://raw.githubusercontent.com/Dimonovich/TV/refs/heads/Dimonovich/FREE/FILMS.m3u"
        ],
        "target_groups": [
            'group-title="🐺🐰Ну Погоди!"',
            'group-title="Наши Мультфильмы"',
            'group-title="👶Наши Мультфильмы"',
            'group-title="Мультфильмы"'
        ],
        "group_renames": {
            "Наши Мультфильмы": "👶Наши Мультфильмы"
        },
        "exclude_groups": [
            "ТОМ И ДЖЕРРИ"  # <-- Теперь мы исключаем всю группу целиком
        ],
        "exclude_channels": [],
        "exclude_url_keywords": [],
        "exclude_keywords": [] # <-- Ключевые слова убрали, чтобы не зацепить лишнее
    }
]
