# -*- coding: utf-8 -*-
# ARIS4C-006 stage2 fix v2: T2'/T3'/T4/T5. 0 API queries. Prints <=20 lines.
# parse tiers: 5A direct CJK (ChineseNames familyname) = t1; 5B romanized surname-dict match = t2; else t3.
import json, math, csv, os, statistics as st
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = json.load(open(os.path.join(ROOT, "data/s2_pilot_works.json"), encoding="utf-8"))
dist = json.load(open(os.path.join(ROOT, "data/chinenames_dist.json"), encoding="utf-8"))

import importlib.util
spec = importlib.util.spec_from_file_location("sn006", os.path.join(ROOT, "data/surnames.py"))
SN = importlib.util.module_from_spec(spec); spec.loader.exec_module(SN)
SURN = SN.SURNAMES

fam_n, fam_ini, fam_comp, fam_single = {}, {}, set(), set()
with open(os.path.join(ROOT, "data/chinenames_pkg/familyname.csv"), encoding="utf-8") as f:
    for r in csv.DictReader(f):
        s = (r.get("surname") or "").strip()
        if not s: continue
        try: n = float(r.get("n.1930_2008") or 0)
        except Exception: n = 0.0
        fam_n[s] = n
        fam_ini[s] = (r.get("initial") or "").strip().lower()
        if len(s) == 2:
            try:
                if float(r.get("compound") or 0) == 1.0: fam_comp.add(s)
            except Exception: pass
        else:
            fam_single.add(s)
COMPS = fam_comp | set(k for k in SURN if len(k) == 2)

char_py = {}
with open(os.path.join(ROOT, "data/chinenames_pkg/givenname.csv"), encoding="utf-8") as f:
    rd = csv.reader(f); next(rd)
    for row in rd:
        if len(row) >= 2 and row[0].strip():
            py = row[1].strip().lower().rstrip("012345")
            if py: char_py[row[0].strip()] = py

def py_of(sur):
    if sur in SURN: return SURN[sur].lower()
    parts = [char_py.get(c) for c in sur]
    return "".join(parts) if all(parts) else None

surn_map = defaultdict(list)
for s, n in fam_n.items():
    py = py_of(s)
    if py: surn_map[py].append((s, n))
surn_py_set = set(surn_map.keys())
def top_cjk(py):
    lst = surn_map.get(py, [])
    if not lst: return None, 0
    lst.sort(key=lambda t: -t[1])
    return lst[0][0], len(lst)

def is_cjk(s):
    s = (s or "").strip()
    return bool(s) and all("\u4e00" <= c <= "\u9fff" for c in s)

def parse(name):
    """-> (tier, sortkey_pinyin, cjk_surname, n_cjk_cands, both_match)"""
    name = (name or "").strip()
    if not name: return (3, None, None, 0, False)
    if is_cjk(name):
        if name[:2] in COMPS: sur = name[:2]
        elif name[0] in fam_single: sur = name[0]
        else: return (3, None, None, 0, False)
        py = py_of(sur)
        if py is None: return (3, sur, sur, 1, False)
        return (1, py, sur, 1, False)
    toks = [t.strip().lower() for t in name.replace(",", " ").split()]
    toks = [t for t in toks if t]
    if len(toks) == 2:
        m = [t for t in toks if t in surn_py_set]
        if len(m) == 1:
            cjk, nc = top_cjk(m[0]); return (2, m[0], cjk, nc, False)
        if len(m) == 2:
            cjk, nc = top_cjk(toks[0]); return (2, toks[0], cjk, nc, True)
        return (3, None, None, 0, False)
    if len(toks) == 3:
        two = toks[0] + toks[1]
        if two in surn_py_set:
            cjk, nc = top_cjk(two); return (2, two, cjk, nc, False)
        return (3, None, None, 0, False)
    return (3, None, None, 0, False)

tot = sum(v for v in fam_n.values() if v > 0)
ps = [v / tot for v in fam_n.values() if v > 0]
MAXN = 64
dp = [0.0] * (MAXN + 1); dp[0] = 1.0
for p in ps:
    for k in range(MAXN, 0, -1):
        dp[k] += dp[k - 1] * p
