#!/usr/bin/env python3
"""Score ARIS4C-023 v0.2 H-vs-M validation with family-level diagnostics."""
import argparse,csv,json,math
from collections import Counter,defaultdict
from pathlib import Path

ALLOWED={"present","absent","uncertain","not_observed"}
KEY=("bundle_id","motif_id")

def load(path):
    out={}
    with open(path,newline="",encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            k=tuple(row[x].strip() for x in KEY)
            s=row["state"].strip().lower()
            if s not in ALLOWED: raise ValueError(f"{path}: incomplete/invalid state {s!r} at {k}")
            if k in out: raise ValueError(f"{path}: duplicate {k}")
            out[k]=(s,row["family"].strip())
    return out

def agree(a,b): return sum(x==y for x,y in zip(a,b))/len(a) if a else math.nan
def kappa(a,b):
    n=len(a)
    if not n:return math.nan
    pa=agree(a,b);ca,cb=Counter(a),Counter(b);cats=set(ca)|set(cb)
    pe=sum((ca[c]/n)*(cb[c]/n) for c in cats)
    return (pa-pe)/(1-pe) if pe<1 else math.nan
def ac1(a,b):
    n=len(a)
    if not n:return math.nan
    cats=sorted(set(a)|set(b));q=len(cats)
    if q<=1:return math.nan
    pa=agree(a,b); pooled={c:(a.count(c)+b.count(c))/(2*n) for c in cats}
    pe=sum(p*(1-p) for p in pooled.values())/(q-1)
    return (pa-pe)/(1-pe) if pe<1 else math.nan
def finite(x): return None if isinstance(x,float) and (math.isnan(x) or math.isinf(x)) else x

def metrics(A,B,keys):
    av=[A[k][0] for k in keys];bv=[B[k][0] for k in keys]
    binary=[k for k in keys if A[k][0] in {"present","absent"} and B[k][0] in {"present","absent"}]
    ab=[A[k][0] for k in binary];bb=[B[k][0] for k in binary]
    return {
      "n":len(keys),"raw_agreement":finite(agree(av,bv)),
      "cohen_kappa_four_state":finite(kappa(av,bv)),"gwet_ac1_four_state":finite(ac1(av,bv)),
      "binary_n":len(binary),"binary_raw_agreement":finite(agree(ab,bb)),
      "binary_cohen_kappa":finite(kappa(ab,bb)),"binary_gwet_ac1":finite(ac1(ab,bb))
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--h",required=True);ap.add_argument("--m",required=True);ap.add_argument("--out");args=ap.parse_args()
    H,M=load(args.h),load(args.m)
    if set(H)!=set(M): raise ValueError("H/M key sets differ")
    keys=sorted(H)
    if len(keys)!=190: raise ValueError(f"expected 190 keys, got {len(keys)}")
    byfam=defaultdict(list)
    for k in keys:
      fh,fm=H[k][1],M[k][1]
      if fh!=fm: raise ValueError(f"family mismatch at {k}")
      byfam[fh].append(k)
    out={"overall":metrics(H,M,keys),"by_family":{f:metrics(H,M,ks) for f,ks in sorted(byfam.items())}}
    o=out["overall"]
    fam_pass=all(v["raw_agreement"] is not None and v["raw_agreement"]>=0.75 for v in out["by_family"].values())
    out["frozen_numeric_gate"]={
      "raw_agreement_ge_0_80":o["raw_agreement"] is not None and o["raw_agreement"]>=0.80,
      "binary_kappa_ge_0_70":o["binary_cohen_kappa"] is not None and o["binary_cohen_kappa"]>=0.70,
      "binary_ac1_ge_0_75":o["binary_gwet_ac1"] is not None and o["binary_gwet_ac1"]>=0.75,
      "each_family_raw_ge_0_75":fam_pass
    }
    txt=json.dumps(out,ensure_ascii=False,indent=2)+"\n"
    if args.out:Path(args.out).write_text(txt,encoding="utf-8")
    print(txt,end="")

if __name__=="__main__":
    main()
