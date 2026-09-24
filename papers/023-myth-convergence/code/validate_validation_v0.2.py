#!/usr/bin/env python3
"""Validate ARIS4C-023 v0.2 blinded validation packet/coder files."""
import argparse, csv, sys
from collections import Counter

ALLOWED={"present","absent","uncertain","not_observed"}
FAMILIES={"flood","anthropogony","divine_conflict"}
REQUIRED={"packet_id","bundle_id","case_id","family","motif_id","motif_label","axis",
"inclusion_rule","exclusion_rule","source_work","source_locator","source_url",
"canonical_authority","witness_scope","negative_closed","state","confidence","rationale","ambiguity_flag"}

def load(path):
    rows=[]; seen=set(); errors=[]
    with open(path,newline="",encoding="utf-8-sig") as f:
        r=csv.DictReader(f)
        missing=REQUIRED-set(r.fieldnames or [])
        if missing: errors.append("missing columns: "+str(sorted(missing)))
        for i,row in enumerate(r,2):
            key=(row.get("bundle_id","").strip(),row.get("motif_id","").strip())
            if key in seen: errors.append(f"line {i}: duplicate key {key}")
            seen.add(key); rows.append((i,row))
    return rows,errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--allow-blank",action="store_true")
    args=ap.parse_args()
    rows,errors=load(args.csv)
    states=Counter(); fam=Counter(); completed=0
    for i,row in rows:
        family=row["family"].strip()
        if family not in FAMILIES: errors.append(f"line {i}: invalid family={family!r}")
        fam[family]+=1
        state=row["state"].strip().lower()
        if state:
            completed+=1; states[state]+=1
            if state not in ALLOWED: errors.append(f"line {i}: invalid state={state!r}")
            conf=row["confidence"].strip()
            try:
                c=int(conf)
                if not 0<=c<=100: raise ValueError
            except Exception: errors.append(f"line {i}: confidence must be integer 0-100")
            if not row["rationale"].strip(): errors.append(f"line {i}: completed state requires rationale")
            if row["ambiguity_flag"].strip() not in {"0","1"}: errors.append(f"line {i}: ambiguity_flag must be 0/1")
        elif not args.allow_blank:
            errors.append(f"line {i}: blank state")
    if len(rows)!=190: errors.append(f"expected 190 rows, got {len(rows)}")
    expected={"flood":63,"anthropogony":55,"divine_conflict":72}
    if dict(fam)!=expected: errors.append(f"family counts {dict(fam)} != {expected}")
    print("rows:",len(rows),"completed:",completed,"families:",dict(fam),"states:",dict(states))
    if errors:
        for e in errors: print("ERROR:",e,file=sys.stderr)
        raise SystemExit(1)
    print("PASS")

if __name__=="__main__":
    main()
