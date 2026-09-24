#!/usr/bin/env python3
"""Descriptive publication-to-retraction lag profile among retracted works.

This is NOT a survival analysis because the input contains only retracted works.
The confirmatory time-to-event model requires the non-retracted publication universe.
"""
from __future__ import annotations
import argparse,csv,json,statistics
from collections import defaultdict,Counter
from pathlib import Path

def quantile(xs,p):
    xs=sorted(xs)
    return xs[round((len(xs)-1)*p)] if xs else None

def summarize(xs):
    xs=[x for x in xs if x is not None]
    return {
        "n":len(xs),
        "p10":quantile(xs,.10),"p25":quantile(xs,.25),
        "median":quantile(xs,.50),"p75":quantile(xs,.75),"p90":quantile(xs,.90),
        "mean":sum(xs)/len(xs) if xs else None,
        "negative":sum(x<0 for x in xs)
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("work_jsonl",type=Path)
    ap.add_argument("--out",type=Path,default=Path("papers/020-global-retraction-ecology/data/derived/lag_profile.json"))
    args=ap.parse_args()

    overall=[]; by_pub_year=defaultdict(list); by_reason=defaultdict(list)
    by_country=defaultdict(list); by_subject=defaultdict(list)
    with args.work_jsonl.open("r",encoding="utf-8") as fh:
        for line in fh:
            if not line.strip(): continue
            w=json.loads(line)
            lag=w.get("lag_days")
            if lag is None: continue
            overall.append(lag)
            pd=w.get("earliest_publication_date")
            if pd: by_pub_year[pd[:4]].append(lag)
            for r in w.get("reasons") or []: by_reason[r].append(lag)
            for c in w.get("countries") or []: by_country[c].append(lag)
            for s in w.get("subjects") or []: by_subject[s].append(lag)

    payload={
        "schema_version":1,
        "estimand":"lag among observed retracted works; not population survival",
        "overall":summarize(overall),
        "by_publication_year":{k:summarize(v) for k,v in sorted(by_pub_year.items())},
        "by_reason":{k:summarize(v) for k,v in sorted(by_reason.items()) if len(v)>=50},
        "by_country":{k:summarize(v) for k,v in sorted(by_country.items()) if len(v)>=50},
        "by_subject":{k:summarize(v) for k,v in sorted(by_subject.items()) if len(v)>=50}
    }
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload["overall"],indent=2))

if __name__=="__main__":
    main()
