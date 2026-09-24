#!/usr/bin/env python3
"""Validate reconstructed Williams control identities and left-truncation correction."""
from __future__ import annotations
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
NEG=ROOT/"data"/"WILLIAMS_NEGATIVE_CASES_IDENTITY_V1.csv"
EXC=ROOT/"data"/"LEFT_TRUNCATION_EXCLUSIONS_V1.csv"
def read(p):
    with p.open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))
neg=read(NEG); exc=read(EXC)
assert len(neg)==99, f"expected 99 controls, got {len(neg)}"
assert len(exc)==3, f"expected 3 exclusions, got {len(exc)}"
assert {r["sftgcode"] for r in exc}=={"COL","CUB","IRN"}
assert all(int(r["panel_start_year"])==1955 for r in exc)
assert all(int(r["historical_start_year"])<1955 for r in exc)
assert len({r["case_id"] for r in neg})==99
print("PASS: 99 controls after deterministic exclusion of 3 pre-1955 left-truncation artifacts")
