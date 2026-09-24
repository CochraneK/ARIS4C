#!/usr/bin/env python3
"""Aggregate OpenAlex 0/1/N DOI match wrappers into a compact coverage report."""
from __future__ import annotations
import argparse,json
from collections import Counter
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("jsonl",type=Path,nargs="+")
    ap.add_argument("--out",type=Path,default=Path("papers/020-global-retraction-ecology/data/derived/openalex_match_summary.json"))
    args=ap.parse_args()

    seen={}; malformed=0
    for path in args.jsonl:
        with path.open("r",encoding="utf-8") as fh:
            for line in fh:
                if not line.strip(): continue
                try: row=json.loads(line)
                except json.JSONDecodeError:
                    malformed+=1; continue
                q=(row.get("query_doi") or "").strip().lower()
                if q: seen[q]=row

    counts=Counter()
    type_counts=Counter()
    retract_flags=Counter()
    ambiguous=[]
    for q,row in seen.items():
        n=int(row.get("candidate_count",0))
        if n==0: counts["unmatched"]+=1
        elif n==1: counts["unique"]+=1
        else:
            counts["ambiguous"]+=1
            ambiguous.append({"query_doi":q,"candidate_count":n,"candidate_ids":[w.get("id") for w in row.get("candidates",[])]})
        for w in row.get("candidates",[]):
            type_counts[w.get("type") or "unknown"]+=1
            retract_flags[str(bool(w.get("is_retracted")))]+=1

    total=len(seen); matched=counts["unique"]+counts["ambiguous"]
    payload={
      "schema_version":1,
      "queried_unique_dois":total,
      "matched_unique_dois":matched,
      "match_rate":matched/total if total else None,
      "unique_single_candidate":counts["unique"],
      "ambiguous_multi_candidate":counts["ambiguous"],
      "unmatched":counts["unmatched"],
      "malformed_jsonl_rows":malformed,
      "candidate_work_types":dict(type_counts.most_common()),
      "candidate_is_retracted":dict(retract_flags.most_common()),
      "ambiguous_examples":ambiguous[:100],
      "gate":"Ambiguous multi-candidate DOI matches require concordance QA before a single OpenAlex Work is selected."
    }
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in payload.items() if k not in {"candidate_work_types","candidate_is_retracted","ambiguous_examples"}},indent=2))

if __name__=="__main__":
    main()
