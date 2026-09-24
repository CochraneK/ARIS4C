#!/usr/bin/env python3
"""Batch-fetch OpenAlex citing works for uniquely matched RWDB works.

Uses filter=cites:W1|W2|... and referenced_works to materialize target→citer
edges. Each completed target batch is stored as a separate JSONL file so the
job is resumable and crash-safe.
"""
from __future__ import annotations
import argparse, hashlib, json, os, time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

def openalex_short_id(value:str)->str:
    x=(value or "").strip().rstrip("/")
    return x.split("/")[-1] if x else ""

def get_json(url:str, api_key:str="", retries:int=6):
    headers={"User-Agent":"ARIS4C-020-citation-afterlife/1.0"}
    if api_key:
        headers["Authorization"]=f"Bearer {api_key}"
    for attempt in range(retries):
        try:
            with urlopen(Request(url,headers=headers),timeout=90) as resp:
                return json.load(resp)
        except HTTPError as exc:
            if exc.code not in {429,500,502,503,504} or attempt==retries-1:
                raise
            wait=min(60,2**attempt)
            retry_after=exc.headers.get("Retry-After") if exc.headers else None
            if retry_after and str(retry_after).isdigit():
                wait=max(wait,int(retry_after))
            time.sleep(wait)
        except URLError:
            if attempt==retries-1:
                raise
            time.sleep(min(60,2**attempt))
    raise RuntimeError("unreachable")

def iter_unique_matches(paths):
    seen={}
    for path in paths:
        with path.open("r",encoding="utf-8") as fh:
            for line in fh:
                if not line.strip(): continue
                row=json.loads(line)
                q=(row.get("query_doi") or "").strip().lower()
                cands=row.get("candidates") or []
                if q and len(cands)==1:
                    seen[q]=cands[0]
    return seen

def batch_name(ids):
    h=hashlib.sha256("|".join(sorted(ids)).encode()).hexdigest()[:16]
    return f"citation_batch_{h}.jsonl"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("match_jsonl",type=Path,nargs="+")
    ap.add_argument("--out-dir",type=Path,default=Path(
        "papers/020-global-retraction-ecology/data/interim/openalex_citation_batches"
    ))
    ap.add_argument("--batch-size",type=int,default=25)
    ap.add_argument("--api-key-env",default="OPENALEX_API_KEY")
    ap.add_argument("--sleep",type=float,default=0.08)
    args=ap.parse_args()
    if not 1 <= args.batch_size <= 100:
        raise SystemExit("batch-size must be 1..100")

    matches=iter_unique_matches(args.match_jsonl)
    targets=[]
    for doi,work in matches.items():
        wid=openalex_short_id(work.get("id",""))
        if wid.startswith("W"):
            targets.append((doi,wid))
    targets=sorted(targets,key=lambda x:x[0])
    args.out_dir.mkdir(parents=True,exist_ok=True)
    api_key=os.getenv(args.api_key_env,"").strip()

    completed=0; queried=0; edges=0
    for i in range(0,len(targets),args.batch_size):
        batch=targets[i:i+args.batch_size]
        ids=[wid for _,wid in batch]
        path=args.out_dir/batch_name(ids)
        if path.exists():
            completed+=1
            continue

        target_by_id={wid:doi for doi,wid in batch}
        cursor="*"; batch_edges={}
        while cursor:
            params={
                "filter":"cites:"+"|".join(ids),
                "per_page":200,
                "cursor":cursor,
                "select":"id,doi,display_name,publication_date,publication_year,type,is_retracted,referenced_works",
                "corpus":"core",
            }
            url="https://api.openalex.org/works?"+urlencode(params,safe=":|/,")
            obj=get_json(url,api_key=api_key)
            for citing in obj.get("results",[]):
                citer_id=openalex_short_id(citing.get("id",""))
                refs={openalex_short_id(x) for x in (citing.get("referenced_works") or [])}
                for target_id in refs.intersection(target_by_id):
                    key=(target_id,citer_id)
                    batch_edges[key]={
                        "target_query_doi":target_by_id[target_id],
                        "target_openalex_id":target_id,
                        "citer_openalex_id":citer_id,
                        "citer_doi":citing.get("doi"),
                        "citer_publication_date":citing.get("publication_date"),
                        "citer_publication_year":citing.get("publication_year"),
                        "citer_type":citing.get("type"),
                        "citer_is_retracted":citing.get("is_retracted"),
                    }
            cursor=(obj.get("meta") or {}).get("next_cursor")
            time.sleep(args.sleep)

        tmp=path.with_suffix(".tmp")
        with tmp.open("w",encoding="utf-8") as fh:
            meta={"_meta":{
                "schema_version":1,
                "corpus":"core",
                "target_count":len(batch),
                "targets":[{"query_doi":d,"openalex_id":w} for d,w in batch],
                "edge_count":len(batch_edges),
            }}
            fh.write(json.dumps(meta,ensure_ascii=False,separators=(",",":"))+"\n")
            for row in sorted(batch_edges.values(),key=lambda r:(r["target_query_doi"],r["citer_openalex_id"])):
                fh.write(json.dumps(row,ensure_ascii=False,separators=(",",":"))+"\n")
        tmp.replace(path)
        queried+=1; edges+=len(batch_edges)
        print(f"batch={i//args.batch_size+1} targets={len(batch)} edges={len(batch_edges)}")

    print(json.dumps({
        "unique_matched_targets":len(targets),
        "batch_size":args.batch_size,
        "batches_skipped_existing":completed,
        "batches_queried_now":queried,
        "edges_written_now":edges,
        "corpus":"core",
        "api_key_used":bool(api_key),
    },indent=2))

if __name__=="__main__":
    main()
