import urllib.request

CONFIGS = [
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
            "Познавательные": "🔎‍Познавательные", 
            "Развлекательные": "🤣Развлекательные",
            "Музыкальные": "🎶Музыкальные", 
            "Спорт": "⛹🏿Спортивные",
            "Детские": "🧒Детские", 
            "Кино": "🎦📺Фильмы 🔹 Сериалы"
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
    {
        "output_file": "AVBCinemaFull.m3u8",
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
        "exclude_keywords": ["Shop", "18+", "магазин", "test", "backup"]
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
                is_target = any(group in clean for group in config["target_groups"])
                current_group = ""
                if 'group-title="' in clean:
                    start = clean.find('group-title="') + len('group-title="')
                    end = clean.find('"', start)
                    current_group = clean[start:end]
                
                # 🔧 ВОССТАНОВЛЕННЫЙ БЛОК: Переименование группы в #EXTINF
                if current_group in config["group_renames"]:
                    new_group = config["group_renames"][current_group]
                    current_block[0] = current_block[0].replace(f'group-title="{current_group}"', f'group-title="{new_group}"')
                    current_group = new_group
            
            elif clean.startswith('#EXTGRP:'):
                current_group = clean.replace('#EXTGRP:', '').strip()
                is_target = any(current_group in target or f'group-title="{current_group}"' in target for target in config["target_groups"])
                
                # 🔧 ДОПОЛНИТЕЛЬНО: Переименование группы в #EXTGRP (если источник использует этот формат)
                if current_group in config["group_renames"]:
                    new_group = config["group_renames"][current_group]
                    clean = f'#EXTGRP:{new_group}'
                    current_group = new_group
                
                current_block.append(clean)
                continue
            
            elif is_target:
                current_block.append(clean)
                if clean.startswith('http://') or clean.startswith('https://'):
                    block_text = " ".join(current_block).lower()
                    channel_name = current_block[0].split(',')[-1].strip()
                    
                    if any(kw.lower() in block_text for kw in config["exclude_keywords"]):
                        is_target = False
                        continue
                    
                    if any(current_group == grp and channel_name == ch for grp, ch in config["exclude_channels"]):
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
