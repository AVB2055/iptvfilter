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
            'group-title="ТОМ И ДЖЕРРИ"',
            'group-title="Наши Мультфильмы"',
            'group-title="🐺🐰Ну Погоди!"',
            'group-title="👶Наши Мультфильмы"',
            'Мультфильмы'
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
        
        # ВАЖНО: Блок try-except должен быть именно таким, с правильными отступами
        try:
            with urllib.request.urlopen(req) as response:
                text = response.read().decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"  ❌ Ошибка скачивания {url}: {e}")
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
                current_group = ""
                
                if 'group-title="' in clean:
                    start = clean.find('group-title="') + len('group-title="')
                    end = clean.find('"', start)
                    current_group = clean[start:end]
                
                is_target = any(group in clean for group in config["target_groups"])
                if current_group and any(current_group in target for target in config["target_groups"]):
                    is_target = True
                
                if current_group in config["group_renames"]:
                    new_group = config["group_renames"][current_group]
                    current_block[0] = current_block[0].replace(f'group-title="{current_group}"', f'group-title="{new_group}"')
                    current_group = new_group
            
            elif clean.startswith('#EXTGRP:'):
                group_name = clean.replace('#EXTGRP:', '').strip()
                
                if group_name in config["group_renames"]:
                    group_name = config["group_renames"][group_name]
                
                if any(group_name in target or f'group-title="{group_name}"' in target for target in config["target_groups"]):
                    is_target = True
                
                current_group = group_name
                
                if len(current_block) > 0 and ',' in current_block[0]:
                    tag, name = current_block[0].split(',', 1)
                    tag = tag.replace('#EXTINF:0', '#EXTINF:-1').replace('#EXTINF:1', '#EXTINF:-1')
                    current_block[0] = f'{tag} group-title="{group_name}",{name}'
                
                continue
            
            elif is_target:
                current_block.append(clean)
                if clean.startswith('http://') or clean.startswith('https://'):
                    block_text = " ".join(current_block).lower()
                    channel_name = current_block[0].split(',')[-1].strip()
                    
                    if any(kw.lower() in block_text for kw in config.get("exclude_keywords", [])):
                        is_target = False
                        continue
                    
                    if any(kw.lower() in clean for kw in config.get("exclude_url_keywords", [])):
                        is_target = False
                        continue
                    
                    if any(current_group == grp and channel_name == ch for grp, ch in config.get("exclude_channels", [])):
                        is_target = False
                        continue
                    
                    normalized_url = clean.replace('http://', 'https://')
                    if normalized_url in seen_urls:
                        is_target = False
                        continue
                    
                    seen_urls.add(normalized_url)
                    result.extend(current_block)
                    is_target = False
    
    with open(config["output_file"], 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))
    
    unique_count = len([line for line in result if line.startswith('#EXTINF')])
    print(f"  ✅ Готово! В файл {config['output_file']} добавлено уникальных каналов: {unique_count}")

print("\n🎉 Все плейлисты успешно обновлены!")
