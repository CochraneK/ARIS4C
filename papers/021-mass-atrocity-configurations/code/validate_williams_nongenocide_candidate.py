#!/usr/bin/env python3
"""Validate the candidate Williams 99-control reconstruction."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/"data"/"WILLIAMS_NONGENOCIDE_CANDIDATE_V0.csv"

with PATH.open(encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f))

assert len(rows)==99, f"expected 99 rows, got {len(rows)}"
assert all(r["outcome_genocide"]=="0" for r in rows)
assert len({r["case_id"] for r in rows})==99, "duplicate case_id"
years=[]
for r in rows:
    start=r["start"]
    y=int(start.split("/")[-1])
    years.append(y)
assert min(years)>=1955, min(years)
assert max(years)<=1998, max(years)
print("PASS: 99 candidate non-genocide cases, start years 1955-1998")
