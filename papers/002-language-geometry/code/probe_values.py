# probe_values.py — 驱动器接管（第 10 次·接力 4）2026-09-26
# 目的：字符串口径（排除 '?'）统计各 crossling 表特征列取值数分布 + 抽样值字母表 + 列名。
import pandas as pd, os, json

RAW = r"D:\Software\ARIS4C-local\002-language-geometry\data\raw\crossling"
LAY = {
    "TLI_stat_small": "statisticalTLI_full_densified_small.csv",
    "TLI_stat_large": "statisticalTLI_full_densified_large.csv",
    "TLI_log_small":  "logicalTLI_full_densified_small.csv",
    "GBI_stat":       "statisticalGBI_densified.csv",
    "GBI_log":        "logicalGBI_densified.csv",
}
res = {}
for name, fn in LAY.items():
    raw = pd.read_csv(os.path.join(RAW, fn), index_col=0, dtype=str, keep_default_na=False)
    raw = raw.drop(columns=[c for c in raw.columns if str(c).startswith("Unnamed")])
    gcol = [c for c in raw.columns if str(c).lower() == "glottocode"]
    feat = raw.drop(columns=gcol)
    d = feat.apply(lambda c: c[c != "?"].nunique())
    alphabet = set()
    for c in feat.columns:
        for v in feat[c][feat[c] != "?"].unique():
            alphabet.add(v)
        if len(alphabet) > 300:
            break
    res[name] = {
        "n_rows": int(len(feat)),
        "n_feats": int(feat.shape[1]),
        "colnames_head": [str(c) for c in feat.columns[:8]],
        "nuniq_eq1": int((d == 1).sum()),
        "nuniq_eq2": int((d == 2).sum()),
        "nuniq_gt2": int((d > 2).sum()),
        "nuniq_zero": int((d == 0).sum()),
        "nuniq_med": float(d.median()),
        "nuniq_max": int(d.max()),
        "alphabet_size": len(alphabet),
        "alphabet_head": sorted(alphabet)[:40],
    }
out = r"D:\Software\ARIS4C-local\002-language-geometry\results\probe_values.json"
json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("OK")
for k, v in res.items():
    print("%s feats=%d eq1=%d eq2=%d gt2=%d zero=%d med=%s max=%d alph=%d" % (
        k, v["n_feats"], v["nuniq_eq1"], v["nuniq_eq2"], v["nuniq_gt2"],
        v["nuniq_zero"], v["nuniq_med"], v["nuniq_max"], v["alphabet_size"]))
print("TLI_stat_small colnames:", res["TLI_stat_small"]["colnames_head"])
print("TLI_stat_small alphabet:", res["TLI_stat_small"]["alphabet_head"])
print("GBI_stat alphabet:", res["GBI_stat"]["alphabet_head"][:12])
