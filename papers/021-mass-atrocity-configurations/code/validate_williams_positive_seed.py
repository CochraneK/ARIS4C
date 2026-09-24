#!/usr/bin/env python3
"""Validate the literature-derived Williams positive-case seed."""
from __future__ import annotations
import csv
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "WILLIAMS_POSITIVE_CASES_SEED.csv"
with PATH.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
included = [r for r in rows if r["analysis_included"] == "1"]
excluded = [r for r in rows if r["analysis_included"] == "0"]
assert len(included) == 40, f"expected 40 included Williams positives, got {len(included)}"
assert len(excluded) == 1, f"expected 1 excluded Sudan-2003 reference row, got {len(excluded)}"
assert excluded[0]["case_id"] == "SDN_2003_OPEN"
assert all(r["outcome_genocide"] == "1" for r in rows)
assert len({r["case_id"] for r in rows}) == len(rows)
print("PASS: 40 included positives + 1 explicitly excluded Sudan-2003 row")
