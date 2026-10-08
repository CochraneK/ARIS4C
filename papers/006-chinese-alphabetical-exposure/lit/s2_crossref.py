import json, os, re, time, urllib.request, urllib.parse
os.makedirs("lit", exist_ok=True)
UA = {"User-Agent": "aris4c006/1.0 (mailto:aris4c-006@polite.example)"}
def get(url, tries=(0, 30, 60, 120, 240)):
    last = None
    for d in tries:
        if d: time.sleep(d)
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            last = e
    raise RuntimeError("GET fail " + url + " " + str(last))
def cx(q, rows=15):
    u = ("https://api.crossref.org/works?query.bibliographic=" + urllib.parse.quote(q)
         + "&rows=%d&select=DOI,title,author,container-title,issued,type" % rows)
    return get(u)["message"]["items"]
def norm(items, kws_any, kws_all=()):
    out = []
    for it in items:
        t = (it.get("title") or [""])[0]
        tl = t.lower()
        if kws_any and not any(k in tl for k in kws_any): continue
        if kws_all and not all(k in tl for k in kws_all): continue
        a = it.get("author") or []
        yr = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
        out.append({"doi": it.get("DOI"), "title": t, "year": yr,
                    "authors": ["%s %s" % (x.get("family", ""), x.get("given", "")).strip() for x in a[:3]],
                    "venue": (it.get("container-title") or [""])[0], "type": it.get("type")})
    return out
DIRS = {
 "D1_alpha_convention": (["alphabetical author order", "alphabetization authorship convention",
    "alphabetical ordering of authors physics"], ["alphabet", "order"], ()),
 "D2_position_outcomes": (["first author effect citation", "author position academic promotion",
    "corresponding author advantage"], ["author"], ()),
 "D3_egotism": (["implicit egotism", "name-letter effect"], ["egotism", "name-letter", "name letter"], ()),
 "D4_chinese_names": (["Chinese name romanization pinyin", "author name disambiguation Chinese",
    "pinyin romanization Chinese names"], ["chinese name", "romanization", "pinyin", "disambiguat", "surname"], ()),
 "D5_name_bias": (["resume callback ethnic names discrimination", "name bias hiring ethnic"],
    ["name"], ("bias", "discriminat", "callback", "résumé", "resume", "stigma")),
}
CP = ["alphabetical author order surname career", "alphabetization authors career outcomes",
      "alphabetical order authorship China pinyin", "surname order academic career"]
res = {}
for k, (qs, anyk, allk) in DIRS.items():
    seen, allw = set(), []
    for q in qs:
        try:
            for w in norm(cx(q), anyk, allk):
                key = w["doi"] or w["title"]
                if key not in seen:
                    seen.add(key); allw.append(w)
        except Exception as e:
            print("Q-FAIL", k, q, str(e)[:60])
        time.sleep(2)
    res[k] = allw[:12]
    print(k, len(allw))
cp = []
for q in CP:
    try:
        for w in norm(cx(q), (), ())[:6]:
            cp.append({"q": q, **w})
    except Exception as e:
        print("CP-FAIL", q, str(e)[:60])
    time.sleep(2)
res["closest_prior"] = cp
# verify DOIs via Crossref
def verify(w):
    if not w["doi"]:
        w["status"] = "UNVERIFIED (no DOI)"; return
    try:
        d = get("https://api.crossref.org/works/" + urllib.parse.quote(w["doi"], safe="") + "?select=DOI,title")
        t2 = (d["message"].get("title") or [""])[0].lower()
        w["status"] = "VERIFIED" if t2 and w["title"].lower()[:25] in t2 or t2[:25] in w["title"].lower() else "VERIFIED(meta-diff)"
        time.sleep(1)
    except Exception as e:
        w["status"] = "UNVERIFIED (%s)" % str(e)[:40]
for k, v in res.items():
    for w in v:
        verify(w)
json.dump(res, open("lit/crossref_raw.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
lines = []
for k in list(DIRS) + ["closest_prior"]:
    lines.append("## " + k)
    for w in res[k]:
        lines.append("| %s | %s | %s | %s | %s | %s | %s |" % (
            w["year"], w["authors"][0] if w["authors"] else "?", w["title"][:75],
            w["venue"][:30], w["doi"], w["status"], w.get("q", "")))
    lines.append("")
open("lit/registry_rows.md", "w", encoding="utf-8").write("\n".join(lines))
nv = sum(1 for v in res.values() for w in v if w["status"].startswith("VERIFIED"))
print("TOTAL", sum(len(v) for v in res.values()), "VERIFIED", nv)
