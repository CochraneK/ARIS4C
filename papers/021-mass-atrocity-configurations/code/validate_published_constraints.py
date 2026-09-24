#!/usr/bin/env python3
"""Validate a partial/complete Williams condition matrix against published case-level constraints."""

from __future__ import annotations
import argparse, csv, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CFILE=ROOT/"data"/"WILLIAMS_PUBLISHED_CONSTRAINTS_V1.json"
SYMS=["A","P","W","I","S","E"]

def match(row, formula):
    for lit in formula.split("*"):
        neg=lit.startswith("~")
        key=lit[1:] if neg else lit
        v=str(row.get(key,"")).strip()
        if v not in {"0","1"}:
            return False
        if (v=="1") == neg:
            return False
    return True

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("matrix", type=Path)
    args=ap.parse_args()
    cfg=json.loads(CFILE.read_text(encoding="utf-8"))
    with args.matrix.open(encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    by={r["case_id"]:r for r in rows}
    failures=[]

    for cid,vals in cfg["exact_known_rows"].items():
        if cid not in by:
            failures.append(f"missing case {cid}")
            continue
        for k,v in vals.items():
            if k not in SYMS:
                continue
            got=str(by[cid].get(k,"")).strip()
            if got and got!=str(v):
                failures.append(f"{cid}.{k}={got}, expected {v}")

    for formula,spec in cfg["positive_path_memberships"].items():
        expected=set(spec["case_ids"])
        known={cid for cid in expected if cid in by and all(str(by[cid].get(s,"")).strip() in {"0","1"} for s in SYMS)}
        bad=[cid for cid in sorted(known) if not match(by[cid],formula)]
        if bad:
            failures.append(f"{formula}: published positive members fail formula: {bad}")

    sol=cfg["intermediate_solution"]
    complete=[r for r in rows if all(str(r.get(s,"")).strip() in {"0","1"} for s in SYMS)]
    if len(complete)==139:
        predicted={r["case_id"] for r in complete if any(match(r,f) for f in sol["formulas"])}
        expected=set(sol["expected_true_positive_case_ids"])|set(sol["expected_false_positive_case_ids"])
        if predicted!=expected:
            failures.append(
                "solution case membership mismatch: "
                f"extra={sorted(predicted-expected)} missing={sorted(expected-predicted)}"
            )

    print(json.dumps({
        "status":"PASS" if not failures else "FAIL",
        "rows":len(rows),
        "complete_six_condition_rows":len(complete),
        "failures":failures
    },indent=2))
    return 0 if not failures else 2

if __name__=="__main__":
    raise SystemExit(main())
