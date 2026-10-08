import re, json, os, sys, time, tarfile, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from surnames import SURNAMES
UA = {"User-Agent": "aris4c006/1.0 (mailto:aris4c-006@polite.example)"}
os.makedirs("data/chinenames_pkg", exist_ok=True)
def get(url, bin_=False):
    last = None
    for d in (0, 30, 60, 120, 240):
        if d: time.sleep(d)
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=90) as r:
                b = r.read()
                return b if bin_ else b.decode("utf-8", "replace")
        except Exception as e:
            last = e
    raise RuntimeError("GET fail " + url + " " + str(last))
page = get("https://cran.r-project.org/web/packages/ChineseNames/index.html")
vm = re.search(r"Version:\s*</td>\s*<td[^>]*>\s*([\d.]+)", page) or re.search(r"Version[:\s]+([\d.]+)", page)
links = re.findall(r'href="([^"]*ChineseNames[^"]*\.tar\.gz)"', page)
print("PKG_VERSION", vm.group(1) if vm else "?")
print("TARBALL_LINKS", links[:3])
tu = None
if vm:
    tu = "https://cran.r-project.org/src/contrib/ChineseNames_%s.tar.gz" % vm.group(1)
if not tu:
    for u in links:
        if "Archive" not in u:
            tu = u if u.startswith("http") else "https://cran.r-project.org" + u
            break
if not tu:
    tu = "https://cran.r-project.org/src/contrib/ChineseNames_1.0.tar.gz"
print("TARBALL_URL", tu)
blob = get(tu, bin_=True)
open("data/chinenames_pkg.tar.gz", "wb").write(blob)
print("TARBALL_BYTES", len(blob))
tf = tarfile.open("data/chinenames_pkg.tar.gz")
names = tf.getnames()
print("FILE_COUNT", len(names))
print("FILELIST", " ; ".join(n.split("/")[-1] for n in names[:30]))
tf.extractall("data/chinenames_pkg")
descf = [n for n in names if n.endswith("DESCRIPTION")]
if descf:
    d = open("data/chinenames_pkg/" + descf[0], encoding="utf-8", errors="replace").read()
    for line in d.splitlines()[:12]:
        print("DESC>", line[:100])
datafiles = [n for n in names if re.search(r"\.(csv|tsv|txt|json|jsonl|csv\.gz|tibble)$", n, re.I)]
print("DATAFILES", datafiles[:10])
def head(f, n=6):
    p = "data/chinenames_pkg/" + f
    try:
        with open(p, encoding="utf-8", errors="replace") as fh:
            return [fh.readline().rstrip()[:90] for _ in range(n)]
    except Exception as e:
        return ["<unreadable %s>" % str(e)[:60]]
if datafiles:
    for f in datafiles[:3]:
        print("HEAD", f)
        for line in head(f):
            print("   ", line)
    # try to parse surname freq + pinyin from first parseable file
    parsed = False
    for f in datafiles[:4]:
        p = "data/chinenames_pkg/" + f
        if not f.lower().endswith((".csv", ".tsv", ".txt")):
            continue
        lines = [l.rstrip("\n") for l in open(p, encoding="utf-8", errors="replace") if l.strip()]
        if len(lines) < 5:
            continue
        sep = "\t" if "\t" in lines[0] else ","
        hdr = [h.strip().lower() for h in lines[0].split(sep)]
        def col(*cands):
            for c in cands:
                for i, h in enumerate(hdr):
                    if c in h:
                        return i
            return None
        ic = col("count", "freq", "frequency", "weight", "prop", "n")
        iname = col("name", "surname", "姓")
        ipiny = col("pinyin", "roman", "拼音", "py")
        rows = []
        for l in lines[1:]:
            parts = l.split(sep)
            if ic is None or len(parts) <= ic:
                continue
            try:
                c = float(re.sub(r"[^0-9.]", "", parts[ic]) or 0)
            except Exception:
                continue
            nm = parts[iname].strip() if iname is not None and iname < len(parts) else ""
            py = parts[ipiny].strip().lower() if ipiny is not None and ipiny < len(parts) else ""
            if c > 0:
                rows.append((nm, py, c))
        if len(rows) < 20:
            continue
        total = sum(r[2] for r in rows)
        dist = {}
        nknown = 0
        for nm, py, c in rows:
            if not py and nm:
                py = SURNAMES.get(nm, "") or SURNAMES.get(nm[:2], "")
            if py:
                nknown += 1
                dist[py[0].upper()] = dist.get(py[0].upper(), 0.0) + c
            else:
                dist["?"] = dist.get("?", 0.0) + c
        if total > 0 and nknown / len(rows) > 0.5:
            print("FREQ_FILE", f, "ROWS", len(rows), "TOTAL", round(total), "PINYIN_KNOWN_RATE", round(known_rate := nknown / len(rows), 3))
            s = " ".join("%s=%.4f" % (L, dist[L] / total) for L in sorted(dist) if L != "?" and dist[L] / total > 0.001)
            print("DIST ", s[:300])
            if "?" in dist:
                print("DIST ? = %.4f" % (dist["?"] / total))
            json.dump({"file": f, "rows": len(rows), "total": total,
                       "pinyin_known_rate": round(nknown / len(rows), 3),
                       "initial_dist": {L: round(v / total, 6) for L, v in sorted(dist.items())}},
                      open("data/chinenames_dist.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            parsed = True
            break
    if not parsed:
        print("PARSE-FAIL no parseable freq file; structure reported above")
else:
    rdas = [n for n in names if n.endswith((".rda", ".rds"))]
    print("RDA_ONLY", rdas[:8])
    print("NEED-R or pip pyreadr to parse binary RDA (not attempted in-stage)")
print("CHECK-DONE")
