#!/usr/bin/env python3
"""Build pairwise motif similarity while preserving unknown/not-observed states."""

import argparse, csv, math
from collections import defaultdict
from itertools import combinations

SCORABLE = {"present", "absent"}

def load(path):
    by_trad = defaultdict(dict)
    with open(path, newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            t = r["tradition_id"].strip()
            m = r["motif_id"].strip()
            s = r["motif_state"].strip().lower()
            if s and s not in {"present","absent","uncertain","not_observed"}:
                raise ValueError(f"Invalid motif_state {s!r} for {t}/{m}")
            if m in by_trad[t]:
                raise ValueError(f"Duplicate coding for {t}/{m}")
            by_trad[t][m] = s
    return by_trad

def safe_div(a,b):
    return a/b if b else math.nan

def pair_stats(a, b):
    shared = sorted(set(a) & set(b))
    comparable = [m for m in shared if a[m] in SCORABLE and b[m] in SCORABLE]
    pp = sum(a[m]=="present" and b[m]=="present" for m in comparable)
    pa = sum(a[m]=="present" and b[m]=="absent" for m in comparable)
    ap = sum(a[m]=="absent" and b[m]=="present" for m in comparable)
    aa = sum(a[m]=="absent" and b[m]=="absent" for m in comparable)
    union_present = pp + pa + ap
    return {
        "n_shared_motif_ids": len(shared),
        "n_comparable": len(comparable),
        "both_present": pp,
        "a_present_b_absent": pa,
        "a_absent_b_present": ap,
        "both_absent": aa,
        # Jaccard deliberately ignores joint absences.
        "jaccard_present": safe_div(pp, union_present),
        # Simple matching is secondary because shared absences can dominate sparse matrices.
        "simple_matching": safe_div(pp+aa, len(comparable)),
    }

def fmt(v):
    if isinstance(v,float) and math.isnan(v):
        return ""
    return v

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--coding", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--min-comparable", type=int, default=10)
    args=ap.parse_args()

    data=load(args.coding)
    fields=["tradition_a","tradition_b","n_shared_motif_ids","n_comparable","both_present",
            "a_present_b_absent","a_absent_b_present","both_absent",
            "jaccard_present","simple_matching","passes_min_comparable"]
    with open(args.out,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields)
        w.writeheader()
        for ta,tb in combinations(sorted(data),2):
            s=pair_stats(data[ta],data[tb])
            row={"tradition_a":ta,"tradition_b":tb,**s,
                 "passes_min_comparable":s["n_comparable"]>=args.min_comparable}
            w.writerow({k:fmt(v) for k,v in row.items()})

if __name__=="__main__":
    main()
