# ARIS4C-005 stage1 S3 — data feasibility probes (no analysis, no rates)
# order: RetractionWatch -> NIH RePORTER -> OpenAlex (3 test queries, per-page<=200)
# incremental save to data/_raw/s3_results.json; resumable (skips done items)
import json, time, random
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import requests

ROOT = Path(r"D:\Software\ARIS4C-local\005-hidden-burden-bad-science")
RAW = ROOT / "data" / "_raw"
RAW.mkdir(parents=True, exist_ok=True)
OUT = RAW / "s3_results.json"
R = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
UA = {"User-Agent": "aris4c005-stage1/1.0 (mailto:aris4c005@example.org)"}
MAILTO = "aris4c005@example.org"
BACKOFF = (0, 30, 60, 120, 240)
ROUNDS = 3
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

def save():
    OUT.write_text(json.dumps(R, indent=1, default=str), encoding="utf-8")

def get(url, params=None, body=None, tag=""):
    last = "init"
    for _ in range(ROUNDS):
        for i, wait in enumerate(BACKOFF):
            if wait:
                time.sleep(wait + random.uniform(0, 5))
            try:
                if body is not None:
                    r = requests.post(url, data=body,
                                      headers={**UA, "Content-Type": "application/json"},
                                      timeout=60)
                else:
                    r = requests.get(url, params=params, headers=UA, timeout=60)
                if r.status_code == 200:
                    return r
                if r.status_code in (400, 401, 403, 404):
                    return r
                last = f"HTTP{r.status_code}@try{i}"
            except Exception as e:
                last = f"{type(e).__name__}@try{i}"
    raise RuntimeError(f"{tag}: gave up ({last})")

def done(item):
    return item in R and "error" not in R[item]

# ---- item 2: RetractionWatch (API record structure + CSV probes)
if not done("rw"):
    res = {"snapshot_date": TODAY, "api": {}}
    try:
        r = get("https://api.retractionwatch.org/v1/retractions/",
                {"limit": 1}, tag="rw-api")
        j = r.json()
        data = j.get("results", j) if isinstance(j, dict) else j
        res["api"]["status"] = r.status_code
        res["api"]["top_level_type"] = type(j).__name__
        res["api"]["count_field"] = j.get("count") if isinstance(j, dict) else None
        if data:
            rec = data[0]
            res["api"]["record_keys"] = sorted(rec.keys())
            res["api"]["sample"] = {k: str(rec.get(k))[:60] for k in
                                    ["id", "retraction_date", "doi", "title"]
                                    if k in rec}
        res["api"]["link_header"] = (r.headers.get("Link") or "")[:200]
    except Exception as e:
        res["api"]["error"] = str(e)
    res["csv_probes"] = {}
    for u in ["https://retractionwatch.org/wp-content/uploads/2024-01/retractions.csv",
              "https://retractionwatch.org/wp-content/uploads/2023-05/retractions.csv",
              "https://retractionwatch.org/wp-content/uploads/2021/04/retractions.csv"]:
        try:
            p = requests.head(u, headers=UA, timeout=20, allow_redirects=True)
            res["csv_probes"][u.split("/")[-3] + "/" + u.split("/")[-1]] = p.status_code
        except Exception as e:
            res["csv_probes"][u.split("/")[-1]] = f"exc:{type(e).__name__}"
    R["rw"] = res
    save()
    print("rw:", json.dumps(res, default=str)[:300])

# ---- item 4: NIH RePORTER (legacy private search + new API key check)
if not done("nih"):
    res = {"snapshot_date": TODAY}
    body = json.dumps({"query": {"bool": {"must": [{"match": {"AgencyCode": "NIAID"}}]}},
                       "start": 0, "rows": 1})
    try:
        r = get("https://reporter.nih.gov/private/search", body=body, tag="nih-legacy")
        if r.status_code == 200:
            j = r.json()
            inner = j.get("result", {})
            res["legacy"] = {"status": 200,
                             "total": inner.get("total"),
                             "award_keys": sorted((inner.get("result") or [{}])[0].keys())}
        else:
            res["legacy"] = {"status": r.status_code}
    except Exception as e:
        res["legacy"] = {"error": str(e)}
    try:
        r = get("https://api.reporter.nih.gov/v2/search",
                {"query": "NIAID", "rows": 1}, tag="nih-new")
        res["new_api"] = {"status": r.status_code,
                          "note": "requires API key (developer.nih.gov) if 401/403"}
    except Exception as e:
        res["new_api"] = {"error": str(e)}
    R["nih"] = res
    save()
    print("nih:", json.dumps(res, default=str)[:400])

