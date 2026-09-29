# probe_exposure_urls.py — discover COW + OWID colonial dataset file URLs (page-level only, no data yet)
import re, urllib.request, urllib.parse as up, os, time

UA = {"User-Agent": "aris4c-003-stage2/0.1 (local research)"}
os.makedirs("data/raw/exposure/pages", exist_ok=True)

def fetch(tag, url):
    path = "data/raw/exposure/pages/" + tag + ".html"
    if os.path.exists(path) and os.path.getsize(path) > 500:
        html = open(path, encoding="utf-8", errors="replace").read()
        print(tag, "CACHED", len(html))
        return html
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
            html = r.read().decode("utf-8", errors="replace")
        open(path, "w", encoding="utf-8").write(html)
        print(tag, "200", len(html))
    except Exception as e:
        print(tag, "ERR", type(e).__name__, str(e)[:120])
        return ""
    time.sleep(2)
    return html

def links(tag, html, pat):
    for m in sorted(set(re.findall(pat, html, re.I))):
        print(tag, "LINK:", m[:160])

print("== COW main page ==")
h = fetch("cow_main", "https://cow.ei.columbia.edu/cow")
links("cow", h, r'href="([^"]*(?:colonial|colstate|files)[^"]*)"')
print("== OWID colonialism ==")
h2 = fetch("owid_colon", "https://ourworldindata.org/colonialism")
links("owid", h2, r'(?:href|src)="([^"]*(?:colon|dataset|grapher|data)[^"]*)"')
