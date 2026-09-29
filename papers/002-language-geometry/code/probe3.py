# probe3.py - 段3 开工探针：环境/冻结件结构速览（stdout <=40 行，不 cat 数据文件）
import json
import os

import numpy as np
import pandas as pd

from common import BASE, ORDER, RAW, RES, load_table

print("cpu", os.cpu_count())
print("scripts", sorted(os.listdir(os.path.join(BASE, "scripts"))))
print("results", sorted(os.listdir(RES)))
for k in ORDER:
    t = load_table(k)
    print(k, "n_langs", t["n_langs"], "n_feat", t["n_feat"], "n_bin", t["n_bin"])
hold = pd.read_csv(os.path.join(RES, "holdout_families.tsv"), sep="\t", dtype=str)
print("holdout cols", list(hold.columns))
print("holdout per-layer", hold["layer"].value_counts().to_dict())
for k in ORDER:
    p = os.path.join(RES, "m2_folds_%s.tsv" % k)
    df = pd.read_csv(p, sep="\t")
    ncf = int(df["logloss_circular"].isna().sum())
    nmf = int(df["logloss_marginal"].isna().sum())
    print("m2_folds", k, "rows", len(df), "ll_c_nan", ncf, "ll_m_nan", nmf,
          "cols", len(df.columns))
agg = json.load(open(os.path.join(RES, "m2_results.json"), encoding="utf-8"))
for k in ORDER:
    r = agg[k]
    print("m2", k, "dir", r["h1_direction"], "mc", round(r["mean_logloss_circular"], 4),
          "mm", round(r["mean_logloss_marginal"], 4), "sp", r["sign_test_p"],
          "nvalid", r["n_families_valid"])
lk = pd.read_csv(os.path.join(RES, "leakage_check.tsv"), sep="\t", dtype=str)
print("leak cols", list(lk.columns), "rows", len(lk),
      "per-table", lk["table"].value_counts().to_dict())
print("leak first", lk.iloc[0].tolist())
glo = pd.read_csv(os.path.join(RAW, "glottolog", "languages.csv"), dtype=str, nrows=3)
glofull_cols = pd.read_csv(os.path.join(RAW, "glottolog", "languages.csv"),
                           dtype=str, usecols=lambda c: True)
print("glottolog cols", list(glofull_cols.columns), "nrows", len(glofull_cols))
print("glottolog has Macroarea", any("macro" in c.lower() for c in glofull_cols.columns))
if any("macro" in c.lower() for c in glofull_cols.columns):
    mc = [c for c in glofull_cols.columns if "macro" in c.lower()][0]
    print("macroarea sample", glofull_cols[["Glottocode", "Level", mc]].head(3).to_dict("records"))
wl = pd.read_csv(os.path.join(RAW, "wals", "languages.csv"), dtype=str, nrows=2)
print("wals languages cols", list(wl.columns))
with open(os.path.join(RAW, "crossling", "statisticalTLI_full_densified_small.csv"),
          encoding="utf-8") as f:
    r1 = f.readline().strip().split(",")[:6]
    r2 = f.readline().strip().split(",")[:6]
print("TLI_small raw row1 head", r1)
print("TLI_small raw row2 head", r2)
