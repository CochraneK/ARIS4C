#!/usr/bin/env python3
from __future__ import annotations
import csv,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
DER=ROOT/"data"/"derived_physics_v0.3.csv"; EV=ROOT/"data"/"evidence_state_v1.0.csv"; RAW=ROOT/"data"/"raw_physical_core_v0.2.csv"
def read(p):
    with p.open(newline="",encoding="utf-8") as fh:return list(csv.DictReader(fh))
def main():
    der,ev,raw=read(DER),read(EV),read(RAW); db={r["case_id"]:r for r in der}; rb={r["case_id"]:r for r in raw}
    cov={"scale":0,"material":0,"atmosphere":0,"organization":0,"solar":0,"complete":0}; strata={"planet":0,"dwarf_planet":0,"satellite":0,"small_body":0}
    for e in ev:
        d=db[e["case_id"]]
        ok={"scale":bool(d["escape_velocity_m_s"]),"material":bool(d["density_from_mass_radius_g_cm3"]),"atmosphere":bool(e["atmosphere_value"]),"organization":bool(e["differentiation_value"]),"solar":bool(d["insolation_rel_earth"])}
        for k in ("scale","material","atmosphere","organization","solar"):cov[k]+=int(ok[k])
        if all(ok.values()):cov["complete"]+=1;strata[e["official_class"]]+=1
    assert cov=={'scale':44,'material':44,'atmosphere':41,'organization':40,'solar':44,'complete':37},cov
    assert strata=={'planet':8,'dwarf_planet':4,'satellite':15,'small_body':10},strata
    assert all(cov[k]>=40 for k in ("scale","material","atmosphere","organization","solar"))
    assert cov["complete"]>=35 and strata["planet"]==8 and strata["dwarf_planet"]>=4 and strata["satellite"]>=12 and strata["small_body"]>=10
    for name in ("Quaoar","Orcus"):
        r=next(x for x in raw if x["name"]==name)
        assert "SYSTEM_MASS" in r["mass_value_type"]
        assert "system mass" in r["notes"].lower()
    pending=[r["name"] for r in raw if r["official_class"]=="small_body" and r["ingestion_status"]!="INGESTED_PRIORITY10"]
    assert len(pending)==6,pending
    assert all(e["review_status"]=="UNEXPOSED_TO_QCA_RESULT" for e in ev)
    print("PASS: ARIS4C022 M2 readiness")
    print("PASS:",cov)
    print("PASS:",strata)
    print("PASS: calibration may now be frozen independently; QCA results remain closed")
if __name__=="__main__":main()
