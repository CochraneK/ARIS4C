"""Orchestrator takeover (driver, 10th): family-held-out feasibility stats.
Same family definition as frozen RESEARCH_PLAN §5 (Glottolog top-level family =
glottolog languages.csv Family_ID). Per layer: eligible families (>=3 langs),
total/non-missing holdout cells, family-size distribution, top-15 list.
Full lists -> results/holdout_families.tsv (compact, one row per layer-family).
Prints <=40 lines. Deterministic, no LLM."""
import os
import pandas as pd

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW = os.path.join(BASE, "data", "raw")
RES = os.path.join(BASE, "results")
MISS = {"?", "NA", "nan", ""}

glo = pd.read_csv(os.path.join(RAW, "glottolog", "languages.csv"), dtype=str)
fam_map = {}
for _, r in glo.iterrows():
    g = str(r["Glottocode"]) if pd.notna(r["Glottocode"]) else ""
    if not g or g == "nan":
        continue
    fc = str(r["Family_ID"]) if pd.notna(r["Family_ID"]) else ""
    if r["Level"] == "family" or fc in ("", "nan"):
        fc = g
    fam_map[g] = fc

LAYS = {
    "TLI_stat_small": "crossling/statisticalTLI_full_densified_small.csv",
    "TLI_stat_large": "crossling/statisticalTLI_full_densified_large.csv",
    "TLI_log_small": "crossling/logicalTLI_full_densified_small.csv",
    "GBI_stat": "crossling/statisticalGBI_densified.csv",
    "GBI_log": "crossling/logicalGBI_densified.csv",
}
n_feats = {}
for k, p in LAYS.items():
    df = pd.read_csv(os.path.join(RAW, p), dtype=str)
    v = df[[c for c in df.columns if c != "glottocode"]]
    for m in MISS:
        v = v.replace(m, pd.NA)
    n_feats[k] = (int(v.shape[1]), int(v.notna().sum().sum()))
wl = pd.read_csv(os.path.join(RAW, "wals", "languages.csv"), dtype=str)
vc = pd.read_csv(os.path.join(RAW, "wals", "values.csv"), dtype=str)
pv = vc.pivot_table(index="Language_ID", columns="Parameter_ID",
                    values="Value", aggfunc="first")
pv = pv.reindex(wl["ID"].astype(str))
n_feats["WALS"] = (int(pv.shape[1]), int(pv.notna().sum().sum()))

wgl = wl.set_index("ID")["Glottocode"].astype(str)
rows_out = []
summary = {}
for k in list(LAYS) + ["WALS"]:
    if k in LAYS:
        df = pd.read_csv(os.path.join(RAW, LAYS[k]), dtype=str)
        gl = df["glottocode"].astype(str)
        v = df[[c for c in df.columns if c != "glottocode"]]
        for m in MISS:
            v = v.replace(m, pd.NA)
        nonmiss_row = v.notna().sum(axis=1)
    else:
        gl = wgl
        nonmiss_row = pv.notna().sum(axis=1)
    fams = gl.map(fam_map)
    vc_ = fams.value_counts()
    eligible = vc_[vc_ >= 3]
    total_cells = sum(eligible) * n_feats[k][0]
    nm_cells = int(nonmiss_row[fams.isin(eligible.index)].sum())
    summary[k] = (int(eligible.shape[0]), int(total_cells), nm_cells,
                  eligible.index[0], int(eligible.iloc[0]),
                  int(eligible.min()))
    for f, n in eligible.items():
        rows_out.append((k, f, int(n)))
pd.DataFrame(rows_out, columns=["layer", "family", "n_langs"]).to_csv(
    os.path.join(RES, "holdout_families.tsv"), sep="\t", index=False)

print(f"{'layer':15s} {'fams_ge3':>8s} {'tot_cells':>9s} {'nonmiss_cells':>13s} {'largest':>10s} {'largest_n':>9s} {'min_n':>5s}")
for k, (nf, tc, nm, f0, n0, mn) in summary.items():
    print(f"{k:15s} {nf:8d} {tc:9d} {nm:13d} {f0:>10s} {n0:9d} {mn:5d}")
print("--- top 15 eligible families per layer (fam x n_langs) ---")
for k in list(LAYS) + ["WALS"]:
    sub = [r for r in rows_out if r[0] == k]
    sub.sort(key=lambda r: (-r[2], r[1]))
    print(k, ": " + " ".join(f"{f}x{n}" for f, n in [ (r[1], r[2]) for r in sub[:15] ]))
print("holdout_families.tsv rows:", len(rows_out))
