import csv, pathlib

BASE = pathlib.Path(r"D:\Software\ARIS4C-local\007-cross-species-age-equivalence")
p = BASE / "data" / "suppl" / "anage_lu2023_snapshot.csv"
with p.open("r", encoding="utf-8", errors="replace") as f:
    rows = [next(csv.reader(f)) for _ in range(3)]
for i, r in enumerate(rows[:2]):
    print("row%d ncols=%d first3=%s" % (i, len(r), r[:3]))
hdr = None
for r in rows:
    if any("Latin" in c for c in r):
        hdr = r
        break
if hdr is None:
    hdr = rows[1]
hits = [h for h in hdr if any(k in h.lower() for k in ("age", "lifespan", "median", "longev", "surviv"))]
print("cands: " + " | ".join(h[:28] for h in hits[:25]))
