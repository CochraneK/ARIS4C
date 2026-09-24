#!/usr/bin/env python3
"""Rebuild ARIS4C022 Pilot-1 derived physics from frozen raw tables."""

from __future__ import annotations
import csv, math, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw_physical_core_v0.1.csv"
ORB = ROOT / "data" / "orbital_geometry_v0.1.csv"
OUT = ROOT / "data" / "derived_physics_v0.1.csv"

G = 6.67430e-11
M_EARTH = 5.97217e24
C_HILL = 2.0 * math.sqrt(3.0)

def f(x):
    return None if x in ("", None) else float(x)

def margot_mclear_main_sequence(a_au: float) -> float:
    return 1.9e-4 * C_HILL ** 1.5 * a_au ** (9.0 / 8.0)

def main():
    with RAW.open(newline="", encoding="utf-8") as fh:
        physical = {r["case_id"]: r for r in csv.DictReader(fh)}
    with ORB.open(newline="", encoding="utf-8") as fh:
        orbit = {r["case_id"]: r for r in csv.DictReader(fh)}

    fields = [
        "case_id","name","official_class","derived_status","surface_gravity_m_s2",
        "escape_velocity_m_s","density_from_mass_radius_g_cm3",
        "density_rel_diff_vs_source","stellar_distance_au","insolation_rel_earth",
        "margot_pi","margot_applicability","source_dependencies","notes"
    ]
    out = []
    for cid, p in physical.items():
        o = orbit[cid]
        m, rkm = f(p["mass_kg"]), f(p["mean_radius_km"])
        row = {"case_id":cid,"name":p["name"],"official_class":p["official_class"],
               "source_dependencies":"raw_physical_core_v0.1 + orbital_geometry_v0.1"}
        if m is None or rkm is None:
            row.update(derived_status="NA_INPUT_MISSING",
                       margot_applicability="PENDING_SMALL_BODY_INPUT" if p["primary_body"]=="Sun" else "NA_SATELLITE",
                       notes="No derived numeric value emitted without required raw inputs.")
            out.append(row); continue

        R = rkm * 1000.0
        dens = m / ((4.0/3.0) * math.pi * R**3) / 1000.0
        source_dens = f(p["density_g_cm3"])
        stellar = f(o["host_solar_distance_au"]) or f(o["heliocentric_semimajor_axis_au"])
        row.update(
            derived_status="DERIVED",
            surface_gravity_m_s2=G*m/R**2,
            escape_velocity_m_s=math.sqrt(2*G*m/R),
            density_from_mass_radius_g_cm3=dens,
            density_rel_diff_vs_source="" if source_dens is None else (dens-source_dens)/source_dens,
            stellar_distance_au="" if stellar is None else stellar,
            insolation_rel_earth="" if stellar is None else 1.0/(stellar**2),
            notes="Derived deterministically; density uses spherical mean-radius approximation and is diagnostic rather than a replacement for source density."
        )
        if p["primary_body"]=="Sun":
            a = f(o["heliocentric_semimajor_axis_au"])
            if a is not None:
                row["margot_pi"] = (m/M_EARTH)/margot_mclear_main_sequence(a)
                row["margot_applicability"] = "DIRECT_SUN_ORBIT_AUDIT"
        else:
            row["margot_applicability"] = "NA_SATELLITE"
        out.append(row)

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=fields); w.writeheader(); w.writerows(out)
    print(f"wrote {len(out)} rows")

if __name__=="__main__":
    main()
