#!/usr/bin/env python3
"""Validate ARIS4C022 evidence-state v0.3 after moon/boundary batch 02."""

from __future__ import annotations
import csv, pathlib

ROOT=pathlib.Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"evidence_state_v0.3.csv"
PREFIXES=["composition","atmosphere","differentiation","geologic_activity","ocean","tidal_heating"]
ALLOWED={"PENDING_REVIEW","DIRECT_MEASURED","STRONGLY_CONSTRAINED","MODEL_INFERRED","EVIDENCE_OF_ABSENCE","NA_NOT_MEASURED","NA_UNCERTAIN","NA_SOURCE_CONFLICT","NA_NOT_APPLICABLE"}
EXPECTED={"composition":19,"atmosphere":18,"differentiation":18,"geologic_activity":9,"ocean":5,"tidal_heating":13}

def main():
    with DATA.open(newline="",encoding="utf-8") as fh:
        rows=list(csv.DictReader(fh))
    assert len(rows)==50 and len({r["case_id"] for r in rows})==50
    assert all(r["review_status"]=="UNEXPOSED_TO_QCA_RESULT" for r in rows)
    for r in rows:
        for p in PREFIXES:
            st=r[p+"_state"]; val=r[p+"_value"]; src=r[p+"_source_key"]
            assert st in ALLOWED,(r["name"],p,st)
            if st=="PENDING_REVIEW":
                assert val=="" and src=="",(r["name"],p)
            else:
                assert src!="",(r["name"],p,st)
                if st!="NA_NOT_APPLICABLE": assert val!="",(r["name"],p,st)
    counts={p:sum(r[p+"_state"]!="PENDING_REVIEW" for r in rows) for p in PREFIXES}
    assert counts==EXPECTED,(counts,EXPECTED)
    moon_batch=[r for r in rows if r["coding_batch"]=="MOON_BOUNDARY_02_2026-09-24"]
    assert len(moon_batch)==9
    charon=next(r for r in rows if r["name"]=="Charon")
    assert charon["ocean_state"]=="PENDING_REVIEW"
    europa=next(r for r in rows if r["name"]=="Europa")
    assert europa["ocean_value"]=="STRONG_EVIDENCE"
    enc=next(r for r in rows if r["name"]=="Enceladus")
    assert enc["ocean_value"]=="CONFIRMED_OR_NEAR_CONSENSUS"
    print("PASS: evidence_state_v0.3")
    print("PASS:",counts,"total",sum(counts.values()))
    print("PASS: 9-case moon/boundary batch remains QCA-unexposed")

if __name__=="__main__":
    main()
