import json, os, sys, time, math, urllib.request, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from surnames import parse5a
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.makedirs("data", exist_ok=True)
UA = {"User-Agent": "aris4c006/1.0 (mailto:aris4c-006@polite.example)"}
OUT = "data/feasibility.json"
def save(d):
    json.dump(d, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
res = {"snapshot": "2026-09-29", "items": {}}
def get(url, tries=(0, 30, 60, 120, 240, 300, 300, 300, 300, 300)):
    last = None
    for d in tries:
        if d: time.sleep(d)
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except Exception as e:
            last = e
    raise RuntimeError("GET fail %s %s" % (url, last))
def is_cjk(s):
    return bool(s) and all("\u4e00" <= c <= "\u9fff" for c in s.strip())

def main():
    # ---- item1+5: filter discovery + counts ----
    fopts = ["authorships.country_code:CN", "authorships.institutions.country_code:CN", "institutions.country_code:CN"]
    disc = {}
    for f in fopts:
        u = "https://api.openalex.org/works?filter=%s&per-page=1&select=id" % urllib.parse.quote(f)
        try:
            d = get(u)
            disc[f] = {"ok": True, "count": d["meta"]["count"]}
            print("FILTER-OK", f, d["meta"]["count"]); save({"snapshot": res["snapshot"], "items": {"filter_discovery": disc}})
        except Exception as e:
            disc[f] = {"ok": False, "err": str(e)[:80]}
            print("FILTER-FAIL", f, str(e)[:60])
    res["items"]["filter_discovery"] = disc
    fwork = next((f for f in fopts if disc.get(f, {}).get("ok")), None)
    if fwork:
        res["items"]["item5_panel_estimate"] = {"filter": fwork, "works_count": disc[fwork]["count"],
            "note": "author-yr rows ~= works x avg CN authorships/work (avg from item1 sample)"}
    save(res)

    # ---- field id discovery ----
    fids = {}
    for name in ["mathematics", "physics", "nursing", "medicine"]:
        try:
            d = get("https://api.openalex.org/fields?search=%s&per-page=3&select=id,display_name" % name)
            for f in d["results"]:
                fids.setdefault(f["display_name"].lower(), f["id"])
            print("FIELD", name, [ (f["display_name"], f["id"]) for f in d["results"] ][:3])
        except Exception as e:
            print("FIELD-FAIL", name, str(e)[:60])
        time.sleep(2)
    res["items"]["field_ids"] = fids
    save(res)
    fid = {}
    for k, v in fids.items():
        if "math" in k: fid["math"] = v
        if k == "physics": fid["physics"] = v
        if "nurs" in k: fid["nursing"] = v
        if k == "medicine": fid["medicine"] = v

    # ---- item1: 2 test queries (coverage) ----
    cov = {}
    for tag, fld in [("math", fid.get("math")), ("medicine", fid.get("medicine"))]:
        if not fld: continue
        u = ("https://api.openalex.org/works?filter=authorships.country_code:CN,type:article,primary_topic.field.id:%s,publication_year:2018-2022&per-page=200&select=id,doi,title,publication_year,authorships,primary_topic" % fld)
        try:
            d = get(u)
            ws = d["results"]
            nauth = 0; nraw = 0; ncorr = 0; ncinst = 0; cnauth = 0; cjk = 0; works_cn = 0
            for w in ws:
                ashs = w.get("authorships", [])
                has_cn = False
                for a in ashs:
                    nauth += 1
                    r = a.get("raw_author_name")
                    if r:
                        nraw += 1
                        if is_cjk(r): cjk += 1
                    if a.get("is_corresponding"): ncorr += 1
                    if any((i.get("country_code") for i in a.get("institutions", []))): ncinst += 1
                    if any(i.get("country_code") == "CN" for i in a.get("institutions", [])):
                        cnauth += 1; has_cn = True
                if has_cn: works_cn += 1
            cov[tag] = {"works": len(ws), "authorships": nauth, "raw_name_rate": round(nraw / max(nauth, 1), 3),
                        "corresponding_rate": round(ncorr / max(nauth, 1), 3),
                        "inst_cc_rate": round(ncinst / max(nauth, 1), 3),
                        "cn_authorships": cnauth, "cjk_raw_rate": round(cjk / max(nauth, 1), 3),
                        "works_with_cn": works_cn, "avg_cn_auth_per_work": round(cnauth / max(works_cn, 1), 2)}
            print("COV", tag, cov[tag]); save(res | {"items": dict(res["items"], **{("item1_cov_%s" % tag): cov[tag]})})
        except Exception as e:
            print("COV-FAIL", tag, str(e)[:80])
    res["items"]["item1_coverage"] = cov
    # item5 refine with sample avg
    if fwork and cov:
        avg = [v["avg_cn_auth_per_work"] for v in cov.values() if v]
        if avg:
            res["items"]["item5_panel_estimate"]["est_author_yr_rows"] = int(disc[fwork]["count"] * (sum(avg) / len(avg)))
    save(res)

    # ---- item3: estimator trial (4 contexts x 50) ----
    est = {}
    for tag, fld in [("math_hi", fid.get("math")), ("physics_hi", fid.get("physics")),
                     ("nursing_lo", fid.get("nursing")), ("medicine_lo", fid.get("medicine"))]:
        if not fld: continue
        u = ("https://api.openalex.org/works?filter=authorships.country_code:CN,type:article,primary_topic.field.id:%s,publication_year:2015-2023&per-page=50&select=id,title,authorships" % fld)
        try:
            d = get(u)
            valid = 0; sorted_ok = 0; sumch = 0.0; cjkonly = 0; teams = {}
            for w in d["results"]:
                names = [(a.get("raw_author_name") or (a.get("author") or {}).get("display_name") or "") for a in w.get("authorships", [])]
                if len(names) < 2: continue
                if not all(is_cjk(n) for n in names): continue
                cjkonly += 1
                keys = []
                for n in names:
                    s, p = parse5a(n)
                    if not p: keys = None; break
                    keys.append(p)
                if not keys: continue
                valid += 1
                n = len(keys)
                teams[n] = teams.get(n, 0) + 1
                from collections import Counter
                cc = Counter(keys)
                ch = math.prod(math.factorial(v) for v in cc.values()) / math.factorial(n)
                sumch += ch
                if all(keys[i] <= keys[i + 1] for i in range(len(keys) - 1)): sorted_ok += 1
            if valid:
                obs = sorted_ok / valid; exp = sumch / valid
                est[tag] = {"fetched": len(d["results"]), "cjk_only": cjkonly, "valid": valid,
                            "obs_alpha": round(obs, 4), "exp_chance": round(exp, 4),
                            "excess_alpha": round((obs - exp) / (1 - exp), 4), "teams": teams}
            else:
                est[tag] = {"fetched": len(d["results"]), "cjk_only": cjkonly, "valid": 0}
            print("EST", tag, est[tag]); save(res | {"items": dict(res["items"], **{("item3_est_%s" % tag): est[tag]})})
        except Exception as e:
            print("EST-FAIL", tag, str(e)[:80])
        time.sleep(2)
    res["items"]["item3_estimator"] = est
    save(res)

    # ---- item4: parser trial on first 100 CJK raw names ----
    u = "https://api.openalex.org/works?filter=authorships.country_code:CN,type:article,primary_topic.field.id:%s,publication_year:2018-2022&per-page=200&select=authorships" % fid.get("math")
    try:
        d = get(u)
        seen = []
        for w in d["results"]:
            for a in w.get("authorships", []):
                r = a.get("raw_author_name")
                if r and is_cjk(r) and r not in seen:
                    seen.append(r)
            if len(seen) >= 100: break
        ok = 0; fail = []
        for n in seen[:100]:
            s, p = parse5a(n)
            if p: ok += 1
            else: fail.append(n)
        res["items"]["item4_parser"] = {"sample": len(seen[:100]), "parsed": ok,
                                        "rate": round(ok / max(len(seen[:100]), 1), 3), "failures": fail[:10]}
        print("PARSER", res["items"]["item4_parser"])
    except Exception as e:
        res["items"]["item4_parser"] = {"err": str(e)[:100]}
        print("PARSER-FAIL", str(e)[:80])
    save(res)
    print("ALL-DONE")

if __name__ == "__main__":
    main()
