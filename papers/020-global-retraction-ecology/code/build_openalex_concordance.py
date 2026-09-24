#!/usr/bin/env python3
"""Quantify RWDB→OpenAlex retraction-status concordance for uniquely matched works.

RWDB defines the primary Retraction population. Therefore OpenAlex
is_retracted=false/unknown among these works is a discordance signal, not a
reason to drop the work.
"""
from __future__ import annotations
import argparse,csv,json
from collections import Counter,defaultdict
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("match_jsonl",type=Path,nargs="+")
    ap.add_argument("--out",type=Path,default=Path(
        "papers/020-global-retraction-ecology/data/derived/openalex_retraction_concordance.json"
    ))
    ap.add_argument("--discordant-csv",type=Path,default=Path(
        "papers/020-global-retraction-ecology/data/derived/openalex_retraction_discordant.csv"
    ))
    args=ap.parse_args()

    rows={}
    malformed=0
    for path in args.match_jsonl:
        with path.open("r",encoding="utf-8") as fh:
            for line in fh:
                if not line.strip(): continue
                try: row=json.loads(line)
                except json.JSONDecodeError:
                    malformed+=1; continue
                q=(row.get("query_doi") or "").strip().lower()
                if q: rows[q]=row

    status=Counter(); by_type=defaultdict(Counter); by_year=defaultdict(Counter)
    discordant=[]
    ambiguous=0; unmatched=0
    for doi,row in rows.items():
        cands=row.get("candidates") or []
        if not cands:
            unmatched+=1; continue
        if len(cands)>1:
            ambiguous+=1; continue
        w=cands[0]
        flag=w.get("is_retracted")
        if flag is True: key="true"
        elif flag is False: key="false"
        else: key="unknown"
        status[key]+=1
        typ=w.get("type") or "unknown"
        year=str(w.get("publication_year") or "unknown")
        by_type[typ][key]+=1
        by_year[year][key]+=1
        if key!="true":
            discordant.append({
                "query_doi":doi,
                "openalex_id":w.get("id"),
                "openalex_is_retracted":flag,
                "openalex_type":typ,
                "publication_year":w.get("publication_year"),
                "display_name":w.get("display_name"),
            })

    unique=sum(status.values())
    payload={
        "schema_version":1,
        "direction":"RWDB primary Retraction work -> OpenAlex metadata concordance",
        "queried_dois":len(rows),
        "unmatched_dois":unmatched,
        "ambiguous_multi_candidate_dois":ambiguous,
        "unique_candidate_dois":unique,
        "openalex_is_retracted":dict(status),
        "concordance_true_share":status["true"]/unique if unique else None,
        "discordant_false_or_unknown":len(discordant),
        "by_openalex_type":{k:dict(v) for k,v in sorted(by_type.items())},
        "by_publication_year":{k:dict(v) for k,v in sorted(by_year.items())},
        "malformed_jsonl_rows":malformed,
        "interpretation":"RWDB defines case membership; OpenAlex false/unknown is a metadata discordance signal, not an exclusion rule.",
        "boundary":"This report estimates RWDB->OpenAlex concordance only. It does not estimate OpenAlex false positives among works absent from RWDB."
    }
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

    fields=["query_doi","openalex_id","openalex_is_retracted","openalex_type","publication_year","display_name"]
    with args.discordant_csv.open("w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=fields); w.writeheader(); w.writerows(sorted(discordant,key=lambda r:r["query_doi"]))

    print(json.dumps({
        "unique_candidate_dois":unique,
        "openalex_true":status["true"],
        "openalex_false":status["false"],
        "openalex_unknown":status["unknown"],
        "concordance_true_share":payload["concordance_true_share"],
        "unmatched":unmatched,
        "ambiguous":ambiguous,
    },indent=2))

if __name__=="__main__":
    main()
