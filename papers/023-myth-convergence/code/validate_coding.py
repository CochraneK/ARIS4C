#!/usr/bin/env python3
"""Validate ARIS4C-023 long-form coding table."""

import argparse, csv, sys
from collections import Counter

ALLOWED_STATES={"present","absent","uncertain","not_observed"}
ALLOWED_SCOPES={"in-window","inherited_or_transmitted","later-comparator","uncertain"}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("coding")
    args=ap.parse_args()
    seen=set(); errors=[]; states=Counter(); scopes=Counter()
    with open(args.coding,newline="",encoding="utf-8-sig") as f:
        r=csv.DictReader(f)
        required={"tradition_id","motif_id","motif_state","source_id","witness_scope"}
        missing=required-set(r.fieldnames or [])
        if missing:
            errors.append(f"missing columns: {sorted(missing)}")
        else:
            for i,row in enumerate(r,2):
                key=(row["tradition_id"].strip(),row["motif_id"].strip(),row["source_id"].strip())
                if key in seen: errors.append(f"line {i}: duplicate {key}")
                seen.add(key)
                state=row["motif_state"].strip().lower()
                scope=row["witness_scope"].strip().lower()
                if state not in ALLOWED_STATES: errors.append(f"line {i}: invalid motif_state={state!r}")
                if scope not in ALLOWED_SCOPES: errors.append(f"line {i}: invalid witness_scope={scope!r}")
                states[state]+=1; scopes[scope]+=1
    print("states:",dict(states))
    print("witness_scope:",dict(scopes))
    if errors:
        for e in errors: print("ERROR:",e,file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {len(seen)} coding rows")

if __name__=="__main__":
    main()
