#!/usr/bin/env python3
"""Compare reason labels observed in a frozen RWDB snapshot with Appendix-B reference labels."""
from __future__ import annotations
import argparse,csv,json,re,unicodedata
from pathlib import Path

def loose(s):
    s=unicodedata.normalize("NFKC",s or "").strip().casefold()
    s=s.replace("–","-").replace("—","-")
    s=re.sub(r"[.]+$","",s)
    s=re.sub(r"\s+"," ",s)
    return s

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("reason_nodes_csv",type=Path)
    ap.add_argument("reference_json",type=Path)
    ap.add_argument("--out",type=Path,default=Path("papers/020-global-retraction-ecology/data/derived/reason_vocab_reconciliation.json"))
    args=ap.parse_args()
    with args.reason_nodes_csv.open("r",encoding="utf-8",newline="") as fh:
        observed=[r["reason"] for r in csv.DictReader(fh)]
    reference=json.loads(args.reference_json.read_text(encoding="utf-8"))["labels"]

    o=set(observed); r=set(reference)
    o_loose={loose(x):x for x in observed}; r_loose={loose(x):x for x in reference}
    payload={
      "schema_version":1,
      "observed_count":len(o),"reference_count":len(r),
      "exact_shared":sorted(o&r),
      "observed_only_exact":sorted(o-r),
      "reference_only_exact":sorted(r-o),
      "loose_shared_count":len(set(o_loose)&set(r_loose)),
      "observed_only_after_loose_normalization":sorted(o_loose[k] for k in set(o_loose)-set(r_loose)),
      "reference_only_after_loose_normalization":sorted(r_loose[k] for k in set(r_loose)-set(o_loose)),
      "normalization_rule":"NFKC + casefold + Unicode dash normalization + terminal-period removal + whitespace collapse"
    }
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in payload.items() if k.endswith("_count") or k.startswith("observed_only") or k.startswith("reference_only")},ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
