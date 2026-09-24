#!/usr/bin/env python3
"""Validate the 139-case candidate universe."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/"data"/"CASE_UNIVERSE_CANDIDATE_V0.csv"

with PATH.open(encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f))
pos=[r for r in rows if r["outcome_genocide"]=="1"]
neg=[r for r in rows if r["outcome_genocide"]=="0"]

assert len(rows)==139, len(rows)
assert len(pos)==40, len(pos)
assert len(neg)==99, len(neg)
assert len({r["case_id"] for r in rows})==139
print("PASS: candidate case universe = 139 (40 genocide + 99 non-genocide)")
