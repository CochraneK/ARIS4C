"""A1 最大寿命相对年龄 (max-lifespan relative age) - frozen formula.

Formula:  R_max(s, a) = a / L_max_s
Output coordinate: NORMALIZED relative age in [0,1] (0 = birth, 1 = L_max).
NOTE: per the frozen definition A1's output is NOT human-equivalent years (that is the
A0/A2 coordinate). Consequence: on the grid a_q = q*L_max,anAge, the anAge-side value is
exactly R = q (identity); the cross-source interval comes from the PanTHERIA L_max.

Input : data/tableA_species.csv
  L_max,s := max_age_yrs (anAge primary), max_age_crosscheck_yrs_PanTHERIA (sensitivity)
Grid  : a_q = q * L_max_anAge(s), q in {0.25,0.50,0.75,0.90,0.95,0.99}
Output: data/fragments/fragA1.csv
  species,species_id,q,a_years,R_low,R_high,R_mid,out_unit,input_note
Constant: 365.25 d/y (grid in years; declared for reproducibility).
No fitting, no result-aware parameters.
"""
import csv
import os

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DPY = 365.25
QS = [0.25, 0.50, 0.75, 0.90, 0.95, 0.99]


def build():
    rows = list(csv.DictReader(open(os.path.join(D, "data", "tableA_species.csv"), newline="", encoding="utf-8")))
    out = os.path.join(D, "data", "fragments")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "fragA1.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["species", "species_id", "q", "a_years", "R_low", "R_high", "R_mid", "out_unit", "input_note"])
        for r in rows:
            La, Lp = float(r["max_age_yrs"]), float(r["max_age_crosscheck_yrs_PanTHERIA"])
            for q in QS:
                a = q * La
                vals = [a / L for L in (La, Lp)]  # a/Lmax with anAge vs PanTHERIA Lmax
                w.writerow([r["common_name"], r["species_id"], q, round(a, 6),
                            round(min(vals), 6), round(max(vals), 6), round(sum(vals) / 2, 6),
                            "relative_age_0_1",
                            "R = a/Lmax; Lmax anAge primary + PanTHERIA crosscheck"])


if __name__ == "__main__":
    build()