def exp_of(n): return dp[n] if n <= MAXN else dp[MAXN]
def sorted_ok(ks): return all(ks[i] <= ks[i + 1] for i in range(len(ks) - 1))
def excess(ob, e):
    if e is None or e >= 1: return None
    return round((ob - e) / (1.0 - e), 4)

res = {"snapshot": "2026-09-30",
       "source": "data/s2_pilot_works.json (prior-run fetch; 0 new queries this run)",
       "estimator": "Obs=1 if all author surnames parsed t1/t2 and pinyin surname keys non-decreasing in listed order; Exp=h_n(pop surname dist, familyname n.1930_2008 normalized)=P(i.i.d. population surnames come out sorted), tie-adjusted by construction, team-size dependent; Excess=(Obs-Exp)/(1-Exp); context=journal x field x year, cell n<30 degraded to field-year",
       "parse_rule": "5A: CJK name, longest match vs ChineseNames (2-char compound in fam_comp|SURN else 1-char in fam_single) -> tier1, key=surname pinyin (SURN duoyin override else per-char givenname); 5B: romanized, 2 tokens, token in surname-pinyin set -> tier2 (both tokens match -> surname=token0, flagged); 3 tokens -> 2-token compound surname else tier3; else tier3"}

counts = D["counts"]
pages = {k: int(math.ceil(v / 200.0)) for k, v in counts.items()}
res["s1_panel_and_budget"] = {
    "counts_2010_2024": counts, "pages_count_over_200": pages, "sum_pages": sum(pages.values()),
    "cap_queries": 5000, "subsamp_rule": "published asc, take 1 of every k pages (deterministic)",
    "k": 3, "est_queries_k3": sum(int(math.ceil(p / 3.0)) for p in pages.values()),
    "host_precompute": "math713 physics1702 nursing213 medicine8053 sum10681",
    "field_filter_form": "primary_topic.field.id:<fid> (probe ok; probe-key cosmetic typo only)"}

FIELDS = ["math", "physics", "nursing", "medicine"]
names_all, work_rows = [], {}
for k in FIELDS:
    rows = []
    for w in D["fields"][k]["results"]:
        names = [(a.get("raw_author_name") or (a.get("author") or {}).get("display_name") or "")
                 for a in w.get("authorships", [])]
        pl = w.get("primary_location") or {}
        jr = ((pl.get("source") or {}).get("display_name")) or "NA"
        rows.append({"id": w.get("id"), "year": w.get("publication_year"), "jr": jr, "names": names, "n": len(names)})
        for nm in names:
            t, s, cjk, nc, bm = parse(nm)
            names_all.append((k, nm, t, s, cjk, nc, bm))
    work_rows[k] = rows

td = Counter(t for x in names_all for t in (x[2],))
cjk_n = sum(1 for x in names_all if is_cjk(x[1]))
t12 = [x for x in names_all if x[2] in (1, 2)]
both_n = sum(1 for x in names_all if x[6])
t3_n = td.get(3, 0)
spot = []
for k in FIELDS:
    for x in [y for y in names_all if y[0] == k and y[2] in (1, 2)][:13]:
        if len(spot) < 50:
            spot.append({"f": k, "name": x[1], "tier": x[2], "key": x[3], "cjk_top": x[4], "n_cands": x[5], "both": x[6]})
inok = sum(1 for x in t12 if x[2] == 1 and x[3] and fam_ini.get(x[4]) and fam_ini[x[4]][0] == x[3][0].lower())
res["s3_parsing"] = {"n_names": len(names_all),
    "tier_dist": {"t0_empty": 0, "tier1_5A_cjk": td.get(1, 0), "tier2_5B_rom": td.get(2, 0), "tier3_excluded": t3_n},
    "cjk_names": cjk_n, "romanized_names": len(names_all) - cjk_n,
    "both_token_match_flagged": both_n,
    "t12_coverage_all": round(len(t12) / max(len(names_all), 1), 4),
    "t1_pinyin_initial_matches_famcsv": inok,
    "surnames_in_famcsv": len(fam_n), "surn_pinyin_set": len(surn_py_set), "char_pinyin": len(char_py),
    "spot_check_le50": spot}

