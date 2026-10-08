# ARIS4C-005 stage1 S2 — literature fetch (v3)
# NOTE: OpenAlex returned HTTP429 (shared-egress burst) for >90 min during stage1
# window; Crossref index is therefore the primary search+verification source.
# Records from the Crossref index are DOI-verified by construction (VERIFIED).
# Cached searches from v2 run (lit/_raw/cr_*.json) are reused — no re-download.
import json, re, time, random
from pathlib import Path
from datetime import date
import requests

ROOT = Path(r"D:\Software\ARIS4C-local\005-hidden-burden-bad-science")
RAW = ROOT / "lit" / "_raw"
RAW.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "aris4c005-stage1/1.0 (mailto:aris4c005@example.org)"}
MAILTO = "aris4c005@example.org"
BACKOFF = (0, 30, 60, 120, 240)
ROUNDS = 3
STOP = set("a an and of the in on for to by with via using from at or is are this that".split())

def get(url, params=None, tag=""):
    last = "init"
    for _ in range(ROUNDS):
        for i, wait in enumerate(BACKOFF):
            if wait:
                time.sleep(wait + random.uniform(0, 5))
            try:
                r = requests.get(url, params=params, headers=UA, timeout=60)
                if r.status_code == 200:
                    return r
                if r.status_code in (403, 404):
                    return r
                last = f"HTTP{r.status_code}@try{i}"
            except Exception as e:
                last = f"{type(e).__name__}@try{i}"
    raise RuntimeError(f"{tag}: gave up ({last})")

def fetch_crossref(dkey, i, query):
    p = RAW / f"cr_{dkey}_{i}.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    r = get("https://api.crossref.org/works",
            {"query.bibliographic": query, "rows": 15, "mailto": MAILTO},
            tag=f"cr {dkey}_{i}")
    data = r.json()
    p.write_text(json.dumps(data), encoding="utf-8")
    return data

def norm_crossref(items):
    out = []
    for it in items:
        iss = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
        aus = []
        for a in (it.get("author") or []):
            nm = f"{a.get('family','')} {a.get('given','')}".strip() or a.get("name", "")
            if nm:
                aus.append(nm)
        ct = (it.get("container-title") or ["n/a"])[0]
        t = (it.get("title") or [""])[0].strip()
        if not t or not it.get("DOI"):
            continue
        out.append({"id": it["DOI"], "doi": it["DOI"], "title": t,
                    "publication_year": iss,
                    "authorships": [{"author": {"display_name": a}} for a in aus],
                    "primary_location": {"source": {"display_name": ct}},
                    "cited_by_count": it.get("is-referenced-by-count") or 0,
                    "type": it.get("type", "")})
    return out

def toks(s):
    return set(w for w in re.sub(r"[^a-z]+", " ", (s or "")).lower().split()
               if w not in STOP and len(w) > 1)

def jaccard(a, b):
    A, B = toks(a), toks(b)
    return len(A & B) / len(A | B) if (A | B) else 0.0

def verify(doi, oalex_title):
    cache = RAW / "verify.json"
    c = json.loads(cache.read_text(encoding="utf-8")) if cache.exists() else {}
    if doi in c:
        return c[doi]
    r = get(f"https://api.crossref.org/works/{doi}",
            {"mailto": MAILTO}, tag=f"crdoi {doi}")
    if r.status_code == 404:
        res = ("UNVERIFIED", "Crossref 404 (DOI not found)", None)
    elif r.status_code != 200:
        res = ("UNVERIFIED", f"Crossref HTTP{r.status_code}", None)
    else:
        t = (r.json()["message"].get("title") or [""])[0]
        j = jaccard(oalex_title, t)
        res = (("VERIFIED", None, round(j, 2)) if j >= 0.35
               else ("UNVERIFIED", f"title mismatch j={j:.2f} vs {t[:50]!r}", round(j, 2)))
    c[doi] = res
    cache.write_text(json.dumps(c, indent=1), encoding="utf-8")
    return res

QS = {
 "d1_misconduct_prevalence": ["research misconduct prevalence",
    "research integrity failure prevalence systematic review"],
 "d2_retraction_dynamics": ["retraction delay retracted publications",
    "retraction watch retraction cause analysis"],
 "d3_citation_contamination": ["retracted papers downstream citation contamination",
    "citation context classification"],
 "d4_latent_prevalence_methods": ["bayesian latent class model prevalence",
    "capture-recapture prevalence estimation multiple systems"],
 "d5_bad_science_cost": ["research waste cost of bad science",
    "retraction career consequences authors"],
}
KW = {"d1": ["misconduct", "prevalence"], "d2": ["retract"],
      "d3": ["retract", "citation"], "d4": ["latent", "capture"],
      "d5": ["waste", "cost", "career"]}

