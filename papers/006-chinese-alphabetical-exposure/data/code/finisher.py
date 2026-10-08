import json, os, sys, time, runpy, urllib.request, urllib.parse, urllib.error
t0 = time.time()
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.makedirs("lit", exist_ok=True)
UA = {"User-Agent": "aris4c006/1.0 (mailto:aris4c-006@polite.example)"}
def get(url, tries=(0, 30, 60)):
    last = None
    for d in tries:
        if d: time.sleep(d)
        if time.time() - t0 > 1200:
            raise RuntimeError("deadline")
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.load(r)
        except Exception as e:
            last = e
    raise RuntimeError("GET fail " + str(last)[:50])
def onestr(v):
    if isinstance(v, (list, tuple)):
        return v[0] if v else ""
    return v or ""
def cx(q, rows=10):
    u = ("https://api.crossref.org/works?query.bibliographic=" + urllib.parse.quote(q)
         + "&rows=%d&select=DOI,title,author,container-title,issued" % rows)
    return get(u)["message"]["items"]
def norm(items, anyk):
    out = []
    for it in items:
        t = onestr(it.get("title")).strip(); tl = t.lower()
        if anyk and not any(k in tl for k in anyk): continue
        a = it.get("author") or []
        auths = [("%s %s" % (onestr(x.get("family")), onestr(x.get("given")))).strip() for x in a[:3]]
        out.append({"doi": it.get("DOI"), "title": t,
                    "year": (it.get("issued", {}).get("date-parts") or [[None]])[0][0],
                    "authors": auths, "venue": onestr(it.get("container-title"))})
    return out
DIRS = {
 "D1_alpha_convention": (["alphabetical author order", "alphabetization authorship"], ["alphabet"]),
 "D2_position_outcomes": (["first author effect citation", "author position promotion corresponding author"], ["author"]),
 "D3_egotism": (["implicit egotism", "name-letter effect"], ["egotism", "name-letter", "name letter"]),
 "D4_chinese_names": (["Chinese name romanization pinyin", "author name disambiguation Chinese surname"],
    ["chinese name", "romanization", "pinyin", "disambiguat", "surname"]),
 "D5_name_bias": (["ethnic names resume callback discrimination", "name bias hiring"],
    ["name bias", "discriminat", "ethnic name", "resume", "résumé", "stigma"]),
}
print("=== LIT PHASE ===")
res = {}
for k, (qs, anyk) in DIRS.items():
    seen, allw = set(), []
    for q in qs:
        try:
            for w in norm(cx(q), anyk):
                key = w["doi"] or w["title"]
                if key not in seen:
                    seen.add(key); allw.append(w)
        except Exception as e:
            print("Q-FAIL", k, str(e)[:50])
        time.sleep(1)
    res[k] = allw[:12]
    print("DIR", k, len(allw))
cp = []
for q in ["alphabetical author order surname career", "alphabetical order authorship China",
          "surname order academic career"]:
    try:
        cp += [dict({"q": q}, **w) for w in norm(cx(q), ["author", "authorship"])[:5]]
    except Exception as e:
        print("CP-FAIL", str(e)[:50])
    time.sleep(1)
res["closest_prior"] = cp
n = 0
for v in res.values():
    for w in v:
        n += 1
        if n > 35:
            w["status"] = "UNVERIFIED (skip)"; continue
        if not w["doi"]:
            w["status"] = "UNVERIFIED (no DOI)"; continue
        if time.time() - t0 > 1200:
            w["status"] = "UNVERIFIED (deadline)"; continue
        ok = False
        try:
            d = get("https://api.crossref.org/works/" + urllib.parse.quote(w["doi"], safe="") + "?select=title")
            t2 = onestr(d["message"].get("title")).lower()
            w["status"] = "VERIFIED" if t2 and (w["title"].lower()[:18] in t2 or t2[:18] in w["title"].lower()) else "VERIFIED(meta-diff)"
            time.sleep(0.7); ok = True
        except Exception:
            pass
        if not ok:
            try:
                req = urllib.request.Request("https://doi.org/" + urllib.parse.quote(w["doi"]), headers=UA)
                with urllib.request.urlopen(req, timeout=25) as r:
                    w["status"] = "VERIFIED(doi.org)"
                time.sleep(0.5)
            except urllib.error.HTTPError as he:
                w["status"] = ("VERIFIED(doi.org,http%d)" % he.code) if he.code in (301, 302, 303, 307, 401, 403, 405) else ("UNVERIFIED (doi.org %d)" % he.code)
            except Exception:
                w["status"] = "UNVERIFIED (net)"
json.dump(res, open("lit/crossref_raw.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
lines = []
for k in list(DIRS) + ["closest_prior"]:
    lines.append("## " + k)
    for w in res[k]:
        lines.append("| %s | %s | %s | %s | %s | %s | %s |" % (w["year"],
            w["authors"][0] if w["authors"] else "?", w["title"][:75], w["venue"][:30], w["doi"], w["status"], w.get("q", "")))
    lines.append("")
open("lit/registry_rows.md", "w", encoding="utf-8").write("\n".join(lines))
nv = sum(1 for v in res.values() for w in v if w["status"].startswith("VERIFIED"))
print("LIT-TOTAL", sum(len(v) for v in res.values()), "VERIFIED", nv, "ELAPSED_MIN", round((time.time() - t0) / 60, 1))
for k in list(DIRS) + ["closest_prior"]:
    for w in res[k][:5]:
        print("ROW %s | %s | %s | %s | %s | %s" % (k[:2], w["year"], (w["authors"][0] if w["authors"] else "?")[:20],
                                                   w["title"][:52], (w["venue"] or "")[:20], w["status"]))
print("=== CN PHASE ===")
if os.path.exists("data/chinenames_done.txt"):
    print("CN-DONE-ALREADY")
else:
    try:
        runpy.run_path("data/chinenames_check.py", run_name="__main__")
        open("data/chinenames_done.txt", "w").write("done " + time.strftime("%F %T"))
    except Exception as e:
        print("CN-FAIL", str(e)[:120])
print("=== FEAS PHASE ===")
def feas_ok():
    for p in ("data/feasibility_v2.json", "data/feasibility.json"):
        if os.path.exists(p):
            try:
                items = json.load(open(p, encoding="utf-8")).get("items", {})
                have = 0
                for key in ("filter_discovery", "item1_coverage", "item3_estimator", "item4_parser", "item5_panel_estimate"):
                    v = items.get(key)
                    if key == "filter_discovery":
                        if v and any(x.get("ok") for x in v.values()):
                            have += 1
                    elif v:
                        have += 1
                return (have >= 4), p
            except Exception:
                return False, None
    return False, None
fd = time.time() + 4500
ok, p = feas_ok()
while not ok and time.time() < fd:
    time.sleep(120)
    ok, p = feas_ok()
if os.path.exists("data/s3_v2_log.txt"):
    t = open("data/s3_v2_log.txt", encoding="utf-8", errors="replace").read()
    print("WAITER-TAIL", t[-300:].replace("\n", " | "))
if ok:
    d = json.load(open(p, encoding="utf-8"))
    print("FEAS-FILE", p)
    for k in ("filter_discovery", "item5_panel_estimate", "item1_coverage", "item3_estimator", "item4_parser"):
        v = d.get("items", {}).get(k)
        if v is not None:
            print("FEAS", k, json.dumps(v, ensure_ascii=False)[:330])
else:
    print("FEAS-PENDING re-run data/s3_waiter.py after OpenAlex budget reset (midnight UTC)")
print("=== FINISHER-DONE ===")
