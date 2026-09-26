import json, os, urllib.request, urllib.parse

BASE = "https://api.openalex.org/works"
SEL = ("id,doi,title,publication_year,authorships,primary_location,"
       "open_access,best_oa_location,abstract_inverted_index")

def q(params):
    return urllib.parse.quote(params, safe=':,"=()')

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
    ("a_avila", "search=" + q("Avila d'Avila Leal") + "&per-page=25"),
    ("t_optout2", "filter=" + q('title.search:"opt out"') + ",title.search:bee&per-page=20"),
    ("t_gca", "filter=" + q('title.search:"general cognitive ability"') + "&per-page=20"),
    ("s_uncert", "search=" + q("honey bee uncertainty decision") + "&per-page=20"),
    ("s_dyerview", "search=" + q("Dyer cognitive abilities of bees") + "&per-page=15"),
    ("s_oxman", "search=" + q("Oxman bees confidence recruitment") + "&per-page=10"),
    ("t_conf2", "filter=" + q('title.search:"confidence"') + ",title.search:honey&per-page=20"),
    ("s_diff", "search=" + q("honey bee opt-out difficulty") + "&per-page=20"),
]

rows = json.load(open("results/openalex_raw.json", encoding="utf-8"))
seen = set((r.get("doi") or r.get("oa_loc")) for r in rows)
added = 0

for tag, params in QS:
    try:
        data = fetch(params)
    except Exception as e:
        print(tag, "FETCH_FAIL", repr(e)); continue
    ws = data.get("results", [])
    print("==", tag, "|", params[:70], "| returned:", len(ws),
          "| total:", data.get("meta", {}).get("count"))
    for w in ws:
        doi = (w.get("doi") or "").replace("https://doi.org/", "")
        key = doi or w["id"]
        if key in seen:
            continue
        seen.add(key); added += 1
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
print("ADDED", added, "| TOTAL", len(rows))

BEE = ("bee", "honey", "apis", "bombus")
KW = ("opt", "confiden", "patterning", "configur", "revers", "discrim",
      "individual", "cognit", "uncertain", "metacogn", "decision", "learning",
      "memory", "forag", "recruit")
out = []
for r in sorted(rows, key=lambda r: (r["year"] or 0)):
    t = (r["title"] or "").lower()
    a = (r["first_author"] or "").lower()
    if any(b in t or b in a for b in BEE) and any(k in t for k in KW):
        out.append(r)
with open("results/bees_cand.txt", "w", encoding="utf-8") as f:
    for r in out:
        f.write("%s | %s | %s | %s | OA:%s | %s\n%s\n\n" % (
            r["year"], r["first_author"], r["title"], r["source"],
            "Y" if r["oa"] else "n", r["doi"], r["abstract"][:400]))
print("BEE_CAND", len(out))
for r in out:
    print(r["year"], "|", r["first_author"][:24], "|", r["title"][:70],
          "|OA:" + ("Y" if r["oa"] else "n"), "|", r["doi"] or r["oa_loc"][-14:])