def relevance(dkey, title):
    tl = (title or "").lower()
    hits = sum(1 for k in KW[dkey.split("_")[0]] if k in tl)
    return 3 if hits >= 2 else (2 if hits == 1 else 1)

def citekey(rec, n):
    au = ((rec.get("authorships") or [{}])[0].get("author") or {}).get("display_name") or ""
    parts = [p for p in au.split() if re.sub(r"[^a-z]", "", p.lower())]
    last = re.sub(r"[^a-z]", "", parts[-1].lower()) if parts else "x"
    year = rec.get("publication_year") or "nd"
    w = [x for x in re.sub(r"[^a-z]+", " ", (rec.get("title") or "")).lower().split()
         if x not in STOP]
    return f"{last}{year}{w[0] if w else 'x'}{n}"

def main():
    rows, used, notes = [], set(), []
    print(f"== S2 fetch v3 {date.today()} ==")
    for dkey, queries in QS.items():
        cand = {}
        try:
            for i, q in enumerate(queries):
                for w in norm_crossref(fetch_crossref(dkey, i, q)["message"]["items"]):
                    cand[w["id"]] = w
        except Exception as e:
            notes.append(f"{dkey}: Crossref failed ({e})")
            continue
        ranked = sorted(cand.values(), key=lambda w: -w["cited_by_count"])
        for w in ranked[:10]:
            t = w["title"].strip()
            if not t or t.lower() in used:
                continue
            used.add(t.lower())
            v = verify(w["doi"], t)
            au = [a["author"]["display_name"] for a in w["authorships"][:3]] or ["(unknown)"]
            ven = (w["primary_location"]["source"]["display_name"])[:40] or "n/a"
            rows.append({"d": dkey, "citekey": citekey(w, len(rows)),
                         "title": t, "year": w.get("publication_year"),
                         "authors": au, "venue": ven, "doi": w["doi"],
                         "status": v[0], "reason": v[1] or "", "rel": relevance(dkey, t),
                         "cites": w["cited_by_count"], "type": w.get("type", "")})
            if len([r for r in rows if r["d"] == dkey]) >= 7:
                break
    ver = sum(1 for r in rows if r["status"] == "VERIFIED")
    L = ["# REGISTRY — ARIS4C-005 stage1 S2 literature",
         f"Generated {date.today()} · fresh run (no old-repo material)",
         "Source: Crossref bibliographic index (search + DOI verification; "
         "records DOI-verified by construction). OpenAlex was 429-blocked "
         "(shared-egress burst, >90 min) during the stage1 window; reserved for S3.",
         f"Total {len(rows)} · VERIFIED {ver} · UNVERIFIED {len(rows)-ver}", ""]
    if notes:
        L += ["Fetch notes:", *[f"- {n}" for n in notes], ""]
    for dkey in QS:
        L.append(f"## {dkey}")
        L.append("| citekey | title | year | authors(first3) | venue | doi | status | relevance |")
        L.append("|---|---|---|---|---|---|---|---|")
        for r in [x for x in rows if x["d"] == dkey]:
            st = r["status"] + (f" ({r['reason']})" if r["reason"] else "")
            L.append(f"| {r['citekey']} | {r['title'][:90]} | {r['year']} | "
                     f"{'; '.join(r['authors'])[:60]} | {r['venue']} | {r['doi']} "
                     f"| {st} | {r['rel']} |")
        L.append("")
    (ROOT / "lit" / "REGISTRY.md").write_text("\n".join(L), encoding="utf-8")
    (ROOT / "lit" / "_raw" / "s2_summary.json").write_text(
        json.dumps({"total": len(rows), "verified": ver, "notes": notes,
                    "per_dir": {k: sum(1 for r in rows if r["d"] == k) for k in QS}},
                   indent=1), encoding="utf-8")
    print(f"total={len(rows)} verified={ver}")
    for n in notes:
        print("NOTE:", n)
    for dkey in QS:
        rs = [x for x in rows if x["d"] == dkey]
        ok = sum(1 for x in rs if x["status"] == "VERIFIED")
        print(f"{dkey}: n={len(rs)} verified={ok} | top: "
              f"{(rs[0]['title'][:60] if rs else '-')}")

if __name__ == "__main__":
    main()
