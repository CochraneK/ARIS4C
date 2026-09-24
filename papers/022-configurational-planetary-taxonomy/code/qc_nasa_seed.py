#!/usr/bin/env python3
"""Diagnostic comparison of simple spherical derivations against NASA catalog values.

This is a QC tool, not a source-replacement tool. The NASA comparison table reports
equatorial diameter and equatorial/1-bar gravity, so large flattened planets are
expected to disagree with naive spherical calculations.
"""
from __future__ import annotations
import csv
import math
from pathlib import Path

G = 6.67430e-11
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "raw" / "nasa_nssdc_planetary_fact_sheet_seed.csv"
OUT = ROOT / "data" / "derived" / "nasa_seed_spherical_qc.csv"

def f(x):
    return float(x)

def main():
    with SRC.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    out = []
    for r in rows:
        mass = f(r["mass_1e24kg"]) * 1e24
        radius = f(r["diameter_km"]) * 1000.0 / 2.0
        rho = mass / ((4.0 / 3.0) * math.pi * radius**3)
        grav = G * mass / radius**2
        vesc = math.sqrt(2.0 * G * mass / radius) / 1000.0
        out.append({
            "name": r["name"],
            "density_catalog_kg_m3": r["density_kg_m3"],
            "density_spherical_from_equatorial_diameter_kg_m3": f"{rho:.6f}",
            "density_pct_diff": f"{100*(rho/f(r['density_kg_m3'])-1):.6f}",
            "gravity_catalog_m_s2": r["gravity_m_s2"],
            "gravity_simple_spherical_m_s2": f"{grav:.6f}",
            "gravity_pct_diff": f"{100*(grav/f(r['gravity_m_s2'])-1):.6f}",
            "escape_catalog_km_s": r["escape_velocity_km_s"],
            "escape_simple_spherical_km_s": f"{vesc:.6f}",
            "escape_pct_diff": f"{100*(vesc/f(r['escape_velocity_km_s'])-1):.6f}",
        })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    print(f"wrote {OUT} ({len(out)} rows)")

if __name__ == "__main__":
    main()
