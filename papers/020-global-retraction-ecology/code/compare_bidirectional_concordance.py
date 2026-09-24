#!/usr/bin/env python3
"""Bidirectional DOI concordance between frozen RWDB and OpenAlex retracted works."""
from __future__ import annotations
import argparse,csv,json
from collections import Counter
from pathlib import Path

MISSING={"","0","unavailable","n/a","na"}
def norm(v):
    x=(v or "").strip().lower()
    for p in ("https://doi.org/","http://doi.org/","doi:"):
        if x.startswith(p): x=x[len(p):]
    return "" if x in MISSING else x

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("rwdb_csv",type=Path)
    ap.add_argument("openalex_retracted_jsonl",type=Path)
    ap.add_argument("--out",type=Path,default=Path(
        "papers/020-global-retraction-ecology/data/derived/bidirectional_retraction_concordance.json"
    ))
    ap.add_argument("--openalex-unmatched-csv",type=Path,default=Path(
        "papers/020-global-retraction-ecology/data/derived/openalex_retracted_not_rwdb_original.csv"
    ))
    args=ap.parse_args()

    original=set(); notice=set()
    with args.rwdb_csv.open("r",encoding="utf-8-sig",newline="") as fh:
        for row in csv.DictReader(fh):
            if (row.get("RetractionNature") or "").strip()!="Retraction": continue
            d=norm(row.get("OriginalPaperDOI",""))
            n=norm(row.get("RetractionDOI",""))
            if d: original.add(d)
            if n: notice.add(n)

    oa=[]; oa_by_doi={}; oa_no_doi=0
    with args.openalex_retracted_jsonl.open("r",encoding="utf-8") as fh:
        for line in fh:
            if not line.strip(): continue
            w=json.loads(line); d=norm(w.get("doi",""))
            if d:
                oa.append((d,w))
                oa_by_doi.setdefault(d,[]).append(w)
            else:
                oa_no_doi+=1

    def classify(d):
        if d in original:
            return "matches_rwdb_original_doi"
        if d in notice:
            return "matches_rwdb_notice_doi_only"
        return "absent_from_rwdb_original_and_notice_doi"

    row_cls=Counter(classify(d) for d,_ in oa)
    unique_cls=Counter(classify(d) for d in oa_by_doi)
    unmatched=[]
    for d,works in sorted(oa_by_doi.items()):
        cls=classify(d)
        if cls=="matches_rwdb_original_doi":
            continue
        exemplar=sorted(works,key=lambda w:w.get("id",""))[0]
        unmatched.append({
            "class":"notice_doi_only" if cls=="matches_rwdb_notice_doi_only" else "absent_both",
            "doi":d,
            "openalex_candidate_count":len(works),
            "openalex_id":exemplar.get("id"),
            "type":exemplar.get("type"),
            "publication_year":exemplar.get("publication_year"),
            "display_name":exemplar.get("display_name")
        })

    oa_doi=set(oa_by_doi)
    rwdb_missing=sorted(original-oa_doi)
    payload={
        "schema_version":1,
        "rwdb_unique_original_retraction_doi":len(original),
        "rwdb_unique_notice_doi":len(notice),
        "openalex_core_is_retracted_works_with_doi_rows":len(oa),
        "openalex_core_unique_is_retracted_doi":len(oa_doi),
        "openalex_core_is_retracted_without_doi":oa_no_doi,
        "openalex_to_rwdb_classification_unique_doi":dict(unique_cls),
        "openalex_to_rwdb_classification_work_rows":dict(row_cls),
        "duplicate_doi_work_rows":len(oa)-len(oa_doi),
        "rwdb_original_doi_absent_from_openalex_is_retracted_doi":len(rwdb_missing),
        "rwdb_original_absent_examples":rwdb_missing[:100],
        "interpretation":[
            "RWDB remains the primary event authority.",
            "OpenAlex matches to RWDB notice DOI but not original DOI may represent notice/original object confusion rather than independent false positives.",
            "Absent-both OpenAlex records require title/date/source audit before any false-positive label.",
            "RWDB original DOI absent from OpenAlex is_retracted may reflect metadata lag, missing works, or classification discordance."
        ]
    }
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    fields=["class","doi","openalex_candidate_count","openalex_id","type","publication_year","display_name"]
    with args.openalex_unmatched_csv.open("w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=fields); w.writeheader(); w.writerows(unmatched)
    print(json.dumps({k:v for k,v in payload.items() if isinstance(v,(int,str)) or k.startswith("openalex_to_rwdb_classification")},indent=2))

if __name__=="__main__":
    main()
