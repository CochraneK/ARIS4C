# xcheck_profile.py — 驱动器接管（第10次·接力2）2026-09-26 22:1x
# 目的：独立重算 profile.json / holdout_stats.txt 关键数字（双跑一致性），
#       并补 1 次 Crossref 查询（Gower & Rossman 1969 精确题名）。
# 独立实现：不复用 profile_data*.py 代码；约定差异逐项标注。
import json, os, re
import pandas as pd

BASE = r"D:\Software\ARIS4C-local\002-language-geometry"
R = os.path.join(BASE, "results")
out = []

def p(s=""):
    out.append(str(s))

# ---------- 0) 探针 ----------
gl = pd.read_csv(os.path.join(BASE, r"data\raw\glottolog\languages.csv"), dtype=str, keep_default_na=False)
p("[PROBE] glottolog cols: " + ",".join(gl.columns.tolist()[:12]))
p("[PROBE] glottolog rows: " + str(len(gl)))
p("[PROBE] sample rows (ID,Name,Glottocode,Family_ID):")
for _, r in gl.head(4).iterrows():
    p(f"   {r['ID']} | {r['Name'][:30]} | {r['Glottocode']} | {r['Family_ID']}")
fam_pat = re.compile(r"^[a-z]{4}\d{4}$")
fid_ok = gl["Family_ID"].str.match(fam_pat).mean()
p(f"[PROBE] Family_ID glottocode-pattern rate: {fid_ok:.3f}")

t0 = pd.read_csv(os.path.join(BASE, r"data\raw\crossling\statisticalTLI_full_densified_small.csv"),
                 dtype=str, keep_default_na=False, nrows=6)
p("[PROBE] TLI_stat_small first col name: " + repr(t0.columns[0]))
p("[PROBE] TLI_stat_small first col values: " + repr(t0.iloc[:5, 0].tolist()))

# ---------- 1) 语系映射 ----------
id2glot = dict(zip(gl["ID"], gl["Glottocode"]))
def top_fam(fid, glot_own):
    if fam_pat.match(fid or ""):
        return fid
    g = id2glot.get(fid)
    return g if g else None

gl_map = {}
for _, r in gl.iterrows():
    gl_map[r["Glottocode"]] = top_fam(r["Family_ID"], r["Glottocode"])

# ---------- 2) profile.json 引用 ----------
prof = json.load(open(os.path.join(R, "profile.json"), encoding="utf-8"))
L = prof["layers"]

def cmp(metric, mine, ref, layer):
    tag = "MATCH" if mine == ref else "DIFF"
    p(f"[{layer}] {metric}: mine={mine} ref={ref} [{tag}]")
    return mine == ref

# ---------- 3) crossling 层 ----------
LAYS = {
    "TLI_stat_small": r"data\raw\crossling\statisticalTLI_full_densified_small.csv",
    "TLI_stat_large": r"data\raw\crossling\statisticalTLI_full_densified_large.csv",
    "TLI_log_small":  r"data\raw\crossling\logicalTLI_full_densified_small.csv",
    "GBI_stat":       r"data\raw\crossling\statisticalGBI_densified.csv",
    "GBI_log":        r"data\raw\crossling\logicalGBI_densified.csv",
}
from collections import Counter
for name, rel in LAYS.items():
    df = pd.read_csv(os.path.join(BASE, rel), dtype=str, keep_default_na=False)
    n_rows = len(df)
    n_uniq_g = df["glottocode"].nunique()
    n_cols = df.shape[1]
    # 语系
    fams = [gl_map.get(g) for g in df["glottocode"]]
    fam_known = sum(1 for f in fams if f)
    cnt = Counter(f for f in fams if f)
    n_fams = len(cnt)
    ge3 = {k: v for k, v in cnt.items() if v >= 3}
    n_ge3 = len(ge3)
    elig = sum(1 for f in fams if f in ge3)
    ref = L[name]
    cmp("n_rows", n_rows, ref["n_langs"], name)
    cmp("n_uniq_glottocode", n_uniq_g, ref["n_langs"], name + "_uniq")
    cmp("n_cols_total", n_cols, None if True else 0, name + "_cols")  # 仅报告
    cmp("fam_known", fam_known, ref["fam_known"], name)
    cmp("n_fams", n_fams, ref["n_fams"], name)
    cmp("fams_ge3", n_ge3, ref["fams_ge3"], name)
    # 特征列约定
    feat_cols = [c for c in df.columns if c != "glottocode"]          # profile 约定（含未命名列）
    true_feat = [c for c in feat_cols if c != df.columns[0]]          # 真特征列
    cmp("n_feats_conv(含首列)", len(feat_cols), ref["n_feats"], name)
    p(f"[{name}] 真特征列数(去首列)={len(true_feat)}  首列样例={df.iloc[0,0]!r}")
    # bin/poly（两约定）
    def bp(cols):
        b = po = 0
        for c in cols:
            d = df[c][df[c] != ""]
            n = d.nunique()
            if n == 0:
                continue
            b += 1 if n <= 2 else 0
            po += 1 if n > 2 else 0
        return b, po
    b1, p1 = bp(feat_cols)
    b2, p2 = bp(true_feat)
    cmp("bin_conv", b1, ref["bin"], name)
    cmp("poly_conv", p1, ref["poly"], name)
    p(f"[{name}] bin/poly 去首列: bin={b2} poly={p2}")
    # 缺失
    miss = (df[feat_cols] == "").mean().mean()
    cmp("miss_conv(≈)", round(miss, 3), ref["miss"], name)
    # holdout cells
    sub = df[fams.index and [f in ge3 for f in fams]]
    tot_cells = len(sub) * len(feat_cols)
    nonmiss = int((sub[feat_cols] != "").sum().sum())
    p(f"[{name}] eligible_langs={len(sub)} tot_cells={tot_cells} nonmiss={nonmiss}")

