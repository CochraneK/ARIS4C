# exposure_parse_full (chunk A) — Path A: COW Entities.pdf -> ownership intervals
# verbatim reuse of code/exposure_parse.py (executor, died 2026-09-29 21:51 before run)
import csv, io, json, os, re
from collections import defaultdict

EX = "data/raw/exposure"
RAWC = EX + "/raw_csv"

def pdf_text(path, maxlen=1000000):
    b = open(path, "rb").read()
    try:
        from pypdf import PdfReader
        r = PdfReader(io.BytesIO(b))
        return "\n".join((p.extract_text() or "") for p in r.pages)[:maxlen]
    except Exception as e:
        print("pypdf fail:", str(e)[:80])
    out = []
    for m in re.finditer(rb"\((.*?)\)\s*Tj", b, re.S):
        out.append(m.group(1).decode("latin-1", "replace"))
    for m in re.finditer(rb"\[(.*?)\]\s*TJ", b, re.S):
        out.append("".join(x.decode("latin-1", "replace") for x in re.findall(rb"\((.*?)\)", m.group(1), re.S)))
    return "\n".join(out)[:maxlen]

ent = pdf_text(os.path.join(RAWC, "Entities.pdf"))
open(os.path.join(EX, "entities_full.txt"), "w", encoding="utf-8").write(ent)
print("entities_full chars:", len(ent))

YR = r"(?:1[7-9]\d{2}|20\d{2})"
rows, names = [], {}
for line in ent.splitlines():
    toks = line.split()
    if len(toks) < 6 or not toks[0].isdigit():
        continue
    for i in range(1, len(toks) - 2):
        if re.fullmatch(YR, toks[i]) and re.fullmatch(YR, toks[i + 1]):
            code, name = int(toks[0]), " ".join(toks[1:i])
            if code not in names:
                names[code] = name
            rows.append((code, name, int(toks[i]), int(toks[i + 1]), " ".join(toks[i + 2:])))
            break

def classify(status):
    m = re.match(r"^Became colony of (\d+)$", status)
    if m:
        return "colony", int(m.group(1))
    m = re.match(r"^Became part of (\d+)$", status)
    if m:
        return "part", int(m.group(1))
    m = re.match(r"^Occupied by (\d+)$", status)
    if m:
        return "occupied", int(m.group(1))
    return "other", None

print("parsed rows:", len(rows), "distinct entities:", len(names))
colony = defaultdict(list)   # (metropole, entity) -> [(b, e)]
occupied = defaultdict(list)
part = defaultdict(list)
status_kinds = defaultdict(int)
for code, name, b, e, status in rows:
    kind, other = classify(status)
    status_kinds[kind] += 1
    if kind == "colony":
        colony[(other, code)].append((b, e))
    elif kind == "occupied":
        occupied[(other, code)].append((b, e))
    elif kind == "part":
        part[(other, code)].append((b, e))
print("status kinds:", dict(status_kinds))
print("colony pairs:", len(colony), "occupied pairs:", len(occupied), "part pairs:", len(part))

def merge(ivs):
    ivs = sorted(ivs)
    out, cb, ce = [], None, None
    for b, e in ivs:
        if cb is None:
            cb, ce = b, e
        elif b <= ce + 1:
            ce = max(ce, e)
        else:
            out.append((cb, ce)); cb, ce = b, e
    if cb is not None:
        out.append((cb, ce))
    return out

# ---- Path A pair summary (window 1816-2016, clipped) ----
pairs = []
for (mp, entc), ivs in colony.items():
    m = merge([(max(b, 1816), min(e, 2016)) for b, e in ivs])
    dur = sum(e - b + 1 for b, e in m)
    occ = merge(occupied.get((mp, entc), []))
    occ_dur = sum(e - b + 1 for b, e in occ)
    pairs.append({
        "mp_code": mp, "mp_name": names.get(mp, "?"),
        "col_code": entc, "col_name": names.get(entc, "?"),
        "first": m[0][0], "last": m[-1][1], "dur": dur, "n_iv": len(m),
        "occ_dur": occ_dur, "intervals": ";".join("%d-%d" % (b, e) for b, e in m),
    })
