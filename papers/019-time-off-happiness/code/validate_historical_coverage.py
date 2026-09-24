#!/usr/bin/env python3
"""Validate ARIS4C019 historical coverage seed registries.

This script intentionally checks source/coverage structure only. It does not inspect
new time-off × happiness effects.
"""
from __future__ import annotations

import csv
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

    assert len(sources) >= 10
    ids = {r["source_id"] for r in sources}
    required = {"ILO_C052","ILO_C132","WORLD_2015","WDH_NATIONS","CANTRIL_7023","EUROBAROMETER","WVS","WHR_GALLUP","OECD_HOURS"}
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
    wvs1 = [r for r in early if r["source_id"] == "WVS_W1"]
    assert len(cantril) == 10
    assert len(wvs1) == 10

    print(f"sources={len(sources)}")
    print(f"wvs_waves={len(wvs)}")
    print(f"wvs_metadata_mismatch_waves={','.join(r['wave'] for r in mismatches)}")
    print(f"cantril_country_rows={len(cantril)}")
    print(f"wvs1_country_rows={len(wvs1)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
