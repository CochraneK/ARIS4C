"""Orchestrator takeover: keyword-score lit candidates, print shortlist.
Coverage floor needed: (a) periodic-table hypothesis source, (b) circular
seriation method, (c) hierarchy/tree/latent comparators, (d) TLI/GBI/WALS
data-layer descriptions, (e) family-held-out typology prediction."""
import os
import pandas as pd

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
df = pd.read_csv(os.path.join(BASE, "results", "lit_candidates.tsv"),
                 sep="\t", dtype=str).fillna("")
df["t"] = (df["crf_title"].str.lower())

RULES = [("periodic table", 10), ("seriation", 8), ("circular", 6),
         ("robinson", 6), ("held-out", 6), ("held out", 6),
         ("language universals", 5), ("linguistic universals", 5),
         ("crossling", 5), ("glottolog", 4), ("wals", 4),
         ("grambank", 4), ("type and language index", 5),
         ("phylogen", 4), ("typolog", 3), ("multidimensional", 3),
         ("prediction", 2), ("latent", 2), ("hierarchy", 2),
         ("hierarchical", 2), ("factor", 2), ("tree", 1)]

def score(t):
    s = 0
    for kw, w in RULES:
        if kw in t:
            s += w
    return s

df["score"] = df["t"].map(score)
df = df[df["crf_status"] == "OK"].copy()
print("verified-OK candidates:", len(df))
print("found_in counts:", df["found_in"].value_counts().to_dict())
print("--- periodic matches (hypothesis source) ---")
pm = df[df["t"].str.contains("periodic")]
for _, r in pm.iterrows():
    print(f"{r['crf_year']} | {r['crf_authors'][:60]} | {r['crf_venue'][:30]} | {r['crf_title'][:90]} | doi={r['doi']}")
print("--- top 35 by score ---")
top = df.sort_values("score", ascending=False).head(35)
for _, r in top.iterrows():
    print(f"{int(r['score']):2d} | {r['crf_year']} | {r['crf_authors'][:42]:42s} | {r['crf_title'][:80]}")
print("--- zero-score OK count:", int((df['score'] == 0).sum()))
