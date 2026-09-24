#!/usr/bin/env python3
"""Snapshot OpenAlex core works where is_retracted=true.

The output is an interim JSONL source for bidirectional concordance QA.
"""
from __future__ import annotations
import argparse,hashlib,json,os,time
from datetime import datetime,timezone
from pathlib import Path
from urllib.error import HTTPError,URLError
from urllib.parse import urlencode
from urllib.request import Request,urlopen

def get_json(url,api_key="",retries=6):
    headers={"User-Agent":"ARIS4C-020-openalex-retracted-snapshot/1.0"}
    if api_key: headers["Authorization"]=f"Bearer {api_key}"
    for attempt in range(retries):
        try:
            with urlopen(Request(url,headers=headers),timeout=90) as resp:
                return json.load(resp)
        except HTTPError as exc:
            if exc.code not in {429,500,502,503,504} or attempt==retries-1: raise
            wait=min(60,2**attempt)
            ra=exc.headers.get("Retry-After") if exc.headers else None
            if ra and str(ra).isdigit(): wait=max(wait,int(ra))
            time.sleep(wait)
        except URLError:
            if attempt==retries-1: raise
            time.sleep(min(60,2**attempt))
    raise RuntimeError("unreachable")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",type=Path,default=Path(
        "papers/020-global-retraction-ecology/data/interim/openalex_is_retracted_core.jsonl"
    ))
    ap.add_argument("--api-key-env",default="OPENALEX_API_KEY")
    ap.add_argument("--force",action="store_true",help="Refetch even if the snapshot already exists.")
    ap.add_argument("--manifest-out",type=Path,default=Path("papers/020-global-retraction-ecology/data/manifests/openalex_is_retracted_core.json"),help="Small tracked provenance manifest copied from the local sidecar.")
    args=ap.parse_args()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    meta_path=args.out.with_suffix(args.out.suffix+".meta.json")
    if args.out.exists() and not args.force:
        if meta_path.exists():
            meta=json.loads(meta_path.read_text(encoding="utf-8"))
            args.manifest_out.parent.mkdir(parents=True,exist_ok=True)
            args.manifest_out.write_text(json.dumps(meta,indent=2)+"\n",encoding="utf-8")
        print(json.dumps({"status":"SKIP_EXISTING","out":str(args.out),"meta":str(meta_path),"manifest":str(args.manifest_out)},indent=2))
        return
    api_key=os.getenv(args.api_key_env,"").strip()
    retrieved_at=datetime.now(timezone.utc).isoformat()

    cursor="*"; page=0; total=0
    tmp=args.out.with_suffix(".tmp")
    with tmp.open("w",encoding="utf-8") as fh:
        while cursor:
            params={
                "filter":"is_retracted:true",
                "per_page":200,
                "cursor":cursor,
                "select":"id,doi,display_name,publication_year,publication_date,type,is_retracted",
                "corpus":"core",
            }
            url="https://api.openalex.org/works?"+urlencode(params,safe=":,|/")
            obj=get_json(url,api_key)
            page+=1
            for w in obj.get("results",[]):
                fh.write(json.dumps(w,ensure_ascii=False,separators=(",",":"))+"\n")
                total+=1
            cursor=(obj.get("meta") or {}).get("next_cursor")
            print(f"page={page} total={total}")
    tmp.replace(args.out)
    sha=hashlib.sha256(args.out.read_bytes()).hexdigest()
    meta={
        "schema_version":1,
        "retrieved_at":retrieved_at,
        "endpoint":"https://api.openalex.org/works",
        "filter":"is_retracted:true",
        "corpus":"core",
        "works":total,
        "bytes":args.out.stat().st_size,
        "sha256":sha,
        "api_key_used":bool(api_key),
    }
    meta_path.write_text(json.dumps(meta,indent=2)+"\n",encoding="utf-8")
    args.manifest_out.parent.mkdir(parents=True,exist_ok=True)
    args.manifest_out.write_text(json.dumps(meta,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({**meta,"out":str(args.out),"meta":str(meta_path),"manifest":str(args.manifest_out)},indent=2))

if __name__=="__main__":
    main()