ctx, ctxw = {}, {}
fsum = {k: dict(valid=0, obs=0.0, exp=0.0, v2=0, o2=0.0, e2=0.0, n2=0, single=0, multi=0) for k in FIELDS}
for k in FIELDS:
    for r in work_rows[k]:
        n = r["n"]
        if n == 1:
            fsum[k]["single"] += 1; continue
        fsum[k]["multi"] += 1
        fsum[k]["n2"] += (1 if n == 2 else 0)
        ps_ = [parse(nm) for nm in r["names"]]
        if any(p[0] not in (1, 2) or not p[1] for p in ps_): continue
        keys = [p[1] for p in ps_]
        ob = 1.0 if sorted_ok(keys) else 0.0
        e = exp_of(n)
        f = fsum[k]; f["valid"] += 1; f["obs"] += ob; f["exp"] += e
        if n >= 3: f["v2"] += 1; f["o2"] += ob; f["e2"] += e
        for key in ((k, r["jr"], r["year"]), (k, "FIELD", r["year"])):
            c = ctx.setdefault(key, [0, 0.0, 0.0]); c[0] += 1; c[1] += ob; c[2] += e
            ctxw.setdefault(key, []).append((ob, e))

cells = []
for key in sorted(ctx.keys()):
    k, jr, yr = key
    n, ob, e = ctx[key]
    lvl = "field-year" if jr == "FIELD" else ("journal" if n >= 30 else "degraded-to-field-year")
    cells.append({"field": k, "journal": None if jr == "FIELD" else jr, "year": yr, "n": n,
                  "obs": round(ob / n, 4), "exp": round(e / n, 4), "excess": excess(ob / n, e / n), "level": lvl})
fy = {}
for key in ctx:
    k, jr, yr = key
    if jr != "FIELD": continue
    n, ob, e = ctx[key]
    fy[(k, yr)] = excess(ob / n, e / n)
work_exc = []
for key in ctx:
    k, jr, yr = key
    if jr == "FIELD": continue
    n, ob, e = ctx[key]
    v = excess(ob / n, e / n) if n >= 30 else fy.get((k, yr))
    if v is not None: work_exc.extend([v] * n)
jex = [c["excess"] for c in cells if c["excess"] is not None]
res["s2_excess"] = {
    "n_cells": len(cells), "n_journal_cells": sum(1 for c in cells if c["journal"]),
    "cells": cells,
    "across_contexts": {
        "n": len(jex), "var": round(st.pvariance(jex), 5) if len(jex) > 1 else None,
        "min": min(jex) if jex else None, "max": max(jex) if jex else None,
        "range": round(max(jex) - min(jex), 4) if jex else None,
        "p10": round(st.quantiles(jex, n=10)[0], 4) if len(jex) >= 10 else None,
        "p50": round(st.median(jex), 4) if jex else None,
        "p90": round(st.quantiles(jex, n=10)[8], 4) if len(jex) >= 10 else None},
    "work_level_assigned": {"n": len(work_exc),
        "p10": round(st.quantiles(work_exc, n=10)[0], 4) if len(work_exc) >= 10 else None,
        "p50": round(st.median(work_exc), 4) if work_exc else None,
        "p90": round(st.quantiles(work_exc, n=10)[8], 4) if len(work_exc) >= 10 else None,
        "min": min(work_exc) if work_exc else None, "max": max(work_exc) if work_exc else None}}
jcells = [(key, c) for key, c in ctx.items() if key[1] != "FIELD"]
if jcells:
    bk = max(jcells, key=lambda t: t[1][0])[0]; n, ob, e = max(jcells, key=lambda t: t[1][0])[1]
    looms = []
    for obi, ei in ctxw[bk]:
        if n < 2: break
        ob2 = (ob - obi) / (n - 1); e2 = (e - ei) / (n - 1)
        looms.append(abs(excess(ob2, e2) - excess(ob / n, e / n)))
    res["s2_excess"]["loo_largest_cell"] = {"cell": [bk[0], bk[1], bk[2]], "n": n,
        "max_abs_delta": round(max(looms), 5) if looms else None}
else:
    res["s2_excess"]["loo_largest_cell"] = None

