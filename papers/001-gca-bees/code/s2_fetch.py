# code/s2_fetch.py — ARIS4C-001 段2 取数（单一入口，各部分独立 try/except）
# 1) Oxman 2026 原始数据：Zenodo 10.5281/zenodo.17771502 → data/oxman2026/
# 2) 四篇 OA 全文 + SI：Finke 2023 (Springer) / Perry 2013 (PNAS) / Raine 2012 (PLoS ONE) / Evans 2017 (Sci Rep)
#    每篇另取 Crossref 元数据（标题/年/摘要）作降级出口；清单 → results/s2_fetch.json。
import json, os, re, hashlib, urllib.request, urllib.parse

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(BASE, "results")
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

def get(url, to=None, timeout=120, referer=None):
    h = dict(UA)
    if referer:
        h["Referer"] = referer
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout) as r:
        b = r.read()
    if to:
        with open(to, "wb") as f:
            f.write(b)
    return b

def sha256(p):
    hx = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            hx.update(c)
    return hx.hexdigest()

def html2text(b):
    t = b.decode("utf-8", "ignore")
    t = re.sub(r"<(script|style|noscript)[\s\S]*?</\1>", " ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    for a, c in (("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&#39;", "'")):
        t = t.replace(a, c)
    return re.sub(r"\s+", " ", t).strip()

def si_fetch(out, html, url, sipats, cap):
    """抓 SI/媒体文件链接并下载；返回 (链接列表, {序号: 状态})。"""
    pre = urllib.parse.urlsplit(url).scheme + "://" + urllib.parse.urlsplit(url).netloc
    si, rep = [], {}
    for u in re.findall(r'href="([^"]+)"', html.decode("utf-8", "ignore")):
        if u.startswith("#") or u in si or not any(re.search(p, u, re.I) for p in sipats):
            continue
        si.append(u if u.startswith("http") else pre + u)
    for i, u in enumerate(si[:cap]):
        fn = os.path.join(out, "si_%d_%s" % (i, os.path.basename(u.split("?")[0]) or ("f%d" % i)))
        if os.path.exists(fn):
            rep[i] = "exists"
            continue
        try:
            get(u, to=fn, referer=url)
            rep[i] = "ok %dB" % os.path.getsize(fn)
        except Exception as e:
            rep[i] = "failed %s" % str(e)[:120]
    return si, rep

rep = {}

# ---- 1) Oxman 2026 Zenodo 17771502 ----
try:
    out = os.path.join(BASE, "data", "oxman2026")
    os.makedirs(out, exist_ok=True)
    rec = json.loads(get("https://zenodo.org/api/records/17771502"))
    files = rec.get("files", [])
    tot = sum(f.get("size", 0) for f in files)
    BUDGET = 50 * 1024 * 1024
    if tot <= BUDGET:
        sel = files
    else:
        sel = sorted([f for f in files if f.get("key", "").lower().endswith((".csv", ".tsv", ".txt", ".parquet", ".json"))], key=lambda f: f.get("size", 0))
    mani = {"recid": rec.get("id"), "title": rec.get("title"), "doi": rec.get("doi"),
            "publication_date": rec.get("publication_date"), "n_files": len(files), "total_size": tot,
            "selection": "full(<=50MB)" if sel is files else "partial(>50MB): tabular files under 50MB budget"}
    s, dl = 0, []
    for f in sel:
        key = f.get("key", "")
        to = os.path.join(out, os.path.basename(key))
        if os.path.exists(to) and os.path.getsize(to) == f.get("size"):
            dl.append([key, "exists"])
            continue
        if s + f.get("size", 0) > BUDGET:
            dl.append([key, "skipped-budget"])
            continue
        try:
            get(f["links"]["self"], to=to)
            s += f.get("size", 0)
            dl.append([key, "ok sha256_ok=%s" % (sha256(to) == f.get("checksum", "").replace("sha256:", ""))])
        except Exception as e:
            dl.append([key, "failed %s" % str(e)[:120]])
    mani["downloaded"] = dl
    rep["zenodo"] = mani
except Exception as e:
    rep["zenodo"] = "FAILED %s" % str(e)[:200]

# ---- 2) OA 全文 + SI（四篇） ----
T = [("finke2023", "10.1007/s10071-022-01741-2", "https://link.springer.com/article/10.1007/s10071-022-01741-2", [r"(MediaObjects|supplementary|\.pdf)"], 8),
     ("perry2013", "10.1073/pnas.1314571110", "https://www.pnas.org/doi/10.1073/pnas.1314571110", [r"/suppl/", r"\.pdf"], 4),
     ("raine2012", "10.1371/journal.pone.0045096", "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0045096", [r"\.pdf", r"s1.?file"], 4),
     ("evans2017", "10.1038/s41598-017-00389-0", "https://www.nature.com/articles/s41598-017-00389-0", [r"\.pdf", r"mediaObjects"], 4)]
for key, doi, url, sipats, cap in T:
    try:
        out = os.path.join(BASE, "data", key)
        os.makedirs(out, exist_ok=True)
        pre = urllib.parse.urlsplit(url).scheme + "://" + urllib.parse.urlsplit(url).netloc
        e = {}
        try:
            cr = json.loads(get("https://api.crossref.org/works/" + doi))["message"]
            e["crossref"] = {"title": cr.get("title"), "year": ((cr.get("issued", {}).get("date-parts") or [[None]])[0][0]),
                             "abstract": re.sub(r"<[^>]+>", " ", cr.get("abstract", ""))[:1500]}
            with open(os.path.join(out, "crossref_meta.json"), "w", encoding="utf-8") as f:
                json.dump(e["crossref"], f, ensure_ascii=False, indent=1)
        except Exception as ex:
            e["crossref"] = "failed %s" % str(ex)[:120]
        try:
            html = get(url, to=os.path.join(out, "fulltext.html"))
            text = html2text(html)
            with open(os.path.join(out, "fulltext.txt"), "w", encoding="utf-8") as f:
                f.write(text)
            e["fulltext"] = "ok %d chars" % len(text)
            e["si"], e["si_dl"] = si_fetch(out, html, url, sipats, cap)
            for u in [x for x in e["si"] if x.split("?")[0].lower().endswith(".html")][:2]:
                try:
                    sub = get(u, referer=url).decode("utf-8", "ignore")
                    for j, u2 in enumerate(re.findall(r'href="([^"]+)"', sub)):
                        if not u2.lower().split("?")[0].endswith((".pdf", ".xlsx", ".csv", ".xls")):
                            continue
                        u2 = u2 if u2.startswith("http") else pre + u2
                        fn2 = os.path.join(out, "si_sub_%d_%s" % (j, os.path.basename(u2.split("?")[0])[:60] or ("f%d" % j)))
                        if os.path.exists(fn2):
                            continue
                        try:
                            get(u2, to=fn2, referer=u)
                            e.setdefault("si_sub", {})[os.path.basename(fn2)] = "ok %dB" % os.path.getsize(fn2)
                        except Exception as ex2:
                            e.setdefault("si_sub", {})[os.path.basename(fn2)] = "failed %s" % str(ex2)[:100]
                except Exception:
                    pass
        except Exception as ex:
            e["fulltext"] = "BLOCKED %s" % str(ex)[:150]
        rep[key] = e
    except Exception as e:
        rep[key] = "FAILED %s" % str(e)[:150]

with open(os.path.join(RES, "s2_fetch.json"), "w", encoding="utf-8") as f:
    json.dump(rep, f, ensure_ascii=False, indent=1)
out = {}
for k, v in rep.items():
    out[k] = v if isinstance(v, str) else {kk: (str(vv)[:160]) for kk, vv in v.items() if kk != "si"}
print(json.dumps(out, ensure_ascii=False, indent=1)[:2800])
