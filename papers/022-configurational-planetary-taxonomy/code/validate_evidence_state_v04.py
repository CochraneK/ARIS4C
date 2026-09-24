#!/usr/bin/env python3
"""Validate ARIS4C022 evidence-state v0.4 and conflict audit semantics."""

from __future__ import annotations
import csv, pathlib

ROOT=pathlib.Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"evidence_state_v0.4.csv"
PREFIXES=["composition","atmosphere","differentiation","geologic_activity","ocean","tidal_heating"]
ALLOWED={"PENDING_REVIEW","DIRECT_MEASURED","STRONGLY_CONSTRAINED","MODEL_INFERRED","EVIDENCE_OF_ABSENCE","NA_NOT_MEASURED","NA_UNCERTAIN","NA_SOURCE_CONFLICT","NA_NOT_APPLICABLE"}
MISSING_STATES={"NA_NOT_MEASURED","NA_SOURCE_CONFLICT","NA_NOT_APPLICABLE"}
EXPECTED={'composition':34,'atmosphere':24,'differentiation':24,'geologic_activity':23,'ocean':14,'tidal_heating':20}

def main():
    with DATA.open(newline="",encoding="utf-8") as fh:
        rows=list(csv.DictReader(fh))
    assert len(rows)==50 and len({r["case_id"] for r in rows})==50
    assert all(r["review_status"]=="UNEXPOSED_TO_QCA_RESULT" for r in rows)
    for r in rows:
        for p in PREFIXES:
            st,val,src=r[p+"_state"],r[p+"_value"],r[p+"_source_key"]
            assert st in ALLOWED,(r["name"],p,st)
            if st=="PENDING_REVIEW":
                assert val=="" and src=="",(r["name"],p)
            else:
                assert src!="",(r["name"],p,st)
                if st not in MISSING_STATES:
                    assert val!="",(r["name"],p,st)
    counts={p:sum(r[p+"_state"]!="PENDING_REVIEW" for r in rows) for p in PREFIXES}
    assert counts==EXPECTED,(counts,EXPECTED)
    batch=[r for r in rows if r["coding_batch"]=="MID_MOON_DWARF_03_2026-09-24"]
    assert len(batch)==15,len(batch)
    mimas=next(r for r in rows if r["name"]=="Mimas")
    assert mimas["ocean_value"]=="STRONG_EVIDENCE"
    makemake=next(r for r in rows if r["name"]=="Makemake")
    assert makemake["composition_state"]=="NA_NOT_MEASURED" and makemake["composition_value"]==""
    print("PASS: evidence_state_v0.4")
    print("PASS:",counts,"total",sum(counts.values()))
    print("PASS: 15-case batch 03 + Pluto/Triton updates; all QCA-unexposed")

if __name__=="__main__":
    main()
