#!/usr/bin/env python3
"""Build RWDB reason-label prevalence and co-occurrence network."""
from __future__ import annotations
import argparse,csv,json
from collections import Counter
from itertools import combinations
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("work_jsonl",type=Path)
    ap.add_argument("--nodes",type=Path,default=Path("papers/020-global-retraction-ecology/data/derived/reason_nodes.csv"))
    ap.add_argument("--edges",type=Path,default=Path("papers/020-global-retraction-ecology/data/derived/reason_edges.csv"))
    args=ap.parse_args()

    nodes=Counter(); edges=Counter(); n_works=0
    with args.work_jsonl.open("r",encoding="utf-8") as fh:
        for line in fh:
            if not line.strip(): continue
            work=json.loads(line); n_works+=1
            labels=sorted(set(work.get("reasons") or []))
            nodes.update(labels)
            for pair in combinations(labels,2): edges[pair]+=1

    args.nodes.parent.mkdir(parents=True,exist_ok=True)
    with args.nodes.open("w",encoding="utf-8",newline="") as fh:
        w=csv.writer(fh); w.writerow(["reason","n","share"])
        for reason,n in nodes.most_common():
            w.writerow([reason,n,n/n_works if n_works else 0])

    with args.edges.open("w",encoding="utf-8",newline="") as fh:
        w=csv.writer(fh); w.writerow(["reason_a","reason_b","n","jaccard","lift"])
        for (a,b),n in sorted(edges.items(),key=lambda kv:(-kv[1],kv[0])):
            den=nodes[a]+nodes[b]-n
            j=n/den if den else 0
            pa=nodes[a]/n_works; pb=nodes[b]/n_works; pab=n/n_works
            lift=pab/(pa*pb) if pa and pb else 0
            w.writerow([a,b,n,j,lift])

    print(json.dumps({"works":n_works,"reason_labels":len(nodes),"edges":len(edges)},indent=2))

if __name__=="__main__":
    main()
