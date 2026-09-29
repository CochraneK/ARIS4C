
# ---- pair summary (window 1816-2016, clipped) ----
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
print("pairs:", len(pairs), "metropoles:", len(metros), metros[:20])
top = [(r["mp_name"], r["col_name"], r["first"], r["last"], r["dur"]) for r in pairs[:25]]
for t in top:
    print("PAIR", t)

# ---- OWID: age of electoral democracy (decolonization-era cross-check) ----
owid_lines = open(os.path.join(EX, "owid_age_of_electoral_democracy.csv"), encoding="utf-8").read().splitlines()
hdr = [h.strip() for h in owid_lines[0].split(",")]
print("OWID header:", hdr[:8], "rows:", len(owid_lines) - 1)
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
print("owid entities with data:", len(first_elec), "sample:", list(first_elec.items())[:5])

# ---- OpenAlex country list (name -> ISO2) ----
import time, urllib.request, urllib.parse as up
UA = {"User-Agent": "aris4c-003-stage2/0.1 (local research)"}
cpath = "data/raw/countries_oa.json"
if not os.path.exists(cpath):
    with urllib.request.urlopen(urllib.request.Request("https://api.openalex.org/countries?per-page=300", headers=UA), timeout=90) as r:
        open(cpath, "wb").write(r.read())
    time.sleep(2)
cj = json.load(open(cpath, encoding="utf-8"))
oa_countries = {}
for c in cj.get("results", []):
    oa_countries[c["display_name"].lower()] = (c["display_name"], c["id"].split("/")[-1])
print("oa countries:", len(oa_countries))
