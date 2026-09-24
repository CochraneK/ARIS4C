#!/usr/bin/env python3
from __future__ import annotations
import csv,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
EV=ROOT/"data"/"evidence_state_v0.8.csv"
DER=ROOT/"data"/"derived_physics_v0.2.csv"
def read(p):
    with p.open(newline="",encoding="utf-8") as fh:return list(csv.DictReader(fh))
def main():
    ev,der=read(EV),read(DER); db={r["case_id"]:r for r in der}
    cov={"scale":0,"material":0,"atmosphere":0,"organization":0,"solar":0,"complete":0}
    strata={"planet":0,"dwarf_planet":0,"satellite":0,"small_body":0}
    assert len(ev)==50 and all(r["review_status"]=="UNEXPOSED_TO_QCA_RESULT" for r in ev)
    for r in ev:
        d=db[r["case_id"]]
        ok={"scale":bool(d["escape_velocity_m_s"]),"material":bool(d["density_from_mass_radius_g_cm3"]),"atmosphere":bool(r["atmosphere_value"]),"organization":bool(r["differentiation_value"]),"solar":bool(d["insolation_rel_earth"])}
        for k in ("scale","material","atmosphere","organization","solar"):cov[k]+=int(ok[k])
        if all(ok.values()):cov["complete"]+=1;strata[r["official_class"]]+=1
    exp={'scale':34,'material':34,'atmosphere':31,'organization':40,'solar':34,'complete':25}
    exps={'planet':8,'dwarf_planet':4,'satellite':13,'small_body':0}
    assert cov==exp,(cov,exp);assert strata==exps,(strata,exps)
    assert cov["organization"]>=40
    assert next(r for r in ev if r["name"]=="Phobos")["atmosphere_value"]=="NONE_OR_NEGLIGIBLE"
    assert next(r for r in ev if r["name"]=="Iapetus")["atmosphere_value"]=="NONE_OR_NEGLIGIBLE"
    assert next(r for r in ev if r["name"]=="Ariel")["differentiation_value"]=="DIFFERENTIATED"
    print("PASS: readiness Batch 07",cov,strata)
    print("PASS: INTERNAL_ORGANIZATION gate >=40")
    print("PASS: calibration remains closed")
if __name__=="__main__":main()
