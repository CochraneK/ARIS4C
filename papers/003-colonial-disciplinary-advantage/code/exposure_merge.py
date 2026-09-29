# exposure_merge.py — merge Path A + Path B pair tables with resolved names
import csv, os, re
from collections import defaultdict

EX = "data/raw/exposure"
RAWC = EX + "/raw_csv"

# name maps: entities (colonies) from entities_full.txt; state abbs from contcol master
names = {}
YR = r"(?:1[7-9]\d{2}|20\d{2})"
for line in open(os.path.join(EX, "entities_full.txt"), encoding="utf-8"):
    toks = line.split()
    if len(toks) < 6 or not toks[0].isdigit():
        continue
    for i in range(1, len(toks) - 2):
        if re.fullmatch(YR, toks[i]) and re.fullmatch(YR, toks[i + 1]):
            if int(toks[0]) not in names:
                names[int(toks[0])] = " ".join(toks[1:i])
            break
ab = {}
with open(os.path.join(RAWC, "contcol.csv"), encoding="utf-8") as f:
    for row in csv.DictReader(f):
        ab[int(row["statelno"])] = row["statelab"]
        ab[int(row["statehno"])] = row["statehab"]

def nm(code):
    return names.get(code) or ab.get(code) or "?"

merged = {}
with open(os.path.join(EX, "exposure_pair_summary.csv"), encoding="utf-8") as f:
    for r in csv.DictReader(f):
        key = (int(r["mp_code"]), int(r["col_code"]))
        merged.setdefault(key, {"first": int(r["first"]), "last": int(r["last"]), "dur": int(r["dur"]), "src": "A", "occ_dur": r["occ_dur"]})
nB = 0
with open(os.path.join(EX, "exposure_pair_summary_cow.csv"), encoding="utf-8") as f:
    for r in csv.DictReader(f):
        nB += 1
        key = (int(r["mp"]), int(r["cl"]))
        if key in merged:
            merged[key]["src"] = "both"
        else:
            merged[key] = {"first": int(r["first"]), "last": int(r["last"]), "dur": int(r["dur"]), "src": "B", "occ_dur": ""}
rows = []
for (mp, cl), v in merged.items():
    rows.append({"mp_code": mp, "mp_name": nm(mp), "col_code": cl, "col_name": nm(cl),
                 "first": v["first"], "last": v["last"], "dur": v["dur"], "src": v["src"], "occ_dur": v.get("occ_dur", "")})
rows.sort(key=lambda r: (-r["dur"], r["mp_name"], r["col_name"]))
with open(os.path.join(EX, "exposure_pair_merged.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["mp_code", "mp_name", "col_code", "col_name", "first", "last", "dur", "src", "occ_dur"])
    w.writeheader(); w.writerows(rows)
cnt = defaultdict(int)
for r in rows:
    cnt[r["src"]] += 1
print("MERGED rows:", len(rows), "by src:", dict(cnt))
unres = sorted(set(r["mp_name"] for r in rows if r["mp_name"] == "?") | set(r["col_name"] for r in rows if r["col_name"] == "?"))
print("unresolved codes:", unres[:20], "count:", len(unres))
print("metros resolved:", sorted(set(r["mp_name"] for r in rows if r["mp_name"] != "?")))
for r in rows[:12]:
    print("TOP", r["mp_name"], "|", r["col_name"], r["first"], "-", r["last"], "dur=", r["dur"], r["src"])
print("MERGE DONE")
