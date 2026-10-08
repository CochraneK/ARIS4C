import csv, json, hashlib, os
def stratum(y):
    return "2000-04" if y <= 2004 else "2005-09" if y <= 2009 else "2010-14" if y <= 2014 else "2015-19" if y <= 2019 else "2020-24" if y <= 2024 else "2025"
rows = [r for r in csv.DictReader(open("data/stage3/e1_numerators.csv", encoding="utf-8")) if (r.get("doi") or "").strip()]
assert len(rows) == 60348, len(rows)
out = [r for r in rows if not (2000 <= int(r["orig_year"]) <= 2025)]
for r in rows:
    r["stratum"] = stratum(int(r["orig_year"])); r["h"] = hashlib.sha256(("20261008|" + r["doi"].strip()).encode()).hexdigest()
order = ["2000-04", "2005-09", "2010-14", "2015-19", "2020-24", "2025"]
by = {s: sorted((r for r in rows if r["stratum"] == s), key=lambda x: x["h"]) for s in order}
q = {s: (max(1, round(len(by[s]) / len(rows) * 300)) if by[s] else 0) for s in order}
q[max(order, key=lambda s: len(by[s]))] += 300 - sum(q.values())
sel = [r for s in order for r in by[s][:q[s]]]
assert len(sel) == 300, len(sel)
os.makedirs("data/stage3b", exist_ok=True)
with open("data/stage3b/audit_subset.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["doi", "orig_year", "stratum", "subject", "country", "bucket", "n_reasons"])
    [w.writerow([r["doi"], r["orig_year"], r["stratum"], r["subject"], r["country"], r["bucket"], r["n_reasons"]]) for r in sel]
json.dump({"seed": "20261008", "total_with_doi": len(rows), "year_range_violations": len(out), "stratum_sizes": {s: len(by[s]) for s in order}, "quotas": q, "hash_key": "sha256(20261008|doi) asc within stratum"}, open("data/stage3b/subset_selection.json", "w"), indent=1)
print("ok", len(sel), q, "viol:", len(out))
