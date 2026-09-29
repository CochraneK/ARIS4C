import json, os, re, time, difflib, urllib.request, urllib.error, urllib.parse
UA = {"User-Agent": "aris4c-003-stage1/0.1 (mailto:research@example.org)"}
CAT = {"q1": 1, "q2": 1, "q3": 2, "q4": 2, "q5": 2, "q6": 3, "q7": 3, "q8": 4, "q9": 5, "q10": 5}
def abs20(w):
    inv = w.get("abstract_inverted_index")
    if not inv:
        return ""
    pos = []
    for word, idxs in inv.items():
        for i in idxs:
            pos.append((i, word))
    pos.sort()
    return " ".join(x[1] for x in pos[:20])
def norm(s):
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())
papers = {}
for q in sorted(CAT):
    p = "lit/raw/%s.json" % q
    if not os.path.exists(p):
        print("MISSING", p); continue
    for w in json.load(open(p, encoding="utf-8")).get("results", []):
        doi = (w.get("doi") or "").replace("https://doi.org/", "").lower()
        key = doi or norm(w.get("title"))[:80]
        rec = {"doi": doi, "title": w.get("title") or "", "year": w.get("publication_year"),
               "cited": w.get("cited_by_count") or 0, "cat": CAT[q], "oa": w.get("id"),
               "auth": (w.get("authorships") or [{}])[0].get("author", {}).get("display_name") or "",
               "venue": ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or "",
               "abs": abs20(w)}
        if key not in papers or rec["cited"] > papers[key]["cited"]:
            papers[key] = rec
sel = []
for c in range(1, 6):
    grp = sorted([r for r in papers.values() if r["cat"] == c], key=lambda r: -r["cited"])[:10]
    print("CAT%d unique=%d sel=%d" % (c, sum(1 for r in papers.values() if r["cat"] == c), len(grp)))
    for r in grp:
        sel.append(r)
with open("lit/extracted.tsv", "w", encoding="utf-8", newline="") as f:
    f.write("idx\tcat\ttitle\tyear\tfirst_author\tvenue\tdoi\tcited\toa_url\tabs20\n")
    for i, r in enumerate(sel, 1):
        r["idx"] = i
        f.write("%d\t%d\t%s\t%s\t%s\t%s\t%s\t%d\t%s\t%s\n" % (
            i, r["cat"], r["title"], r["year"], r["auth"], r["venue"], r["doi"], r["cited"], r["oa"], r["abs"]))
print("SEL_TOTAL", len(sel))
def cr_get(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA["User-Agent"], "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return -1, None
rows = []
for r in sel:
    doi, note, cr = r["doi"], "", None
    if doi:
        s, cr = cr_get("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe=""))
    else:
        s, cr = cr_get("https://api.crossref.org/works?query.bibliographic=" +
                       urllib.parse.quote(r["title"]) + "&rows=3"); note = "no_DOI_title_search"
    m = (cr or {}).get("message")
    if not m:
        rows.append((r["idx"], doi, s, "", "", "", "NOT_FOUND" if s == 404 else "ERR_%s" % s, note))
        print("V", r["idx"], s, note); time.sleep(0.35); continue
    ct = m.get("title", [""])[0]
    for k in ("issued", "published-online", "published-print", "published", "created"):
        if m.get(k, {}).get("date-parts", [None])[0]:
            cy = m[k]["date-parts"][0][0]; break
    else:
        cy = ""
    ca = (m.get("author") or [{}])[0].get("family") or (m.get("author") or [{}])[0].get("name", "")
    tr = difflib.SequenceMatcher(None, norm(r["title"]), norm(ct)).ratio()
    yr_ok = abs(int(cy) - int(r["year"])) <= 1 if str(cy).isdigit() and str(r["year"]).isdigit() else False
    a_ok = norm(ca)[:6] != "" and (norm(ca)[:6] in norm(r["auth"]) or norm(r["auth"]).split()[-1][:6] in norm(ca))
    if tr >= 0.8 and yr_ok and a_ok:
        v = "VERIFIED"
    elif tr >= 0.8 and yr_ok:
        v = "VERIFIED_author_mismatch"
    else:
        v = "MISMATCH"
    rows.append((r["idx"], doi, s, ct[:90], cy, ca, v, note + (" tr=%.2f" % tr if v != "VERIFIED" else "")))
    print("V", r["idx"], s, v, ("tr=%.2f cy=%s ca=%s" % (tr, cy, ca)) if v != "VERIFIED" else "")
    time.sleep(0.35)
with open("lit/verification.tsv", "w", encoding="utf-8", newline="") as f:
    f.write("idx\tdoi\thttp\tcr_title\tcr_year\tcr_author\tverdict\tnote\n")
    for row in rows:
        f.write("\t".join(str(x) for x in row) + "\n")
from collections import Counter
print("VERDICTS", Counter(x[6].split("_")[0] for x in rows))
URLS = [("owid_colonialism", "https://ourworldindata.org/colonialism"),
        ("cia_factbook", "https://www.cia.gov/the-world-factbook/"),
        ("easterly_data", "https://www.princeton.edu/~easterly/data.html"),
        ("cow_codes", "https://correlatesofwar.org/data-sets/"),
        ("cepr", "https://www.cepr.org/"),
        ("worldbank", "https://data.worldbank.org/"),
        ("qs", "https://topuniversities.com/world-university-rankings"),
        ("the", "https://www.timeshighereducation.com/world-university-rankings/"),
        ("arwu", "https://www.shanghairanking.com/")]
with open("lit/urls_check.tsv", "w", encoding="utf-8", newline="") as f:
    for tag, u in URLS:
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
            with urllib.request.urlopen(req, timeout=25) as r:
                st = r.status
        except urllib.error.HTTPError as e:
            st = e.code
        except Exception as e:
            st = "EXC_" + type(e).__name__
        f.write("%s\t%s\t%s\n" % (tag, st, u))
        print("URL", tag, st)
        time.sleep(0.4)
print("DONE")
