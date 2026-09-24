#!/usr/bin/env python3
"""Build event-aware unique-work table and compact counting outputs."""
from __future__ import annotations
import argparse,csv,json
from pathlib import Path
from pipeline_core import build_work_records,full_counts,fractional_counts

def serial(w):
    out=dict(w)
    for k in ("retraction_dates","publication_dates"):
        out[k]=[d.isoformat() for d in out[k]]
    for k in ("earliest_retraction_date","earliest_publication_date"):
        out[k]=out[k].isoformat() if out[k] else None
    for k in ("reasons","countries","subjects","institutions","authors","article_types","publishers","journals"):
        out[k]=sorted(out[k])
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("rwdb_csv",type=Path)
    ap.add_argument("--out",type=Path,default=Path("papers/020-global-retraction-ecology/data/derived/work_table.jsonl"))
    ap.add_argument("--summary",type=Path,default=Path("papers/020-global-retraction-ecology/data/derived/work_table_summary.json"))
    args=ap.parse_args()

    with args.rwdb_csv.open("r",encoding="utf-8-sig",newline="") as fh:
        works=build_work_records(csv.DictReader(fh))

    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open("w",encoding="utf-8") as sink:
        for key in sorted(works):
            sink.write(json.dumps(serial(works[key]),ensure_ascii=False,separators=(",",":"))+"\n")

    lags=[w["lag_days"] for w in works.values() if w["lag_days"] is not None]
    summary={
        "unique_work_records":len(works),
        "key_types":{},
        "multi_record_works":sum(len(w["record_ids"])>1 for w in works.values()),
        "max_records_per_work":max((len(w["record_ids"]) for w in works.values()),default=0),
        "negative_lag_works":sum(x<0 for x in lags),
        "country_full_counts":dict(full_counts(works,"countries").most_common()),
        "country_fractional_counts":dict(fractional_counts(works,"countries").most_common()),
        "subject_full_counts":dict(full_counts(works,"subjects").most_common()),
        "subject_fractional_counts":dict(fractional_counts(works,"subjects").most_common())
    }
    for w in works.values():
        summary["key_types"][w["key_type"]]=summary["key_types"].get(w["key_type"],0)+1
    args.summary.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in summary.items() if not k.endswith("_counts")},ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
