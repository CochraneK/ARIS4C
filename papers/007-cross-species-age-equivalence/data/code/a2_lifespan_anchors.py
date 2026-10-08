"""A2 生活史锚点映射 (life-history anchor map) - SELF-BUILT.
Baseline status: Animal-Age GitHub baseline search -> 0 results (prior session) => self-built.

Frozen design (no fitting): piecewise-linear (hence monotone) mapping of species age ->
human-equivalent age through homologous anchors; reference frame = human anAge anchors.
Anchors (tableB age_days):
  primary (anAge rows): conception, birth, weaning, sexual_maturity_female
  sensitivity (PanTHERIA rows where present): weaning_PanTHERIA, sexual_maturity_PanTHERIA
  (tableB has no PanTHERIA gestation row -> conception shared anAge-derived; documented)
Anchors kept in canonical order conception<birth<weaning<sexmat; a PT anchor breaking
monotonicity is dropped (guard). Below first / above last anchor: linear extrapolation with
the adjacent segment slope (crude beyond sexual maturity; documented limitation).

Input : data/tableA_species.csv (grid L_max,anAge), data/tableB_events.csv (anchor ages, days)
Grid  : a_q = q * L_max_anAge(s) yrs -> days (365.25 d/y) -> map -> /365.25 = human yrs
Output: data/fragments/fragA2.csv
  species,species_id,q,a_years,y_low,y_high,y_mid,out_unit,input_note
"""
import csv
import os

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DPY = 365.25
QS = [0.25, 0.50, 0.75, 0.90, 0.95, 0.99]
ORDER = ["conception", "birth", "weaning", "sexual_maturity"]
EVAR = {"an": {"conception": "conception", "birth": "birth", "weaning": "weaning",
               "sexual_maturity": "sexual_maturity_female"},
        "pt": {"conception": "conception", "birth": "birth", "weaning": "weaning_PanTHERIA",
               "sexual_maturity": "sexual_maturity_PanTHERIA"}}


def pts_for(events, var, sid):
    pts, prev = [], -1e18
    for key in ORDER:
        row = next((x for x in events if x["species_id"] == sid and x["event"] == EVAR[var][key]), None)
        if row:
            a = float(row["age_days"])
            if a > prev:  # canonical order + monotonicity guard
                pts.append((key, a))
                prev = a
    return pts


def map_age(a, sp, hum):
    if len(sp) < 2:
        return None
    if a <= sp[0][1]:
        (k0, a0), (k1, a1) = sp[0], sp[1]
        return hum[k0] + (a - a0) * (hum[k1] - hum[k0]) / (a1 - a0)
    for i in range(len(sp) - 1):
        (k0, a0), (k1, a1) = sp[i], sp[i + 1]
        if a <= a1:
            return hum[k0] + (a - a0) * (hum[k1] - hum[k0]) / (a1 - a0)
    (k0, a0), (k1, a1) = sp[-2], sp[-1]
    return hum[k1] + (a - a1) * (hum[k1] - hum[k0]) / (a1 - a0)


def build():
    A = list(csv.DictReader(open(os.path.join(D, "data", "tableA_species.csv"), newline="", encoding="utf-8")))
    B = list(csv.DictReader(open(os.path.join(D, "data", "tableB_events.csv"), newline="", encoding="utf-8")))
    hum = {k: float(next(x["age_days"] for x in B if x["species_id"] == "2410" and x["event"] == EVAR["an"][k]))
           for k in ORDER}
    out = os.path.join(D, "data", "fragments")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "fragA2.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["species", "species_id", "q", "a_years", "y_low", "y_high", "y_mid", "out_unit", "input_note"])
        for r in A:
            sid, La = r["species_id"], float(r["max_age_yrs"])
            for q in QS:
                a = q * La * DPY
                vals, used = [], []
                for var in ("an", "pt"):
                    p = pts_for(B, var, sid)
                    y = map_age(a, p, hum)
                    if y is not None:
                        vals.append(y / DPY)
                        used.append(var + ":" + ",".join(k for k, _ in p))
                if vals:
                    w.writerow([r["common_name"], sid, q, round(a / DPY, 6), round(min(vals), 6),
                                round(max(vals), 6), round(sum(vals) / len(vals), 6), "human_eq_years",
                                "; ".join(used)])


if __name__ == "__main__":
    build()
