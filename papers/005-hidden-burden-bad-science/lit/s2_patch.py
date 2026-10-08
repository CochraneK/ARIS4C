# ARIS4C-005 stage1 S2 patch: better queries for d1/d5, re-rank all by (rel, cites)
import json, re, time, random
from pathlib import Path
from datetime import date
import requests
import importlib.util

spec = importlib.util.spec_from_file_location(
    "s2", r"D:\Software\ARIS4C-local\005-hidden-burden-bad-science\lit\s2_fetch.py")
s2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module.__self__ if False else None
# load module without running main
src = open(r"D:\Software\ARIS4C-local\005-hidden-burden-bad-science\lit\s2_fetch.py",
           encoding="utf-8").read().split('if __name__ == "__main__":')[0]
exec(src, s2.__dict__)
s2.KW["d1"] = ["misconduct", "prevalence", "integrity", "fraud", "questionable"]
s2.KW["d5"] = ["waste", "cost", "career", "misconduct", "reproducib",
               "replication", "sleeping", "delay"]

RAW = s2.RAW
EXTRA = {
 "d1_misconduct_prevalence": ["questionable research practices prevalence",
    "scientific fraud prevalence research integrity"],
 "d5_bad_science_cost": ["research misconduct cost funding waste",
    "sleeping beauties scientific literature"],
}
for dkey, qs in EXTRA.items():
    for i, q in enumerate(qs, start=2):
        s2.fetch_crossref(dkey, i, q)
        print(f"fetched {dkey}_{i}: {q}")

rows, used = [], set()
print(f"== S2 rebuild {date.today()} ==")
for dkey, queries in s2.QS.items():
    cand = {}
    for i in range(2 + (2 if dkey in EXTRA else 0)):
        p = RAW / f"cr_{dkey}_{i}.json"
        if p.exists():
            for w in s2.norm_crossref(json.loads(p.read_text(encoding="utf-8"))
                                      ["message"]["items"]):
                cand[w["id"]] = w
    def keyf(w):
        return (-s2.relevance(dkey, w["title"]), -w["cited_by_count"])
    for w in sorted(cand.values(), key=keyf):
        t = w["title"].strip()
        if not t or t.lower() in used:
            continue
        used.add(t.lower())
        v = s2.verify(w["doi"], t)
        au = [a["author"]["display_name"] for a in w["authorships"][:3]] or ["(unknown)"]
        ven = (w["primary_location"]["source"]["display_name"])[:40] or "n/a"
        rows.append({"d": dkey, "citekey": s2.citekey(w, len(rows)),
                     "title": t, "year": w.get("publication_year"),
                     "authors": au, "venue": ven, "doi": w["doi"],
                     "status": v[0], "reason": v[1] or "",
                     "rel": s2.relevance(dkey, t),
                     "cites": w["cited_by_count"]})
        if len([r for r in rows if r["d"] == dkey]) >= 7:
            break
ver = sum(1 for r in rows if r["status"] == "VERIFIED")
L = ["# REGISTRY — ARIS4C-005 stage1 S2 literature",
     f"Generated {date.today()} · fresh run (no old-repo material)",
     "Source: Crossref bibliographic index (search + DOI verification; records "
     "DOI-verified by construction). OpenAlex was 429-blocked (shared-egress "
     "burst, >90 min) during the stage1 window; reserved for S3.",
     f"Total {len(rows)} · VERIFIED {ver} · UNVERIFIED {len(rows)-ver}",
     "Selection: per direction, rank by (relevance 1-3, then Crossref citation count).",
     ""]
for dkey in s2.QS:
    L.append(f"## {dkey}")
    L.append("| citekey | title | year | authors(first3) | venue | doi | status | relevance |")
    L.append("|---|---|---|---|---|---|---|---|")
    for r in [x for x in rows if x["d"] == dkey]:
        st = r["status"] + (f" ({r['reason']})" if r["reason"] else "")
        L.append(f"| {r['citekey']} | {r['title'][:90]} | {r['year']} | "
                 f"{'; '.join(r['authors'])[:60]} | {r['venue']} | {r['doi']} "
                 f"| {st} | {r['rel']} |")
    L.append("")
(s2.ROOT / "lit" / "REGISTRY.md").write_text("\n".join(L), encoding="utf-8")
print(f"total={len(rows)} verified={ver}")
for dkey in s2.QS:
    rs = [x for x in rows if x["d"] == dkey]
    print(dkey, "·", " | ".join(f"{r['title'][:45]}(r{r['rel']})" for r in rs))
