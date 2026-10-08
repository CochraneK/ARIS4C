"""A3 log-linear life-history transform - Lu et al. 2023 (Nat Aging 3:1144) clock-3 forward map.
Frozen formulas (lit/clock3_formulas.txt, verified 2026-09-30; do NOT re-touch XML):
  (4) RAA = (Age + G) / (ASM + G)      G=gestation, ASM=adult sexual maturity (yr or days)
  (5) y = x/m - 1  if x/m >= 1  else  y = log(x/m)     x = RAA
  (8) m_hat = 5 * (G/ASM)^0.38         DEFAULT; L_max-free; c2 = 5.0 is the paper's constant
  (9) forward map y = f(RAA; m_hat)
  (6) oracle m* = c1*(Lmax+G)/(ASM+G)  robustness variant ONLY (1.3x Lmax correction) - NOT default.

Input : data/tableA_species.csv (G = gestation_days; ASM = female_maturity_days, anAge primary)
        data/tableB_events.csv (ASM_PT = sexual_maturity_PanTHERIA; G shared from tableA,
        because tableB has no PanTHERIA gestation row - documented limitation)
Grid  : a_q = q * L_max_anAge(s) yrs -> days via 365.25 d/y (declared constant)
Output coordinate: standardized log-linear age y (dimensionless, cross-species comparable).
Output: data/fragments/fragA3.csv
  species,species_id,q,a_years,y_low,y_high,y_mid,out_unit,input_note
Ref check: 6 hand-computed values in lit/clock3_formulas.txt, tol 1e-6 (code/spotcheck.py).
No fitting; no result-aware parameters.
"""
import csv
import math
import os

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DPY = 365.25
QS = [0.25, 0.50, 0.75, 0.90, 0.95, 0.99]


def mhat(G, asm):
    return 5.0 * (G / asm) ** 0.38


def f_raa(raa, m):
    return raa / m - 1.0 if raa >= m else math.log(raa / m)


def build():
    A = list(csv.DictReader(open(os.path.join(D, "data", "tableA_species.csv"), newline="", encoding="utf-8")))
    B = list(csv.DictReader(open(os.path.join(D, "data", "tableB_events.csv"), newline="", encoding="utf-8")))
    out = os.path.join(D, "data", "fragments")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "fragA3.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["species", "species_id", "q", "a_years", "y_low", "y_high", "y_mid", "out_unit", "input_note"])
        for r in A:
            G = float(r["gestation_days"])
            La = float(r["max_age_yrs"])
            asm = float(r["female_maturity_days"])
            sid = r["species_id"]
            rowpt = next((x for x in B if x["species_id"] == sid and x["event"] == "sexual_maturity_PanTHERIA"), None)
            asm_pt = float(rowpt["age_days"]) if rowpt else asm
            for q in QS:
                a = q * La * DPY  # species age in days
                ys = []
                for A_ in (asm, asm_pt):
                    raa = (a + G) / (A_ + G)
                    ys.append(f_raa(raa, mhat(G, A_)))
                w.writerow([r["common_name"], sid, q, round(a / DPY, 6), round(min(ys), 6), round(max(ys), 6),
                            round(sum(ys) / len(ys), 6), "std_loglinear_y",
                            "G={}d anAge(shared, no PT gestation row in tableB); ASM={}d anAge / {}d PT".format(G, asm, asm_pt)])


if __name__ == "__main__":
    build()
