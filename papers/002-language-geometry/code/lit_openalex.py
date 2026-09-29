"""Stage1 Group B: OpenAlex search (7 rounds) + Crossref verification.
Outputs: results/openalex_raw.json, results/lit_candidates.tsv,
         results/crossref_check.txt. Prints <=40 lines."""
import json, os, time, datetime
import requests

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RES = os.path.join(BASE, "results")
os.makedirs(RES, exist_ok=True)
UA = "aris4c-002-stage1 literature recon (research use; mailto:local@example.org)"
TODAY = datetime.date.today().isoformat()

QUERIES = [
    ("R1 periodic-table", "periodic table of languages"),
    ("R2 circular-seriation", "circular seriation"),
    ("R3 circular-robinson", "circular Robinson matrix arrangement"),
    ("R4 geometry-universals", "geometry of language universals"),
    ("R5 wals-prediction", "WALS typological features prediction"),
    ("R6 phylo-typology", "phylogenetic control typological features independence"),
    ("R7 mds-linguistic", "multidimensional scaling linguistic typology arrangement"),
]

oa = requests.Session()
oa.headers.update({"User-Agent": UA})
raw = {}
cands = {}
for tag, q in QUERIES:
    url = ("https://api.openalex.org/works?search=" + requests.utils.quote(q)
           + "&per-page=25&select=id,doi,title,publication_year,authorships,primary_location")
    r = oa.get(url, timeout=60)
    r.raise_for_status()
    js = r.json()
    raw[tag] = {"query": q, "count": js.get("meta", {}).get("count"),
                "date": TODAY, "works": js.get("results", [])}
    for w in js.get("results", []):
        key = (w.get("doi") or (w.get("title") or "")).lower()
        if key and key not in cands:
            cands[key] = {
                "oa_id": w.get("id"), "doi": w.get("doi"),
                "title": (w.get("title") or "").strip(),
                "year": w.get("publication_year"),
                "authors": [a["author"]["display_name"]
                            for a in (w.get("authorships") or [])[:4]],
                "venue": ((w.get("primary_location") or {}).get("source") or {})
                          .get("display_name"),
                "found_in": tag,
            }
    time.sleep(0.3)

# anchor DOIs from prior background (to be re-verified independently)
ANCHORS = ["10.1137/21M139356X", "10.1016/j.patcog.2019.107192",
           "10.1038/s41597-024-04319-4", "10.1038/s41562-025-02325-z",
           "10.1038/s41467-025-67463-4", "10.1007/s11786-017-0329-x",
           "10.1007/s11786-021-00520-5", "10.18653/v1/N19-1156",
           "10.1126/sciadv.adg6175"]
for d in ANCHORS:
    if d not in cands:
        cands[d] = {"oa_id": None, "doi": d, "title": "", "year": None,
                    "authors": [], "venue": None, "found_in": "anchor"}

with open(os.path.join(RES, "openalex_raw.json"), "w") as f:
    json.dump(raw, f, ensure_ascii=False)
print(f"openalex rounds: {len(raw)}; unique candidates: {len(cands)}")
