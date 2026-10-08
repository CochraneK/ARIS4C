import csv, json, os, time, urllib.request, urllib.error
MAILTO = "aris4c005@example.org"
API = "https://api.openalex.org/works"
QUERIES = 0
def get(url):
    global QUERIES
    for s in (0, 30, 60, 120, 240):
        if s: time.sleep(s)
        QUERIES += 1
        if QUERIES > 20: raise RuntimeError("hard cap 20 queries reached")
        try:
            req = urllib.request.Request(url, headers={"mailto": MAILTO})
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429: continue
            raise
def norm(d):
    d = (d or "").strip().lower()
    for p in ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "http://dx.doi.org/", "doi:"):
        if d.startswith(p): d = d[len(p):]
    return d
RWP = "data/raw/rw_official/retraction_watch.csv"
sub = list(csv.DictReader(open("data/stage3b/audit_subset.csv", encoding="utf-8"))); assert len(sub) == 300, len(sub)
S = {norm(r["doi"]) for r in sub}; lookup = {}
with open(RWP, encoding="utf-8-sig", errors="replace") as f:
    for row in csv.DictReader(f):
        d = norm(row.get("OriginalPaperDOI"))
        if d in S and d not in lookup:
            lookup[d] = {"title": (row.get("Title") or "").strip(), "reasons": [x.strip() for x in (row.get("Reason") or "").split(";") if x.strip()]}
json.dump(lookup, open("data/stage3b/rw_subset_lookup.json", "w"), ensure_ascii=False); print("rw_lookup:", len(lookup), "with_title:", sum(1 for v in lookup.values() if v["title"]))
os.makedirs("data/stage3b/_evidence", exist_ok=True); found = {}
for b in range(3):
    ds = [norm(r["doi"]) for r in sub[b * 100:(b + 1) * 100] if norm(r["doi"])]
    url = API + "?filter=doi:" + "|".join(ds) + "&per-page=200&select=id,doi,display_name,publication_year&mailto=" + MAILTO
    js = get(url)
    json.dump(js, open("data/stage3b/_evidence/batch%d.json" % (b + 1), "w"), ensure_ascii=False)
    for w in js.get("results", []):
        d = norm(w.get("doi")); found.setdefault(d, {"work_id": w.get("id"), "oa_title": w.get("display_name"), "oa_year": w.get("publication_year")}) if d else None
rows = []
for r in sub:
    d = norm(r["doi"]); m = found.get(d); t = (lookup.get(d) or {}).get("title", "")
    a = ((m or {}).get("oa_title") or "").strip().lower().replace("  ", " "); b2 = t.strip().lower().replace("  ", " ")
    tm = ("exact" if a and a == b2 else "prefix40" if a and b2 and a[:40] == b2[:40] and min(len(a), len(b2)) >= 20 else "no") if m else ""
    rows.append(dict(r, matched="true" if m else "false", work_id=(m or {}).get("work_id") or "", oa_title=(m or {}).get("oa_title") or "", oa_year=str((m or {}).get("oa_year") or ""), year_match="true" if m and str((m or {}).get("oa_year")) == r["orig_year"] else "false", rw_title=t, title_match=tm))
with open("data/stage3b/doi_match_results.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
js = get(API + "?filter=publication_year:2000-2025&per-page=1&mailto=" + MAILTO)
json.dump(js, open("data/stage3b/_evidence/denominator.json", "w"))
nc = js["meta"]["count"]
json.dump({"frozen": 222714158, "new_count": nc, "drift_pct": round((nc - 222714158) / 222714158 * 100, 6), "query": "GET /works?filter=publication_year:2000-2025&per-page=1&mailto=" + MAILTO, "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "mailto": MAILTO, "evidence": "data/stage3b/_evidence/denominator.json"}, open("data/stage3b/denominator_reprobe.json", "w"), indent=1)
print("matched:", sum(1 for r in rows if r["matched"] == "true"), "of", len(rows), "queries:", QUERIES, "denom:", nc, "drift_pct:", round((nc - 222714158) / 222714158 * 100, 6))
