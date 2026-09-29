# probe_stage2b.py — subfield IDs for confirmatory set + filter-path verification + d_inst_name retry
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

def sub(tag, q):
    j = get(tag, BASE + "/subfields?" + up.urlencode({"search": q, "per-page": 8}))
    for r in (j or {}).get("results", [])[:4]:
        print(tag, ">", r.get("id"), "|", r.get("display_name"))

def cnt(tag, filt):
    j = get(tag, BASE + "/works?filter=" + up.quote(filt, safe=",:|=") + "&per-page=1")
    print(tag, "count=", (j or {}).get("meta", {}).get("count"))

print("== D-layer name filter retry ==")
cnt("d_inst_name", "authorships.institutions.display_name.search:university")
print("== subfields: confirmatory names ==")
sub("s_philosophy", "philosophy")
sub("s_linguistics", "linguistics")
sub("s_political", "political science")
sub("s_law", "law")
sub("s_archaeology", "archaeology")
sub("s_mining", "mining")
print("== concept: evolutionary biology ==")
j = get("c_evolutionary", BASE + "/concepts?" + up.urlencode({"search": "evolutionary biology", "per-page": 5}))
for r in (j or {}).get("results", [])[:4]:
    print("c_evolutionary >", r.get("id"), "|", r.get("display_name"))
print("== filter-path verification (BR x anthropology subfield 3314) ==")
cnt("v_sub_anth_topics", "authorships.countries:BR,topics.subfield.id:https://openalex.org/subfields/3314")
cnt("v_sub_anth_fos", "authorships.countries:BR,fields_of_study.subfields.id:https://openalex.org/subfields/3314")
cnt("v_topic_botany", "authorships.countries:BR,topics.id:https://openalex.org/T12618")
print("DONE")
