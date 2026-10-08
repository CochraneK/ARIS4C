# Host-side (orchestrator) helper, 2026-09-30.
# Computes the reproducible expected initial-letter distribution (pilot #5)
# from the frozen ChineseNames 2025.8 familyname dataset.
# Input : data/chinenames_pkg/familyname.csv (dumped by chinenames_dump_rda.py)
# Output: data/chinenames_dist.json
import json
import csv
from collections import defaultdict

rows = list(csv.DictReader(open("data/chinenames_pkg/familyname.csv", encoding="utf-8")))
ALPHA = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
tot = 0.0
dist = defaultdict(float)
unknown = 0.0
top = []
for r in rows:
    try:
        n = float(r["n.1930_2008"] or 0)
    except ValueError:
        n = 0.0
    ini = (r.get("initial") or "").strip().upper()
    if ini[:1] in ALPHA:
        dist[ini[:1]] += n
    else:
        unknown += n
    tot += n
    top.append((r.get("surname", ""), r.get("compound", ""), ini, n))
top.sort(key=lambda x: -x[3])
out = {
    "source": "ChineseNames 2025.8 (CRAN; frozen tarball data/chinenames_pkg.tar.gz, 359498 bytes, pkg date 2025-08-15)",
    "file": "familyname.csv (dumped from familyname.rda via chinenames_dump_rda.py, pyreadr 0.5.7)",
    "rows": len(rows),
    "total": tot,
    "initial_dist": {L: round(v / tot, 6) for L, v in sorted(dist.items()) if tot},
    "unknown_initial_share": round(unknown / tot, 6) if tot else None,
    "top20_surnames": [[s, c, i, round(n)] for s, c, i, n in top[:20]],
}
json.dump(out, open("data/chinenames_dist.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("ROWS", len(rows), "TOTAL", round(tot))
print("INITIALS", len(dist), "UNKNOWN_SHARE", out["unknown_initial_share"])
for L in sorted(dist):
    print("  %s %.4f" % (L, dist[L] / tot))
print("TOP5", [(s, i) for s, c, i, n in top[:5]])
print("PARSE-DONE")
