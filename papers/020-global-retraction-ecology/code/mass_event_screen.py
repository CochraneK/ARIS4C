#!/usr/bin/env python3
"""Screen concentrated retraction episodes without treating them as misconduct incidence."""
from __future__ import annotations
import argparse,csv,json
from collections import Counter,defaultdict
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("work_jsonl",type=Path)
    ap.add_argument("--out",type=Path,default=Path("papers/020-global-retraction-ecology/data/derived/mass_event_screen.json"))
    ap.add_argument("--min-count",type=int,default=25)
    ap.add_argument("--min-year-share",type=float,default=.02)
    args=ap.parse_args()

    yearly=Counter(); publisher_year=Counter(); reason_year=Counter(); journal_year=Counter()
    paper_mill_year=Counter()
    with args.work_jsonl.open("r",encoding="utf-8") as fh:
        for line in fh:
            if not line.strip(): continue
            w=json.loads(line)
            rd=w.get("earliest_retraction_date")
            if not rd: continue
            year=rd[:4]; yearly[year]+=1
            for p in set(w.get("publishers") or []): publisher_year[(year,p)]+=1
            for j in set(w.get("journals") or []): journal_year[(year,j)]+=1
            reasons=set(w.get("reasons") or [])
            for r in reasons: reason_year[(year,r)]+=1
            if "Paper Mill" in reasons: paper_mill_year[year]+=1

    def clusters(counter):
        rows=[]
        for (year,label),n in counter.items():
            den=yearly[year]
            share=n/den if den else 0
            if n>=args.min_count and share>=args.min_year_share:
                rows.append({"year":int(year),"label":label,"n":n,"year_share":share})
        return sorted(rows,key=lambda x:(-x["year_share"],-x["n"],x["year"],x["label"]))

    payload={
        "schema_version":1,
        "interpretation":"screen for concentrated database/retraction episodes; flags are not misconduct incidence estimates",
        "thresholds":{"min_count":args.min_count,"min_year_share":args.min_year_share},
        "yearly_unique_retracted_works":dict(sorted(yearly.items())),
        "paper_mill_by_year":dict(sorted(paper_mill_year.items())),
        "publisher_year_clusters":clusters(publisher_year),
        "journal_year_clusters":clusters(journal_year),
        "reason_year_clusters":clusters(reason_year)
    }
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"years":len(yearly),"publisher_clusters":len(payload["publisher_year_clusters"]),"reason_clusters":len(payload["reason_year_clusters"])},indent=2))

if __name__=="__main__":
    main()
