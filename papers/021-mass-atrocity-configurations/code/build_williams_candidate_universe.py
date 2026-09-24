#!/usr/bin/env python3
"""Build the ARIS4C021 candidate Williams non-genocide universe from PITF country-year data.

Input is expected to be Ulfelder's public transformed PITF 2014 panel (data.out/pit.csv)
or an equivalent file with pit.{reg,rev,eth,gen}.ongoing fields.

This produces the 2014-lineage candidate control universe only. It is NOT the final
Williams 99-case control set until the 2012-era PITF version gap is resolved.
"""
from __future__ import annotations
import argparse, csv
from pathlib import Path

TYPES=("reg","rev","eth","gen")

def read_panel(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def intervals(rows, code, typ):
    ys=sorted(int(r["year"]) for r in rows if r["sftgcode"]==code and 1955 <= int(r["year"]) <= 2014)
    by={int(r["year"]):r for r in rows if r["sftgcode"]==code and 1955 <= int(r["year"]) <= 2014}
    out=[]; cur=None
    col=f"pit.{typ}.ongoing"
    for y in ys:
        on=float(by[y].get(col,0) or 0)==1
        if on:
            if cur is None or y>cur[1]+1:
                if cur is not None: out.append(cur)
                cur=[y,y,typ]
            else:
                cur[1]=y
        elif cur is not None:
            out.append(cur); cur=None
    if cur is not None: out.append(cur)
    return out

def build(rows):
    codes=sorted({r["sftgcode"] for r in rows})
    all_cases=[]
    for code in codes:
        ints=[]
        for typ in TYPES:
            ints.extend(intervals(rows,code,typ))
        ints.sort(key=lambda x:(x[0],x[1]))
        cur=None
        for start,end,typ in ints:
            if cur is None:
                cur={"sftgcode":code,"start_year":start,"end_year":end,"types":{typ}}
            elif start <= cur["end_year"] + 5:
                cur["end_year"]=max(cur["end_year"],end)
                cur["types"].add(typ)
            else:
                all_cases.append(cur)
                cur={"sftgcode":code,"start_year":start,"end_year":end,"types":{typ}}
        if cur is not None: all_cases.append(cur)
    controls=[x for x in all_cases if 1955<=x["start_year"]<=1998 and "gen" not in x["types"]]
    controls.sort(key=lambda x:(x["sftgcode"],x["start_year"]))
    return controls

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("pit_csv",type=Path)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    rows=read_panel(args.pit_csv)
    controls=build(rows)
    if len(controls)!=102:
        raise SystemExit(f"candidate control contract failed: expected 102, got {len(controls)}")
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f)
        w.writerow(["candidate_id","sftgcode","start_year","end_year","event_types","outcome_genocide","canonical_status","source_lineage"])
        for i,x in enumerate(controls,1):
            w.writerow([
                f"NEG2014_{i:03d}",x["sftgcode"],x["start_year"],x["end_year"],
                "+".join(sorted(x["types"])),0,"candidate_not_canonical",
                "Ulfelder EWP replication PITF-2014 transformed panel; <=5y consolidated reconstruction"
            ])
    print(f"PASS: {len(controls)} candidate controls (Williams target=99; unresolved version gap=3)")
if __name__=="__main__":
    main()