pairs.sort(key=lambda r: (-r["dur"], r["mp_name"], r["col_name"]))
with open(os.path.join(EX, "exposure_pair_summary.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["mp_code", "mp_name", "col_code", "col_name", "first", "last", "dur", "n_iv", "occ_dur", "intervals"])
    w.writeheader(); w.writerows(pairs)
metros = sorted(set(r["mp_name"] for r in pairs))
print("PATHA pairs:", len(pairs), "metropoles:", len(metros))
print("PATHA metros:", metros)
for t in pairs[:10]:
    print("PAIR_A", t["mp_name"], "|", t["col_name"], t["first"], "-", t["last"], "dur=", t["dur"])

# ---- OWID: first year of (numerically coded) electoral democracy ----
owid_lines = open(os.path.join(EX, "owid_age_of_electoral_democracy.csv"), encoding="utf-8").read().splitlines()
hdr = [h.strip() for h in owid_lines[0].split(",")]
i_ent = next(i for i, h in enumerate(hdr) if h.lower() == "entity")
i_yr = next(i for i, h in enumerate(hdr) if h.lower() == "year")
i_met = next(i for i, h in enumerate(hdr) if h.lower() not in ("entity", "code", "year", "metric"))
first_elec = {}
for line in owid_lines[1:]:
    parts = line.split(",")
    if len(parts) <= max(i_ent, i_yr, i_met) or not parts[i_met].strip():
        continue
    try:
        yr, val = int(float(parts[i_yr])), float(parts[i_met])
    except ValueError:
        continue
    if val >= 0:
        e = parts[i_ent].strip()
        if e not in first_elec or yr < first_elec[e]:
            first_elec[e] = yr
with open(os.path.join(EX, "owid_first_electoral_year.tsv"), "w", encoding="utf-8", newline="") as f:
    f.write("entity\tfirst_electoral_year\n")
    for k in sorted(first_elec):
        f.write("%s\t%d\n" % (k, first_elec[k]))
print("OWID entities:", len(first_elec), "sample:", list(first_elec.items())[:5])

# ---- OpenAlex country list (name -> ISO2) ----
import time, urllib.request
UA = {"User-Agent": "aris4c-003-stage2/0.1 (local research)"}
cpath = "data/raw/countries_oa.json"
if not os.path.exists(cpath):
    allres, page = [], 1
    while True:
        url = "https://api.openalex.org/countries?per-page=200&page=%d" % page
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
            res = json.load(r).get("results", [])
        allres.extend(res)
        if len(res) < 200:
            break
        page += 1
        time.sleep(2)
    json.dump(allres, open(cpath, "w", encoding="utf-8"))
cj = json.load(open(cpath, encoding="utf-8"))
oa_countries = {c["display_name"].lower(): c["display_name"] for c in cj}
print("OA countries fetched:", len(oa_countries))

# ---- Path B: contcol master (DependL/DependH) -> metropole-colony intervals ----
b_iv = defaultdict(list); b_ct = defaultdict(int); b_ab = {}
with open(os.path.join(RAWC, "contcol.csv"), encoding="utf-8") as f:
    rd = csv.DictReader(f)
    for row in rd:
        b_ct[row["conttype"]] += 1
        b_ab[int(row["statehno"])] = row["statehab"]; b_ab[int(row["statelno"])] = row["statelab"]
        b, e = int(row["begin"]), int(row["end"])
        if int(row["dependl"]) > 0:
            b_iv[(int(row["statelno"]), int(row["dependl"]))].append((b, e))
        if int(row["dependh"]) > 0:
            b_iv[(int(row["statehno"]), int(row["dependh"]))].append((b, e))
pairsB = []
for (mp, cl), ivs in b_iv.items():
    m = merge([(max(b, 1816), min(e, 2016)) for b, e in ivs])
    pairsB.append({"mp": mp, "cl": cl, "first": m[0][0], "last": m[-1][1], "dur": sum(e - b + 1 for b, e in m)})
pairsB.sort(key=lambda r: -r["dur"])
with open(os.path.join(EX, "exposure_pair_summary_cow.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["mp", "cl", "first", "last", "dur"])
    w.writeheader(); w.writerows(pairsB)
print("PATHB pairs:", len(pairsB), "conttype:", dict(b_ct), "year range:", min(r['first'] for r in pairsB), "-", max(r['last'] for r in pairsB))
print("PATHB top:", [(b_ab.get(r['mp'],'?'), b_ab.get(r['cl'],'?'), r['first'], r['last']) for r in pairsB[:8]])

# ---- cross-check Path A (colony) vs Path B ----
a_set = {(mp, cl) for (mp, cl) in colony.keys()}
b_set = set(b_iv.keys())
print("XCHECK union:", len(a_set | b_set), "Aonly:", len(a_set - b_set), "Bonly:", len(b_set - a_set), "both:", len(a_set & b_set))
print("XCHECK Aonly sample:", sorted(a_set - b_set)[:8])
print("XCHECK Bonly sample:", sorted(b_set - a_set)[:8])
print("FULL DONE")
