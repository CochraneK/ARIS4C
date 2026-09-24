#!/usr/bin/env python3
"""Build the 139-case candidate universe from frozen positive and non-genocide seeds."""

from __future__ import annotations
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
POS=ROOT/"data"/"WILLIAMS_POSITIVE_CASES_SEED.csv"
NEG=ROOT/"data"/"WILLIAMS_NONGENOCIDE_CANDIDATE_V0.csv"
OUT=ROOT/"data"/"CASE_UNIVERSE_CANDIDATE_V0.csv"

def read(path):
    with path.open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))

pos=[r for r in read(POS) if r["analysis_included"]=="1"]
neg=read(NEG)

rows=[]
for r in pos:
    rows.append({
        "case_id":r["case_id"],
        "country":r["country"],
        "start":r["start_year"],
        "end":r["end_year"],
        "outcome_genocide":"1",
        "event_type":"genocide/politicide case",
        "frame_status":"literature_seed",
        "source_basis":"Williams 2016 positive-case list",
    })
for r in neg:
    rows.append({
        "case_id":r["case_id"],
        "country":r["country"],
        "start":r["start"],
        "end":r["end"],
        "outcome_genocide":"0",
        "event_type":r["event_type"],
        "frame_status":r["reconstruction_status"],
        "source_basis":r["source_basis"],
    })

assert len(pos)==40
assert len(neg)==99
assert len(rows)==139
assert len({r["case_id"] for r in rows})==139

OUT.parent.mkdir(parents=True,exist_ok=True)
fields=["case_id","country","start","end","outcome_genocide","event_type","frame_status","source_basis"]
with OUT.open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields)
    w.writeheader()
    w.writerows(rows)
print(f"wrote {OUT}: 40 positive + 99 controls = 139")
