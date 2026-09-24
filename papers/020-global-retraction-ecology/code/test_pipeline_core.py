#!/usr/bin/env python3
"""Regression tests for ARIS4C-020 core identity/counting rules."""
from pipeline_core import build_work_records,fractional_counts,reason_cooccurrence,norm_doi

def fixture():
    return [
      {"Record ID":"1","RetractionNature":"Retraction","OriginalPaperDOI":"10.1/A","OriginalPaperPubMedID":"",
       "RetractionDate":"01/10/2020 0:00","OriginalPaperDate":"01/01/2019 0:00",
       "Reason":"Paper Mill; Compromised Peer Review","Country":"China; United States","Subject":"Tech; CS",
       "Institution":"","Author":"","ArticleType":"Research Article","Publisher":"P","Journal":"J"},
      {"Record ID":"2","RetractionNature":"Retraction","OriginalPaperDOI":"https://doi.org/10.1/a","OriginalPaperPubMedID":"",
       "RetractionDate":"02/10/2020 0:00","OriginalPaperDate":"01/01/2019 0:00",
       "Reason":"Investigation by Journal/Publisher; Paper Mill","Country":"China","Subject":"Tech",
       "Institution":"","Author":"","ArticleType":"Research Article","Publisher":"P","Journal":"J"},
      {"Record ID":"3","RetractionNature":"Retraction","OriginalPaperDOI":"","OriginalPaperPubMedID":"123",
       "RetractionDate":"01/10/2021 0:00","OriginalPaperDate":"01/10/2020 0:00",
       "Reason":"Error in Data","Country":"United Kingdom","Subject":"Medicine",
       "Institution":"","Author":"","ArticleType":"Research Article","Publisher":"Q","Journal":"K"},
      {"Record ID":"4","RetractionNature":"Correction","OriginalPaperDOI":"10.1/b","OriginalPaperPubMedID":"",
       "RetractionDate":"01/10/2021 0:00","OriginalPaperDate":"01/10/2020 0:00",
       "Reason":"Error in Data","Country":"France","Subject":"Medicine",
       "Institution":"","Author":"","ArticleType":"Research Article","Publisher":"Q","Journal":"K"}
    ]

def main():
    assert norm_doi("https://doi.org/10.1/A")=="10.1/a"
    works=build_work_records(fixture())
    assert len(works)==2
    a=works[("doi","10.1/a")]
    assert a["record_ids"]==["1","2"]
    assert a["earliest_retraction_date"].isoformat()=="2020-01-10"
    assert a["lag_days"]==374
    assert a["reasons"]=={"Paper Mill","Compromised Peer Review","Investigation by Journal/Publisher"}
    frac=fractional_counts(works,"countries")
    assert abs(sum(frac.values())-2.0)<1e-12
    assert abs(frac["China"]-.5)<1e-12
    assert abs(frac["United States"]-.5)<1e-12
    assert abs(frac["United Kingdom"]-1.0)<1e-12
    nodes,edges=reason_cooccurrence(works)
    assert nodes["Paper Mill"]==1
    assert edges[("Compromised Peer Review","Paper Mill")]==1
    assert edges[("Investigation by Journal/Publisher","Paper Mill")]==1
    print("ARIS4C-020 core regression tests: PASS")

if __name__=="__main__":
    main()
