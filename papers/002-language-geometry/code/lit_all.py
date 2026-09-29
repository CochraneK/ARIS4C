"""Driver takeover (10th): full verified candidate dump for registry curation.
Prints all crf_status=OK candidates (dedup by DOI) + non-OK rows compactly.
Deterministic, no LLM. Output saved to results/takeover_lit_all.txt."""
import os
import pandas as pd

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
df = pd.read_csv(os.path.join(BASE, "results", "lit_candidates.tsv"), sep="\t",
                 dtype=str).fillna("")
ok = df[df["crf_status"] == "OK"].copy()
ok["key"] = ok["doi"].where(ok["doi"] != "", ok["crf_title"].str.lower())
rows = []
for key, g in ok.groupby("key"):
    year = next((y for y in g["crf_year"] if y), "?")
    authors = next((a for a in g["crf_authors"] if a), "?")
    title = next((t for t in g["crf_title"] if t), "?")
    venue = next((v for v in g["crf_venue"] if v), "?")
    doi = next((d for d in g["doi"] if d), "(no-doi)")
    found = "+".join(sorted(set(x for x in g["found_in"] if x)))
    rows.append((int(year) if year.isdigit() else 0, str(year), authors, title, venue, doi, found))
rows.sort(key=lambda r: (r[6], r[0], r[3]))
print("OK unique:", len(rows))
for i, (yy, year, authors, title, venue, doi, found) in enumerate(rows, 1):
    print(f"{i:3d}|{found:28s}|{year:>4}|{authors[:34]:34s}|{title[:84]}|{venue[:26]}|{doi}")
bad = df[df["crf_status"] != "OK"]
print("--- NON-OK:", len(bad), "rows ---")
for i, r in bad.iterrows():
    print(f"BAD|{r['crf_status']:10s}|{r['found_in']:24s}|{(r['title'] or r['crf_title'])[:80]}|{r['doi']}")
