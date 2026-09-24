#!/usr/bin/env python3
"""Fetch the 16 frozen ARIS4C022 small-body cases from the JPL SBDB API.

This script intentionally snapshots the raw JSON before flattening selected fields.
It never converts missing values to zero.
"""

from __future__ import annotations

import csv
import json
import pathlib
import time
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
CASE_FRAME = ROOT / "data" / "case_frame_v0.1.csv"
RAW_JSON = ROOT / "data" / "sbdb_small_body_snapshot.json"
FLAT_CSV = ROOT / "data" / "sbdb_small_body_core_v0.1.csv"
BASE = "https://ssd-api.jpl.nasa.gov/sbdb.api"


def fetch_one(name: str) -> dict:
    query = urllib.parse.urlencode({"sstr": name, "phys-par": "1"})
    request = urllib.request.Request(
        f"{BASE}?{query}",
        headers={"User-Agent": "ARIS4C022/0.1 (research data provenance)"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def phys_map(payload: dict) -> dict:
    return {item.get("name"): item for item in payload.get("phys_par", [])}


def orbit_map(payload: dict) -> dict:
    orbit = payload.get("orbit", {})
    return {item.get("name"): item for item in orbit.get("elements", [])}


def value(item: dict | None):
    return "" if not item else item.get("value", "")


def sigma(item: dict | None):
    return "" if not item else item.get("sigma", "")


def main() -> None:
    with CASE_FRAME.open(newline="", encoding="utf-8") as fh:
        cases = [r for r in csv.DictReader(fh) if r["official_class"] == "small_body"]

    snapshot = {}
    flat = []
    for i, case in enumerate(cases):
        payload = fetch_one(case["name"])
        snapshot[case["case_id"]] = payload
        p = phys_map(payload)
        o = orbit_map(payload)
        flat.append(
            {
                "case_id": case["case_id"],
                "name": case["name"],
                "spkid": payload.get("object", {}).get("spkid", ""),
                "diameter_km": value(p.get("diameter")),
                "diameter_sigma_km": sigma(p.get("diameter")),
                "gm_km3_s2": value(p.get("GM")),
                "gm_sigma_km3_s2": sigma(p.get("GM")),
                "density_g_cm3": value(p.get("density")),
                "density_sigma_g_cm3": sigma(p.get("density")),
                "rotation_period_h": value(p.get("rot_per")),
                "geometric_albedo": value(p.get("albedo")),
                "semimajor_axis_au": value(o.get("a")),
                "eccentricity": value(o.get("e")),
                "inclination_deg": value(o.get("i")),
                "source": "JPL_SBDB_API",
            }
        )
        if i + 1 < len(cases):
            time.sleep(0.15)

    RAW_JSON.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with FLAT_CSV.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(flat[0]))
        writer.writeheader()
        writer.writerows(flat)

    print(f"wrote {len(flat)} cases to {FLAT_CSV}")
    print(f"raw snapshot: {RAW_JSON}")


if __name__ == "__main__":
    main()
