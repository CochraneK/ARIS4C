import csv, json
from collections import Counter
sub, res = list(csv.DictReader(open("data/stage3b/audit_subset.csv", encoding="utf-8"))), list(csv.DictReader(open("data/stage3b/doi_match_results.csv", encoding="utf-8")))
spot, den = json.load(open("data/stage3b/title_spotcheck.json")), json.load(open("data/stage3b/denominator_reprobe.json"))
lookup = json.load(open("data/stage3b/rw_subset_lookup.json"))
nd = lambda s: next((s[len(p):] for p in ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "http://dx.doi.org/", "doi:") if s.startswith(p)), s)
raw = list(csv.reader(open("data/rw_e1_mapping.csv", encoding="utf-8")))
ri = next(i for i, h in enumerate(h.strip().lower() for h in raw[3]) if "reason" in h)
mapped = {r[ri].strip() for r in raw[4:] if len(r) > ri and r[ri].strip()}
ru = Counter(x.strip().lower() for r in sub for x in (lookup.get(nd(r["doi"].strip().lower())) or {}).get("reasons", []))
unm, bu = sorted(k for k in ru if k not in mapped), Counter(r["bucket"] for r in sub)
n = len(res); m = sum(1 for r in res if r["matched"] == "true"); cov = round(m / n, 4)
ur = [r for r in res if r["matched"] == "false"]
byy, ty, bys, ts = Counter(r["orig_year"] for r in ur), Counter(r["orig_year"] for r in res), Counter(r["subject"] for r in ur), Counter(r["subject"] for r in res)
g = len(ur) / n; sy = {y: round(byy[y] / ty[y], 3) for y in byy if ty[y] >= 5 and byy[y] / ty[y] > 2 * g}
ss, dr = {s: round(bys[s] / ts[s], 3) for s in bys if ts[s] >= 5 and bys[s] / ts[s] > 2 * g}, den["drift_pct"]
lims = (["denominator drift %s%% >= 0.5%% (noted; re-pin next stage)" % dr] if abs(dr) >= 0.5 else []) + (["systemic unmatched year(s): %s" % sy] if sy else []) + (["systemic unmatched subject(s): %s" % ss] if ss else []) + (["unmapped reason(s): %s" % unm] if unm else [])
v = "PASS" if cov >= 0.85 and not unm and not sy and not ss else ("PASS_WITH_LIMITATIONS" if cov >= 0.70 else "FAIL")
json.dump({"criteria": {"coverage_pass": ">=0.85", "coverage_pwl": ">=0.70 and <0.85", "coverage_fail": "<0.70", "unmapped_reasons_must": 0, "systemic_rule": "no single year/subject unmatched rate >2x global (group n>=5)", "denom": "drift<0.5% note only; >=0.5% -> limitation"}, "values": {"n": n, "matched": m, "coverage": cov, "unmatched": len(ur), "unmatched_dois": [r["doi"] for r in ur], "unmatched_by_year": dict(byy), "year_totals": dict(ty), "unmatched_by_subject": dict(bys), "subject_totals": dict(ts), "systemic_years": sy, "systemic_subjects": ss, "bucket_dist": dict(bu), "unmapped_reasons": unm, "denominator": {"frozen": den["frozen"], "new": den["new_count"], "drift_pct": dr}, "title_spotcheck": {"queried": spot["cases_queried"], "http400": spot.get("http400", 0), "found_exact": spot["found_exact"], "found_rate": spot["found_rate"], "any_found": sum(1 for c in spot["cases"] if c["any_result"])}}, "verdict": v, "limitations": lims, "unmatched_cases_pointer": "data/stage3b/doi_match_results.csv (matched=false rows)", "evidence": ["data/stage3b/_evidence/batch1.json", "data/stage3b/_evidence/batch2.json", "data/stage3b/_evidence/batch3.json", "data/stage3b/_evidence/denominator.json", "data/stage3b/_evidence/spotcheck_01..03.json"]}, open("data/stage3b/gate1_decision.json", "w"), indent=1, ensure_ascii=False)
json.dump({"subset_n": n, "bucket_dist": dict(bu), "distinct_reasons_in_subset": len(ru), "reason_mentions": sum(ru.values()), "mapping_reasons_total": len(mapped), "unmapped_reasons": unm, "unmapped_count": len(unm), "mapping_file": "data/rw_e1_mapping.csv (header line 4, skiprows=3)"}, open("data/stage3b/reason_coding_subset.json", "w"), indent=1, ensure_ascii=False); print("VERDICT", v, "cov", cov, "m", m, "unmapped", unm, "sy", sy, "ss", ss, "dr", dr, "spot_exact", spot["found_exact"], "/", spot["cases_queried"], "http400", spot.get("http400"))
