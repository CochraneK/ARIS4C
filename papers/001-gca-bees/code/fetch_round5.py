import json, urllib.request, urllib.parse

UA = {"User-Agent": "aris4c-stage1 (research; contact: local)"}

def get(url):
    req = urllib.request.Request(url, headers=UA)
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

out = []

def workline(w):
    src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or ""
    oa = (w.get("best_oa_location") or {}).get("landing_page_url") or ""
    doi = (w.get("doi") or "").replace("https://doi.org/", "")
    return "%s | %s | %s | OA:%s | %s" % (
        w.get("publication_year"), (w.get("title") or "")[:85],
        src[:28], "Y" if oa else "n", doi)

out.append("=== A) authors: Avila Leal ===")
d = get("https://api.openalex.org/authors?search="
         + urllib.parse.quote("Avila Leal") + "&per-page=8")
for a in d.get("results", []):
    out.append("AUTHOR %s | n=%s | %s" % (a["id"], a.get("works_count"),
                                          a.get("display_name")))
    if a.get("works_count", 999) < 120:
        d2 = get("https://api.openalex.org/works?filter=author.id:" + a["id"]
                 + "&per-page=30&select=id,doi,title,publication_year,"
                   "primary_location,open_access,best_oa_location,"
                   "abstract_inverted_index")
        for w in d2.get("results", []):
            out.append("   " + workline(w))
            ab = uninv(w.get("abstract_inverted_index"))
            if ab and any(k in ab.lower() for k in
                          ("opt-out", "opt out", "confidence", "patterning",
                           "reversal")):
                out.append("     ABS: " + ab[:250])

out.append("=== B) works search: abstention / opt out bees ===")
for q in ["honey bee abstention", "bee \"opt out\" confidence",
          "Apis mellifera uncertainty"]:
    try:
        d = get("https://api.openalex.org/works?search="
                + urllib.parse.quote(q)
                + "&per-page=8&select=id,doi,title,publication_year,"
                  "primary_location,open_access,best_oa_location,"
                  "abstract_inverted_index")
        out.append("-- q: %s | total %s" % (q, d.get("meta", {}).get("count")))
        for w in d.get("results", []):
            t = (w.get("title") or "").lower()
            if any(b in t for b in ("bee", "honey", "apis", "insect",
                                    "butterfl", "moth", "fly", "wasp")):
                out.append("   " + workline(w))
    except Exception as e:
        out.append("-- q: %s FAIL %r" % (q, e))

with open("results/round5.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("R5_LINES", len(out))
print("\n".join(out[:37]))
