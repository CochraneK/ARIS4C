# code/s2_inspect.py — ARIS4C-001 段2 数据检视（v2：xlsx 支持，openpyxl 失败时纯 stdlib XML 兜底）
# (1) data/{oxman2026,finke2023,perry2013,raine2012,evans2017} 全部表格文件画像 → results/s2_data_profile.json
# (2) SI 文件类型判别（magic）；无扩展名 PDF 改名；pypdf/PyPDF2 可用则抽 PDF 文本 → <name>.txt
# (3) 全文统计上下文窗扫描 → results/s2_stat_windows.txt
# stdout 仅摘要（<=40 行），大内容写盘。
import json, os, re, glob, importlib.util, zipfile
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(BASE, "results")
KEYS = ("oxman2026", "finke2023", "perry2013", "raine2012", "evans2017")
prof = {}

def _prof_df(df):
    cols = {}
    for c in df.columns:
        s = df[c]
        info = {"n_missing": int(s.isna().sum()), "n_unique": int(s.nunique(dropna=True))}
        if pd.api.types.is_numeric_dtype(s):
            info.update(dtype=str(s.dtype), min=float(s.min()), max=float(s.max()), mean=round(float(s.mean()), 4))
        else:
            vc = s.value_counts(dropna=False)
            info.update(dtype="cat", top={str(k): int(v) for k, v in vc.head(10).items()})
        cols[str(c)] = info
    return {"shape": [int(df.shape[0]), int(df.shape[1])], "columns": cols,
            "head5": json.loads(df.head(5).to_json(orient="records"))}

def _xlsx_stdlib(p):
    from xml.etree import ElementTree as ET
    ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    z = zipfile.ZipFile(p)
    try:
        ss = [(t.text or "") for t in ET.fromstring(z.read("xl/sharedStrings.xml")).iter(ns + "t")]
    except Exception:
        ss = []
    sheets = {}
    for n in z.namelist():
        if not re.match(r"xl/worksheets/sheet\d+\.xml$", n):
            continue
        rows = []
        for row in ET.fromstring(z.read(n)).iter(ns + "row"):
            vals = []
            for c in row.iter(ns + "c"):
                v = c.find(ns + "v")
                if v is None:
                    vals.append(None)
                    continue
                if c.get("t") == "s":
                    vals.append(ss[int(v.text)])
                else:
                    try:
                        vals.append(float(v.text))
                    except Exception:
                        vals.append(v.text)
            rows.append(vals)
        if rows:
            sheets[os.path.basename(n)] = _prof_df(pd.DataFrame(rows[1:], columns=[str(x) for x in rows[0]]))
    return sheets

def profile_table(p):
    ext = os.path.splitext(p)[1].lower()
    if ext == ".xlsx":
        try:
            return {sh: _prof_df(df) for sh, df in pd.read_excel(p, sheet_name=None).items()}
        except Exception:
            sh = _xlsx_stdlib(p)
            if not sh:
                raise RuntimeError("xlsx: no sheets parsed")
            return sh
    if ext in (".csv", ".tsv"):
        return _prof_df(pd.read_csv(p, sep=("\t" if ext == ".tsv" else ",")))
    return _prof_df(pd.read_parquet(p))

def extract_pdf(p, entry):
    if not (importlib.util.find_spec("pypdf") or importlib.util.find_spec("PyPDF2")):
        entry["pdf"].append(os.path.basename(p) + " [no pypdf lib; text not extracted]")
        return
    try:
        try:
            from pypdf import PdfReader
        except ImportError:
            from PyPDF2 import PdfReader
        txt = "\n".join((pg.extract_text() or "") for pg in PdfReader(p).pages)
        with open(p[:-4] + ".txt", "w", encoding="utf-8") as f:
            f.write(txt)
        entry["pdf"].append(os.path.basename(p) + " -> text %d chars" % len(txt))
    except Exception as e:
        entry["pdf"].append(os.path.basename(p) + " [pdf extract failed %s]" % str(e)[:80])

