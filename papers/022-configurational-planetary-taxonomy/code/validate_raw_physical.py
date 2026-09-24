#!/usr/bin/env python3
"""Deterministic QA for ARIS4C022 raw physical core v0.1."""

from __future__ import annotations

import csv
import pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw_physical_core_v0.1.csv"


def main() -> None:
    with DATA.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    assert len(rows) == 50, f"expected 50 rows, got {len(rows)}"
    assert len({r["case_id"] for r in rows}) == 50
    assert len({r["name"] for r in rows}) == 50

    status = Counter(r["ingestion_status"] for r in rows)
    source = Counter(r["source_key"] for r in rows)
    assert status == Counter({"INGESTED_CORE": 34, "NA_NOT_INGESTED": 16}), status
    assert source["JPL_PLANET_PHYS"] == 13, source
    assert source["JPL_SAT_PHYS"] == 21, source
    assert source["JPL_SBDB_API_PLANNED"] == 16, source

    by_name = {r["name"]: r for r in rows}
    mars = by_name["Mars"]
    assert mars["official_class"] == "planet"
    assert mars["ingestion_status"] == "INGESTED_CORE"
    assert float(mars["mass_kg"]) > 0

    for r in rows:
        if r["source_key"] == "JPL_SAT_PHYS":
            assert r["mass_value_type"] == "DERIVED_FROM_GM_CODATA2018"
            assert float(r["gm_km3_s2"]) > 0
            assert float(r["mass_kg"]) > 0
        if r["source_key"] == "JPL_SBDB_API_PLANNED":
            for field in ("mass_kg", "gm_km3_s2", "mean_radius_km", "density_g_cm3"):
                assert r[field] == "", (r["name"], field, r[field])

    print("PASS: raw physical core has 50 rows")
    print("PASS: 34 ingested core / 16 pending SBDB")
    print("PASS: 13 planet+dwarf source rows / 21 satellite source rows")
    print("PASS: pending small bodies contain no fabricated numeric values")


if __name__ == "__main__":
    main()
