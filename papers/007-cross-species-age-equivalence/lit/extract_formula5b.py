import re, html
raw = open("lit/lu2023.xml", encoding="utf-8", errors="replace").read()
def clean(seg):
    seg = re.sub(r'<[^>]+>', ' ', seg)
    return html.unescape(re.sub(r'\s+', ' ', seg)).strip()
# all log-linear positions + "universal clock 3" definitions in Methods
pos = [m.start() for m in re.finditer(r'log[–\- ]linear', raw, re.I)]
print("positions:", pos)
seen = set()
for p in pos:
    key = p // 3000
    if key in seen: continue
    seen.add(key)
    seg = clean(raw[max(0,p-1200):p+1500])
    print("=== pos", p, "===")
    print(seg[:1500])
    print()
