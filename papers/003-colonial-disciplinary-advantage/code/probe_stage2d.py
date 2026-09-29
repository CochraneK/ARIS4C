# probe_stage2d.py — verify concepts.id is filterable on works (archaeology + botany)
import json, os, time, urllib.request, urllib.parse as up

BASE = "https://api.openalex.org"
UA = {"User-Agent": "aris4c-003-stage2/0.1 (local research)"}
RAW = "data/raw/probes"
BACKOFF = [3, 6, 12, 24]

def get(tag, url, max_attempts=4):
    path = os.path.join(RAW, tag + ".json")
    if os.path.exists(path) and os.path.getsize(path) > 2:
        j = json.load(open(path, encoding="utf-8"))
        print(tag, "CACHED")
        return j
    for i in range(max_attempts):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                body = r.read()
            open(path, "wb").write(body)
            j = json.loads(body)
            print(tag, "200 count=", (j or {}).get("meta", {}).get("count"))
            time.sleep(2.2)
            return j
        except urllib.error.HTTPError as e:
            if 400 <= e.code < 500:
                try:
                    open(path + ".err4xx", "w", encoding="utf-8").write(e.read().decode("utf-8", "replace")[:300])
                except Exception:
                    pass
                print(tag, "HTTP%d" % e.code)
                return None
            print(tag, "attempt%d HTTP%d" % (i + 1, e.code))
            time.sleep(BACKOFF[min(i, 3)])
        except Exception as e:
            print(tag, "attempt%d %s" % (i + 1), type(e).__name__)
            time.sleep(BACKOFF[min(i, 3)])
    print(tag, "FAILED")
    return None

get("v_concept_arch", BASE + "/works?filter=" + up.quote("authorships.countries:BR,concepts.id:https://openalex.org/C166957645", safe=",:|=") + "&per-page=1")
get("v_concept_botany", BASE + "/works?filter=" + up.quote("authorships.countries:BR,concepts.id:https://openalex.org/C59822182", safe=",:|=") + "&per-page=1")
print("DONE")
