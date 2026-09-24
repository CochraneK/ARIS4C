#!/usr/bin/env python3
"""Core deterministic transforms for ARIS4C-020."""
from __future__ import annotations
from collections import Counter
from datetime import datetime
from itertools import combinations
from typing import Iterable

MISSING_DOI={"","0","unavailable","n/a","na"}
DATE_FORMATS=("%m/%d/%Y %H:%M","%m/%d/%Y %H:%M:%S","%m/%d/%Y","%Y-%m-%d","%Y/%m/%d")

def norm_doi(value:str)->str:
    x=(value or "").strip().lower()
    for p in ("https://doi.org/","http://doi.org/","doi:"):
        if x.startswith(p):
            x=x[len(p):]
    return "" if x in MISSING_DOI else x

def split_multi(value:str)->tuple[str,...]:
    return tuple(dict.fromkeys(x.strip() for x in (value or "").split(";") if x.strip()))

def parse_date(value:str):
    x=(value or "").strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(x,fmt).date()
        except ValueError:
            pass
    return None

def work_key(row:dict)->tuple[str,str]:
    doi=norm_doi(row.get("OriginalPaperDOI",""))
    if doi:
        return ("doi",doi)
    pmid=(row.get("OriginalPaperPubMedID") or "").strip()
    if pmid and pmid.lower() not in {"0","unavailable","n/a","na"}:
        return ("pmid",pmid)
    return ("record",(row.get("Record ID") or "").strip())

def build_work_records(rows:Iterable[dict])->dict[tuple[str,str],dict]:
    works={}
    for row in rows:
        if (row.get("RetractionNature") or "").strip()!="Retraction":
            continue
        key=work_key(row)
        w=works.setdefault(key,{
            "key_type":key[0],"key":key[1],"record_ids":[],
            "retraction_dates":[],"publication_dates":[],
            "reasons":set(),"countries":set(),"subjects":set(),
            "institutions":set(),"authors":set(),"article_types":set(),
            "publishers":set(),"journals":set()
        })
        rid=(row.get("Record ID") or "").strip()
        if rid: w["record_ids"].append(rid)
        rd=parse_date(row.get("RetractionDate","")); pd=parse_date(row.get("OriginalPaperDate",""))
        if rd: w["retraction_dates"].append(rd)
        if pd: w["publication_dates"].append(pd)
        for field,target in [
            ("Reason","reasons"),("Country","countries"),("Subject","subjects"),
            ("Institution","institutions"),("Author","authors"),("ArticleType","article_types")
        ]:
            w[target].update(split_multi(row.get(field,"")))
        for field,target in [("Publisher","publishers"),("Journal","journals")]:
            value=(row.get(field) or "").strip()
            if value: w[target].add(value)

    for w in works.values():
        w["earliest_retraction_date"]=min(w["retraction_dates"]) if w["retraction_dates"] else None
        w["earliest_publication_date"]=min(w["publication_dates"]) if w["publication_dates"] else None
        if w["earliest_retraction_date"] and w["earliest_publication_date"]:
            w["lag_days"]=(w["earliest_retraction_date"]-w["earliest_publication_date"]).days
        else:
            w["lag_days"]=None
    return works

def full_counts(works:dict,attr:str)->Counter:
    out=Counter()
    for w in works.values():
        vals=sorted(w.get(attr) or [])
        if not vals:
            out["Unknown"]+=1
        else:
            out.update(vals)
    return out

def fractional_counts(works:dict,attr:str)->Counter:
    out=Counter()
    for w in works.values():
        vals=sorted(w.get(attr) or [])
        if not vals:
            out["Unknown"]+=1.0
        else:
            weight=1.0/len(vals)
            for value in vals:
                out[value]+=weight
    return out

def reason_cooccurrence(works:dict):
    nodes=Counter(); edges=Counter()
    for w in works.values():
        labels=sorted(w.get("reasons") or [])
        nodes.update(labels)
        for a,b in combinations(labels,2):
            edges[(a,b)]+=1
    return nodes,edges

def edge_metrics(nodes:Counter,edges:Counter,n_works:int):
    out=[]
    for (a,b),n in edges.items():
        pa=nodes[a]/n_works if n_works else 0
        pb=nodes[b]/n_works if n_works else 0
        pab=n/n_works if n_works else 0
        lift=(pab/(pa*pb)) if pa and pb else None
        jaccard=n/(nodes[a]+nodes[b]-n) if (nodes[a]+nodes[b]-n) else None
        out.append({"reason_a":a,"reason_b":b,"n":n,"jaccard":jaccard,"lift":lift})
    return out
