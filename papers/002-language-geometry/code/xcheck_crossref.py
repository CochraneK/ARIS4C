# xcheck_crossref.py — 驱动器接管（第10次·接力2）2026-09-26 22:0x
# 目的：(1) 打印本地数据版本元数据（钉版溯源）(2) Crossref 补核 4 条描述/方法文献
#       (3) 打印 6 分析表 + glottolog 表头（供独立重算脚本使用）
# 输出：results/lit_takeover2_check.txt + stdout（截断 6000 字符）
import json, csv, urllib.request, urllib.parse, os

BASE = r"D:\Software\ARIS4C-local\002-language-geometry"
UA = {"User-Agent": "ARIS4C-002-stage1-takeover/1.0 (driver lit recheck; mailto:sandbox@localhost)"}
out = []

def local_json(rel, keys):
    p = os.path.join(BASE, rel)
    try:
        with open(p, encoding="utf-8") as f:
            d = json.load(f)
        info = {k: d[k] for k in keys if k in d}
        extra = {k: v for k, v in d.items() if k not in keys and isinstance(v, (str, int, float))}
        s = "; ".join(f"{k}={v}" for k, v in list(info.items()) + list(extra.items())[:6])
        out.append(f"[LOCAL] {rel}: {s}")
        return d
    except Exception as e:
        out.append(f"[LOCAL] {rel}: ERR {type(e).__name__} {str(e)[:60]}")
        return None

def csv_head(rel):
    p = os.path.join(BASE, rel)
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            head = next(csv.reader(f))
        out.append(f"[CSVHEAD] {rel}: ncols={len(head)} first14={head[:14]}")
    except Exception as e:
        out.append(f"[CSVHEAD] {rel}: ERR {type(e).__name__} {str(e)[:60]}")

def crf(tag, params):
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=20) as resp:
            d = json.load(resp)
        items = d.get("message", {}).get("items", [])
        out.append(f"[CRF {tag}] got {len(items)}")
        for it in items[:3]:
            t = (it.get("title") or ["?"])[0][:88]
            a = ";".join(x.get("family", "") for x in (it.get("author") or [])[:3])
            y = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
            ct = it.get("container-title") or ["?"]
            v = ct[0][:46] if ct else "?"
            out.append(f"  {y} | {a} | {t} | {v} | doi={it.get('DOI','?')}")
    except Exception as e:
        out.append(f"[CRF {tag}] FAIL {type(e).__name__}: {str(e)[:70]}")

# 1) 本地版本元数据
try:
    with open(os.path.join(BASE, r"data\raw\pins.json"), encoding="utf-8") as f:
        out.append("[LOCAL] data/raw/pins.json: " + f.read().strip()[:280])
except Exception as e:
    out.append(f"[LOCAL] pins.json ERR {e}")
gl = local_json(r"data\raw\glottolog\cldf-metadata.json", ["Title", "Name", "Version", "Date", "URL"])
local_json(r"data\raw\wals\metadata.json", ["Title", "Name", "Version", "Date", "URL"])
local_json(r"data\raw\crossling\StructureDataset-metadata.json", ["Title", "Name", "Version", "Date"])

# 2) 表头
for rel in [r"data\raw\crossling\statisticalTLI_full_densified_small.csv",
            r"data\raw\crossling\statisticalTLI_full_densified_large.csv",
            r"data\raw\crossling\logicalTLI_full_densified_small.csv",
            r"data\raw\crossling\statisticalGBI_densified.csv",
            r"data\raw\crossling\logicalGBI_densified.csv",
            r"data\raw\wals\values.csv",
            r"data\raw\glottolog\languages.csv"]:
    csv_head(rel)

# 3) Crossref 补核（UA 头必需）
crf("gower-rossman-1969", {"query.bibliographic": "Gower Rossman seriation and abundance", "rows": 3})
crf("wals-book", {"query.bibliographic": "Haspelmath Dryer Comrie World Atlas of Language Structures", "rows": 3})
gl_title = (gl or {}).get("Title") or (gl or {}).get("Name") or "Glottolog Hammarstrom Forkel Haspelmath"
crf("glottolog", {"query.bibliographic": str(gl_title), "rows": 3})
crf("crossling-dataset", {"query.bibliographic": "crossling typological language inventory dataset", "rows": 3})

text = "\n".join(out)
with open(os.path.join(BASE, r"results\lit_takeover2_check.txt"), "w", encoding="utf-8") as f:
    f.write(text + "\n")
print(text[:6000])
