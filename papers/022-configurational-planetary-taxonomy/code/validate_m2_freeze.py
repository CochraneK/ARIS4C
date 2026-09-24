#!/usr/bin/env python3
"""Validate the frozen anti-circularity M2 condition manifest."""

from __future__ import annotations
import json, pathlib

ROOT=pathlib.Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"process"/"M2_CONDITION_FREEZE.json"

def main():
    obj=json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert obj["qca_results_exposed"] is False
    conds=obj["primary_conditions"]
    assert len(conds)==5
    families=[c["family"] for c in conds]
    assert len(set(families))==5
    assert families==["SCALE","BULK_MATERIAL","ATMOSPHERE_RETENTION","INTERNAL_ORGANIZATION","SOLAR_ENERGY"]
    reps={c["representative"] for c in conds}
    prohibited={"direct_sun_orbit","is_satellite","primary_body","margot_pi","soter_mu","official_class"}
    assert not reps.intersection(prohibited)
    assert obj["outcome"]["role"]=="outcome_only"
    assert obj["readiness_gate"]["complete_cases_min"]>=35
    assert obj["calibration_status"]=="CLOSED_NOT_READY"
    print("PASS: frozen five-condition M2 manifest")
    print("PASS: no definitional/dynamical outcome leakage in primary conditions")
    print("PASS: calibration remains closed")

if __name__=="__main__":
    main()
