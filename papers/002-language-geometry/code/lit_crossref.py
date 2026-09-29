"""Crossref verification of all OpenAlex candidates + anchor DOIs.
Writes results/crossref_check.txt and results/lit_candidates.tsv.
Prints a <=40-line relevance shortlist for registry curation."""
import json, os, time, datetime
import requests

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RES = os.path.join(BASE, "results")
UA = {"User-Agent": "aris4c-002-stage1 literature verification (mailto:local@example.org)"}
TODAY = datetime.date.today().isoformat()

raw = json.load(open(os.path.join(RES, "openalex_raw.json")))
cands = {}
for tag, d in raw.items():
    for w in d["works"]:
        key = (w.get("doi") or (w.get("title") or "")).lower()
        if key and key not in cands:
            cands[key] = {"doi": w.get("doi"), "title": (w.get("title") or "").strip(),
                          "year": w.get("publication_year"),
                          "authors": [a["author"]["display_name"]
                                      for a in (w.get("authorships") or [])[:4]],
                          "venue": ((w.get("primary_location") or {}).get("source") or {})
                                    .get("display_name"), "found_in": tag}
ANCHORS = ["10.1137/21M139356X", "10.1016/j.patcog.2019.107192",
           "10.1038/s41597-024-04319-4", "10.1038/s41562-025-02325-z",
           "10.1038/s41467-025-67463-4", "10.1007/s11786-017-0329-x",
           "10.1007/s11786-021-00520-5", "10.18653/v1/N19-1156",
           "10.1126/sciadv.adg6175"]
for a in ANCHORS:
    if a not in cands:
        cands[a] = {"doi": a, "title": "", "year": None, "authors": [],
                    "venue": None, "found_in": "anchor"}

sess = requests.Session()
lines = [f"# crossref_check.txt — {TODAY} — all DOIs of lit candidates verified one-by-one"]
rows = []
ok = fail = nodoi = 0
for key, c in sorted(cands.items()):
    doi = c.get("doi")
    if not doi:
        nodoi += 1
        lines.append(f"NO-DOI\t{c['title'][:80]} (skipped, not Crossref-verifiable)")
        continue
    r = sess.get(f"https://api.crossref.org/works/{doi}", headers=UA, timeout=60)
    if r.status_code == 200:
        ok += 1
        m = r.json()["message"]
        title = (m.get("title") or [""])[0]
        venue = (m.get("container-title") or [""])[0]
        yr = ""
        for k in ("published-print", "published-online", "issued", "created"):
            if m.get(k, {}).get("date-parts"):
                yr = m[k]["date-parts"][0][0]; break
        auth = "; ".join(a.get("family", "") for a in m.get("author", [])[:6])
        c2 = dict(c); c2.update(crf_title=title, crf_venue=venue, crf_year=yr,
                        crf_authors=auth, crf_vol=m.get("volume", ""),
                        crf_issue=m.get("issue", ""), crf_pages=m.get("page", ""),
                        crf_status="OK")
        rows.append(c2)
        lines.append(f"OK\t{doi}\t{yr}\t{auth}\t{venue}\t{title[:90]}")
    else:
        fail += 1
        c2 = dict(c); c2.update(crf_status=f"FAIL:{r.status_code}"); rows.append(c2)
        lines.append(f"FAIL\t{doi}\tHTTP {r.status_code}\t{c['title'][:80]}")
    time.sleep(0.15)

with open(os.path.join(RES, "crossref_check.txt"), "w") as f:
    f.write("\n".join(lines) + "\n")
hdr = ["doi", "crf_title", "crf_year", "crf_authors", "crf_venue", "crf_vol",
       "crf_issue", "crf_pages", "title", "year", "authors", "venue", "found_in", "crf_status"]
with open(os.path.join(RES, "lit_candidates.tsv"), "w") as f:
    f.write("\t".join(hdr) + "\n")
    for c in rows:
        f.write("\t".join(str(c.get(h, "")).replace("\t", " ") for h in hdr) + "\n")
print(f"crossref: OK={ok} FAIL={fail} noDOI={nodoi}")

KW = ["periodic", "circular", "seriation", "seriate", "robinson", "typolog",
      "wals", "universal", "phylogen", "m.d.s", "mds", "arrangement",
      "embedding", "geometr", "tree", "genealog", "language"]
def score(c):
    t = (c.get("crf_title") or c.get("title") or "").lower()
    return sum(2 if k in t else 0 for k in KW[:9]) + sum(1 for k in KW[9:])
short = sorted(rows, key=score, reverse=True)[:32]
print("shortlist (title score desc):")
for c in short:
    print(f"  {c.get('crf_year')} | {c.get('crf_authors','?')[:40]} | "
          f"{(c.get('crf_title') or c.get('title'))[:70]} | {c.get('doi')}")
