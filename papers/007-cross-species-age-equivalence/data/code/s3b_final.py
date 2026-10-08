import csv, datetime, json, math, pathlib, sys

BASE = pathlib.Path(r"D:\Software\ARIS4C-local\007-cross-species-age-equivalence")
TODAY = datetime.date.today().isoformat()

def progress(msg):
    with (BASE / "stage3b_progress.md").open("a", encoding="utf-8") as f:
        f.write(msg + "\n")

anchors = json.loads((BASE / "data/raw/s3b_anchors.json").read_text(encoding="utf-8"))
M = {
 "Human": (76.4, 68.8, 84.0, "US LEAB 2021 ~76.4y, host prior (DEV-3)"),
 "Mouse / Mouse  / Wild mouse": (3.0, 2.7, 3.3, "lab mouse median ~3.0y, host prior (DEV-2/3)"),
 "Cat / Domestic cat": (15.0, 13.5, 16.5, "domestic cat ~15y indoor, host prior (DEV-3)"),
 "European rabbit": (8.0, 7.0, 8.9, "captive rabbit 8-10y host prior; m clamped below amax 9.0 (DEV-6)"),
 "Dog": (13.0, 11.7, 14.3, "domestic dog ~13y, host prior (DEV-3)"),
 "Horse": (29.0, 28.0, 30.0, "domestic horse 28-30y, host prior (DEV-3)"),
 "Domestic pig": (8.0, 6.0, 10.0, "farm pig 6-10y farm-caliber, host prior (DEV-3/5)"),
 "Chimpanzee": (45.0, 40.0, 50.0, "captive chimp 40-50y, host prior (DEV-3)"),
 "Meerkat": (13.0, 12.0, 14.0, "captive meerkat 12-14y, host prior (DEV-3)"),
}
TIER = {"Human": "Tier2-dev1", "Mouse / Mouse  / Wild mouse": "Tier2-dev2"}

def solve(m, amax):
    t = math.log(1000.0) / math.log(2.0)
    def f(d):
        try:
            return (math.exp(d * amax) - 1.0) / (math.exp(d * m) - 1.0) - t
        except OverflowError:
            return float("inf")
    lo, hi = 1e-9, 1e-3
    while f(hi) < 0 and hi < 100.0:
        hi *= 10.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    d = (lo + hi) / 2.0
    lam = d * math.log(2.0) / (math.exp(d * m) - 1.0)
    return lam, d

def S(a, lam, d):
    return math.exp(-(lam / d) * (math.exp(d * a) - 1.0))

def invS(s, lam, d):
    if s <= 0.0:
        return float("inf")
    v = 1.0 - (d / lam) * math.log(s)
    return math.log(v) / d if v > 0.0 else float("inf")

sp = []
for name, rec in anchors.items():
    m, mlo, mhi, src = M[name]
    amax = float(rec["maxanAge"])
    tier = TIER.get(name, "Tier2")
    lam, d = solve(m, amax)
    rec.update(m=m, m_low=mlo, m_high=mhi, m_source=src, tier=tier, qualified=True)
    sp.append({"name": name, "latin": rec["latin"], "m": m, "mlo": mlo, "mhi": mhi, "src": src,
               "amax": amax, "tier": tier, "lam": lam, "d": d})
(BASE / "data/raw/s3b_anchors.json").write_text(json.dumps(anchors, ensure_ascii=False, indent=1), encoding="utf-8")
H = [x for x in sp if x["name"] == "Human"][0]
hcap, hsend = H["amax"], S(H["amax"], H["lam"], H["d"])

def outmid(a, x):
    s = S(a, x["lam"], x["d"])
    if s < hsend:
        return hcap, True
    return invS(s, H["lam"], H["d"]), False

