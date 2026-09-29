# download_exposure.py — S4: COW colonial zip + OWID decolonization-era cross-check
import csv, hashlib, io, json, os, re, time, urllib.request, zipfile

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) aris4c-003-stage2/0.1 (local research)"}
EX = "data/raw/exposure"
os.makedirs(EX, exist_ok=True)

def fetch_bytes(tag, url, ext="bin"):
    path = os.path.join(EX, tag + "." + ext)
    if os.path.exists(path) and os.path.getsize(path) > 100:
        b = open(path, "rb").read()
        print(tag, "CACHED", len(b), "sha256=", hashlib.sha256(b).hexdigest()[:16])
        return b
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180) as r:
                b = r.read()
            open(path, "wb").write(b)
            print(tag, "200", len(b), "sha256=", hashlib.sha256(b).hexdigest()[:16], "final=", r.geturl()[:100])
            time.sleep(2)
            return b
        except Exception as e:
            print(tag, "attempt%d" % (i + 1), type(e).__name__, str(e)[:100])
            time.sleep(3 + 3 * i)
    return None

print("== COW Colonial/Dependency Contiguity v3.1 ==")
z = fetch_bytes("cow_colonial_contiguity_v310", "https://correlatesofwar.org/wp-content/uploads/ColonialContiguity310.zip")
if z:
    zf = zipfile.ZipFile(io.BytesIO(z))
    print("ZIP members:", zf.namelist())
    for name in zf.namelist():
        if name.lower().endswith((".csv", ".txt")):
            data = zf.read(name).decode("utf-8", "replace")
            open(os.path.join(EX, "cow_" + os.path.basename(name)), "w", encoding="utf-8").write(data)
            lines = [l for l in data.splitlines() if l.strip()]
            print("FILE", name, "lines=", len(lines))
            for l in lines[:6]:
                print("   ", l[:220])

print("== OWID: age of electoral democracy (decolonization-era cross-check) ==")
b = fetch_bytes("owid_age_of_electoral_democracy", "https://ourworldindata.org/grapher/age-of-electoral-democracy.csv", ext="csv")
if b is None:
    # fallback: fetch grapher page, find CSV download link
    h = None
    p = os.path.join(EX, "pages", "owid_grapher_age.html")
    if not (os.path.exists(p) and os.path.getsize(p) > 500):
        try:
            with urllib.request.urlopen(urllib.request.Request("https://ourworldindata.org/grapher/age-of-electoral-democracy", headers=UA), timeout=60) as r:
                h = r.read().decode("utf-8", errors="replace")
            open(p, "w", encoding="utf-8").write(h)
        except Exception as e:
            print("grapher page ERR", type(e).__name__, str(e)[:100])
    if h:
        for m in sorted(set(re.findall(r'href="([^"]*\.csv[^"]*)"', h)))[:10]:
            print("OWID_CSV_LINK:", m[:180])
print("DONE")
