#!/usr/bin/env python3
"""Validate ARIS4C022 source-hardened orbit + evidence-state layers."""

from __future__ import annotations
import csv, pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
ORB = ROOT / "data" / "orbital_geometry_v0.2.csv"
DER = ROOT / "data" / "derived_physics_v0.2.csv"
EVID = ROOT / "data" / "evidence_state_v0.1.csv"

def read(path):
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))

def main():
    orb, der, ev = read(ORB), read(DER), read(EVID)
    assert len(orb) == len(der) == len(ev) == 50
    assert len({r["case_id"] for r in orb}) == 50

    oc = Counter(r["orbit_status"] for r in orb)
    assert oc["INGESTED_JPL_APPROX_ELEMENTS"] == 8, oc
    assert oc["INGESTED_DERIVED_A"] == 5, oc
    assert oc["INGESTED_JPL_MEAN_ELEMENTS"] == 21, oc
    assert oc["NA_NOT_INGESTED"] == 16, oc

    sc = Counter(r["source_key"] for r in orb)
    assert sc["JPL_APPROX_PLANET_ELEMENTS"] == 7
    assert sc["JPL_APPROX_PLANET_ELEMENTS_EMB_PROXY"] == 1
    assert sc["JPL_PLANET_PHYS_PERIOD"] == 5
    assert sc["JPL_SAT_MEAN_ELEMENTS"] == 21
    assert sc["JPL_SBDB_API_PLANNED"] == 16

    dc = Counter(r["derived_status"] for r in der)
    assert dc["DERIVED"] == 34 and dc["NA_INPUT_MISSING"] == 16
    assert sum(bool(r["margot_pi"]) for r in der) == 13

    state_cols = [c for c in ev[0] if c.endswith("_state")]
    for r in ev:
        assert r["review_status"] == "UNEXPOSED_TO_QCA_RESULT"
        for c in state_cols:
            assert r[c] == "PENDING_REVIEW", (r["name"], c, r[c])

    earth = next(r for r in orb if r["name"] == "Earth")
    assert earth["heliocentric_a_value_type"] == "JPL_RAW_EM_BARY_PROXY"

    print("PASS: 8 JPL planet-element rows / 5 derived dwarf rows / 21 satellite rows / 16 pending small bodies")
    print("PASS: 34 derived-physics rows and 13 Margot-Pi rows")
    print("PASS: 50-case evidence matrix remains unexposed and fully PENDING_REVIEW")

if __name__ == "__main__":
    main()