per, aa, aa2 = {}, [], []
for k in FIELDS:
    f = fsum[k]
    ex = excess(f["obs"] / f["valid"], f["exp"] / f["valid"]) if f["valid"] else None
    ex2 = excess(f["o2"] / f["v2"], f["e2"] / f["v2"]) if f["v2"] else None
    per[k] = {"works": len(work_rows[k]), "single": f["single"], "multi": f["multi"], "n_two_auth": f["n2"],
              "valid": f["valid"], "valid_ex2": f["v2"],
              "obs_alpha": round(f["obs"] / f["valid"], 4) if f["valid"] else None,
              "exp_chance": round(f["exp"] / f["valid"], 4) if f["valid"] else None,
              "excess_alpha": ex,
              "obs_alpha_ex2": round(f["o2"] / f["v2"], 4) if f["v2"] else None,
              "excess_alpha_ex2": ex2}
    if ex is not None and ex2 is not None:
        aa.append(ex); aa2.append(ex2)
m1 = sum(aa) / len(aa) if aa else 0.0; m2 = sum(aa2) / len(aa2) if aa2 else 0.0
cov = sum((a - m1) * (b - m2) for a, b in zip(aa, aa2)) if aa else 0.0
den = math.sqrt(sum((a - m1) ** 2 for a in aa) * sum((b - m2) ** 2 for b in aa2)) if aa else 0.0
res["s4_stability"] = {"per_field": per,
    "pearson_r_excess_all_vs_ex2": round(cov / den, 4) if den > 0 else None,
    "max_abs_delta": round(max(abs(a - b) for a, b in zip(aa, aa2)), 4) if aa else None}

P = []
P.append("SETS fam=%d surnpy=%d charpy=%d" % (len(fam_n), len(surn_py_set), len(char_py)))
P.append("S1 pages=%s sum=%d est_k3=%d" % (pages, sum(pages.values()), res["s1_panel_and_budget"]["est_queries_k3"]))
for k in FIELDS:
    p = per[k]
    P.append("S2f %-8s multi=%3d v=%3d obs=%s exp=%s ex=%s | ex2v=%3d ex2=%s n2=%d" % (
        k, p["multi"], p["valid"], p["obs_alpha"], p["exp_chance"], p["excess_alpha"],
        p["valid_ex2"], p["excess_alpha_ex2"], p["n_two_auth"]))
P.append("S2 ctx n=%d j=%d var=%s min=%s p50=%s max=%s range=%s | worklvl n=%d p50=%s" % (
    res["s2_excess"]["n_cells"], res["s2_excess"]["n_journal_cells"],
    res["s2_excess"]["across_contexts"]["var"], res["s2_excess"]["across_contexts"]["min"],
    res["s2_excess"]["across_contexts"]["p50"], res["s2_excess"]["across_contexts"]["max"],
    res["s2_excess"]["across_contexts"]["range"], res["s2_excess"]["work_level_assigned"]["n"],
    res["s2_excess"]["work_level_assigned"]["p50"]))
loo = res["s2_excess"]["loo_largest_cell"]
P.append("S2b LOO %s n=%s max_abs_delta=%s" % (loo["cell"] if loo else None, loo["n"] if loo else None, loo["max_abs_delta"] if loo else None))
t = res["s3_parsing"]["tier_dist"]
P.append("S3 names=%d cjk=%d rom=%d t1=%d t2=%d t3=%d both=%d cov_all=%s inok=%d" % (
    res["s3_parsing"]["n_names"], res["s3_parsing"]["cjk_names"], res["s3_parsing"]["romanized_names"],
    t["tier1_5A_cjk"], t["tier2_5B_rom"], t["tier3_excluded"], both_n, res["s3_parsing"]["t12_coverage_all"], inok))
P.append("S4 pearson=%s maxdelta=%s" % (res["s4_stability"]["pearson_r_excess_all_vs_ex2"], res["s4_stability"]["max_abs_delta"]))
P.append("DONE -> data/s2_pilot_results.json")
assert len(P) <= 20
print("\n".join(P))
json.dump(res, open(os.path.join(ROOT, "data/s2_pilot_results.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
