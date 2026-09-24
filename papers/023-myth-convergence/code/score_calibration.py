#!/usr/bin/env python3
"""Score blinded ARIS4C-023 motif coding without external dependencies."""

import argparse, csv, json, math
from collections import Counter, defaultdict
from pathlib import Path

ALLOWED = {"present", "absent", "uncertain", "not_observed"}
KEYS = ("packet_id", "motif_id")

def load(path):
    rows = {}
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            key = tuple(row[k].strip() for k in KEYS)
            state = row.get("state", "").strip().lower()
            if state and state not in ALLOWED:
                raise ValueError(f"{path}: invalid state {state!r} for {key}")
            if key in rows:
                raise ValueError(f"{path}: duplicate key {key}")
            rows[key] = state
    return rows

def agreement(a, b):
    return sum(x == y for x, y in zip(a, b)) / len(a) if a else math.nan

def kappa(a, b):
    n = len(a)
    if not n:
        return math.nan
    pa = agreement(a, b)
    ca, cb = Counter(a), Counter(b)
    cats = set(ca) | set(cb)
    pe = sum((ca[c] / n) * (cb[c] / n) for c in cats)
    return (pa - pe) / (1 - pe) if pe < 1 else math.nan

def gwet_ac1(a, b):
    n = len(a)
    if not n:
        return math.nan
    cats = sorted(set(a) | set(b))
    q = len(cats)
    if q <= 1:
        return math.nan
    pa = agreement(a, b)
    pooled = {c: (a.count(c) + b.count(c)) / (2 * n) for c in cats}
    pe = sum(p * (1 - p) for p in pooled.values()) / (q - 1)
    return (pa - pe) / (1 - pe) if pe < 1 else math.nan

def confusion(a, b):
    cats = ["present", "absent", "uncertain", "not_observed"]
    out = {x: {y: 0 for y in cats} for x in cats}
    for x, y in zip(a, b):
        out[x][y] += 1
    return out

def finite(x):
    return None if isinstance(x, float) and (math.isnan(x) or math.isinf(x)) else x

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--out")
    args = ap.parse_args()

    A, B = load(args.a), load(args.b)
    common = sorted(set(A) & set(B))
    completed = [k for k in common if A[k] and B[k]]
    av = [A[k] for k in completed]
    bv = [B[k] for k in completed]

    binary = [k for k in completed if A[k] in {"present","absent"} and B[k] in {"present","absent"}]
    ab = [A[k] for k in binary]
    bb = [B[k] for k in binary]

    result = {
        "n_keys_a": len(A),
        "n_keys_b": len(B),
        "n_common_keys": len(common),
        "n_completed_pairs": len(completed),
        "four_state": {
            "raw_agreement": finite(agreement(av, bv)),
            "cohen_kappa": finite(kappa(av, bv)),
            "gwet_ac1": finite(gwet_ac1(av, bv)),
            "confusion_a_rows_b_columns": confusion(av, bv) if completed else {}
        },
        "binary_present_absent_subset": {
            "n": len(binary),
            "raw_agreement": finite(agreement(ab, bb)),
            "cohen_kappa": finite(kappa(ab, bb)),
            "gwet_ac1": finite(gwet_ac1(ab, bb))
        },
        "unmatched_keys_a_only": [list(k) for k in sorted(set(A)-set(B))],
        "unmatched_keys_b_only": [list(k) for k in sorted(set(B)-set(A))]
    }
    txt = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        Path(args.out).write_text(txt, encoding="utf-8")
    print(txt, end="")

if __name__ == "__main__":
    main()
