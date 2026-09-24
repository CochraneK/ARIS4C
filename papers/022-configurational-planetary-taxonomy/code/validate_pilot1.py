#!/usr/bin/env python3
"""Validate ARIS4C022 Pilot-1 orbit + derived layers."""

from __future__ import annotations
import csv, pathlib
from collections import Counter

ROOT=pathlib.Path(__file__).resolve().parents[1]
ORB=ROOT/"data"/"orbital_geometry_v0.1.csv"
DER=ROOT/"data"/"derived_physics_v0.1.csv"

def read(path):
    with path.open(newline="",encoding="utf-8") as fh:
        return list(csv.DictReader(fh))

def main():
    orb, der = read(ORB), read(DER)
    assert len(orb)==50 and len(der)==50
    assert len({r["case_id"] for r in orb})==50
    assert len({r["case_id"] for r in der})==50
    oc=Counter(r["orbit_status"] for r in orb)
    assert oc["INGESTED_DERIVED_A"]==13, oc
    assert oc["INGESTED_JPL_MEAN_ELEMENTS"]==21, oc
    assert oc["NA_NOT_INGESTED"]==16, oc
    dc=Counter(r["derived_status"] for r in der)
    assert dc["DERIVED"]==34 and dc["NA_INPUT_MISSING"]==16, dc
    assert sum(bool(r["margot_pi"]) for r in der)==13
    for r in orb:
        if r["orbit_status"]=="NA_NOT_INGESTED":
            assert r["heliocentric_semimajor_axis_au"]==""
            assert r["primary_orbit_semimajor_axis_km"]==""
    mars=next(r for r in der if r["name"]=="Mars")
    assert 50 < float(mars["margot_pi"]) < 60
    print("PASS: 50-row orbit and derived layers")
    print("PASS: 13 direct-Sun + 21 satellite orbit descriptors + 16 explicit pending")
    print("PASS: 34 derived physics rows and 13 Margot-Pi rows")
    print("PASS: no fabricated orbital values in pending small-body rows")

if __name__=="__main__":
    main()
