import urllib.request
from config import CONFIGS  # <-- ДОБАВЬТЕ ЭТУ СТРОКУ

# ==========================================================
# ШАГ 1: Строгая проверка конфига перед запуском
# ==========================================================
print("🔍 Проверка конфигурации...")
for config in CONFIGS:
    for item in config.get("exclude_channels", []):
        if not isinstance(item, (list, tuple)) or len(item) != 2:
            raise ValueError(f"❌ Ошибка в '{config['output_file']}': элемент должен быть кортежем из 2 элементов. Получено: {item}")
print("✅ Конфигурация валидна, ошибок формата нет.\n")
print("🔍 Проверка конфигурации...")
# ==========================================================
# ШАГ 1: Строгая проверка конфига перед запуском
# ==========================================================
print("🔍 Проверка конфигурации...")
for config in CONFIGS:
    for item in config.get("exclude_channels", []):
        if not isinstance(item, (list, tuple)) or len(item) != 2:
            raise ValueError(f"❌ Ошибка в '{config['output_file']}': элемент должен быть кортежем из 2 элементов. Получено: {item}")
print("✅ Конфигурация валидна, ошибок формата нет.\n")


# ==========================================================
# ШАГ 2: Основной цикл обработки
# ==========================================================
for config in CONFIGS:
    print(f"\n{'='*50}")
    print(f"🚀 Начинаем сборку: {config['output_file']}")
    print(f"{'='*50}")
    
    result = ["#EXTM3U"]
    seen_urls = set()
    excluded_count = 0  # Счетчик исключений
    
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
                        excluded_count += 1
                        is_target = False
                        continue
                    
                    if any(kw.lower() in clean for kw in config.get("exclude_url_keywords", [])):
                        excluded_count += 1
                        is_target = False
                        continue
                    
                    if any(current_group == grp and channel_name == ch for grp, ch in config.get("exclude_channels", [])):
                        excluded_count += 1
                        is_target = False
                        continue
                    
                    normalized_url = clean.replace('http://', 'https://')
                    if normalized_url in seen_urls:
                        excluded_count += 1
                        is_target = False
                        continue
                    
                    seen_urls.add(normalized_url)
                    result.extend(current_block)
                    is_target = False
    
    with open(config["output_file"], 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))
    
    unique_count = len([line for line in result if line.startswith('#EXTINF')])
    print(f"  ✅ Готово! В файл {config['output_file']} добавлено уникальных каналов: {unique_count}")
    print(f"  🗑️ Отфильтровано (исключено или дубликатов): {excluded_count}")

print("\n🎉 Все плейлисты успешно обновлены!")
