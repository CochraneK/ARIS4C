#!/usr/bin/env python
"""Stage 3a T2/T3a: Translating Time (Workman et al. 2013) 11-event subset fits.

Per task spec: per species Y = onset + slope*rank (OLS), where
  Y    = post-conception (PC) day, median of the published 95% CI
  rank = shared ordinal position of the event (1..11), assigned by pooling
         median PC days across all mapped species (same event -> same rank)

Note: the official model (quasi-Newton, predicted-vs-empirical r=0.993) uses an
optimized latent "eventscale" plus per-species interaction terms; rank-OLS is
the documented simplified form requested for this subset reproduction.

Outputs: data/tt_fit.csv (fit params/domain/CI-violations),
         data/tt_events.csv (per species per event: rank, pc_median, lower95, upper95)
Run: python code/fit_tt.py            -> write CSVs, print fit table
     python code/fit_tt.py --validate -> print CI-violation table only
"""
import csv
import sys

import numpy as np

TT = "lit/tt_2013/tt_related_tables.csv"
FIT_OUT = "data/tt_fit.csv"
EVT_OUT = "data/tt_events.csv"
# Each table block has 10 event rows + 1 "Location" legend row (the brief's
# "11 events" counts the legend row; 198 data rows = 18 tables x 11 rows).
N_EVENTS = 10

# csv column numbers (col_N) of each species' (lower, upper) pair per table block.
# row index of col_N in the parsed csv row = N + 1 (r[0]=table_id, r[1]=context,
# r[2]=col_1=wdt_ID, r[3]=col_2=Event, r[4]=col_3=Location, r[5]=col_4=first number).
# 5-col tables: 1 pair; 9-col: 3 pairs; 13-col: 5 pairs; T18 (7-col): 2 pairs.
TABLES = {
    "T01": [("Quoll", 4, 5), ("Brush-tailed Opossum", 6, 7), ("Quokka", 8, 9)],
    "T02": [("Cat", 4, 5)],
    "T03": [("Rhesus Macaque", 4, 5), ("Human", 6, 7), ("Short-tailed Opossum", 8, 9),
            ("Dunnart", 10, 11), ("Wallaby", 12, 13)],
    "T04": [("Ferret", 4, 5)],
    "T05": [("Rat", 4, 5), ("Mouse", 6, 7), ("Hamster", 8, 9),
            ("Gerbil", 10, 11), ("Spiny Mouse", 12, 13)],
    "T06": [("Guinea Pig", 4, 5)],
    "T07": [("Rat", 4, 5), ("Mouse", 6, 7), ("Hamster", 8, 9),
            ("Gerbil", 10, 11), ("Spiny Mouse", 12, 13)],
    "T08": [("Rhesus Macaque", 4, 5), ("Human", 6, 7), ("Short-tailed Opossum", 8, 9),
            ("Dunnart", 10, 11), ("Wallaby", 12, 13)],
    "T09": [("Rat", 4, 5), ("Mouse", 6, 7), ("Hamster", 8, 9),
            ("Gerbil", 10, 11), ("Spiny Mouse", 12, 13)],
    "T10": [("Quoll", 4, 5), ("Brush-tailed Opossum", 6, 7), ("Quokka", 8, 9)],
    "T11": [("Quoll", 4, 5), ("Brush-tailed Opossum", 6, 7), ("Quokka", 8, 9)],
    "T12": [("Rabbit", 4, 5)],
    "T13": [("Rat", 4, 5), ("Mouse", 6, 7), ("Hamster", 8, 9),
            ("Gerbil", 10, 11), ("Spiny Mouse", 12, 13)],
    "T14": [("Rhesus Macaque", 4, 5), ("Human", 6, 7), ("Short-tailed Opossum", 8, 9),
            ("Dunnart", 10, 11), ("Wallaby", 12, 13)],
    "T15": [("Sheep", 4, 5)],
    "T16": [("Rhesus Macaque", 4, 5), ("Human", 6, 7), ("Short-tailed Opossum", 8, 9),
            ("Dunnart", 10, 11), ("Wallaby", 12, 13)],
    "T17": [("Rat", 4, 5), ("Mouse", 6, 7), ("Hamster", 8, 9),
            ("Gerbil", 10, 11), ("Spiny Mouse", 12, 13)],
    "T18": [("Dunnart", 4, 5), ("Wallaby", 6, 7)],
}
# Column order in shared 13-col tables follows the site's own HTML header row
# (parsed by parse_tt_tables.py): rodents Rat,Mouse,Hamster,Gerbil,Spiny; primates
# Macaque,Human,STO + Dunnart,Wallaby (Dunnart/Wallaby confirmed by cross-table
# value identity T03p4==T18p1, T03p5==T18p2). Sanity: across all 10 events the rat
# column is ~1.5 d later than the mouse and the human column later than the macaque
# column, matching known neurodevelopmental sequencing. NOTE: the brief's mouse/human
# domains (9.1-27.4 / 22.9-108.4) are actually the 1st-column (Rat/Macaque) domains
# (host-side "ctx species = first column" mislabeling; correct only for single-species
# tables T02 Cat / T12 Rabbit, which match the brief exactly).
NOTES = {
    "Quokka": "9-col table 3rd pair (by elimination)",
    "Mouse": "13-col shared table, 2nd pair (site header order)",
    "Human": "13-col shared table, 2nd pair (site header order)",
    "Rat": "13-col shared table, 1st pair (site header order)",
    "Rhesus Macaque": "13-col shared table, 1st pair (site header order)",
}


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def load():
    rows = [r for r in csv.reader(open(TT, encoding="utf-8")) if r and r[0].strip()]
    per = {}        # species -> event_key -> (L, U)
    per_name = {}   # species -> event_key -> display name
    per_tables = {}  # species -> set(table ids)
    mismatch = 0
    for r in rows[1:]:
        tid = r[0].strip()
        if tid not in TABLES:
            continue
        ev = r[3].strip() if len(r) > 3 else ""
        if not ev or ev.lower() == "location":
            continue
        key = ev.lower()
        for sp, cl, cu in TABLES[tid]:
            if len(r) <= cu + 1:
                continue
            L, U = num(r[cl + 1]), num(r[cu + 1])
            if L is None or U is None:
                continue
            if sp in per and key in per[sp]:
                if per[sp][key] != (L, U):
                    mismatch += 1
            else:
                per.setdefault(sp, {})[key] = (L, U)
                per_name.setdefault(sp, {})[key] = ev
            per_tables.setdefault(sp, set()).add(tid)
    return per, per_name, per_tables, mismatch


