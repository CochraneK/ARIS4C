#!/usr/bin/env python3
from __future__ import annotations
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRAME = ROOT / "data" / "case_frame_v0.1.csv"
EXPECTED = {"planet": 8, "dwarf_planet": 5, "satellite": 21, "small_body": 16}

def main():
    with FRAME.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if len(rows) != 50:
        raise SystemExit(f"expected 50 cases, found {len(rows)}")
    ids = [r["case_id"] for r in rows]
    names = [r["name"] for r in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate case_id")
    if len(names) != len(set(names)):
        raise SystemExit("duplicate name")
    counts = Counter(r["official_class"] for r in rows)
    if dict(counts) != EXPECTED:
        raise SystemExit(f"class counts differ: {dict(counts)}")
    for r in rows:
        direct = int(r["direct_sun_orbit"])
        sat = int(r["is_satellite"])
        if r["official_class"] == "satellite" and (direct != 0 or sat != 1):
            raise SystemExit(f"satellite hierarchy inconsistency: {r['case_id']}")
        if r["official_class"] != "satellite" and sat != 0:
            raise SystemExit(f"non-satellite flagged satellite: {r['case_id']}")
    mars = next(r for r in rows if r["name"] == "Mars")
    if mars["official_class"] != "planet" or mars["boundary_tag"] != "positive_control":
        raise SystemExit("Mars positive-control invariant failed")
    print("PASS: 50-case Pilot-0 frame is internally consistent")
    print("class counts:", dict(counts))

if __name__ == "__main__":
    main()
