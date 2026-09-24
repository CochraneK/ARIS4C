#!/usr/bin/env python3
"""Validate ARIS4C022 evidence-state coding without QCA leakage."""

from __future__ import annotations
import csv, pathlib
from collections import Counter

ROOT=pathlib.Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"evidence_state_v0.2.csv"

ALLOWED_STATES={
"PENDING_REVIEW","DIRECT_MEASURED","STRONGLY_CONSTRAINED","MODEL_INFERRED",
"EVIDENCE_OF_ABSENCE","NA_NOT_MEASURED","NA_UNCERTAIN","NA_SOURCE_CONFLICT","NA_NOT_APPLICABLE"
}
STATE_PREFIXES=["composition","atmosphere","differentiation","geologic_activity","ocean","tidal_heating"]

def main():
    with DATA.open(newline="",encoding="utf-8") as fh:
        rows=list(csv.DictReader(fh))
    assert len(rows)==50
    assert len({r["case_id"] for r in rows})==50
    assert all(r["review_status"]=="UNEXPOSED_TO_QCA_RESULT" for r in rows)
    for r in rows:
        for p in STATE_PREFIXES:
            state=r[p+"_state"]
            assert state in ALLOWED_STATES,(r["name"],p,state)
            value=r[p+"_value"]; source=r[p+"_source_key"]
            if state=="PENDING_REVIEW":
                assert value=="" and source=="",(r["name"],p)
            elif state=="NA_NOT_APPLICABLE":
                assert source!="",(r["name"],p)
            else:
                assert value!="" and source!="",(r["name"],p)
    anchors=[r for r in rows if r["coding_batch"]=="ANCHOR_01_2026-09-24"]
    assert len(anchors)==10
    counts={p:sum(r[p+"_state"]!="PENDING_REVIEW" for r in rows) for p in STATE_PREFIXES}
    assert counts=={"composition":10,"atmosphere":10,"differentiation":10,"geologic_activity":1,"ocean":0,"tidal_heating":10},counts
    print("PASS: 50 evidence rows; 10-anchor batch; all rows unexposed to QCA results")
    print("PASS:",counts)

if __name__=="__main__":
    main()
