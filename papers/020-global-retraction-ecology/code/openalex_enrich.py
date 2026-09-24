#!/usr/bin/env python3
"""Resumable OpenAlex enrichment for unique RWDB Retraction DOIs.

One JSONL row is written per *query DOI*, not per OpenAlex Work. This makes
0/1/N candidate matches explicit and prevents duplicate OpenAlex records for
one DOI from silently inflating downstream counts.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, os, time
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

MISSING={"","0","unavailable","n/a","na"}

def norm_doi(v:str)->str:
    x=(v or "").strip().lower()
    for p in ("https://doi.org/","http://doi.org/","doi:"):
        if x.startswith(p):
            x=x[len(p):]
    return "" if x in MISSING else x

def get_json(url:str):
    req=Request(url,headers={"User-Agent":"ARIS4C-020/1.1"})
    with urlopen(req,timeout=60) as resp:
        return json.load(resp)

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("rwdb_csv",type=Path)
    ap.add_argument("--shard",type=int,default=0)
    ap.add_argument("--shards",type=int,default=4)
    ap.add_argument("--out",type=Path)
    ap.add_argument("--sleep",type=float,default=0.08)
    ap.add_argument("--retry-unmatched",action="store_true",
                    help="Retry query DOIs already recorded with zero OpenAlex candidates.")
    ap.add_argument("--api-key-env",default="OPENALEX_API_KEY",
                    help="Environment variable containing an optional OpenAlex API key.")
    args=ap.parse_args()
    if not 0 <= args.shard < args.shards:
        raise SystemExit("invalid shard")

    out=args.out or Path(
        f"papers/020-global-retraction-ecology/data/interim/openalex_shard_{args.shard:02d}.jsonl"
    )
    out.parent.mkdir(parents=True,exist_ok=True)

    with args.rwdb_csv.open("r",encoding="utf-8-sig",newline="") as fh:
        reader=csv.DictReader(fh)
        dois={
            norm_doi(r.get("OriginalPaperDOI",""))
            for r in reader
            if (r.get("RetractionNature") or "").strip()=="Retraction"
        }
    dois.discard("")
    shard=lambda d:int(hashlib.sha256(d.encode()).hexdigest()[:8],16)%args.shards
    todo=sorted(d for d in dois if shard(d)==args.shard)

    done=set()
    if out.exists():
        with out.open("r",encoding="utf-8") as fh:
            for line in fh:
                try:
                    row=json.loads(line)
                except json.JSONDecodeError:
                    continue
                q=norm_doi(row.get("query_doi",""))
                if not q:
                    continue
                if row.get("candidate_count",0)>0 or not args.retry_unmatched:
                    done.add(q)

    pending=[d for d in todo if d not in done]
    select=(
        "id,doi,display_name,publication_year,publication_date,primary_topic,"
        "cited_by_count,type,open_access,is_retracted,authorships,primary_location"
    )
    api_key=os.getenv(args.api_key_env,"").strip()
    matched=unmatched=ambiguous=0

    with out.open("a",encoding="utf-8") as sink:
        for i in range(0,len(pending),100):
            batch=pending[i:i+100]
            params={
                "filter":"doi:"+"|".join(batch),
                "per_page":"100",
                "select":select,
            }
            if api_key:
                params["api_key"]=api_key
            url="https://api.openalex.org/works?"+urlencode(params,safe=":|/,")
            obj=get_json(url)

            grouped=defaultdict(list)
            for work in obj.get("results",[]):
                d=norm_doi(work.get("doi",""))
                if d:
                    grouped[d].append(work)

            for query_doi in batch:
                candidates=sorted(grouped.get(query_doi,[]),key=lambda w:w.get("id",""))
                row={
                    "query_doi":query_doi,
                    "candidate_count":len(candidates),
                    "candidates":candidates,
                }
                sink.write(json.dumps(row,ensure_ascii=False,separators=(",",":"))+"\n")
                if len(candidates)==0: unmatched+=1
                elif len(candidates)==1: matched+=1
                else:
                    matched+=1
                    ambiguous+=1
            sink.flush()
            print(
                f"shard={args.shard} batch={i//100+1}/{(len(pending)+99)//100} "
                f"matched={matched} unmatched={unmatched} ambiguous={ambiguous}"
            )
            time.sleep(args.sleep)

    print(json.dumps({
        "shard":args.shard,
        "shards":args.shards,
        "input_dois":len(todo),
        "already_done":len(done),
        "attempted_now":len(pending),
        "matched_now":matched,
        "unmatched_now":unmatched,
        "ambiguous_now":ambiguous,
        "api_key_used":bool(api_key),
    },indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
