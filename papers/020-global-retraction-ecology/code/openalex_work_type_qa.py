#!/usr/bin/env python3
"""Create deterministic QA sample for anomalous OpenAlex work types.

This script does not auto-adjudicate correctness. It materializes the cases
needed for a blinded/manual concordance review before denominator eligibility
is frozen.
"""
from __future__ import annotations
import argparse,csv,hashlib,json
from collections import defaultdict
from pathlib import Path

ANOMALOUS={"retraction","erratum","reference-entry","supplementary-materials","paratext","other"}

def rank_key(doi:str)->str:
    return hashlib.sha256(("ARIS4C020-WORKTYPE:"+doi).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("work_jsonl",type=Path)
    ap.add_argument("match_jsonl",type=Path,nargs="+")
    ap.add_argument("--per-type",type=int,default=50)
    ap.add_argument("--out",type=Path,default=Path(
        "papers/020-global-retraction-ecology/data/derived/openalex_work_type_qa.csv"
    ))
    args=ap.parse_args()

    rw={}
    with args.work_jsonl.open("r",encoding="utf-8") as fh:
        for line in fh:
            if not line.strip(): continue
            w=json.loads(line)
            if w.get("key_type")=="doi":
                rw[w["key"]]=w

    candidates=defaultdict(list)
    for path in args.match_jsonl:
        with path.open("r",encoding="utf-8") as fh:
            for line in fh:
                if not line.strip(): continue
                row=json.loads(line)
                q=(row.get("query_doi") or "").strip().lower()
                for work in row.get("candidates") or []:
                    typ=work.get("type") or "unknown"
                    if typ in ANOMALOUS:
                        candidates[typ].append((q,work,row.get("candidate_count",0)))

    rows=[]
    for typ,items in sorted(candidates.items()):
        unique={}
        for q,w,n in items:
            unique.setdefault(q,(w,n))
        chosen=sorted(unique.items(),key=lambda kv:rank_key(kv[0]))[:args.per_type]
        for q,(w,n) in chosen:
            r=rw.get(q,{})
            rows.append({
                "openalex_type":typ,
                "query_doi":q,
                "candidate_count":n,
                "openalex_id":w.get("id",""),
                "rw_earliest_publication_date":r.get("earliest_publication_date",""),
                "openalex_publication_date":w.get("publication_date",""),
                "rw_journals":"; ".join(r.get("journals") or []),
                "openalex_title":w.get("display_name",""),
                "adjudication":"",
                "note":"",
            })

    args.out.parent.mkdir(parents=True,exist_ok=True)
    fields=list(rows[0]) if rows else [
        "openalex_type","query_doi","candidate_count","openalex_id",
        "rw_earliest_publication_date","openalex_publication_date","rw_journals",
        "openalex_title","adjudication","note"
    ]
    with args.out.open("w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=fields); w.writeheader(); w.writerows(rows)
    print(json.dumps({
        "rows":len(rows),
        "by_type":{k:sum(r["openalex_type"]==k for r in rows) for k in sorted(candidates)},
        "allowed_adjudications":[
            "ORIGINAL_CORRECT_TYPE","OPENALEX_TYPE_MISCLASSIFICATION",
            "NOTICE_ORIGINAL_CONFUSION","MULTI_CANDIDATE_AMBIGUOUS",
            "RWDB_IDENTITY_ISSUE","OTHER_LEGITIMATE_TYPE"
        ]
    },indent=2))

if __name__=="__main__":
    main()
