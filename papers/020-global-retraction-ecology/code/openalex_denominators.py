#!/usr/bin/env python3
"""Fetch compact OpenAlex publication denominators by year and grouping field."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

GROUPS={
    "field":"primary_topic.field.id",
    "country":"authorships.countries:include_unknown",
    "source":"primary_location.source.id:include_unknown",
    "type":"type:include_unknown",
}

def get_json(params):
    url="https://api.openalex.org/works?"+urlencode(params,safe=":,|/")
    req=Request(url,headers={"User-Agent":"ARIS4C-020/1.0"})
    with urlopen(req,timeout=60) as resp:
        return json.load(resp)

def grouped(year:int,group:str):
    cursor="*"; rows=[]
    while cursor:
        obj=get_json({"filter":f"publication_year:{year}","group_by":GROUPS[group],"per_page":200,"cursor":cursor})
        rows.extend(obj.get("group_by",[]))
        cursor=(obj.get("meta") or {}).get("next_cursor")
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--from-year",type=int,default=1990)
    ap.add_argument("--to-year",type=int,default=2025)
    ap.add_argument("--group",choices=sorted(GROUPS),default="field")
    ap.add_argument("--out",type=Path)
    args=ap.parse_args()
    out=args.out or Path(f"papers/020-global-retraction-ecology/data/derived/openalex_denominator_{args.group}_{args.from_year}_{args.to_year}.json")
    payload={"schema_version":1,"group":args.group,"openalex_group_by":GROUPS[args.group],"years":{}}
    for year in range(args.from_year,args.to_year+1):
        print(year)
        payload["years"][str(year)]=grouped(year,args.group)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(out)

if __name__=="__main__":
    main()
