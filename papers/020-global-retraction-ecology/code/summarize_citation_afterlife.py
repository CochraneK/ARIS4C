#!/usr/bin/env python3
"""Summarize OpenAlex citation edges relative to earliest RWDB retraction date."""
from __future__ import annotations
import argparse,csv,json
from collections import defaultdict
from datetime import date
from pathlib import Path

def parse_iso(v):
    try:
        return date.fromisoformat(v) if v else None
    except ValueError:
        return None

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("work_jsonl",type=Path)
    ap.add_argument("citation_batch_dir",type=Path)
    ap.add_argument("--out",type=Path,default=Path(
        "papers/020-global-retraction-ecology/data/derived/citation_afterlife_work.csv"
    ))
    args=ap.parse_args()

    events={}
    with args.work_jsonl.open("r",encoding="utf-8") as fh:
        for line in fh:
            if not line.strip(): continue
            w=json.loads(line)
            if w.get("key_type")=="doi" and w.get("earliest_retraction_date"):
                events[w["key"]]=parse_iso(w["earliest_retraction_date"])

    cites=defaultdict(dict)
    batch_files=sorted(args.citation_batch_dir.glob("citation_batch_*.jsonl"))
    for path in batch_files:
        with path.open("r",encoding="utf-8") as fh:
            for line in fh:
                if not line.strip(): continue
                row=json.loads(line)
                if "_meta" in row: continue
                q=(row.get("target_query_doi") or "").strip().lower()
                cid=row.get("citer_openalex_id")
                if q and cid:
                    cites[q][cid]=row

    rows=[]
    for doi,rdate in sorted(events.items()):
        items=list(cites.get(doi,{}).values())
        before=[]; after=[]; same_day=[]; unknown=[]
        for row in items:
            cdate=parse_iso(row.get("citer_publication_date"))
            if cdate is None:
                unknown.append(row); continue
            delta=(cdate-rdate).days
            if delta<0: before.append(delta)
            elif delta==0: same_day.append(delta)
            else: after.append(delta)

        known=len(before)+len(same_day)+len(after)
        post=len(after)
        row={
            "query_doi":doi,
            "retraction_date":rdate.isoformat() if rdate else "",
            "citations_total_edges":len(items),
            "citations_known_date":known,
            "citations_unknown_date":len(unknown),
            "citations_pre_retraction":len(before),
            "citations_same_day":len(same_day),
            "citations_post_retraction":post,
            "post_share_known_date":post/known if known else "",
            "first_post_days":min(after) if after else "",
            "post_within_365d":sum(0<x<=365 for x in after),
            "post_within_730d":sum(0<x<=730 for x in after),
            "post_within_1095d":sum(0<x<=1095 for x in after),
            "post_within_1825d":sum(0<x<=1825 for x in after),
        }
        rows.append(row)

    args.out.parent.mkdir(parents=True,exist_ok=True)
    fields=list(rows[0]) if rows else [
        "query_doi","retraction_date","citations_total_edges","citations_known_date",
        "citations_unknown_date","citations_pre_retraction","citations_same_day",
        "citations_post_retraction","post_share_known_date","first_post_days",
        "post_within_365d","post_within_730d","post_within_1095d","post_within_1825d"
    ]
    with args.out.open("w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=fields); w.writeheader(); w.writerows(rows)

    print(json.dumps({
        "work_rows":len(rows),
        "batch_files":len(batch_files),
        "works_with_any_citation_edge":sum(r["citations_total_edges"]>0 for r in rows),
        "works_with_post_retraction_citation":sum(r["citations_post_retraction"]>0 for r in rows),
        "interpretation":"citation is scholarly attention, not endorsement",
    },indent=2))

if __name__=="__main__":
    main()
