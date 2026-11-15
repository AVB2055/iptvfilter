import urllib.request

CONFIGS = [
    {
        "output_file": "AVBTVbig.m3u",
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
            "Познавательные": "🔎‍Познавательные+Реклама", 
            "Развлекательные": "🤣Развлекательные+Реклама",
            "Музыкальные": "🎶Музыкальные+Реклама", 
            "Спорт": "⛹🏿Спортивные+Реклама",
            "Детские": "🧒Детские+Реклама", 
            "Кино": "🎦📺Фильмы 🔹 Сериалы+Реклама"
        },
        "exclude_channels": [
            ('🤣Развлекательные+Реклама', 'Інтер+'), ('🤣Развлекательные+Реклама', 'Новий канал'),
            ('🤣Развлекательные+Реклама', 'ICTV 2'), ('🤣Развлекательные+Реклама', 'Світ навиворіт+'),
            ('🤣Развлекательные+Реклама', 'СТБ'), ('🤣Развлекательные+Реклама', '2+2'),
            ('🤣Развлекательные+Реклама', 'FilmUADrama'), ('🤣Развлекательные+Реклама', 'Суспільне Культура'),
            ('🤣Развлекательные+Реклама', 'Опер за викликом+'), ('🤣Развлекательные+Реклама', 'К1'),
            ('🤣Развлекательные+Реклама', 'Міледі ТВ'), ('🤣Развлекательные+Реклама', 'ТЕТ'),
            ('🤣Развлекательные+Реклама', 'Панянка-селянка+'), ('🤣Развлекательные+Реклама', 'ОЦЕ'),
            ('🤣Развлекательные+Реклама', 'НТН'), ('🤣Развлекательные+Реклама', 'Сімейні мелодрами+'),
            ('🤣Развлекательные+Реклама', '36.6'), ('🤣Развлекательные+Реклама', 'Прованс ТВ'),
            ('🤣Развлекательные+Реклама', 'ЖВЛ+'), ('🤣Развлекательные+Реклама', 'Дім'),
            ('🤣Развлекательные+Реклама', 'Загублений світ+'), ('🤣Развлекательные+Реклама', 'Bolt'),
            ('🤣Развлекательные+Реклама', 'Караван ТВ'), ('🤣Развлекательные+Реклама', 'ПлюсПлюс'),
            ('🤣Развлекательные+Реклама', 'Бiгудi'), ('🤣Развлекательные+Реклама', 'Машина Часу'),
            ('🤣Развлекательные+Реклама', 'Знаєм 24'), ('🤣Развлекательные+Реклама', 'Наталі ТВ'),
            ('🤣Развлекательные+Реклама', 'Вікторина'), ('🤣Развлекательные+Реклама', 'Невигадані Історії'),
            ('🤣Развлекательные+Реклама', 'Про Київ'), ('🤣Развлекательные+Реклама', 'Ми - Україна'),
            ('🔎‍Познавательные+Реклама', 'Світ+'), ('🔎‍Познавательные+Реклама', 'ЗооСвіт'),
            ('🔎‍Познавательные+Реклама', 'Quiz TV'), ('🔎‍Познавательные+Реклама', 'Терра'),
            ('🔎‍Познавательные+Реклама', 'Наука'), ('🔎‍Познавательные+Реклама', 'Перший Автомобільний'),
            ('🔎‍Познавательные+Реклама', 'Фронт'), ('🔎‍Познавательные+Реклама', 'Мега'),
            ('🔎‍Познавательные+Реклама', '6 Соток'), ('🔎‍Познавательные+Реклама', 'Закон'),
            ('🔎‍Познавательные+Реклама', 'Масон'), ('🔎‍Познавательные+Реклама', 'Трофей'),
            ('🔎‍Познавательные+Реклама', 'Нано ТВ'),
            ('⛹🏿Спортивные+Реклама', 'Eurosport 1'), ('⛹🏿Спортивные+Реклама', 'Eurosport 2'),
            ('⛹🏿Спортивные+Реклама', 'Setanta Sports UA'), ('⛹🏿Спортивные+Реклама', 'Setanta Sports+'),
            ('⛹🏿Спортивные+Реклама', 'Qazsport'), ('⛹🏿Спортивные+Реклама', 'Sport 1 Baltic'),
            ('⛹🏿Спортивные+Реклама', 'Sport 1'), ('⛹🏿Спортивные+Реклама', 'Sport 2'),
            ('⛹🏿Спортивные+Реклама', 'Sport 3'), ('⛹🏿Спортивные+Реклама', 'Sport 4'),
            ('⛹🏿Спортивные+Реклама', 'Sport 5'), ('⛹🏿Спортивные+Реклама', 'Dynamo Kyiv TV'),
            ('⛹🏿Спортивные+Реклама', 'Trace Sports'), ('⛹🏿Спортивные+Реклама', 'Суспільне Спорт'),
            ('⛹🏿Спортивные+Реклама', 'DiVi Sport'), ('⛹🏿Спортивные+Реклама', 'Maincast sport'),
            ('⛹🏿Спортивные+Реклама', 'Maincast кіберспорт'), ('⛹🏿Спортивные+Реклама', 'TV3 Sport LT'),
            ('⛹🏿Спортивные+Реклама', 'Equalympic'), ('⛹🏿Спортивные+Реклама', 'ОККО Спорт'),
            ('⛹🏿Спортивные+Реклама', 'ОККО Футбол'), ('⛹🏿Спортивные+Реклама', 'ОККО Прайм Спорт'),
            ('🧒Детские+Реклама', 'JimJam'), ('🧒Детские+Реклама', 'Піксель'),
            ('🎶Музыкальные+Реклама', 'М1'), ('🎶Музыкальные+Реклама', 'М2'),
            ('🎶Музыкальные+Реклама', 'Europa Plus TV'), ('🎶Музыкальные+Реклама', 'Музвар'),
            ('Internet42 LLC', 'ТНТ4'), ('Internet42 LLC', 'Театр'), ('Internet42 LLC', 'Телекафе'),
            ('Internet42 LLC', 'Cartoon Network'), ('Uplink (VPN)', 'Живи'),
            ('Turon Media (VPN)', 'Discovery Science'), ('Turon Media (VPN)', 'ТНТ Music'),
            ('Turon Media (VPN)', 'Globus Music'), ('Turon Media (VPN)', '1HD'),
            ('Rutube (VPN)', 'CGTN Русский'), ('Rutube (VPN)', 'Плюс минус 16'),
            ('Rutube (VPN)', 'РБК'), ('Rutube (VPN)', 'Илли ТВ'), ('Rutube (VPN)', 'ТОЛК'),
            ('Квант-Телеком (VPN 🇷🇺)', 'Big Planet'), ('Квант-Телеком (VPN 🇷🇺)', 'Моя планета'),
            ('Квант-Телеком (VPN 🇷🇺)', 'TV XXI'), ('Квант-Телеком (VPN 🇷🇺)', 'КИНОСЕРИЯ'),
            ('Квант-Телеком (VPN 🇷🇺)', 'Индия'), ('Квант-Телеком (VPN 🇷🇺)', 'МУЛЬТ'),
            ('Квант-Телеком (VPN 🇷🇺)', 'Aiva')
        ],
        "exclude_url_keywords": [
            "stream8.cinerama.uz",
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
            'Кинофильмы'
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
            # Исправленные названия групп, которые реально есть в AVBVideo.m3u8
            'group-title="Девяностые"',
            'group-title="Следствие вели"',
            'group-title="Тайны нашего кино"',
            'group-title="Советские артисты"',
            'Девяностые',
            'Следствие вели',
            'Тайны нашего кино',
            'Советские артисты'
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
            # Исправленные названия групп, которые реально есть в AVBCartoon.m3u8
            'group-title="🐺🐰Ну Погоди!"',
            'group-title="👶Наши Мультфильмы"',
            '🐺🐰Ну Погоди!',
            '👶Наши Мультфильмы'
        ],
        "group_renames": {},
        "exclude_channels": [],
        "exclude_url_keywords": [],
        "exclude_keywords": []
    }
]

for config in CONFIGS:
    print(f"\n{'='*50}")
    print(f"🚀 Начинаем сборку: {config['output_file']}")
    print(f"{'='*50}")
    
    result = ["#EXTM3U"]
    seen_urls = set()
    
    for url in config["sources"]:
        print(f"  📥 Обработка источника: {url}")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req) as response:
                text = response.read().decode('utf-8', errors='ignore')
