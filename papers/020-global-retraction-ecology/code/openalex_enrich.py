#!/usr/bin/env python3
"""Resumable OpenAlex enrichment for unique RWDB Retraction DOIs."""
from __future__ import annotations
import argparse, csv, hashlib, json, time
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
    req=Request(url,headers={"User-Agent":"ARIS4C-020/1.0"})
    with urlopen(req,timeout=60) as resp:
        return json.load(resp)

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("rwdb_csv",type=Path)
    ap.add_argument("--shard",type=int,default=0)
    ap.add_argument("--shards",type=int,default=4)
    ap.add_argument("--out",type=Path)
    ap.add_argument("--sleep",type=float,default=0.08)
    args=ap.parse_args()
    if not 0 <= args.shard < args.shards:
        raise SystemExit("invalid shard")
    out=args.out or Path(f"papers/020-global-retraction-ecology/data/interim/openalex_shard_{args.shard:02d}.jsonl")
    out.parent.mkdir(parents=True,exist_ok=True)

    with args.rwdb_csv.open("r",encoding="utf-8-sig",newline="") as fh:
        reader=csv.DictReader(fh)
        dois={norm_doi(r.get("OriginalPaperDOI","")) for r in reader if (r.get("RetractionNature") or "").strip()=="Retraction"}
    dois.discard("")
    shard=lambda d:int(hashlib.sha256(d.encode()).hexdigest()[:8],16)%args.shards
    todo=sorted(d for d in dois if shard(d)==args.shard)

    done=set()
    if out.exists():
        with out.open("r",encoding="utf-8") as fh:
            for line in fh:
                try:
                    d=norm_doi(json.loads(line).get("doi",""))
                    if d: done.add(d)
                except json.JSONDecodeError:
                    pass

    pending=[d for d in todo if d not in done]
    select="id,doi,display_name,publication_year,publication_date,primary_topic,cited_by_count,type,open_access,is_retracted,authorships,primary_location"
    with out.open("a",encoding="utf-8") as sink:
        for i in range(0,len(pending),100):
            batch=pending[i:i+100]
            params=urlencode({"filter":"doi:"+"|".join(batch),"per_page":"100","select":select},safe=":|/,")
            obj=get_json("https://api.openalex.org/works?"+params)
            for work in obj.get("results",[]):
                sink.write(json.dumps(work,ensure_ascii=False,separators=(",",":"))+"\n")
            sink.flush()
            print(f"shard={args.shard} batch={i//100+1}/{(len(pending)+99)//100} returned={len(obj.get('results',[]))}")
            time.sleep(args.sleep)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