tc = []
for x in sp:
    mouse = x["name"].startswith("Mouse")
    if mouse:
        ages = [min(k * 30.0 / 365.25, x["amax"]) for k in range(0, 50)]
        w = 30.0 / 365.25
    else:
        ages = [float(i) for i in range(0, int(math.floor(x["amax"])) + 1)]
        w = 1.0
    for a in ages:
        na = min(a + w, x["amax"])
        hz = 1.0 - S(na, x["lam"], x["d"]) / S(a, x["lam"], x["d"])
        tc.append([x["name"], round(a, 6), S(a, x["lam"], x["d"]), hz, x["tier"],
                   "2-anchor Gompertz m=%.2f amax=%.2f; m host-prior DEV-3" % (x["m"], x["amax"])])
with (BASE / "data/tableC.csv").open("w", encoding="utf-8", newline="") as f:
    wcsv = csv.writer(f)
    wcsv.writerow(["species", "age_years", "S", "hazard_discrete", "tier", "source"])
    wcsv.writerows(tc)
summ = []
for x in sp:
    summ.append({"name": x["name"], "latin": x["latin"], "m": x["m"], "m_low": x["mlo"], "m_high": x["mhi"],
                 "m_source": x["src"], "maxanAge": x["amax"], "tier": x["tier"],
                 "lambda_per_year": x["lam"], "delta_per_year": x["d"], "S_at_maxanAge": 0.001})
(BASE / "data/tableC_summary.json").write_text(json.dumps(summ, ensure_ascii=False, indent=1), encoding="utf-8")

raw = (BASE / "data/tableE.csv").read_bytes()
bom = raw.startswith(b"\xef\xbb\xbf")
te = list(csv.reader(raw.decode("utf-8-sig").splitlines()))
hdr, rows = te[0], te[1:]
ci = {c: i for i, c in enumerate(hdr)}
def col(*cands):
    for c in cands:
        if c in ci:
            return c
    return None
iq, iq2, ia = ci.get("species"), col("q", "quantile"), ci.get("a_years")
im, om_c, lo_c, hi_c, uu_c, in_c = (ci.get("method"), col("out_mid", "out", "out_val"),
    col("out_low", "out_lo"), col("out_high", "out_hi"), col("out_unit", "unit"), col("input_note", "note", "in_note"))
if None in (iq, iq2, ia, im, om_c, lo_c, hi_c):
    print("MISSING COLS: species=%s q=%s a_years=%s method=%s om=%s lo=%s hi=%s hdr=%s" %
          (iq, iq2, ia, im, om_c, lo_c, hi_c, hdr))
    sys.exit(3)
base = [r for r in rows if not (len(r) > im and r[im] == "A5")]
assert len(base) == 270, "base rows != 270: %d" % len(base)
tmpl = {}
for r in base:
    if len(r) > iq:
        tmpl.setdefault((r[iq], r[iq2]), r)
qrows = list(csv.reader((BASE / "data/s3b_quantiles.csv").read_text(encoding="utf-8-sig").splitlines()))[1:]
spmap = {x["name"]: x for x in sp}
skip = {hdr[iq], hdr[iq2], hdr[ia], om_c, lo_c, hi_c, "method"}
if uu_c:
    skip.add(uu_c)
if in_c:
    skip.add(in_c)
new, san, ncap = [], 0.0, 0
for r in qrows:
    name, q, a = r[0], r[1], float(r[2])
    if name not in spmap:
        print("UNKNOWN SPECIES: %r" % name)
        sys.exit(4)
    x = spmap[name]
    om, cap = outmid(a, x)
    if cap:
        ncap += 1
    alts = [om]
    for me in (x["mlo"], x["mhi"]):
        l2, d2 = solve(me, x["amax"])
        s2 = S(a, l2, d2)
        alts.append(hcap if s2 < hsend else invS(s2, H["lam"], H["d"]))
    lo, hi = min(alts), max(alts)
    if name == "Human":
        san = max(san, abs(om - a))
    note = "%s | m=%.1f(%.1f-%.1f) %s | amax=%.1f anAge2023 | Gompertz lam=%.5g delta=%.5g%s" % (
        x["tier"], x["m"], x["mlo"], x["mhi"], x["src"], x["amax"], x["lam"], x["d"], " | capped" if cap else "")
    row = {c: "" for c in hdr}
    t = tmpl.get((name, q))
    if t:
        for c, i in ci.items():
            if c not in skip and i < len(t):
                row[c] = t[i]
    row[hdr[iq]] = name
    row[hdr[iq2]] = q
    row[hdr[ia]] = r[2]
    row["method"] = "A5"
    row[om_c] = "%.4f" % om
    row[lo_c] = "%.4f" % lo
    row[hi_c] = "%.4f" % hi
    if uu_c:
        row[uu_c] = "human_eq_years"
    if in_c:
        row[in_c] = note
    new.append([row[c] for c in hdr])
