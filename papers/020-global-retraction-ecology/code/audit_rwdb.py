#!/usr/bin/env python3
"""Deterministic first-pass audit for the Retraction Watch bulk CSV."""
from __future__ import annotations
import argparse, collections, csv, hashlib, json, statistics
from datetime import datetime
from pathlib import Path

NA_DOI={"","unavailable","n/a","na","0"}

def parse_date(value: str):
    value=(value or "").strip()
    for fmt in ("%m/%d/%Y %H:%M","%m/%d/%Y %H:%M:%S","%m/%d/%Y","%Y-%m-%d","%Y/%m/%d"):
        try:return datetime.strptime(value,fmt).date()
        except ValueError: pass
    return None

def clean_doi(value: str) -> str:
    value=(value or "").strip().lower()
    return "" if value in NA_DOI else value

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv_path",type=Path)
    ap.add_argument("--out",type=Path,default=Path("papers/020-global-retraction-ecology/data/derived/rwdb_audit.json"))
    args=ap.parse_args()

    raw=args.csv_path.read_bytes()
    rows=list(csv.DictReader(raw.decode("utf-8-sig").splitlines()))
    nature=collections.Counter((r.get("RetractionNature") or "").strip() for r in rows)
    primary=[r for r in rows if (r.get("RetractionNature") or "").strip()=="Retraction"]

    orig=collections.Counter(filter(None,(clean_doi(r.get("OriginalPaperDOI","")) for r in primary)))
    notice=collections.Counter(filter(None,(clean_doi(r.get("RetractionDOI","")) for r in primary)))
    lags=[]; reasons=collections.Counter(); reason_card=collections.Counter()
    country_card=collections.Counter(); subject_card=collections.Counter()
    for r in primary:
        a=parse_date(r.get("OriginalPaperDate","")); b=parse_date(r.get("RetractionDate",""))
        if a and b: lags.append((b-a).days)
        rr=[x.strip() for x in (r.get("Reason") or "").split(";") if x.strip()]
        cc=[x.strip() for x in (r.get("Country") or "").split(";") if x.strip()]
        ss=[x.strip() for x in (r.get("Subject") or "").split(";") if x.strip()]
        reasons.update(rr); reason_card[len(rr)]+=1; country_card[len(cc)]+=1; subject_card[len(ss)]+=1

    lag_sorted=sorted(lags)
    def q(p): return lag_sorted[round((len(lag_sorted)-1)*p)] if lag_sorted else None
    out={
      "sha256":hashlib.sha256(raw).hexdigest(),
      "rows":len(rows),"nature_counts":dict(nature),"retraction_rows":len(primary),
      "original_doi_available_rows":sum(orig.values()),"original_doi_unique":len(orig),
      "repeated_original_doi_unique":sum(v>1 for v in orig.values()),"original_doi_max_multiplicity":max(orig.values(),default=0),
      "notice_doi_available_rows":sum(notice.values()),"notice_doi_unique":len(notice),
      "parseable_lags":len(lags),"negative_lag_rows":sum(v<0 for v in lags),
      "lag_days":{"p10":q(.10),"p25":q(.25),"median":q(.50),"p75":q(.75),"p90":q(.90)},
      "reason_label_count_distribution":dict(sorted(reason_card.items())),
      "country_count_distribution":dict(sorted(country_card.items())),
      "subject_count_distribution":dict(sorted(subject_card.items())),
      "unique_reason_labels":len(reasons),"top_reason_labels":reasons.most_common(30)
    }
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
