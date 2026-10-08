import re, html
raw = open("lit/lu2023.xml", encoding="utf-8", errors="replace").read()
def clean(seg):
    seg = re.sub(r'<[^>]+>', ' ', seg)
    return html.unescape(re.sub(r'\s+', ' ', seg)).strip()
# region 189000-200000: m estimation (formula 6/7/8)
seg = clean(raw[189500:201000])
print(seg[:4000])
