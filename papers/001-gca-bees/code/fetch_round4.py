import json, urllib.request, urllib.parse

UA = {"User-Agent": "aris4c-stage1 (research; contact: local)"}

def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.loads(r.read().decode())

out = []

out.append("=== X1) Crossref bib: Apis mellifera opt-out ===")
d = get("https://api.crossref.org/works?query.bibliographic="
         + urllib.parse.quote("Apis mellifera opt-out") + "&rows=12")
for it in d["message"]["items"]:
    ti = (it.get("title") or ["?"])[0][:90]
    au = (it.get("author") or [{}])
    fa = au[0].get("family", "?") if au else "?"
    yr = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
    out.append("%s | %s | %s | %s" % (yr, fa, ti, it.get("DOI")))

out.append("=== X2) Crossref bib: Avila d'Avila Leal honey bee ===")
d = get("https://api.crossref.org/works?query.bibliographic="
         + urllib.parse.quote("Avila d'Avila Leal honey bee learning") + "&rows=15")
for it in d["message"]["items"]:
    ti = (it.get("title") or ["?"])[0][:90]
    au = (it.get("author") or [{}])
    fa = au[0].get("family", "?") if au else "?"
    yr = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
    out.append("%s | %s | %s | %s" % (yr, fa, ti, it.get("DOI")))

out.append("=== X3) Crossref bib: Dyer honey bee cognitive abilities ===")
d = get("https://api.crossref.org/works?query.bibliographic="
         + urllib.parse.quote("Dyer honey bee cognitive abilities review") + "&rows=10")
for it in d["message"]["items"]:
    ti = (it.get("title") or ["?"])[0][:90]
    au = (it.get("author") or [{}])
    fa = au[0].get("family", "?") if au else "?"
    yr = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
    out.append("%s | %s | %s | %s" % (yr, fa, ti, it.get("DOI")))

out.append("=== X4) Crossref bib: honey bee negative patterning ===")
d = get("https://api.crossref.org/works?query.bibliographic="
         + urllib.parse.quote("honey bee negative patterning") + "&rows=10")
for it in d["message"]["items"]:
    ti = (it.get("title") or ["?"])[0][:90]
    au = (it.get("author") or [{}])
    fa = au[0].get("family", "?") if au else "?"
    yr = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
    out.append("%s | %s | %s | %s" % (yr, fa, ti, it.get("DOI")))

out.append("=== X5) OpenAlex authors: Avila d'Avila Leal ===")
d = get("https://api.openalex.org/authors?search="
         + urllib.parse.quote("Avila d'Avila Leal") + "&per-page=5")
ids = []
for a in d.get("results", []):
    out.append("AUTHOR %s | works %s | %s" % (a["id"], a.get("works_count"),
                                              a.get("display_name")))
    ids.append(a["id"])
if ids:
    d2 = get("https://api.openalex.org/works?filter=author.id:" + ids[0]
             + "&per-page=25&select=id,doi,title,publication_year,authorships,"
               "primary_location,open_access,best_oa_location,abstract_inverted_index")
    def uninv(inv):
        if not inv:
            return ""
        pos = {}
        for w, idxs in inv.items():
            for i in idxs:
                pos[i] = w
        return " ".join(pos[i] for i in sorted(pos))
    for w in d2.get("results", []):
        src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or ""
        oa = (w.get("best_oa_location") or {}).get("landing_page_url") or ""
        doi = (w.get("doi") or "").replace("https://doi.org/", "")
        out.append("  %s | %s | %s | %s | OA:%s | %s" % (
            w.get("publication_year"), (w.get("title") or "")[:88],
            src[:30], "Y" if oa else "n", doi, uninv(w.get("abstract_inverted_index"))[:200]))

with open("results/round4.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("ROUND4_LINES", len(out))
print("\n".join(out[:38]))
