import json, urllib.request, urllib.parse

QUERIES = [
    ("q1_discrim", "Apis mellifera discrimination learning"),
    ("q2_reversal", "Apis mellifera reversal learning"),
    ("q3_patterning", "Apis mellifera negative patterning"),
    ("q4_optout", "Apis mellifera opt-out foraging"),
    ("q5_meta", "Apis mellifera metacognition confidence"),
]

def fetch(url):
    req = urllib.request.Request(url,
        headers={"User-Agent": "aris4c-stage1-literature-profile (research; contact: local)"})
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

seen = {}
rows = []
for tag, q in QUERIES:
    url = ("https://api.openalex.org/works?search=" + urllib.parse.quote(q)
           + "&per-page=20&select=id,doi,title,publication_year,authorships,"
             "primary_location,open_access,best_oa_location,abstract_inverted_index")
    try:
        data = fetch(url)
    except Exception as e:
        print(tag, "FETCH_FAIL", repr(e))
        continue
    ws = data.get("results", [])
    print("==", tag, "| q:", q, "| returned:", len(ws),
          "| total_count:", data.get("meta", {}).get("count"))
    shown = 0
    for w in ws:
        doi = (w.get("doi") or "").replace("https://doi.org/", "")
        key = doi or w["id"]
        if key in seen:
            continue
        seen[key] = 1
        auths = w.get("authorships") or []
        fa = auths[0]["author"]["display_name"] if auths else "?"
        src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or ""
        oa = (w.get("best_oa_location") or {}).get("landing_page_url") or ""
        rows.append({"tag": tag, "doi": doi, "oa_loc": w["id"],
                     "title": w.get("title") or "", "year": w.get("publication_year"),
                     "first_author": fa, "source": src, "oa": oa,
                     "abstract": uninv(w.get("abstract_inverted_index"))})
        if shown < 7:
            print("  ", w.get("publication_year"), fa[:24], "|",
                  (w.get("title") or "")[:72], "|", src[:30],
                  "|OA:", "Y" if oa else "n", "|", doi or w["id"][-14:])
            shown += 1

with open("results/openalex_raw.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)
print("TOTAL_UNIQUE", len(rows))