# ---------- 4) WALS（长表） ----------
vals = pd.read_csv(os.path.join(BASE, r"data\raw\wals\values.csv"), dtype=str, keep_default_na=False)
params = pd.read_csv(os.path.join(BASE, r"data\raw\wals\parameters.csv"), dtype=str, keep_default_na=False)
n_langs_w = vals["Language_ID"].nunique()
n_feats_w = params["ID"].nunique()
wgl = dict(zip(gl["ID"], gl["Glottocode"]))
def wtop(lid):
    fid_row = gl.loc[gl["ID"] == lid, "Family_ID"]
    if len(fid_row) == 0:
        return None
    fid = fid_row.iloc[0]
    if fam_pat.match(fid or ""):
        return fid
    return id2glot.get(fid)
wmap = {lid: wtop(lid) for lid in gl["ID"].unique()}
wcnt = Counter(wtop(l) for l in vals["Language_ID"].unique())
wcnt.pop(None, None)
wge3 = {k: v for k, v in wcnt.items() if v >= 3}
wref = L["WALS"]
cmp("n_langs", n_langs_w, wref["n_langs"], "WALS")
cmp("n_feats", n_feats_w, wref["n_feats"], "WALS")
cmp("fam_rate(≈)", round(sum(1 for l in wcnt for _ in [0] if True) and round((sum(1 for l in vals['Language_ID'].unique() if wtop(l)) / n_langs_w), 3), 3), wref["fam_rate"], "WALS")
cmp("n_fams", len(wcnt), wref["n_fams"], "WALS")
cmp("fams_ge3", len(wge3), wref["fams_ge3"], "WALS")
wide = vals.pivot_table(index="Language_ID", columns="Parameter_ID", values="Code_ID", aggfunc="first")
bin_val = sum(1 for c in wide.columns if wide[c].dropna().nunique() <= 2)
bin_val2 = sum(1 for c in wide.columns if vals.loc[vals["Parameter_ID"] == c, "Value"].nunique() <= 2)
p(f"[WALS] bin(按Code_ID distinct≤2)={bin_val}  bin(按Value distinct≤2)={bin_val2}  ref bin={wref['bin']} bin_from_matrix={wref.get('bin_from_matrix')}")
elig_w = [l for l in wide.index if wtop(l) in wge3]
tot_w = len(elig_w) * n_feats_w
nonmiss_w = int(wide.loc[elig_w].notna().sum().sum())
p(f"[WALS] eligible_langs={len(elig_w)} tot_cells={tot_w} nonmiss={nonmiss_w}")

# ---------- 5) holdout_stats.txt 对照 ----------
hs = {}
for line in open(os.path.join(R, "holdout_stats.txt"), encoding="cp1252", errors="replace"):
    parts = line.split()
    if parts and re.match(r"^[A-Z]", parts[0]) and parts[0] != "layer":
        hs[parts[0]] = dict(fams_ge3=int(parts[1]), tot_cells=int(parts[2]), nonmiss=int(parts[3]))
for name in list(LAYS) + ["WALS"]:
    if name in hs:
        mine_tot = locals().get("tot_w") if name == "WALS" else None
        p(f"[HOLDOUT] {name}: ref fams_ge3={hs[name]['fams_ge3']} tot_cells={hs[name]['tot_cells']} nonmiss_cells={hs[name]['nonmiss_cells']}")

# ---------- 6) Gower & Rossman 1969 补核 ----------
try:
    import urllib.request, urllib.parse
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(
        {"query.bibliographic": "Seriation and abundance Journal of the Royal Statistical Society", "rows": 5})
    req = urllib.request.Request(url, headers={"User-Agent": "ARIS4C-002-stage1-takeover/1.0 (mailto:sandbox@localhost)"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        d = json.load(resp)
    for it in d.get("message", {}).get("items", [])[:5]:
        t = (it.get("title") or ["?"])[0][:80]
        a = ";".join(x.get("family", "") for x in (it.get("author") or [])[:3])
        y = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
        ct = it.get("container-title") or ["?"]
        p(f"[CRF gower2] {y} | {a} | {t} | {(ct[0][:44] if ct else '?')} | doi={it.get('DOI','?')}")
except Exception as e:
    p(f"[CRF gower2] FAIL {type(e).__name__}: {str(e)[:70]}")

text = "\n".join(out)
open(os.path.join(R, "xcheck_profile.txt"), "w", encoding="utf-8").write(text + "\n")
print(text[:6500])
