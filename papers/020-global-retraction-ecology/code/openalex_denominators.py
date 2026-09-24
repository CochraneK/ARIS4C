#!/usr/bin/env python3
"""Fetch compact OpenAlex publication denominators with reproducible corpus/auth settings."""
from __future__ import annotations
import argparse, json, os, time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

GROUPS={
    "field":"primary_topic.field.id",
    "country":"authorships.countries:include_unknown",
    "source":"primary_location.source.id:include_unknown",
    "type":"type:include_unknown",
}

def get_json(params, api_key="", retries=6):
    url="https://api.openalex.org/works?"+urlencode(params,safe=":,|/")
    headers={"User-Agent":"ARIS4C-020/1.2"}
    if api_key:
        headers["Authorization"]=f"Bearer {api_key}"
    for attempt in range(retries):
        try:
            req=Request(url,headers=headers)
            with urlopen(req,timeout=90) as resp:
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

def grouped(year:int,group:str,api_key:str):
    cursor="*"; rows=[]
    while cursor:
        obj=get_json({
            "filter":f"publication_year:{year}",
            "group_by":GROUPS[group],
            "per_page":200,
            "cursor":cursor,
            "corpus":"core",
        },api_key=api_key)
        rows.extend(obj.get("group_by",[]))
        cursor=(obj.get("meta") or {}).get("next_cursor")
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--from-year",type=int,default=1990)
    ap.add_argument("--to-year",type=int,default=2025)
    ap.add_argument("--group",choices=sorted(GROUPS),default="field")
    ap.add_argument("--out",type=Path)
    ap.add_argument("--api-key-env",default="OPENALEX_API_KEY")
    args=ap.parse_args()
    if args.from_year>args.to_year:
        raise SystemExit("from-year must be <= to-year")
    api_key=os.getenv(args.api_key_env,"").strip()
    out=args.out or Path(
        f"papers/020-global-retraction-ecology/data/derived/"
        f"openalex_denominator_{args.group}_{args.from_year}_{args.to_year}.json"
    )
    payload={
        "schema_version":2,
        "corpus":"core",
        "group":args.group,
        "openalex_group_by":GROUPS[args.group],
        "from_year":args.from_year,
        "to_year":args.to_year,
        "years":{},
    }
    for year in range(args.from_year,args.to_year+1):
        print(year)
        payload["years"][str(year)]=grouped(year,args.group,api_key)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(out)

if __name__=="__main__":
    main()
