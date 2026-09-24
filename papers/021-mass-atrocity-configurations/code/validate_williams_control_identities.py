#!/usr/bin/env python3
"""Validate the reconstructed Williams 99-control identity universe."""

from __future__ import annotations
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/"data"/"WILLIAMS_CONTROL_IDENTITIES_V1.csv"

with PATH.open(encoding="utf-8-sig", newline="") as f:
    rows=list(csv.DictReader(f))
inc=[r for r in rows if r["analysis_included"]=="1"]
assert len(inc)==99, f"expected 99 controls, got {len(inc)}"
assert len({r["case_id"] for r in inc})==99, "duplicate control case_id"
assert all(r["outcome_genocide"]=="0" for r in inc)
assert not any(r["case_id"]=="KEN_1970" for r in inc), "SCIP Jordan/Kenya rendering artifact leaked into controls"
assert any(r["case_id"]=="DJI_1991" for r in inc), "Djibouti 1991-94 missing"
flagged={r["case_id"] for r in inc if r["date_status"]=="cross-version-date-drift"}
expected={"COL_1984","JOR_1957","NIC_1978","PER_1962"}
assert flagged==expected, f"unexpected date-drift set: {sorted(flagged)}"
print("PASS: 99 unique controls; Kenya-1970 artifact absent; Djibouti present; date-drift flags stable")
