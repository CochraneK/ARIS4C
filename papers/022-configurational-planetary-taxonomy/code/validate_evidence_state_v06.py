#!/usr/bin/env python3
from __future__ import annotations
import csv, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"evidence_state_v0.6.csv"
PREFIXES=["composition","atmosphere","differentiation","geologic_activity","ocean","tidal_heating"]
ALLOWED={"PENDING_REVIEW","DIRECT_MEASURED","STRONGLY_CONSTRAINED","MODEL_INFERRED","EVIDENCE_OF_ABSENCE","NA_NOT_MEASURED","NA_UNCERTAIN","NA_SOURCE_CONFLICT","NA_NOT_APPLICABLE"}
MISSING={"NA_NOT_MEASURED","NA_SOURCE_CONFLICT","NA_NOT_APPLICABLE"}
COMPOSITION_ALLOWED={"ROCK_METAL","ROCK_ICE_MIXED","ICE_VOLATILE_RICH","H_HE_ENVELOPE","CARBONACEOUS_HYDRATED","MIXED_UNCERTAIN"}
EXPECTED={'composition':50,'atmosphere':26,'differentiation':37,'geologic_activity':24,'ocean':15,'tidal_heating':36}
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
                if st not in MISSING:
                    assert val!="",(r["name"],p,st)
        if r["composition_value"]:
            assert r["composition_value"] in COMPOSITION_ALLOWED
    counts={p:sum(r[p+"_state"]!="PENDING_REVIEW" for r in rows) for p in PREFIXES}
    assert counts==EXPECTED,(counts,EXPECTED)
    assert counts["composition"]==50
    batch=[r for r in rows if r["coding_batch"]=="BOUNDARY_REMOTE_05_2026-09-24"]
    assert len(batch)==11,len(batch)
    quaoar=next(r for r in rows if r["name"]=="Quaoar")
    assert quaoar["atmosphere_state"]=="EVIDENCE_OF_ABSENCE"
    sedna=next(r for r in rows if r["name"]=="Sedna")
    assert sedna["composition_state"]=="NA_UNCERTAIN"
    print("PASS: evidence_state_v0.6")
    print("PASS:",counts,"total",sum(counts.values()))
    print("PASS: composition evidence-state layer closed at 50/50; all QCA-unexposed")
if __name__=="__main__":
    main()
