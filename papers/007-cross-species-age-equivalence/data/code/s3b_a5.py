import json, math, datetime
import numpy as np
import pandas as pd
E, C, AN = "data/tableE.csv", "data/tableC.csv", "data/raw/s3b_anchors.json"
QS = [0.25, 0.5, 0.75, 0.9, 0.95, 0.99]
TGT = math.log(1000.0) / math.log(2.0)
dfE = pd.read_csv(E)
nb = int((dfE["method"] == "A5").sum())
dfE = dfE[dfE["method"] != "A5"].reset_index(drop=True)
dfC = pd.read_csv(C)
raw = json.load(open(AN, encoding="utf-8"))
anc = raw if isinstance(raw, dict) else {x.get("species"): x for x in raw}
hum = dfC[dfC["species"].str.lower().str.startswith("human")].sort_values("age_years")
HA, HS = hum["age_years"].to_numpy(float), hum["S"].to_numpy(float)
HMAX, HMIN = float(HA[-1]), float(HS[-1])
def invH(S):
    return 0.0 if S >= 1.0 else (HMAX if S <= HMIN else float(np.interp(S, HS[::-1], HA[::-1])))
def geta(sp):
    return anc[sp] if sp in anc else next(v for k, v in anc.items() if k.lower() in sp.lower() or sp.lower() in k.lower())
def gom(m, amax):
    f = lambda d: (math.exp(d*amax)-1.0)/(math.exp(d*m)-1.0) - TGT
    lo, hi = 1e-9, 1e-3
    while f(hi) < 0:
        hi *= 2.0
    for _ in range(120):
        mid = (lo+hi)/2.0
        lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    d = (lo+hi)/2.0
    return d*math.log(2.0)/(math.exp(d*m)-1.0), d
def Sg(a, m, amax):
    l, d = gom(m, amax)
    return math.exp(-(l/d)*(math.exp(d*a)-1.0))
rows, dev = [], 0.0
for sp in dfC["species"].unique():
    amax = float(dfC[dfC["species"] == sp]["age_years"].max())
    a = geta(sp)
    print(sp, "amax=", amax, "m=", a["m"])
    for q in QS:
        b = dfE[(dfE["species"] == sp) & (dfE["q"] == q)].iloc[0]
        ay = float(b["a_years"])
        r = b.copy(); r["method"] = "A5"; r["out_unit"] = "human_eq_years"
        if sp.lower().startswith("human"):
            om = ol = oh = ay; cap = ""; dev = max(dev, abs(om-ay))
        else:
            om = invH(Sg(min(ay, amax), a["m"], amax))
            ol = min(om, invH(Sg(min(ay, amax), a["m_low"], amax)))
            oh = max(om, invH(Sg(min(ay, amax), a["m_high"], amax)))
            cap = "; capped@amax" if ay > amax else ""
        r["out_mid"], r["out_low"], r["out_high"] = om, ol, oh
        r["input_note"] = f"A5 {a.get('tier','Tier2')}; m={a['m']:g}({a['m_low']:g}-{a['m_high']:g}); {a.get('m_source','')}; amax={amax:g} anAge{cap}"
        rows.append(r)
out = pd.concat([dfE, pd.DataFrame(rows)], ignore_index=True)
assert set("species q a_years method out_mid out_low out_high out_unit input_note".split()) <= set(dfE.columns)
assert len(out) == 324, len(out)
out.to_csv(E, index=False)
b54 = out[out["method"] == "A5"]
bad = int(((b54["out_mid"] < -0.5) | (b54["out_mid"] > HMAX + 0.5) | b54["out_mid"].isna()).sum())
print("keys:", list(anc.keys()))
print(f"removedA5={nb} total={len(out)} humMaxAge={HMAX} humSmin={HMIN:.2e} humanMaxDev={dev:.3f} bad={bad}")
open("stage3b_progress.md", "a", encoding="utf-8").write(f"[stage3b-fix2 T6] {datetime.date().isoformat()} A5 done: removedA5={nb} total={len(out)} humMaxDev={dev:.3f} bad={bad}\n")
