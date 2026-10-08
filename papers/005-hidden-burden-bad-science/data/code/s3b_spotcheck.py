import csv, json, time, hashlib, urllib.request, urllib.parse
MAILTO = "aris4c005@example.org"
def get(url):
    for s in (0, 30, 60, 120, 240):
        if s: time.sleep(s)
        try:
            req = urllib.request.Request(url, headers={"mailto": MAILTO})
            return json.loads(urllib.request.urlopen(req, timeout=120).read().decode())
        except Exception as e:
            if "429" in str(e): continue
            if getattr(e, "code", 0) == 400: print("HTTP400", e.read().decode()[:300]); return None
            raise
res = list(csv.DictReader(open("data/stage3b/doi_match_results.csv", encoding="utf-8")))
lookup = json.load(open("data/stage3b/rw_subset_lookup.json"))
unm = sorted((r for r in res if r["matched"] == "false"), key=lambda r: hashlib.sha256(("20261008|" + r["doi"].strip()).encode()).hexdigest())
pool = [(r, (lookup.get(r["doi"].strip().lower()) or {}).get("title")) for r in unm]
cases, skipped = [], sum(1 for _, t in pool if not t)
for r, t in [x for x in pool if x[1]][:10]:
    u = "https://api.openalex.org/works?filter=title.search:" + urllib.parse.quote(t) + "&per-page=3&mailto=" + MAILTO; js = get(u)
    tops = [{"id": w.get("id"), "title": w.get("display_name"), "year": w.get("publication_year")} for w in (js or {}).get("results", [])[:3]]
    cases.append({"doi": r["doi"], "orig_year": r["orig_year"], "stratum": r["stratum"], "rw_title": t, "query": u, "error": js is None, "found": any(" ".join((x.get("title") or "").lower().split()) == " ".join(t.lower().split()) for x in tops), "any_result": bool(tops), "top3": tops}); json.dump(js, open("data/stage3b/_evidence/spotcheck_%02d.json" % len(cases), "w"), ensure_ascii=False) if js is not None else None
json.dump({"seed": "20261008", "unmatched_total": len(unm), "cases_queried": len(cases), "skipped_no_rw_title": skipped, "http400": sum(1 for c in cases if c["error"]), "found_exact": sum(1 for c in cases if c["found"]), "found_rate": round(sum(1 for c in cases if c["found"]) / len(cases), 3) if cases else None, "any_rate": round(sum(1 for c in cases if c["any_result"]) / len(cases), 3) if cases else None, "cases": cases}, open("data/stage3b/title_spotcheck.json", "w"), indent=1, ensure_ascii=False)
print("unmatched:", len(unm), "queried:", len(cases), "exact:", sum(1 for c in cases if c["found"]), "any:", sum(1 for c in cases if c["any_result"]), "skipped:", skipped, "http400:", sum(1 for c in cases if c["error"]))
