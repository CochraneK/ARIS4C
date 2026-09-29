# -*- coding: utf-8 -*-
# 接力5 最终直核（裁定口径）：WALS 唯一语言口径 family/留出 + TLI/GBI 真特征口径缺失率
import pandas as pd, os
base = r"D:\Software\ARIS4C-local\002-language-geometry"
RAW = os.path.join(base, "data", "raw")
wl = pd.read_csv(os.path.join(RAW, "wals", "languages.csv"), dtype=str)
vc = pd.read_csv(os.path.join(RAW, "wals", "values.csv"), dtype=str)
print("wals values uniq Language_ID:", vc["Language_ID"].nunique())
g = wl.set_index("ID")["Glottocode"].astype(str)
print("wals values uniq Glottocode:", vc["Language_ID"].map(g).nunique())
glo = pd.read_csv(os.path.join(RAW, "glottolog", "languages.csv"), dtype=str)
fam_map = {}
for _, r in glo.iterrows():
    gg = str(r["Glottocode"]) if pd.notna(r["Glottocode"]) else ""
    if not gg or gg == "nan":
        continue
    fc = str(r["Family_ID"]) if pd.notna(r["Family_ID"]) else ""
    if r["Level"] == "family" or fc in ("", "nan"):
        fc = gg
    fam_map[gg] = fc
langs = vc["Language_ID"].unique()
L = pd.DataFrame({"lang": langs})
L["glottocode"] = [g.get(x, "") for x in langs]
L["fam"] = [fam_map.get(x, None) for x in L["glottocode"]]
famc = L["fam"].value_counts()
print("wals uniq langs:", len(langs), " fam_known:", int(L["fam"].notna().sum()),
      " n_fams:", int(famc.shape[0]), " ge3:", int((famc >= 3).sum()))
print("wals uniq top8:", {k: int(v) for k, v in famc.head(8).items()})
elig = famc[famc >= 3]
pv = vc.pivot_table(index="Language_ID", columns="Parameter_ID", values="Value",
                    aggfunc="first").reindex(langs)
nm = pv.notna().sum(axis=1).to_numpy()
sel = L["fam"].isin(elig.index).to_numpy()
print("wals UNIQUE-basis holdout: eligible_langs:", int(elig.sum()),
      " cells:", int(elig.sum()) * 192, " nonmiss:", int(nm[sel].sum()))
DENS = {
    "TLI_stat_small": "crossling/statisticalTLI_full_densified_small.csv",
    "TLI_stat_large": "crossling/statisticalTLI_full_densified_large.csv",
    "TLI_log_small": "crossling/logicalTLI_full_densified_small.csv",
    "GBI_stat": "crossling/statisticalGBI_densified.csv",
    "GBI_log": "crossling/logicalGBI_densified.csv",
}
for k, p in DENS.items():
    df = pd.read_csv(os.path.join(RAW, p), dtype=str)
    v = df[[c for c in df.columns if c not in ("glottocode", "Unnamed: 0")]]
    for m in ("?", "NA", "nan", ""):
        v = v.replace(m, pd.NA)
    print(k, "true_feats:", v.shape[1], " miss:", round(float(v.isna().mean().mean()), 4))
print("DONE")
