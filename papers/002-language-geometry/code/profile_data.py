"""Stage1 Group C main profile: TLI/GBI/WALS + Glottolog family feasibility.
Saves results/profile.json; prints <=40 lines."""
import json, os, sys
import numpy as np
import pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parsers import parse_newick
from loaders import (load_dense_csv, feature_profile, encode_classes,
                     load_wals, wals_matrix, RAW)

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RES = os.path.join(BASE, "results")
os.makedirs(RES, exist_ok=True)
P = {}

# ---------- Glottolog ----------
nex = open(os.path.join(RAW, "glottolog", "classification.nex"),
           encoding="utf-8").read()
nodes, leaf_fam = parse_newick(nex)
glangs = pd.read_csv(os.path.join(RAW, "glottolog", "languages.csv"))
n_fam = sum(1 for lv, nm in nodes.values() if lv == "family")
print(f"GLO nodes={len(nodes)} leaves={len(leaf_fam)} fam_nodes={n_fam} "
      f"glottolog_lang_rows={len(glangs)}")
fam_name = {gc: nm for gc, (lv, nm) in nodes.items() if lv == "family"}
iso2g = {r.iso639_3: r.glottocode for _, r in
         glangs.iterrows() if pd.notna(r.get("iso639_3"))}


def fam_stats(gcodes):
    fams, unmatched = {}, 0
    for g in gcodes:
        f = leaf_fam.get(g)
        if f is None:
            unmatched += 1
            f = f"iso::{g}"
        fams.setdefault(f, []).append(g)
    sizes = pd.Series({k: len(v) for k, v in fams.items()})
    elig = sizes[sizes >= 3]
    return {"n_langs": int(len(gcodes)), "n_matched_glottolog": int(len(gcodes) - unmatched),
            "n_unmatched": unmatched, "n_families": int(len(sizes)),
            "n_fam_ge3": int(len(elig)), "holdout_cells": int(elig.sum()),
            "fam_size_hist": {str(k): int((sizes == k).sum())
                              for k in sorted(sizes.unique())[:15]},
            "top_fams": {k: int(v) for k, v in
                         sizes.sort_values(ascending=False).head(8).items()}}


def layer_from_csv(path, name):
    df, idcol, fcols = load_dense_csv(path)
    fp = feature_profile(df, fcols)
    gc = df[idcol].astype(str).tolist()
    P[name] = {"file": os.path.relpath(path, BASE), "n_langs": int(df.shape[0]),
               "n_feats": int(len(fcols)),
               "enc": encode_classes(fp, df.shape[0]),
               "sample_row": [str(x) for x in df.iloc[0].head(6).tolist()],
               "fam": fam_stats(gc), "glottocodes": gc, "fp": fp}
    print(f"{name}: langs={df.shape[0]} feats={len(fcols)} "
          f"bin={P[name]['enc']['n_binary']} poly={P[name]['enc']['n_poly']} "
          f"many={P[name]['enc']['n_many']} miss={P[name]['enc']['overall_missing_rate']:.3f} "
          f"fams={P[name]['fam']['n_families']} ge3={P[name]['fam']['n_fam_ge3']} "
          f"cells={P[name]['fam']['holdout_cells']}")


for nm, f in [("TLI_stat_small", "crossling/statisticalTLI_full_densified_small.csv"),
              ("TLI_stat_large", "crossling/statisticalTLI_full_densified_large.csv"),
              ("TLI_log_small", "crossling/logicalTLI_full_densified_small.csv"),
              ("GBI_stat", "crossling/statisticalGBI_densified.csv"),
              ("GBI_log", "crossling/logicalGBI_densified.csv")]:
    layer_from_csv(os.path.join(RAW, f), nm)

# ---------- WALS ----------
langs, params, vals, codes = load_wals()
m = wals_matrix(langs, params, vals)
print("wals langs.csv cols:", list(langs.columns))
print("wals params cols:", list(params.columns), "n_params:", len(params))
ft = None
if "FeatureType" in params.columns:
    ft = params["FeatureType"].value_counts().to_dict()
    print("wals FeatureType:", {str(k): int(v) for k, v in ft.items()})
