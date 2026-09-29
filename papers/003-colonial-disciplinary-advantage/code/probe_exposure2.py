# probe_exposure2.py — locate COW colonial dataset + verify OWID colonialism page content
import re, os, time, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) aris4c-003-stage2/0.1 (local research)"}
os.makedirs("data/raw/exposure/pages", exist_ok=True)

def fetch(tag, url):
    path = "data/raw/exposure/pages/" + tag + ".html"
    if os.path.exists(path) and os.path.getsize(path) > 500:
        html = open(path, encoding="utf-8", errors="replace").read()
        print(tag, "CACHED", len(html))
        return html
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                html = r.read().decode("utf-8", errors="replace")
            open(path, "w", encoding="utf-8").write(html)
            print(tag, "200", len(html), "final_url=", r.geturl()[:120])
            time.sleep(2)
            return html
        except Exception as e:
            print(tag, "attempt%d" % (i + 1), type(e).__name__, str(e)[:100])
            time.sleep(3 + 3 * i)
    return ""

print("== OWID cached page: mention of colonial ==")
h = open("data/raw/exposure/pages/owid_colon.html", encoding="utf-8", errors="replace").read()
hits = [m.start() for m in re.finditer(r"colon", h, re.I)]
print("colonial_mentions:", len(hits))
for m in hits[:8]:
    print("  ...", re.sub(r"\s+", " ", h[max(0, m - 120):m + 120])[:240])
title = re.search(r"<title>(.*?)</title>", h, re.S)
print("TITLE:", title.group(1).strip()[:120] if title else None)

print("== COW data-sets page ==")
h2 = fetch("cow_datasets", "https://correlatesofwar.org/data-sets/")
for m in sorted(set(re.findall(r'href="([^"]*colonial[^"]*)"', h2, re.I))):
    print("COLONIAL_LINK:", m[:160])
for m in sorted(set(re.findall(r'href="([^"]*(?:cow|dataset|download|files)[^"]*)"', h2, re.I)))[:60]:
    print("LINK:", m[:150])