for key in KEYS:
    d = os.path.join(BASE, "data", key)
    entry = {"tabular": {}, "other": [], "pdf": []}
    for p in sorted(glob.glob(os.path.join(d, "*"))):
        if not os.path.isfile(p):
            continue
        name = os.path.basename(p)
        ext = os.path.splitext(p)[1].lower()
        try:
            if ext in (".csv", ".tsv", ".parquet", ".xlsx"):
                entry["tabular"][name] = profile_table(p)
            elif ext == ".pdf":
                entry["pdf"].append(name)
                extract_pdf(p, entry)
            elif ext in (".txt",):
                entry["other"].append({"name": name, "chars": os.path.getsize(p)})
            else:
                magic = open(p, "rb").read(8)
                if magic[:4] == b"%PDF":
                    p2 = p + ".pdf"
                    os.rename(p, p2)
                    entry["pdf"].append(name + " (renamed)")
                    extract_pdf(p2, entry)
                elif ext in (".html", ".json"):
                    entry["other"].append({"name": name, "bytes": os.path.getsize(p)})
                else:
                    entry["other"].append({"name": name, "bytes": os.path.getsize(p), "magic": magic.hex()})
        except Exception as e:
            entry["tabular"][name] = {"read_error": str(e)[:150], "bytes": os.path.getsize(p)}
    prof[key] = entry

with open(os.path.join(RES, "s2_data_profile.json"), "w", encoding="utf-8") as f:
    json.dump(prof, f, ensure_ascii=False, indent=1)

# ---- 全文统计上下文窗扫描 ----
wins = []
def scan(path, tag, specs):
    if not os.path.exists(path):
        return
    t = re.sub(r"\s+", " ", open(path, encoding="utf-8").read())
    seen = set()
    for pat, w, cap in specs:
        for m in re.finditer(pat, t, re.I):
            if len(wins) >= 70:
                return
            a, b = max(0, m.start() - w), min(len(t), m.end() + w)
            seg = t[a:b]
            if seg in seen:
                continue
            seen.add(seg)
            wins.append("### [%s] %s\n%s" % (tag, pat, seg))

scan(os.path.join(BASE, "data", "finke2023", "fulltext.txt"), "finke",
     [(r"correlat", 200, 14), (r"\br\s*=\s*-?\d", 200, 10), (r"Table\s*\d", 420, 3), (r"consisten", 160, 4)])
for p in sorted(glob.glob(os.path.join(BASE, "data", "finke2023", "si_*.txt"))):
    scan(p, "finke-si", [(r"correlat", 200, 6), (r"\br\s*=\s*-?\d", 160, 6), (r"Table\s*\d", 300, 3)])
scan(os.path.join(BASE, "data", "perry2013", "fulltext.txt"), "perry",
     [(r"opt-out", 180, 8), (r"abstain", 160, 4), (r"difficult", 160, 4)])
scan(os.path.join(BASE, "data", "raine2012", "fulltext.txt"), "raine",
     [(r"correlat", 200, 6), (r"\br\s*=\s*-?\d", 180, 6)])
scan(os.path.join(BASE, "data", "evans2017", "fulltext.txt"), "evans",
     [(r"correlat", 200, 6), (r"\br\s*=\s*-?\d", 180, 6)])
with open(os.path.join(RES, "s2_stat_windows.txt"), "w", encoding="utf-8") as f:
    f.write("\n\n".join(wins) + "\n")

# ---- stdout 摘要 ----
lines = []
for key, e in prof.items():
    for name, t in e["tabular"].items():
        if "shape" in t:
            cs = ", ".join("%s(%s,n=%d)" % (c, v.get("dtype", "?"), v.get("n_unique", -1)) for c, v in list(t["columns"].items())[:18])
            lines.append("%s/%s rows=%d cols=%d | %s" % (key, name, t["shape"][0], t["shape"][1], cs[:300]))
        elif isinstance(t, dict) and any(isinstance(v, dict) and "shape" in v for v in t.values()):
            for sh, tt in t.items():
                cs = ", ".join("%s(%s,n=%d)" % (c, v.get("dtype", "?"), v.get("n_unique", -1)) for c, v in list(tt["columns"].items())[:14])
                lines.append("%s/%s[Sheet:%s] rows=%d cols=%d | %s" % (key, name, sh, tt["shape"][0], tt["shape"][1], cs[:280]))
        else:
            lines.append("%s/%s ERR %s" % (key, name, str(t.get("read_error", ""))[:80]))
    for x in e.get("pdf", []):
        lines.append("%s/PDF %s" % (key, x))
    for o in e.get("other", [])[:8]:
        lines.append("%s/FILE %s %s" % (key, o.get("name", "?"), o.get("chars", o.get("bytes", "?"))))
lines.append("windows=%d" % len(wins))
print("\n".join(lines[:40]))
