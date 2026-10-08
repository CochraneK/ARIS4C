"""Stage2b acceptance spot-check: 2 species (Human, Mouse) x 2 methods (A1, A3), hand-computed.
A3 MUST match the 6 reference values in lit/clock3_formulas.txt (tol 1e-6; 365.25 d/y).
A1 hand values: R = a / L_max. Also cross-checks written fragments for consistency
(tol 1e-5 to absorb 6-decimal rounding in fragments).
Usage: python code/spotcheck.py   (exit 0 = ALL PASS)
"""
import csv
import math
import os
import sys

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DPY = 365.25
TOL = 1e-6
fails = []


def chk(name, got, want, tol=TOL):
    ok = abs(got - want) <= tol
    print(("PASS " if ok else "FAIL ") + name + " got=%.6f want=%.6f" % (got, want))
    if not ok:
        fails.append(name)


def mhat(G, A):
    return 5.0 * (G / A) ** 0.38


def ymap(G, A, age_y):
    a = age_y * DPY
    raa = (a + G) / (A + G)
    m = mhat(G, A)
    return raa / m - 1.0 if raa >= m else math.log(raa / m)


# --- A3: 6 reference values from lit/clock3_formulas.txt (independent re-computation) ---
chk("A3 human m_hat (G=280,ASM=4745)", mhat(280, 4745), 1.705769)
chk("A3 human Age=30y", ymap(280, 4745, 30.0), 0.311032)
chk("A3 human Age=13y", ymap(280, 4745, 13.0), -0.533370)
chk("A3 mouse m_hat (G=19,ASM=42)", mhat(19, 42), 3.698807)
chk("A3 mouse Age=2y", ymap(19, 42, 2.0), 2.321851)
chk("A3 mouse Age=0.1y", ymap(19, 42, 0.1), -1.402051)

# --- A1: hand values (human q=0.5, mouse q=0.5) ---
chk("A1 human q=0.5 anAge Lmax 61.25/122.5", 61.25 / 122.5, 0.5)
chk("A1 mouse q=0.5 anAge Lmax 2.0/4.0", 2.0 / 4.0, 0.5)
chk("A1 mouse q=0.5 PT Lmax 2.0/6.0", 2.0 / 6.0, 1.0 / 3.0)

# --- fragment consistency (requires run_all.py executed first) ---
def frag_row(fname, sid, q):
    for r in csv.DictReader(open(os.path.join(D, "data", "fragments", fname), newline="", encoding="utf-8")):
        if r["species_id"] == sid and abs(float(r["q"]) - q) < 1e-9:
            return r
    raise SystemExit("missing row in " + fname + " " + sid + " q=" + str(q))


r = frag_row("fragA1.csv", "2410", 0.5)
chk("frag A1 human q=0.5 R_high", float(r["R_high"]), 0.5, 1e-5)
r = frag_row("fragA1.csv", "2683", 0.5)
chk("frag A1 mouse q=0.5 R_low", float(r["R_low"]), 1.0 / 3.0, 1e-5)
r = frag_row("fragA3.csv", "2410", 0.5)
a_h = 0.5 * 122.5
chk("frag A3 human q=0.5 y_mid", float(r["y_mid"]),
    (ymap(280, 4745, a_h) + ymap(280, 5582.93, a_h)) / 2, 1e-5)
print("RESULT:", "ALL PASS" if not fails else "FAILURES: " + str(fails))
sys.exit(1 if fails else 0)
