# probe_exposure3.py — fetch COW colonial-dependency-contiguity page, extract dataset file links
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

h = fetch("cow_colonial", "https://correlatesofwar.org/data-sets/colonial-dependency-contiguity/")
print("== links (csv/zip/xls/download/data) ==")
for m in sorted(set(re.findall(r'href="([^"]+\.(?:csv|zip|xlsx?|txt|dta)[^"]*)"', h, re.I))):
    print("FILE:", m)
for m in sorted(set(re.findall(r'href="([^"]*(?:download|files?/|wp-content/uploads)[^"]*)"', h, re.I)))[:40]:
    print("OTHER:", m[:160])
print("== body text (colonial description) ==")
txt = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S)
txt = re.sub(r"<[^>]+>", " ", txt)
txt = re.sub(r"\s+", " ", txt)
i = txt.lower().find("colonial")
print(txt[max(0, i - 100):i + 1500])
