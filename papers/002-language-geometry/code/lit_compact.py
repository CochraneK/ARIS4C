"""Orchestrator takeover (driver, 10th): domain-filtered lit compact list.
Reads results/lit_candidates.tsv (Crossref-verified cols crf_*), dedups by DOI,
keeps rows whose title is on-domain (linguistics) AND on-method. Prints compact
ranked list to stdout + results/takeover_lit_compact.txt. No LLM, deterministic."""
import os
import pandas as pd

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
df = pd.read_csv(os.path.join(BASE, "results", "lit_candidates.tsv"), sep="\t",
                 dtype=str).fillna("")
print("COLUMNS:", list(df.columns))
print("total candidates:", len(df))
print("crf_status counts:", df["crf_status"].value_counts().to_dict())
print("found_in counts (all):", df["found_in"].value_counts().to_dict())

ok = df[df["crf_status"] == "OK"].copy()
ok["t"] = ok["crf_title"].str.lower()
DOM = ["linguist", "language", "typolog", "universal", "wals", "glottolog",
       "crossling", "grammar", "lexicon", "phonolog", "morpholog", "syntax",
       "phraseolog", "etymolog", "indoeuropean", "indo-european"]
METH = ["seriation", "circular", "robinson", "periodic", "mds",
        "multidimension", "geometry", "geometric", "latent", "factor",
        "hierarch", "phylogen", "predict", "embedd", "spatial", "torus",
        "cluster", "dimensionality"]

def isdom(t):
    return any(k in t for k in DOM)

def ismeth(t):
    return any(k in t for k in METH)

sel = ok[ok["t"].map(lambda t: isdom(t) and ismeth(t))].copy()
sel["key"] = sel["doi"].where(sel["doi"] != "", sel["crf_title"].str.lower())
rows = []
for key, g in sel.groupby("key"):
    t = g["crf_title"].iloc[0]
    year = next((y for y in g["crf_year"] if y), "?")
    authors = next((a for a in g["crf_authors"] if a), "?")
    venue = next((v for v in g["crf_venue"] if v), "?")
    doi = next((d for d in g["doi"] if d), "(no-doi)")
    found = "+".join(sorted(set(x for x in g["found_in"] if x)))
    rows.append((int(year) if year.isdigit() else 0, str(year), authors, t, venue, doi, found))
rows.sort(key=lambda r: (r[0], r[3]))
print("domain+method unique rows:", len(rows))
for i, (yy, year, authors, title, venue, doi, found) in enumerate(rows, 1):
    print(f"{i:2d} | {year:>4} | {authors[:38]:38s} | {title[:92]} | {venue[:30]:30s} | {doi} | {found}")

print("--- 'periodic' rows (all domains, hypothesis-source check) ---")
per = ok[ok["t"].str.contains("periodic")]
for i, r in per.iterrows():
    print(f"PER | {r['crf_year']} | {r['crf_authors'][:38]} | {r['crf_title'][:92]} | {r['doi']}")
print("--- 'robinson' rows ---")
rob = ok[ok["t"].str.contains("robinson")]
for i, r in rob.iterrows():
    print(f"ROB | {r['crf_year']} | {r['crf_authors'][:38]} | {r['crf_title'][:92]} | {r['doi']}")
print("--- 'type and language index' / 'grambank' / 'wals' / 'glottolog' data-layer rows ---")
dl = ok[ok["t"].str.contains("type and language index|grambank|world atlas of language|glottolog|language index")]
for i, r in dl.iterrows():
    print(f"DAT | {r['crf_year']} | {r['crf_authors'][:38]} | {r['crf_title'][:92]} | {r['doi']}")
