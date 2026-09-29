# probe_stage2.py — S1 (P2 OR-semantics + D-layer institution filter) + S2 (subject re-probe) + S5 (window counts)
# idempotent: raw JSON persisted to data/raw/probes/{tag}.json; existing files skipped
# policy: >=2s interval, backoff [3,6,12,24], max 3 retries on 5xx; 4xx recorded, no retry
import json, os, time, urllib.request, urllib.parse as up

BASE = "https://api.openalex.org"
UA = {"User-Agent": "aris4c-003-stage2/0.1 (local research)"}
RAW = "data/raw/probes"
os.makedirs(RAW, exist_ok=True)
BACKOFF = [3, 6, 12, 24]

def get(tag, url, max_attempts=4):
    path = os.path.join(RAW, tag + ".json")
    if os.path.exists(path):
        j = json.load(open(path, encoding="utf-8"))
        print(tag, "CACHED")
        return j
    for i in range(max_attempts):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                body = r.read()
            open(path, "wb").write(body)
            j = json.loads(body)
            print(tag, "200", (j or {}).get("meta", {}).get("count"))
            time.sleep(2.0)
            return j
        except urllib.error.HTTPError as e:
            code = e.code
            try:
                errbody = e.read().decode("utf-8", "replace")[:400]
            except Exception:
                errbody = ""
            if 400 <= code < 500:
                open(path + ".err4xx", "w", encoding="utf-8").write(errbody)
                print(tag, "HTTP%d" % code, errbody[:180])
                return None
            print(tag, "attempt%d HTTP%d" % (i + 1, code))
            time.sleep(BACKOFF[min(i, 3)])
        except Exception as e:
            print(tag, "attempt%d %s %s" % (i + 1, type(e).__name__, str(e)[:80]))
            time.sleep(BACKOFF[min(i, 3)])
    print(tag, "FAILED")
    return None

def works_count(tag, filt):
    url = BASE + "/works?filter=" + up.quote(filt, safe=",:|=") + "&per-page=1"
    j = get(tag, url)
    c = (j or {}).get("meta", {}).get("count")
    print(tag, "count=", c)
    return c

def search(tag, endpoint, q, per=10):
    url = BASE + "/" + endpoint + "?" + up.urlencode({"search": q, "per-page": per})
    j = get(tag, url)
    for r in (j or {}).get("results", [])[:5]:
        p = (r.get("parent") or {})
        print(tag, ">", r.get("id"), "|", r.get("display_name"), "| parent:", p.get("id"), p.get("display_name"))
    return j

print("== S1 P2: same-key multi-value semantics ==")
works_count("p2_br", "authorships.countries:BR")
works_count("p2_us", "authorships.countries:US")
works_count("p2_br_us_comma", "authorships.countries:BR,US")
works_count("p2_br_us_pipe", "authorships.countries:BR|US")
print("== S1 D-layer: institution filter keys ==")
works_count("d_inst_cc", "institutions.country_code:BR")
works_count("d_inst_countr", "institutions.countries:BR")
works_count("d_auth_inst_cc", "authorships.institutions.country_code:BR")
works_count("d_primary_inst_cc", "primary_location.institution.country_code:BR")
works_count("d_inst_name", "authorships.institutions.display_name.search:university")
print("== S5 window: BR x fields/25 ==")
works_count("w_br_mat_all", "authorships.countries:BR,topics.field.id:https://openalex.org/fields/25")
works_count("w_br_mat_1990", "authorships.countries:BR,topics.field.id:https://openalex.org/fields/25,from_publication_date:1990-01-01")
works_count("w_br_mat_2000", "authorships.countries:BR,topics.field.id:https://openalex.org/fields/25,from_publication_date:2000-01-01")
print("== S2 subject re-probe: fields/concepts/topics ==")
for tag, q in [("f_philosophy", "philosophy"), ("f_linguistics", "linguistics"),
               ("f_political", "political science"), ("f_law", "law"),
               ("f_archaeology", "archaeology"), ("f_evolutionary", "evolutionary biology")]:
    search(tag, "fields", q)
for name in ["botany", "mining", "tropical"]:
    search("c_" + name, "concepts", name)
    search("t_" + name, "topics", name)
print("DONE")
