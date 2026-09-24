#!/usr/bin/env python3
"""Validate ARIS4C019 historical coverage registries.

Coverage-only gate. The validator must not read or compute time-off × happiness
effects. It verifies provenance/availability structures and fails on silent
coverage drift.
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read_csv(name: str):
    with (DATA / name).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    sources = read_csv("historical_source_coverage.csv")
    wvs = read_csv("historical_wvs_wave_registry.csv")
    early = read_csv("historical_early_wellbeing_country_seed.csv")
    master = read_csv("historical_country_source_coverage_v1.csv")
    overlap = read_csv("historical_coverage_overlap_summary.csv")
    wdh = read_csv("historical_wdh_trends_comparable_seed.csv")
    euro = read_csv("historical_eurobarometer_coverage.csv")

    ids = {r["source_id"] for r in sources}
    required = {
        "ILO_C052","ILO_C132","WORLD_2015","WB_EW","WDH_NATIONS",
        "CANTRIL_7023","EUROBAROMETER","WVS","WHR_GALLUP",
        "OECD_HOURS","HUBERMAN_MINNS","OWID_HOURS_COMBINED",
    }
    missing = required - ids
    assert not missing, f"missing source ids: {sorted(missing)}"

    wave1 = next(r for r in wvs if r["wave"] == "1")
    wave2 = next(r for r in wvs if r["wave"] == "2")
    assert int(wave1["reported_country_society_count"]) == 10
    assert int(wave1["visible_country_list_count"]) == 10
    assert int(wave2["reported_country_society_count"]) == 18
    assert int(wave2["visible_country_list_count"]) == 18

    mismatches = [
        r for r in wvs
        if r["visible_country_list_count"]
        and int(r["reported_country_society_count"]) != int(r["visible_country_list_count"])
    ]
    assert {r["wave"] for r in mismatches} >= {"3","4","5","6"}

    cantril = [r for r in early if r["source_id"] == "CANTRIL_7023"]
    assert len(cantril) == 10

    counts = Counter(r["source_id"] for r in master)
    expected = {
        "CANTRIL_7023": 10,
        "EUROBAROMETER_OWID2017": 809,
        "OWID_HOURS_COMBINED": 5063,
        "WDH_TRENDS": 105,
        "WHR2024_ANNUAL": 2363,
        "WVS_W1": 10,
        "WVS_W2": 18,
        "WVS_W3": 49,
        "WVS_W4": 39,
        "WVS_W5": 54,
        "WVS_W6": 59,
    }
    assert dict(counts) == expected, f"canonical master coverage drift: {dict(counts)}"
    assert len(master) == 8579
    assert all(r["value_inspected"].strip().lower() == "no" for r in master)

    assert len(wdh) == 105
    assert min(int(r["since_year"]) for r in wdh) == 1946
    assert len(euro) == 809
    assert min(int(r["year"]) for r in euro) == 1973
    assert max(int(r["year"]) for r in euro) == 2016

    overlap_map = {(r["pair"], r["unit"]): int(r["overlap_n"]) for r in overlap}
    assert overlap_map[("WHR2024 annual × OWID hours", "country-year")] == 1951
    assert overlap_map[("WHR2024 annual × OWID hours", "country")] == 125
    assert overlap_map[("WVS visible Waves 1-6 × OWID hours", "country code")] == 89

    print(f"sources={len(sources)}")
    print(f"canonical_master_rows={len(master)}")
    print(f"wdh_comparable_series={len(wdh)}")
    print(f"eurobarometer_entity_years={len(euro)}")
    print(f"wvs_metadata_mismatch_waves={','.join(r['wave'] for r in mismatches)}")
    print("effect_inspection=none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
