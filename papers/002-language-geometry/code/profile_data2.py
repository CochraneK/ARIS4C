"""Stage1 Group C profile v2 (orchestrator takeover, 2026-09-26 16:5x BJT).
Fixes vs v1 (executor-died-incomplete):
 1) family map from glottolog languages.csv (Glottocode -> Family_ID) — no Newick
    (classification.nex holds per-clade tree blocks, not one Newick tree);
 2) encodings: TLI stat = true/false/?; GBI stat = 0/1(/2)/NA; logical = strings;
 3) WALS long-format pivot via languages.csv (ISO3 -> Glottocode);
 4) crossling metadata via 'tables' key (v1 path/key wrong, crashed line 108);
 5) cross-layer overlap by glottocode across all six dense layers.
Writes results/profile.json; prints <=40 lines."""
import json, os
import numpy as np
import pandas as pd

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW = os.path.join(BASE, "data", "raw")
RES = os.path.join(BASE, "results")
os.makedirs(RES, exist_ok=True)
MISS = {"?", "NA", "nan", ""}

# ---------- glottolog family map ----------
glo = pd.read_csv(os.path.join(RAW, "glottolog", "languages.csv"), dtype=str)
fam_map, n_glo = {}, 0
for _, r in glo.iterrows():
    g = str(r["Glottocode"]) if pd.notna(r["Glottocode"]) else ""
    if not g or g == "nan":
        continue
    fc = str(r["Family_ID"]) if pd.notna(r["Family_ID"]) else ""
    if r["Level"] == "family" or fc in ("", "nan"):
        fc = g  # family-level row, or no family ref -> self
    fam_map[g] = fc
    n_glo += 1

def fam_stats(gl, n_langs):
    fams = gl.map(fam_map)
    known = int(fams.notna().sum())
    vc = fams.value_counts()
    return (known, round(known / max(n_langs, 1), 3), int(vc.shape[0]),
            int((vc >= 3).sum()), {k: int(v) for k, v in vc.head(8).items()})

def prof_dense(tag, path, glc="glottocode"):
    df = pd.read_csv(os.path.join(RAW, path), dtype=str)
    feats = [c for c in df.columns if c not in ("", glc)]
    v = df[feats]
    for m in MISS:
        v = v.replace(m, np.nan)
    nuniq = v.nunique(dropna=True)
    gl = df[glc].astype(str)
    n_langs = int(gl.ne("").sum())
    known, frate, nfam, ge3, top = fam_stats(gl, n_langs)
    return {"n_langs": n_langs, "n_feats": int(len(feats)),
            "bin": int((nuniq == 2).sum()), "poly": int((nuniq >= 3).sum()),
            "miss": round(float(v.isna().mean().mean()), 3),
            "fam_known": known, "fam_rate": frate, "n_fams": nfam,
            "fams_ge3": ge3, "top_fams": top}

P = {
    "TLI_stat_small": prof_dense("t", "crossling/statisticalTLI_full_densified_small.csv"),
    "TLI_stat_large": prof_dense("t", "crossling/statisticalTLI_full_densified_large.csv"),
    "TLI_log_small": prof_dense("t", "crossling/logicalTLI_full_densified_small.csv"),
    "GBI_stat": prof_dense("t", "crossling/statisticalGBI_densified.csv"),
    "GBI_log": prof_dense("t", "crossling/logicalGBI_densified.csv"),
}

# ---------- WALS (long format) ----------
wl = pd.read_csv(os.path.join(RAW, "wals", "languages.csv"), dtype=str)
codes = pd.read_csv(os.path.join(RAW, "wals", "codes.csv"), dtype=str)
vc_ = pd.read_csv(os.path.join(RAW, "wals", "values.csv"), dtype=str)
pv = vc_.pivot_table(index="Language_ID", columns="Parameter_ID",
                     values="Value", aggfunc="first")
pv = pv.reindex(wl["ID"].astype(str))
nuniq_w = pv.nunique(dropna=True)
wgl = wl.set_index("ID")["Glottocode"].astype(str)
known, frate, nfam, ge3, top = fam_stats(wgl, int(wgl.ne("").sum()))
nc = codes.groupby("Parameter_ID")["ID"].nunique()
P["WALS"] = {"n_langs": int(wgl.ne("").sum()), "n_feats": int(pv.shape[1]),
             "bin": int((nc == 2).sum()), "poly": int((nc >= 3).sum()),
             "bin_from_matrix": int((nuniq_w == 2).sum()),
             "miss": round(float(pv.isna().mean().mean()), 3),
             "fam_known": known, "fam_rate": frate, "n_fams": nfam,
             "fams_ge3": ge3, "top_fams": top}

# ---------- cross-layer overlap (by glottocode) ----------
def glset(path, glc="glottocode"):
    df = pd.read_csv(os.path.join(RAW, path), dtype=str, usecols=["glottocode"])
    return set(df["glottocode"].dropna().astype(str))
sets = {k: glset(p) for k, p in
        {"TLI_stat_small": "crossling/statisticalTLI_full_densified_small.csv",
         "TLI_stat_large": "crossling/statisticalTLI_full_densified_large.csv",
         "TLI_log_small": "crossling/logicalTLI_full_densified_small.csv",
         "GBI_stat": "crossling/statisticalGBI_densified.csv",
         "GBI_log": "crossling/logicalGBI_densified.csv"}.items()}
sets["WALS"] = set(wgl.dropna().astype(str))
keys = list(sets)
overlap = {}
for i, a in enumerate(keys):
    for b in keys[i+1:]:
        overlap[f"{a}~{b}"] = len(sets[a] & sets[b])
overlap["all6"] = len(set.intersection(*sets.values()))

# ---------- crossling metadata (tables key) ----------
meta = json.load(open(os.path.join(RAW, "crossling",
                                   "StructureDataset-metadata.json"),
                      encoding="utf-8"))
tbl = []
for t in meta.get("tables", []):
    if not isinstance(t, dict):
        continue
    ps = t.get("Parameters", [])
    tbl.append({"title": str(t.get("Title", ""))[:50], "n_params": len(ps),
                "wals_sourced": sum(1 for p in ps if isinstance(p, dict)
                                    and "WALS" in str(p.get("Source", "")))})

# ---------- circularity feasibility ----------
circ = {k: {"bin": P[k]["bin"], "threshold_ge12": P[k]["bin"] >= 12,
            "mds_n": P[k]["n_langs"]} for k in P}

out = {"glo_rows": n_glo, "layers": P, "overlap": overlap,
       "crossling_tables": tbl, "circularity": circ}
json.dump(out, open(os.path.join(RES, "profile.json"), "w"), ensure_ascii=False)

print(f"GLO rows={n_glo}")
for k, d in P.items():
    print(f"{k}: langs={d['n_langs']} feats={d['n_feats']} bin={d['bin']} "
          f"poly={d['poly']} miss={d['miss']} fam_rate={d['fam_rate']} "
          f"fams={d['n_fams']} ge3={d['fams_ge3']}")
print("overlap:", {k2: v2 for k2, v2 in overlap.items() if v2 > 0 or k2 == "all6"})
print("tables:", [(t["title"], t["n_params"], t["wals_sourced"]) for t in tbl][:8])
print("circularity:", {k: (v["bin"], v["threshold_ge12"]) for k, v in circ.items()})
print("profile.json written")
