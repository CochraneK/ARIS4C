"""A0 朴素寿命比 (naive lifespan ratio) - "dog year"-level weak baseline (frozen, no fitting).

Formula (linear map on lifespan ratio):
    y_h = a / L_typ_s * L_typ_h
a = species age (yrs); y_h = human-equivalent age (yrs); L_typ = "typical/expected lifespan".

Proxy choice (documented per frozen spec): tableA has NO typical-lifespan column and the
anAge lu2023 snapshot (MOESM3, 2026-09-30) exposes no typical-lifespan column either
(only maxanAge and PanTHERIA.MaxLongevity_m). Proxy: L_typ := anAge max_age_yrs, the only
available lifespan quantity; PanTHERIA crosscheck (max_age_crosscheck_yrs_PanTHERIA) spans
the interval. L_max overestimates typical lifespan -> A0 is a weak baseline by construction.

Input : data/tableA_species.csv (9 species; human = species_id 2410)
Grid  : a_q = q * L_max_anAge(s), q in {0.25,0.50,0.75,0.90,0.95,0.99}
Output: data/fragments/fragA0.csv
  species,species_id,q,a_years,y_low,y_high,y_mid,out_unit,input_note
Dual input: {anAge, PanTHERIA} L on species side AND human side (4 combos -> interval).
Constant: 365.25 d/y (grid already in years; declared for reproducibility).
No fitting, no result-aware parameters.
"""
import csv
import os

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DPY = 365.25
QS = [0.25, 0.50, 0.75, 0.90, 0.95, 0.99]


def build():
    rows = list(csv.DictReader(open(os.path.join(D, "data", "tableA_species.csv"), newline="", encoding="utf-8")))
    hu = next(r for r in rows if r["species_id"] == "2410")
    Lh = {"an": float(hu["max_age_yrs"]), "pt": float(hu["max_age_crosscheck_yrs_PanTHERIA"])}
    out = os.path.join(D, "data", "fragments")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "fragA0.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["species", "species_id", "q", "a_years", "y_low", "y_high", "y_mid", "out_unit", "input_note"])
        for r in rows:
            La, Lp = float(r["max_age_yrs"]), float(r["max_age_crosscheck_yrs_PanTHERIA"])
            for q in QS:
                a = q * La
                vals = [a / Ls * L for Ls in (La, Lp) for L in (Lh["an"], Lh["pt"])]
                w.writerow([r["common_name"], r["species_id"], q, round(a, 6),
                            round(min(vals), 6), round(max(vals), 6), round(sum(vals) / 4, 6),
                            "human_eq_years",
                            "L_typ proxy = anAge max_age (no typical-lifespan col in snapshot); PT crosscheck"])


if __name__ == "__main__":
    build()
