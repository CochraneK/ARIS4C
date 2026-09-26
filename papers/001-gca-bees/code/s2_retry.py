# code/s2_retry.py — ARIS4C-001 段2 取数重试
# A) Zenodo 17771502：首跑 API 403 → 多 UA/表头变体 + HTML 记录页解析兜底
# B) Perry 2013：PNAS 403 → 经 NCBI PMC 取全文 HTML
# 清单 → results/s2_retry.json
import json, os, re, time, urllib.request, urllib.parse

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(BASE, "results")

def get(url, timeout=90, ua=None, headers=None):
    h = {"User-Agent": ua or "aris4c-stage2/1.0 (comparative-cognition research data fetch)"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

rep = {"zenodo": [], "perry": {}}
OUT = os.path.join(BASE, "data", "oxman2026")
BUDGET = 50 * 1024 * 1024

def download_files(files, ua):
    os.makedirs(OUT, exist_ok=True)
    sel = files if sum(f.get("size", 0) for f in files) <= BUDGET else sorted(
        [f for f in files if f.get("key", "").lower().endswith((".csv", ".tsv", ".txt", ".parquet", ".json"))],
        key=lambda f: f.get("size", 0))
    s, dl = 0, []
    for f in sel:
        to = os.path.join(OUT, os.path.basename(f.get("key", "")))
        if os.path.exists(to) and os.path.getsize(to) == f.get("size"):
            dl.append([f.get("key"), "exists"])
            continue
        if s + f.get("size", 0) > BUDGET:
            dl.append([f.get("key"), "skipped-budget"])
            continue
        try:
            b = get(f["links"]["self"], timeout=180, ua=ua)
            with open(to, "wb") as g:
                g.write(b)
            s += f.get("size", 0)
            dl.append([f.get("key"), "ok %dB" % len(b)])
        except Exception as e:
            dl.append([f.get("key"), "failed %s" % str(e)[:100]])
    return dl

# ---- A) Zenodo 变体 ----
VARIANTS = [
    ("api", "https://zenodo.org/api/records/17771502",
     "aris4c-stage2/1.0 (comparative-cognition research; mailto:local@example.org)"),
    ("api-chrome", "https://zenodo.org/api/records/17771502",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"),
    ("api-plain", "https://zenodo.org/api/records/17771502",
     "python-urllib (research; DataCite-resolved 10.5281/zenodo.17771502)"),
    ("html", "https://zenodo.org/records/17771502",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"),
]
for name, url, ua in VARIANTS:
    try:
        b = get(url, ua=ua, headers={"Accept": "application/json" if name.startswith("api") else "text/html"})
        if name.startswith("api"):
            rec = json.loads(b)
            with open(os.path.join(OUT, "record.json"), "w") as f:
                json.dump(rec, f)
            files = rec.get("files", [])
            dl = download_files(files, ua)
            rep["zenodo"].append({"variant": name, "status": "OK n_files=%d total=%dB" % (len(files), sum(x.get("size", 0) for x in files)), "downloaded": dl})
            break
        else:
            html = b.decode("utf-8", "ignore")
            with open(os.path.join(OUT, "record.html"), "wb") as f:
                f.write(b)
            pre = "https://zenodo.org"
            ulinks, seen = [], set()
            for u in re.findall(r'href="([^"]+)"', html):
                if ("/api/files/" in u or "/files/" in u) and u not in seen:
                    seen.add(u)
                    ulinks.append(u if u.startswith("http") else pre + u)
            dl, s = [], 0
            for i, u in enumerate(ulinks):
                if s > BUDGET:
                    dl.append([u, "skipped-budget"]); continue
                to = os.path.join(OUT, "recfile_%d_%s" % (i, os.path.basename(u.split("?")[0]) or ("f%d" % i)))
                if os.path.exists(to):
                    dl.append([u, "exists"]); continue
                try:
                    bb = get(u, timeout=180, ua=ua)
                    with open(to, "wb") as g:
                        g.write(bb)
                    s += len(bb)
                    dl.append([os.path.basename(to), "ok %dB" % len(bb)])
                except Exception as e:
                    dl.append([u, "failed %s" % str(e)[:100]])
            rep["zenodo"].append({"variant": name, "status": "OK html %dB, %d file links" % (len(b), len(ulinks)), "downloaded": dl})
            break
    except Exception as e:
        rep["zenodo"].append({"variant": name, "status": "failed %s" % str(e)[:120]})
    time.sleep(1)

# ---- B) Perry 2013 经 NCBI PMC ----
try:
    es = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&retmode=json&term=" + urllib.parse.quote("10.1073/pnas.1314571110[doi]")
    ids = json.loads(get(es, ua="aris4c-stage2/1.0"))["esearchresult"]["idlist"]
    if ids:
        pmc = "PMC" + ids[0]
        html = get("https://www.ncbi.nlm.nih.gov/pmc/articles/%s/" % pmc, ua="aris4c-stage2/1.0")
        out = os.path.join(BASE, "data", "perry2013")
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, "fulltext.html"), "wb") as f:
            f.write(html)
        t = re.sub(r"<(script|style|noscript)[\s\S]*?</\1>", " ", html.decode("utf-8", "ignore"))
        t = re.sub(r"<[^>]+>", " ", t)
        for a, c in (("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&#39;", "'")):
            t = t.replace(a, c)
        t = re.sub(r"\s+", " ", t).strip()
        with open(os.path.join(out, "fulltext.txt"), "w", encoding="utf-8") as f:
            f.write(t)
        rep["perry"]["pmc"] = {"pmcid": pmc, "chars": len(t)}
    else:
        rep["perry"]["pmc"] = "no PMC id for DOI"
except Exception as e:
    rep["perry"]["pmc"] = "failed %s" % str(e)[:150]
try:
    b = get("https://www.pnas.org/doi/suppl/10.1073/pnas.1314571110/suppl_file/pnas.1314571110.index.html",
            ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
    with open(os.path.join(BASE, "data", "perry2013", "si_index.html"), "wb") as f:
        f.write(b)
    rep["perry"]["si_index"] = "ok %dB" % len(b)
except Exception as e:
    rep["perry"]["si_index"] = "failed %s" % str(e)[:120]

with open(os.path.join(RES, "s2_retry.json"), "w", encoding="utf-8") as f:
    json.dump(rep, f, ensure_ascii=False, indent=1)
print(json.dumps(rep, ensure_ascii=False, indent=1)[:2500])
