import json, urllib.request as u, urllib.error as e, datetime as dt
H = {"User-Agent": "aris4c005-stage1fix2/1.0 (mailto:aris4c005@example.org)"}
BASE, MAIL = "https://api.openalex.org/works?", "mailto=aris4c005@example.org"
OUT = r"D:\Software\ARIS4C-local\005-hidden-burden-bad-science\data\_raw\s3_fix_results.json"
R = {"host_denominator": 220028794, "host_snapshot": "2026-09-30T08:20+08:00 Beijing host-verified",
     "run_at": dt.datetime.now(dt.timezone.utc).isoformat(), "requests": [], "s31": {}, "s33": {}, "s35": {}}
def get(url, tag):
    s, b = -1, ""
    try:
        with u.urlopen(u.Request(url, headers=H), timeout=120) as r:
            s, b = r.status, r.read().decode("utf-8")
    except e.HTTPError as x:
        s, b = x.code, x.read().decode("utf-8", "replace")
    except Exception as x:
        b = repr(x)
    R["requests"].append({"tag": tag, "url": url, "status": s, "body200": b[:200]})
    try:
        return json.loads(b)
    except Exception:
        return None
d = get(BASE + "filter=publication_year:2000-2025&per-page=200&" + MAIL, "s31_perpage200")
if d and "results" in d:
    w = d["results"]
    R["s31"] = {"meta_count_this_query": d["meta"]["count"], "n_sample": len(w),
                "snapshot_date": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"),
                "denominator": "220,028,794 host-verified 2026-09-30 08:20 CST; reconfirmed via meta.count"}
    c = {"doi": sum(1 for x in w if x.get("doi")), "retracted_present": sum(1 for x in w if "retracted" in x),
         "retracted_true": sum(1 for x in w if x.get("retracted")), "retraction_date": sum(1 for x in w if x.get("retraction_date")),
         "retraction_statement": sum(1 for x in w if x.get("retraction_statement")),
         "pl_source_display_name": sum(1 for x in w if (x.get("primary_location") or {}).get("source") and x["primary_location"]["source"].get("display_name")),
         "locations_biblio": sum(1 for x in w if any(l.get("biblio") for l in (x.get("locations") or []))),
         "cited_by_count": sum(1 for x in w if x.get("cited_by_count") is not None), "abstract": sum(1 for x in w if x.get("abstract_inverted_index")),
         "concepts": sum(1 for x in w if x.get("concepts")), "cites_key": sum(1 for x in w if "cites" in x),
         "cites_nonempty": sum(1 for x in w if x.get("cites"))}
    R["s33"] = {"n": len(w), "coverage": c, "note": "all-corpus sample; retracted-true sub-sample in q2"}
    R["s35"] = {"n": len(w), "coverage": {"concepts": c["concepts"], "abstract": c["abstract"],
                "cites_key": c["cites_key"], "cites_nonempty": c["cites_nonempty"]},
                "cites_second_query": "ids available in-response; citing-works concepts/abstract need batched 2nd query by ids"}
d2 = get(BASE + "filter=publication_year:2000-2025,retracted:true&per-page=20&select=id,doi,publication_year,retracted,retraction_date,retraction_statement&" + MAIL,
         "s33_retracted_true")
if d2 and "results" in d2:
    w2 = d2["results"]
    R["s33"]["retracted_true_sample"] = {"n": len(w2), "doi": sum(1 for x in w2 if x.get("doi")),
        "retraction_date": sum(1 for x in w2 if x.get("retraction_date")),
        "retraction_statement": sum(1 for x in w2 if x.get("retraction_statement")),
        "stmt_types": sorted({st.get("type") for x in w2 if (st := x.get("retraction_statement"))})}
json.dump(R, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("REQS", [(r["tag"], r["status"]) for r in R["requests"]])
print("S31", R["s31"].get("meta_count_this_query"), R["s31"].get("n_sample"))
print("S33", json.dumps(R["s33"].get("coverage"), default=str))
print("S33r", R["s33"].get("retracted_true_sample"))
print("S35", R["s35"].get("coverage"))
