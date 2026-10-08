# S2 fetch: OpenAlex searches for 5 directions -> lit/openalex_raw.json
import json, time, urllib.request, urllib.parse, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
os.makedirs(os.path.join(ROOT, "lit"), exist_ok=True)

def get(url, tries=(0, 30, 60, 120, 240)):
    for i, d in enumerate(tries):
        if d:
            time.sleep(d)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "aris007-stage1 (mailto:aris@example.org)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, r.read().decode("utf-8", "replace")
        except Exception as e:
            print("ERR", i, type(e).__name__, str(e)[:120], file=sys.stderr)
    return None, None

QUERIES = {
    "d1_life_history": "pace-of-life maximum lifespan allometric scaling life history theory",
    "d2_event_scale": "Translating Time age mapping life history events across species",
    "d3_pan_mam_clocks": "pan-mammalian DNA methylation clock epigenetic aging across species",
    "d4_survival_equivalence": "actuarial age equivalence survival curve alignment species aging",
    "d5_universal_clock": "universal scaling aging log-linear gestation sexual maturation clock 1.3",
}

out = {}
for k, q in QUERIES.items():
    u = "https://api.openalex.org/works?search=" + urllib.parse.quote(q) + "&per-page=10&sort=relevance_score:desc&select=id,doi,title,publication_year,authorships,primary_location,author_count"
    st, body = get(u)
    if st == 200:
        works = json.loads(body).get("results", [])
        slim = []
        for w in works:
            slim.append({
                "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
                "title": w.get("title"),
                "year": w.get("publication_year"),
                "first3": [a["author"]["display_name"] for a in (w.get("authorships") or [])[:3]],
                "venue": ((w.get("primary_location") or {}).get("source") or {}).get("display_name"),
            })
        out[k] = slim
        print("OK", k, len(slim))
    else:
        out[k] = []
        print("FAIL", k, st)
    sys.stdout.flush()

json.dump(out, open(os.path.join(BASE, "openalex_raw.json"), "w"), ensure_ascii=False, indent=1)
print("saved openalex_raw.json")
