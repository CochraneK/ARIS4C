import json, os, time, urllib.request, urllib.parse

os.makedirs("lit", exist_ok=True)
UA = {"User-Agent": "aris4c006/1.0 (mailto:aris4c@local)"}

def get(url):
    last = None
    for d in (0, 30, 60, 120, 240):
        if d:
            time.sleep(d)
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            last = e
    raise RuntimeError("GET fail " + url + " " + str(last))

def search(q, per=8, sel="id,doi,title,publication_year,authorships,primary_location", extra=""):
    u = ("https://api.openalex.org/works?search=" + urllib.parse.quote(q)
         + "&per-page=%d&filter=publication_year:1990-2026%s&select=%s" % (per, extra, sel))
    d = get(u)
    out = []
    for w in d.get("results", []):
        a = [x.get("author", {}).get("display_name", "?") for x in w.get("authorships", [])][:3]
        src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name", "")
        out.append({"id": w.get("id"), "doi": w.get("doi"), "title": (w.get("title") or "").strip(),
                    "year": w.get("publication_year"), "authors": a, "venue": src or ""})
    return out

DIRS = {
    "D1_alpha_convention": ["alphabetical author order authorship", "alphabetization author order convention",
                            "equal authorship alphabetical ordering physics mathematics"],
    "D2_position_outcomes": ["first authorship effect citations career", "author position promotion corresponding author",
                             "first author advantage academic promotion"],
    "D3_egotism": ["implicit egotism name letters", "name letter preference psychology"],
    "D4_chinese_names": ["Chinese name romanization pinyin parsing", "author disambiguation Chinese names",
                         "pinyin romanization Chinese names surname dictionary"],
    "D5_name_bias": ["name bias hiring resumes discrimination", "ethnic name labor market bias",
                     "name-based discrimination academic"],
}
raw = {}
for k, qs in DIRS.items():
    seen, allw = set(), []
    for q in qs:
        for w in search(q):
            key = w["doi"] or w["id"]
            if key not in seen:
                seen.add(key)
                allw.append(w)
        time.sleep(1)
    raw[k] = allw[:12]
    print(k, len(allw))

SEL = "id,doi,title,publication_year,authorships,primary_location,abstract_inverted_index"
CPQ = ["alphabetical author order surname career outcomes", "alphabetization author order bias surname",
       "Chinese surname pinyin alphabetical authorship", "surname order academic career China",
       "alphabetical order author position career"]
cp = []
for q in CPQ:
    u = ("https://api.openalex.org/works?search=" + urllib.parse.quote(q)
         + "&per-page=5&filter=publication_year:2005-2026&select=" + SEL)
    for w in get(u).get("results", []):
        inv = w.get("abstract_inverted_index") or {}
        words = [wrd for wrd, _ in sorted(inv.items(), key=lambda kv: min(kv[1]))]
        src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name", "")
        cp.append({"q": q, "id": w.get("id"), "doi": w.get("doi"), "title": w.get("title"),
                   "year": w.get("publication_year"), "venue": src or "", "snip": " ".join(words[:50])})
    time.sleep(1)
    print("cp", q, len(cp))

json.dump({"dirs": raw, "closest": cp}, open("lit/search_raw.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
lines = []
for k in DIRS:
    lines.append("## " + k)
    for w in raw[k]:
        lines.append("%s | %s | %s | %s | %s" % (w["year"], (w["authors"][0] if w["authors"] else "?"),
                                                 w["title"][:80], w["venue"], w["doi"]))
    lines.append("")
open("lit/candidates.md", "w", encoding="utf-8").write("\n".join(lines))
print("OK total", sum(len(v) for v in raw.values()), "cp", len(cp))
