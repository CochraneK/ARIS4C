"""One-click reproduction (stage 2b): run A0-A3 mappers, merge fragments -> data/tableE_partial.csv.

Usage:  python code/run_all.py
Each mapper reads data/tableA_species.csv (+ data/tableB_events.csv for A2/A3) and writes
data/fragments/fragA?.csv; this driver merges them into the Table E partial grid.
Grid: 9 species x q in {0.25,0.50,0.75,0.90,0.95,0.99} (a_q = q * L_max,anAge) x 4 methods.
Every cell keeps an INTERVAL (out_low/out_high/out_mid) over the dual anAge/PanTHERIA
inputs - never collapsed to a single point. No outcome validation is performed here
(Tier 1-4 checks, A4/A5/A6, divergence metrics all belong to stage 3).
"""
import csv
import os
import sys

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(D, "code"))
import a0_natural_lifespan as M0
import a1_max_age as M1
import a2_lifespan_anchors as M2
import a3_loglinear as M3


def merge():
    rows = []
    for name, mod in (("A0", M0), ("A1", M1), ("A2", M2), ("A3", M3)):
        mod.build()
        p = os.path.join(D, "data", "fragments", "frag" + name + ".csv")
        for r in csv.DictReader(open(p, newline="", encoding="utf-8")):
            rows.append({"species": r["species"], "species_id": r["species_id"], "q": r["q"],
                         "a_years": r["a_years"], "method": name,
                         "out_low": r.get("y_low") or r.get("R_low"),
                         "out_high": r.get("y_high") or r.get("R_high"),
                         "out_mid": r.get("y_mid") or r.get("R_mid"),
                         "out_unit": r["out_unit"], "input_note": r["input_note"]})
    rows.sort(key=lambda r: (int(r["species_id"]), float(r["q"]), r["method"]))
    with open(os.path.join(D, "data", "tableE_partial.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("tableE_partial.csv rows={} (expect 216 = 9 species x 6 q x 4 methods)".format(len(rows)))
    for r in rows[:4]:
        print(r["species"], r["method"], "q=" + r["q"], "low=" + r["out_low"], "high=" + r["out_high"])


if __name__ == "__main__":
    merge()
