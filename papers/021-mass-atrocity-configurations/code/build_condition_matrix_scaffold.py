#!/usr/bin/env python3
"""Build an empty dual-track condition matrix from the frozen 139-case identity frame.

R = historical Williams-replication coding.
M = modern/version-pinned reproducible coding.

The scaffold deliberately leaves condition values blank and statuses UNRESOLVED.
Published outcomes, marginal totals, and QCA solutions must not be reverse-engineered
into missing input cells.
"""
from __future__ import annotations
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"data"/"CASE_UNIVERSE_IDENTITY_V1.csv"
OUT=ROOT/"data"/"CONDITION_MATRIX_V0.csv"
CONDS=("A","P","W","I","S","E")
TRACKS=("R","M")

with SRC.open(encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f))

if len(rows)!=139:
    raise SystemExit(f"expected 139 identity rows, got {len(rows)}")

base=list(rows[0].keys())
extra=[]
for track in TRACKS:
    for cond in CONDS:
        extra += [f"{cond}_{track}",f"{cond}_{track}_status",f"{cond}_{track}_source",f"{cond}_{track}_note"]

with OUT.open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=base+extra)
    w.writeheader()
    for row in rows:
        for track in TRACKS:
            for cond in CONDS:
                row[f"{cond}_{track}"]=""
                row[f"{cond}_{track}_status"]="UNRESOLVED"
                row[f"{cond}_{track}_source"]=""
                row[f"{cond}_{track}_note"]=""
        w.writerow(row)

print("PASS: wrote 139-row dual-track condition scaffold")