wfp = feature_profile(m.reset_index().rename(columns={"index": "wid"}).set_index("wid"), m.columns) if False else feature_profile(m, list(m.columns))
wid_col = "wid"
wgc = []
if "Glottocodes" in langs.columns:
    wgc = [str(x) for x in langs["Glottocodes"].dropna()]
elif "iso639_3" in langs.columns:
    wgc = [iso2g.get(str(x), f"noiso::{x}") for x in langs["iso639_3"].dropna()]
P["WALS"] = {"n_langs": int(m.shape[0]), "n_feats": int(m.shape[1]),
             "enc": encode_classes(wfp, m.shape[0]),
             "feature_types": {str(k): int(v) for k, v in ft.items()} if ft else None,
             "n_langs_with_values": int((m.notna().any(axis=1)).sum()),
             "n_params_any_value": int((m.notna().any(axis=0)).sum()),
             "fam": fam_stats(wgc), "glottocodes": wgc, "fp": wfp}
print(f"WALS: langs={m.shape[0]} feats={m.shape[1]} bin={P['WALS']['enc']['n_binary']} "
      f"poly={P['WALS']['enc']['n_poly']} many={P['WALS']['enc']['n_many']} "
      f"miss={P['WALS']['enc']['overall_missing_rate']:.3f} "
      f"fams={P['WALS']['fam']['n_families']} ge3={P['WALS']['fam']['n_fam_ge3']} "
      f"cells={P['WALS']['fam']['holdout_cells']} wgc_n={len(wgc)}")

# ---------- cross-layer overlap ----------
tl, gb, wa = (set(P[k]["glottocodes"]) for k in ("TLI_stat_small", "GBI_stat", "WALS"))
ov = {"tl_gb": len(tl & gb), "tl_wa": len(tl & wa), "gb_wa": len(gb & wa),
      "all3": len(tl & gb & wa)}
print("overlap TLI∩GBI:", ov["tl_gb"], "TLI∩WALS:", ov["tl_wa"],
      "GBI∩WALS:", ov["gb_wa"], "all3:", ov["all3"])

# ---------- crossling metadata (feature sources) ----------
for tag in ("TLI", "GBI"):
    md = json.load(open(os.path.join(RAW, "crossling",
                     f"{'statisticalTLI' if tag=='TLI' else 'statisticalGBI'}"
                     "/cldf/StructureDataset-metadata.json")))
    pars = md.get("Parameters", [])
    src = [str(p.get("Source", "")) + " " + str(p.get("Description", ""))
           for p in pars]
    n_wals = sum(1 for s in src if "WALS" in s)
    print(f"{tag} metadata: name={md.get('Name')!r} n_params={len(pars)} "
          f"params_mentioning_WALS={n_wals}")
    desc = str(md.get("Description", ""))
    print(f"  desc: {desc[:220]}")
    P[f"{tag}_meta"] = {"name": md.get("Name"), "n_params": len(pars),
                        "params_mentioning_WALS": n_wals,
                        "description_head": desc[:400]}

# ---------- circularity feasibility ----------
for k in P:
    if k in ("TLI_meta", "GBI_meta") or "fam" not in P[k]:
        continue
    e = P[k]["enc"]
    P[k]["circularity"] = {
        "usable_feats_nuniq_ge2": sum(1 for f in P[k]["fp"] if f["nuniq"] >= 2),
        "n_binary": e["n_binary"], "threshold_met_ge12_binary": e["n_binary"] >= 12,
        "mds_n": P[k]["n_langs"]}
print("circularity:", {k: (P[k]["circularity"]["n_binary"],
                            P[k]["circularity"]["threshold_met_ge12_binary"])
                        for k in P if "circularity" in P[k]})

json.dump({"P": {k: {kk: vv for kk, vv in v.items() if kk != "fp"}
                 for k, v in P.items()},
           "fam_names_top": {k: fam_name.get(v, v)
                             for k, v in P["WALS"]["fam"]["top_fams"].items()}},
          open(os.path.join(RES, "profile.json"), "w"), ensure_ascii=False)
print("profile.json written")