# ---- item 1: OpenAlex core denominator (2000-2025 journals), per-page=200
if not done("oa_denominator"):
    try:
        r = get("https://api.openalex.org/works",
                {"filter": "from_publication_date:2000-01-01,"
                           "to_publication_date:2025-12-31,"
                           "primary_location.source.type:journal",
                 "per-page": 200,
                 "select": "id,doi,title,publication_year,updated_date,retracted,"
                           "retraction_statement,cites,cited_by_count,"
                           "abstract_inverted_index"},
                tag="oa-denom")
        j = r.json()
        ws = j["results"]
        res = {"snapshot_date": TODAY, "endpoint": "api.openalex.org/works (core corpus)",
               "meta_count": j["meta"]["count"],
               "page_size": len(ws),
               "coverage_n200": {
                   "has_doi": sum(1 for w in ws if w.get("doi")),
                   "retracted_true": sum(1 for w in ws if w.get("retracted")),
                   "has_retraction_stmt": sum(1 for w in ws
                                              if (w.get("retraction_statement") or {}).get("statements")),
                   "has_abstract": sum(1 for w in ws if w.get("abstract_inverted_index")),
                   "cites_nonempty": sum(1 for w in ws if w.get("cites")),
               },
               "updated_date_max": max((w.get("updated_date") for w in ws if w.get("updated_date")), default=None)}
        R["oa_denominator"] = res
    except Exception as e:
        R["oa_denominator"] = {"error": str(e)}
    save()
    print("oa_denominator:", json.dumps(R["oa_denominator"], default=str)[:300])

# ---- item 3: OpenAlex retraction field structure (Module B side)
if not done("oa_retracted_fields"):
    try:
        r = get("https://api.openalex.org/works",
                {"filter": "retracted:true,from_publication_date:2000-01-01,"
                           "to_publication_date:2025-12-31",
                 "per-page": 20,
                 "select": "id,doi,title,publication_year,retracted,retraction_statement"},
                tag="oa-retr")
        ws = r.json()["results"]
        stmts = [w["retraction_statement"] for w in ws if w.get("retraction_statement")]
        res = {"snapshot_date": TODAY, "n_sample": len(ws),
               "n_with_statement": len(stmts),
               "statement_obj_keys": sorted(stmts[0].keys()) if stmts else None,
               "type_counter": dict(Counter(s.get("type") for s in stmts)),
               "source_counter": dict(Counter(s.get("source") for s in stmts))}
        if stmts and stmts[0].get("statements"):
            res["statement_item_keys"] = sorted(stmts[0]["statements"][0].keys())
            res["statement_text_len"] = len(stmts[0]["statements"][0].get("content", ""))
        R["oa_retracted_fields"] = res
    except Exception as e:
        R["oa_retracted_fields"] = {"error": str(e)}
    save()
    print("oa_retracted_fields:", json.dumps(R["oa_retracted_fields"], default=str)[:300])

# ---- item 5: OpenAlex citation context fields (Module C side)
if not done("oa_citation_fields"):
    try:
        r = get("https://api.openalex.org/works",
                {"filter": "from_publication_date:2015-01-01,"
                           "to_publication_date:2025-12-31,"
                           "cited_by_count:100:10000,"
                           "primary_location.source.type:journal",
                 "per-page": 1,
                 "select": "id,doi,title,cited_by"},
                tag="oa-cite")
        w = r.json()["results"][0]
        cb = w.get("cited_by") or []
        res = {"snapshot_date": TODAY, "probe_doi": w.get("doi"),
               "cited_by_len": len(cb),
               "cited_by_entry_keys": sorted(cb[0].keys()) if cb else None,
               "entry_has_abstract": bool(cb and cb[0].get("abstract_inverted_index")),
               "entry_has_retracted": "retracted" in (cb[0] if cb else {}),
               "entry_has_cites": "cites" in (cb[0] if cb else {})}
        R["oa_citation_fields"] = res
    except Exception as e:
        R["oa_citation_fields"] = {"error": str(e)}
    save()
    print("oa_citation_fields:", json.dumps(R["oa_citation_fields"], default=str)[:300])
print("== S3 done ==", sorted(R.keys()))
