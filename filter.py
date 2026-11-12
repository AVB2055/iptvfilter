import urllib.request

SOURCE_URL = "https://raw.githubusercontent.com/Dimonovich/TV/refs/heads/Dimonovich/FREE/TV"

TARGET_GROUPS = [
    'group-title="Квант-Телеком (VPN 🇷🇺)"',
    'group-title="Turon Media (VPN)"',
    'group-title="Uplink (VPN)"',
    'group-title="Оргтехсервис (VPN)"',
    'group-title="Internet42 LLC"'
]

EXCLUDE_KEYWORDS = [
    "Наше новое кино",
    "Shop",
    "18+"
]

req = urllib.request.Request(SOURCE_URL, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        text = response.read().decode('utf-8')
except Exception as e:
    text = ""

lines = text.split('\n')
result = ["#EXTM3U"]
current_block = []
is_target = False

for line in lines:
    clean = line.strip()
    if not clean:
        continue
    if clean.startswith('#EXTINF'):
        current_block = [clean]
        is_target = any(group in clean for group in TARGET_GROUPS)
    elif is_target:
        current_block.append(clean)
        if clean.startswith('http://') or clean.startswith('https://'):
            block_text = " ".join(current_block).lower()
            exclude_keywords_lower = [kw.lower() for kw in EXCLUDE_KEYWORDS]
            if not any(kw in block_text for kw in exclude_keywords_lower):
                result.extend(current_block)
            is_target = False

with open('iptv.m3u', 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))
