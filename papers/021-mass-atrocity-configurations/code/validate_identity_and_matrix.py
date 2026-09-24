#!/usr/bin/env python3
"""Validate ARIS4C021 identity and condition-scaffold contracts."""
from __future__ import annotations
import csv
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ID=ROOT/"data"/"CASE_UNIVERSE_IDENTITY_V1.csv"
MAT=ROOT/"data"/"CONDITION_MATRIX_V0.csv"
CONDS=("A","P","W","I","S","E")
TRACKS=("R","M")
ALLOWED={"SOURCE_EXACT","SOURCE_DERIVED","AUTHOR_RECONSTRUCTED","PUBLISHED_CASE_CLUE","UNRESOLVED","NOT_APPLICABLE"}

def read(path):
    with path.open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))

ids=read(ID)
mat=read(MAT)
assert len(ids)==139, len(ids)
assert len(mat)==139, len(mat)
assert len({r["case_id"] for r in ids})==139
assert [r["case_id"] for r in mat]==[r["case_id"] for r in ids]
counts=Counter(int(r["outcome_genocide"]) for r in ids)
assert counts==Counter({0:99,1:40}), counts

for row in mat:
    for track in TRACKS:
        for cond in CONDS:
            status=row[f"{cond}_{track}_status"]
            assert status in ALLOWED,(row["case_id"],cond,track,status)
            if status=="UNRESOLVED":
                assert row[f"{cond}_{track}"]=="",(row["case_id"],cond,track,"unresolved value must be blank")

print("PASS: identity 40+99=139; dual-track condition scaffold contract valid")
