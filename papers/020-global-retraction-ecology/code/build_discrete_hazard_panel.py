#!/usr/bin/env python3
"""Build aggregated publication-cohort × field × age risk sets.

This avoids downloading the entire non-retracted OpenAlex universe. The
denominator file supplies cohort exposure counts; uniquely matched RWDB works
supply observed retraction events and ages.

IMPORTANT: until no-DOI/unmatched coverage is resolved, event counts are the
DOI/OpenAlex-linkable recorded-retraction subset, not a claim of complete
population incidence.
"""
from __future__ import annotations
import argparse,csv,json
from collections import Counter,defaultdict
from datetime import date
from pathlib import Path

def short_id(x):
    return (x or "").rstrip("/").split("/")[-1]

def parse_date(v):
    try: return date.fromisoformat(v) if v else None
    except ValueError: return None

def field_from_work(work):
    topic=work.get("primary_topic") or {}
    field=topic.get("field") or {}
    if isinstance(field,dict):
        return short_id(field.get("id","")), field.get("display_name") or ""
    return "",""

def load_unique_matches(paths):
    out={}
    for path in paths:
        with path.open("r",encoding="utf-8") as fh:
            for line in fh:
                if not line.strip(): continue
                row=json.loads(line)
                q=(row.get("query_doi") or "").strip().lower()
                c=row.get("candidates") or []
                if q and len(c)==1:
                    out[q]=c[0]
    return out

def load_denominators(path):
    obj=json.loads(path.read_text(encoding="utf-8"))
    if obj.get("group")!="field":
        raise SystemExit("denominator JSON must have group=field")
    out={}
    names={}
    for year,rows in (obj.get("years") or {}).items():
        for row in rows:
            key=short_id(row.get("key",""))
            if not key: continue
            out[(int(year),key)]=int(row.get("count") or 0)
            names[key]=row.get("key_display_name") or row.get("display_name") or key
    return out,names,obj

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("work_jsonl",type=Path)
    ap.add_argument("denominator_field_json",type=Path)
    ap.add_argument("match_jsonl",type=Path,nargs="+")
    ap.add_argument("--analysis-cutoff",default="2026-09-23")
    ap.add_argument("--max-age",type=int,default=15)
    ap.add_argument("--out",type=Path,default=Path(
        "papers/020-global-retraction-ecology/data/derived/discrete_hazard_field_panel.csv"
    ))
    ap.add_argument("--coverage-out",type=Path,default=Path(
        "papers/020-global-retraction-ecology/data/derived/discrete_hazard_coverage.json"
    ))
    args=ap.parse_args()
    cutoff=parse_date(args.analysis_cutoff)
    if cutoff is None:
        raise SystemExit("analysis-cutoff must be YYYY-MM-DD")

    denom,names,denom_meta=load_denominators(args.denominator_field_json)
    matches=load_unique_matches(args.match_jsonl)

    rw={}
    with args.work_jsonl.open("r",encoding="utf-8") as fh:
        for line in fh:
            if not line.strip(): continue
            w=json.loads(line)
            if w.get("key_type")=="doi":
                rw[w["key"]]=w

    events=Counter()
    matched_by_pubyear=Counter()
    all_doi_by_pubyear=Counter()
    for doi,w in rw.items():
        pd=parse_date(w.get("earliest_publication_date"))
        rd=parse_date(w.get("earliest_retraction_date"))
        if pd: all_doi_by_pubyear[pd.year]+=1
        ow=matches.get(doi)
        if not ow or not rd: continue
        pubyear=ow.get("publication_year")
        fid,fname=field_from_work(ow)
        if not pubyear or not fid: continue
        pubyear=int(pubyear)
        matched_by_pubyear[pubyear]+=1
        age=max(0,rd.year-pubyear)
        events[(pubyear,fid,age)]+=1
        if fname: names[fid]=fname

    args.out.parent.mkdir(parents=True,exist_ok=True)
    fields=[
        "publication_year","field_id","field_name","age_year",
        "denominator_at_publication","events_this_age",
        "cumulative_prior_events","at_risk_start",
        "discrete_hazard","cumulative_recorded_retraction_incidence"
    ]
    with args.out.open("w",encoding="utf-8",newline="") as fh:
        wr=csv.DictWriter(fh,fieldnames=fields); wr.writeheader()
        for (pubyear,fid),n0 in sorted(denom.items()):
            if n0<=0 or pubyear>cutoff.year: continue
            max_observed=min(args.max_age,cutoff.year-pubyear)
            cumulative=0
            for age in range(max_observed+1):
                ev=events[(pubyear,fid,age)]
                at_risk=max(0,n0-cumulative)
                hazard=(ev/at_risk) if at_risk else ""
                cumulative_after=cumulative+ev
                incidence=cumulative_after/n0 if n0 else ""
                wr.writerow({
                    "publication_year":pubyear,
                    "field_id":fid,
                    "field_name":names.get(fid,fid),
                    "age_year":age,
                    "denominator_at_publication":n0,
                    "events_this_age":ev,
                    "cumulative_prior_events":cumulative,
                    "at_risk_start":at_risk,
                    "discrete_hazard":hazard,
                    "cumulative_recorded_retraction_incidence":incidence,
                })
                cumulative=cumulative_after

    years=sorted(set(all_doi_by_pubyear)|set(matched_by_pubyear))
    coverage={
        "schema_version":1,
        "analysis_cutoff":args.analysis_cutoff,
        "estimand_boundary":"RWDB DOI/OpenAlex-linkable recorded retractions among OpenAlex core publication denominators until no-DOI/unmatched identity coverage is resolved",
        "denominator_schema_version":denom_meta.get("schema_version"),
        "years":{
            str(y):{
                "rwdb_unique_doi_works_with_publication_date":all_doi_by_pubyear[y],
                "unique_openalex_matched_with_field":matched_by_pubyear[y],
                "match_field_coverage_among_rwdb_doi_works":(
                    matched_by_pubyear[y]/all_doi_by_pubyear[y]
                    if all_doi_by_pubyear[y] else None
                )
            } for y in years
        },
        "gate":"Do not present as full-population hazard until no-DOI/unmatched sensitivity and eligible work-type gates pass."
    }
    args.coverage_out.write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({
        "denominator_cells":len(denom),
        "matched_event_cells":len(events),
        "coverage_file":str(args.coverage_out),
        "panel_file":str(args.out),
    },indent=2))

if __name__=="__main__":
    main()
