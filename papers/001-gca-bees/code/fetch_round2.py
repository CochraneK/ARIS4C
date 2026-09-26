import json, urllib.request, urllib.parse

BASE = "https://api.openalex.org/works"
SEL = ("id,doi,title,publication_year,authorships,primary_location,"
       "open_access,best_oa_location,abstract_inverted_index")

def fetch(params):
    url = BASE + "?" + params + "&select=" + SEL
    req = urllib.request.Request(url, headers={"User-Agent": "aris4c-stage1 (research)"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.loads(r.read().decode())

def uninv(inv):
    if not inv:
        return ""
    pos = {}
    for w, idxs in inv.items():
        for i in idxs:
            pos[i] = w
    return " ".join(pos[i] for i in sorted(pos))

QS = [
    ("t_optout", 'filter=title.search:"opt-out"'),
    ("t_optout2", 'filter=title.search:"opt out"'),
    ("t_rev", 'filter=title.search:"reversal",title.search:"honey"'),
    ("t_disc", 'filter=title.search:"discrimination",title.search:"honey bee"'),
    ("t_pat", 'filter=title.search:"patterning",title.search:"honey"'),
    ("t_indiv", 'filter=title.search:"individual differences"'),
    ("t_conf", 'filter=title.search:"confidence",title.search:"bee"'),
    ("t_meta", 'filter=title.search:"metacognition"'),
    ("t_gca", 'filter=title.search:"general cognitive"'),
    ("a_avila", 'search="Avila d\'Avila Leal"'),
    ("a_dyer", 'search="Dyer honey bee cognitive abilities"'),
]

rows = []
if __import__("os").path.exists("results/openalex_raw.json"):
    rows = json.load(open("results/openalex_raw.json", encoding="utf-8"))
seen = set((r.get("doi") or r.get("oa_loc")) for r in rows)

for tag, params in QS:
    pp = params + "&per-page=20"
    try:
        data = fetch(pp)
    except Exception as e:
        print(tag, "FETCH_FAIL", repr(e)); continue
    ws = data.get("results", [])
    print("==", tag, "|", params[:60], "| returned:", len(ws),
          "| total:", data.get("meta", {}).get("count"))
    for w in ws:
        doi = (w.get("doi") or "").replace("https://doi.org/", "")
        key = doi or w["id"]
        if key in seen:
            continue
        seen.add(key)
        auths = w.get("authorships") or []
        fa = auths[0]["author"]["display_name"] if auths else "?"
        src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or ""
        oa = (w.get("best_oa_location") or {}).get("landing_page_url") or ""
        rows.append({"tag": tag, "doi": doi, "oa_loc": w["id"],
                     "title": w.get("title") or "", "year": w.get("publication_year"),
                     "first_author": fa, "source": src, "oa": oa,
                     "abstract": uninv(w.get("abstract_inverted_index"))})

with open("results/openalex_raw.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)

KW = ["opt-out", "opt out", "opting", "confidence", "patterning", "configur",
      "revers", "discrim", "individual", "cognit", "uncertain", "metacogn",
      "general", "decision", "proboscis", "olfactor", "visual learning"]
cand = [r for r in rows if any(k in (r["title"] or "").lower() for k in KW)]
cand.sort(key=lambda r: (r["year"] or 0))
with open("results/candidates.txt", "w", encoding="utf-8") as f:
    for r in cand:
        f.write("%s | %s | %s | %s | OA:%s | %s | %s\n" % (
            r["year"], r["first_author"][:26], r["title"][:80], r["source"][:30],
            "Y" if r["oa"] else "n", r["doi"], r["abstract"][:220]))
print("CANDIDATES", len(cand), "of", len(rows))
for r in cand:
    print(r["year"], "|", r["first_author"][:22], "|", r["title"][:68],
          "|", r["source"][:26], "|OA:" + ("Y" if r["oa"] else "n"), "|", r["doi"])