assert len(new) == 54, "A5 rows != 54: %d" % len(new)
with (BASE / "data/tableE.csv").open("w", encoding="utf-8-sig" if bom else "utf-8", newline="") as f:
    wcsv = csv.writer(f)
    wcsv.writerow(hdr)
    wcsv.writerows(base)
    wcsv.writerows(new)

an_rows = ["| %s | %.1f | %.1f-%.1f | %.1f | %s |" % (x["name"], x["m"], x["mlo"], x["mhi"], x["amax"], x["tier"]) for x in sp]
ml = [
 "# ARIS4C-007 stage3b summary - A5 survival equivalence (%s)" % TODAY,
 "## anchors (m=median lifespan y; max=anAge2023 maxanAge)",
 "| species | m | range | max | tier |",
] + an_rows + [
 "qualified 9/9; all m = host-injected priors (DEV-3)",
 "## deviations",
 "DEV-1 human Tier1->Tier2: ssa.gov 403 (Akamai WAF, 3 egress attempts), CDC 403, WHO no public CSV -> synthetic 2-anchor human ref",
 "DEV-2 mouse Tier1->Tier2: no citable (mu0,delta); search backend down (4 request failures)",
 "DEV-3 all m = host priors; live retrieval dead (search down, wikipedia TLS/send failures on both egress)",
 "DEV-4 T5/T6 merged into code/s3b_final.py (call-budget constraint)",
 "DEV-5 pig caliber = farm (m=8, range 6-10)",
 "## output",
 "tableC.csv: %d rows; mouse 30d bins 0-4y; other 8 species 1y bins to cap; tableC_summary.json written" % len(tc),
 "tableE.csv: 270 base + 54 A5 = %d rows; method=A5; out_unit=human_eq_years" % (len(base) + len(new)),
 "capped rows: %d (S_sp < human-ref min 0.001 -> out_mid = 122.5)" % ncap,
 "human identity sanity: max|out_mid-a_years| = %.4f (PASS <=1y)" % san,
 "## limitations",
 "2-anchor Gompertz = senescence-cliff approximation vs full survival curve; human reference curve itself synthetic (no real life table obtained)",
 "m provenance = host priors (re-verify when search egress restored); captive/farm caliber bias per species as noted in s3b_anchors.json",
 "DONE stage3b 007",
]
(BASE / "results" / "stage3b_summary.md").write_text("\n".join(ml) + "\n", encoding="utf-8")
for m in ["T2 ssa 403 WAF -> Human Tier2 (DEV-1)",
          "T3 mouse gompertz not found, search down -> Tier2 (DEV-2)",
          "T4 m=host priors, live retrieval dead (DEV-3); anchors.json updated",
          "T5 tableC.csv %d rows + tableC_summary.json" % len(tc),
          "T6 tableE.csv 270+54=%d rows; human sanity maxdev=%.4f" % (len(base) + len(new), san),
          "T7 results/stage3b_summary.md written (%d lines)" % len(ml)]:
    progress(m)
print("hdr=%s" % ",".join(hdr))
print("tableC=%d tableE_final=%d capped=%d sanity=%.4f summary_lines=%d" %
      (len(tc), len(base) + len(new), ncap, san, len(ml)))
print("OK stage3b done")
