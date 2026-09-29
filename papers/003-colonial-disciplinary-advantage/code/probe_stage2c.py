# probe_stage2c.py — final subject probes: mining subfield, archaeology/tropical topics, d_inst_name 3rd try
import json, os, time, urllib.request, urllib.parse as up

BASE = "https://api.openalex.org"
UA = {"User-Agent": "aris4c-003-stage2/0.1 (local research)"}
RAW = "data/raw/probes"
os.makedirs(RAW, exist_ok=True)
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
            print(tag, "200", (j or {}).get("meta", {}).get("count"))
            time.sleep(2.2)
            return j
        except urllib.error.HTTPError as e:
            if 400 <= e.code < 500:
                try:
                    open(path + ".err4xx", "w", encoding="utf-8").write(e.read().decode("utf-8", "replace")[:400])
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

def search(tag, endpoint, q, n=6):
    j = get(tag, BASE + "/" + endpoint + "?" + up.urlencode({"search": q, "per-page": n}))
    for r in (j or {}).get("results", [])[:n]:
        print(tag, ">", r.get("id"), "|", r.get("display_name"))

def cnt(tag, filt):
    j = get(tag, BASE + "/works?filter=" + up.quote(filt, safe=",:|=") + "&per-page=1")
    print(tag, "count=", (j or {}).get("meta", {}).get("count"))

print("== mining subfield via display_name filter ==")
j = get("s_mining2", BASE + "/subfields?" + up.urlencode({"filter": "display_name.search:mining", "per-page": 10}))
for r in (j or {}).get("results", [])[:10]:
    print("s_mining2 >", r.get("id"), "|", r.get("display_name"))
print("== archaeology: concept + topic ==")
search("c_archaeology", "concepts", "archaeology")
search("t_archaeology", "topics", "archaeology")
print("== tropical medicine: topic ==")
search("t_tropmed", "topics", "tropical medicine")
print("== d_inst_name 3rd try ==")
cnt("d_inst_name3", "authorships.institutions.display_name.search:university")
print("DONE")
