# probe_encoding.py v2 — 驱动器接管（第 10 次·接力 4）2026-09-26
# v2 修正：crossling CSV 缺失标记为字面 '?'（非空串）；先 mask '?' 再统计。
# 目的：判定 6 张分析表特征列的真实编码类型（二值/多态/连续），
#       仲裁 profile.json 与 xcheck_profile.txt 的 bin/poly/miss 口径差异。
import pandas as pd, json, os

BASE = r"D:\Software\ARIS4C-local\002-language-geometry"
RAW = os.path.join(BASE, "data", "raw")
out = {"tables": {}, "wals": {}}

LAY = {
    "TLI_stat_small": "crossling/statisticalTLI_full_densified_small.csv",
    "TLI_stat_large": "crossling/statisticalTLI_full_densified_large.csv",
    "TLI_log_small":  "crossling/logicalTLI_full_densified_small.csv",
    "GBI_stat":       "crossling/statisticalGBI_densified.csv",
    "GBI_log":        "crossling/logicalGBI_densified.csv",
}
for name, rel in LAY.items():
    raw = pd.read_csv(os.path.join(RAW, rel), index_col=0, dtype=str, keep_default_na=False)
    raw = raw.drop(columns=[c for c in raw.columns if str(c).startswith("Unnamed")])
    has_glot = any(str(c).lower() == "glottocode" for c in raw.columns)
    feat = raw.drop(columns=[c for c in raw.columns if str(c).lower() == "glottocode"])
    n_q = int((feat == "?").sum().sum())
    n_empty = int((feat == "").sum().sum())
    feat = feat.mask(feat == "?")  # '?' -> NaN；其余按数值读
    try:
        feat = feat.apply(pd.to_numeric, errors="coerce")
    except Exception:
        pass
    d = feat.apply(lambda c: c.nunique(dropna=True))
    nrow, ncol = feat.shape
    nmiss = int(feat.isna().sum().sum())
    sample = None
    if name == "TLI_stat_small":
        c0 = feat.columns[0]
        sample = [round(float(x), 4) for x in feat[c0].dropna().head(6)]
    out["tables"][name] = {
        "n_rows": int(nrow),
        "n_feats": int(ncol),
        "n_q_marks": n_q,
        "n_empty_marks": n_empty,
        "nuniq_le2": int((d <= 2).sum()),
        "nuniq_eq2": int((d == 2).sum()),
        "nuniq_gt2": int((d > 2).sum()),
        "nuniq_min": int(d.min()),
        "nuniq_med": float(d.median()),
        "nuniq_max": int(d.max()),
        "miss_cell_rate": round(nmiss / (nrow * ncol), 4),
        "sample_values_first_feat": sample,
    }

vals = pd.read_csv(os.path.join(RAW, "wals", "values.csv"), dtype=str, keep_default_na=False)
params = pd.read_csv(os.path.join(RAW, "wals", "parameters.csv"), dtype=str, keep_default_na=False)
wide = vals.pivot_table(index="Language_ID", columns="Parameter_ID", values="Code_ID", aggfunc="first")
dc = wide.apply(lambda c: c.nunique())
out["wals"] = {
    "n_langs": int(vals["Language_ID"].nunique()),
    "n_params": int(params["ID"].nunique()),
    "nuniq_le2": int((dc <= 2).sum()),
    "nuniq_eq2": int((dc == 2).sum()),
    "nuniq_gt2": int((dc > 2).sum()),
    "nuniq_min": int(dc.min()),
    "nuniq_med": float(dc.median()),
    "nuniq_max": int(dc.max()),
    "miss_cell_rate": round(float(wide.isna().mean().mean()), 4),
}

json.dump(out, open(os.path.join(BASE, "results", "probe_encoding.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("OK")
for k, v in out["tables"].items():
    print("%s feats=%d q=%d empty=%d le2=%d eq2=%d gt2=%d med_nuniq=%.1f miss=%.4f" % (
        k, v["n_feats"], v["n_q_marks"], v["n_empty_marks"], v["nuniq_le2"], v["nuniq_eq2"],
        v["nuniq_gt2"], v["nuniq_med"], v["miss_cell_rate"]))
w = out["wals"]
print("WALS langs=%d params=%d le2=%d eq2=%d gt2=%d med_nuniq=%.1f miss=%.4f" % (
    w["n_langs"], w["n_params"], w["nuniq_le2"], w["nuniq_eq2"], w["nuniq_gt2"], w["nuniq_med"], w["miss_cell_rate"]))
print("sample first feat (TLI_stat_small):", out["tables"]["TLI_stat_small"]["sample_values_first_feat"])
