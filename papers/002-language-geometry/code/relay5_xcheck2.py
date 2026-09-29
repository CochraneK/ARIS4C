# -*- coding: utf-8 -*-
# 接力5 验收直核脚本：裁定 WALS 语言数/二值特征数、TLI/GBI 首列、holdout_families 结构
import pandas as pd, os
base = r"D:\Software\ARIS4C-local\002-language-geometry"
w = os.path.join(base, "data", "raw", "wals")
v = pd.read_csv(os.path.join(w, "values.csv"), low_memory=False)
print("values rows:", len(v))
print("values cols:", list(v.columns))
print("uniq lang(v.ID):", v["ID"].nunique())
print("uniq param:", v["Parameter_ID"].nunique())
s = v.groupby("Parameter_ID")["Code_ID"].nunique()
sv = v.groupby("Parameter_ID")["Value"].nunique()
print("WALS bin Code_ID<=2:", int((s <= 2).sum()), " poly:", int((s > 2).sum()))
print("WALS bin Value<=2:", int((sv <= 2).sum()))
L = pd.read_csv(os.path.join(w, "languages.csv"), low_memory=False)
print("languages rows:", len(L), " cols:", list(L.columns))
if "Glottocode" in L.columns:
    print("uniq Glottocode:", L["Glottocode"].nunique())
t = pd.read_csv(os.path.join(base, "data", "raw", "crossling", "statisticalTLI_full_densified_small.csv"), low_memory=False)
print("TLI_stat_small shape:", t.shape, " cols[:3]:", list(t.columns[:3]))
print("TLI col0 sample:", t.iloc[:3, 0].tolist())
b = pd.read_csv(os.path.join(base, "data", "raw", "crossling", "statisticalGBI_densified.csv"), low_memory=False)
print("GBI_stat shape:", b.shape, " cols[:3]:", list(b.columns[:3]))
hf = pd.read_csv(os.path.join(base, "results", "holdout_families.tsv"), sep="\t", low_memory=False)
print("holdout_families cols:", list(hf.columns), " rows:", len(hf))
print("holdout_families head3:", hf.head(3).to_dict("records"))
print("holdout_families layer counts:")
col = "layer" if "layer" in hf.columns else hf.columns[0]
print(hf[col].value_counts().to_dict())
