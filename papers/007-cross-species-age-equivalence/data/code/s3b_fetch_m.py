import datetime, json, pathlib, re, urllib.parse, urllib.request

BASE = pathlib.Path(r"D:\Software\ARIS4C-local\007-cross-species-age-equivalence")
API = "https://en.wikipedia.org/w/api.php"
UA = "ARIS4C-007-research/1.0 (cross-species age-equivalence project; contact: local)"
TITLES = ["Domestic cat", "Rabbit", "Dog", "Horse", "Pig", "Chimpanzee", "Meerkat", "House mouse", "List of countries by life expectancy"]

def progress(msg):
    with (BASE / "stage3b_progress.md").open("a", encoding="utf-8") as f:
        f.write(msg + "\n")

params = urllib.parse.urlencode({"action": "query", "format": "json", "prop": "revisions",
                                 "rvprop": "content", "redirects": "1", "titles": "|".join(TITLES)})
req = urllib.request.Request(API + "?" + params, headers={"User-Agent": UA})
with urllib.request.urlopen(req, timeout=60) as r:
    data = json.loads(r.read().decode("utf-8"))
pages = data.get("query", {}).get("pages", {})
out = {}
lines = []
for pid, pg in pages.items():
    title = pg.get("title", "?")
    content = pg.get("revisions", [{}])[0].get("content", "")
    head = content[:6000]
    m = re.search(r"(?im)^\s*\|\s*lifespan\s*=\s*(.+?)\s*$", head)
    raw = m.group(1).strip() if m else ""
    if not raw:
        m2 = re.search(r"(?i)lifespan[=\s:\-]{1,3}([^\n|]{1,90})", content)
        raw = ("fallback:" + m2.group(1).strip()) if m2 else "NOT FOUND"
    nums = re.findall(r"\d+(?:\.\d+)?", raw)
    rec = {"title": title, "raw": raw[:160], "nums": nums[:8],
           "url": "https://en.wikipedia.org/wiki/" + title.replace(" ", "_"),
           "accessed": datetime.date.today().isoformat()}
    out[title] = rec
    lines.append("%s | %s" % (title, raw[:75]))
LE_TITLE = "List of countries by life expectancy"
if LE_TITLE in out:
    pg_le = [pg for pg in pages.values() if pg.get("title") == LE_TITLE]
    c_le = pg_le[0]["revisions"][0]["content"] if pg_le else ""
    us = None
    for mm in re.finditer(r"United States.{0,160}?(\d{2}\.?\d*)", c_le, re.S):
        v = float(mm.group(1))
        if 55 < v < 95:
            us = mm.group(1)
            break
    out[LE_TITLE]["us_match"] = us
    lines.append("LE-US: %s" % us)
with (BASE / "data" / "raw" / "s3b_m_raw.json").open("w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("OK pages=%d" % len(out))
for ln in lines:
    print(ln)
progress("T4 m fetch (wikipedia API) OK pages=%d" % len(out))