def ols(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    X = np.column_stack([np.ones_like(x), x])
    beta, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
    e = y - X @ beta
    s2 = float(e @ e) / (len(x) - 2)
    cov = s2 * np.linalg.inv(X.T @ X)
    ss_res = float(e @ e)
    r2 = 1.0 - ss_res / float(((y - y.mean()) ** 2).sum())
    yhat = X @ beta
    return float(beta[0]), float(beta[1]), r2, cov, yhat, float(np.sqrt(ss_res / len(x)))


def main():
    per, per_name, per_tables, mismatch = load()
    all_keys = sorted({k for d in per.values() for k in d})
    med = {k: float(np.median([(d[k][0] + d[k][1]) / 2 for d in per.values() if k in d]))
           for k in all_keys}
    order = sorted(med, key=med.get)
    rank = {k: i + 1 for i, k in enumerate(order)}

    fits = {}
    for sp in sorted(per):
        evs = [k for k in order if k in per[sp]]
        if len(evs) != N_EVENTS:
            continue
        x = np.array([rank[k] for k in evs], float)
        y = np.array([(per[sp][k][0] + per[sp][k][1]) / 2 for k in evs], float)
        onset, slope, r2, cov, yhat, rmse = ols(x, y)
        viol = int(sum(not (per[sp][k][0] <= yh <= per[sp][k][1]) for k, yh in zip(evs, yhat)))
        Ls = [per[sp][k][0] for k in evs]
        Us = [per[sp][k][1] for k in evs]
        fits[sp] = dict(onset=onset, slope=slope, r2=r2, rmse=rmse, viol=viol, n=len(evs),
                        pc_min_l=min(Ls), pc_max_u=max(Us),
                        pc_min_med=float(y.min()), pc_max_med=float(y.max()),
                        maxres=float(np.max(np.abs(y - yhat))),
                        tables=";".join(sorted(per_tables[sp])), note=NOTES.get(sp, ""),
                        events=[(rank[k], per_name[sp][k], (per[sp][k][0] + per[sp][k][1]) / 2,
                                 per[sp][k][0], per[sp][k][1]) for k in evs])

    if "--validate" in sys.argv:
        print(f"{'species':18s} n   viol  max|resid|")
        for sp in sorted(fits):
            ft = fits[sp]
            print(f"{sp:18s} {ft['n']:3d} {ft['viol']:5d}  {ft['maxres']:.2f}")
        tot = sum(f["viol"] for f in fits.values())
        npts = sum(f["n"] for f in fits.values())
        print(f"total fitted points outside published 95% CI: {tot}/{npts}; cross-table mismatch: {mismatch}")
        return

    with open(FIT_OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["species", "tables", "n", "onset", "slope", "r2", "rmse",
                    "pc_min_l", "pc_max_u", "pc_min_med", "pc_max_med",
                    "ci_violations", "notes"])
        for sp in sorted(fits):
            ft = fits[sp]
            w.writerow([sp, ft["tables"], ft["n"], f'{ft["onset"]:.4f}', f'{ft["slope"]:.4f}',
                        f'{ft["r2"]:.5f}', f'{ft["rmse"]:.4f}', f'{ft["pc_min_l"]:.1f}',
                        f'{ft["pc_max_u"]:.1f}', f'{ft["pc_min_med"]:.2f}', f'{ft["pc_max_med"]:.2f}',
                        ft["viol"], ft["note"]])
    with open(EVT_OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["species", "rank", "event", "pc_median", "lower95", "upper95"])
        for sp in sorted(fits):
            for rk, ev, pc, lo, up in fits[sp]["events"]:
                w.writerow([sp, rk, ev, f"{pc:.2f}", f"{lo:.1f}", f"{up:.1f}"])

    print(f"{'species':18s} n  onset   slope   r2       viol  dom[Lmin,Umax]")
    for sp in sorted(fits):
        ft = fits[sp]
        print(f"{sp:18s} {ft['n']:2d} {ft['onset']:7.2f} {ft['slope']:7.2f} {ft['r2']:8.5f} {ft['viol']:4d}  "
              f"[{ft['pc_min_l']:.1f},{ft['pc_max_u']:.1f}]")
    print(f"cross-table mismatch: {mismatch}; distinct events: {len(order)}; fitted species: {len(fits)}")


if __name__ == "__main__":
    main()
