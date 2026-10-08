import json, urllib.request as u, urllib.error as e
P = r"D:\Software\ARIS4C-local\005-hidden-burden-bad-science\data\_raw\s3_fix_results.json"
R = json.load(open(P, encoding="utf-8"))
def get(url, tag): s, b = -1, ""
    try:
        r = u.urlopen(u.Request(url, headers={"User-Agent": "aris4c005/1.0 (mailto:aris4c005@example.org)"}), timeout=120); s, b = r.status, r.read().decode("utf-8")
    except e.HTTPError as x: s, b = x.code, x.read().decode("utf-8", "replace")
    except Exception as x: b = repr(x)
    R["requests"].append({"tag": tag, "url": url, "status": s, "body200": b[:200]})
    try: return json.loads(b)
    except Exception: return None
d = get("https://api.openalex.org/works?filter=publication_year:2000-2025,retracted:true&per-page=20&mailto=aris4c005@example.org", "s33_retr_v2")
w2 = (d or {}).get("results") or []
if w2:
    R["s33"]["retr_sample"] = {"n": len(w2), "retraction_date": sum(1 for x in w2 if x.get("retraction_date")),
        "stmt_types": sorted({st.get("type") for x in w2 if (st := x.get("retraction_statement"))})}
else:
    d1 = get("https://api.openalex.org/works?filter=publication_year:2000-2025&per-page=1&mailto=aris4c005@example.org", "s33_fullrecord_probe"); w1 = (d1 or {}).get("results") or []
    R["s33"]["top_level_keys"] = sorted(w1[0].keys()) if w1 else []; R["s33"]["retr_keys"] = [k for k in w1[0] if "retract" in k.lower()] if w1 else []
json.dump(R, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print("REQS", [(r["tag"], r["status"]) for r in R["requests"][-2:]])
print("S33", json.dumps(R["s33"].get("retr_sample") or {k: R["s33"].get(k) for k in ("top_level_keys", "retr_keys")}, default=str)[:700])
