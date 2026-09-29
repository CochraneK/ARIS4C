import json, time, urllib.request, urllib.error
UA = {"User-Agent": "aris4c-003-stage1/0.1 (local research)"}
def tryurl(tag, url, save=None):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
            d = r.read()
        print(tag, r.status, len(d))
        if save:
            open(save, "wb").write(d)
        return d
    except urllib.error.HTTPError as e:
        print(tag, e.code, e.read()[:300])
    except Exception as e:
        print(tag, "EXC", type(e).__name__, str(e)[:150])
    time.sleep(1.5)
f1 = json.load(open("data/raw/fields1.json", encoding="utf-8"))
print("fields1_meta:", f1.get("meta"))
tryurl("A_rawcolon", "https://api.openalex.org/works?filter=authorships.country_code:BR&per-page=1")
tryurl("B_pctcolon", "https://api.openalex.org/works?filter=authorships.country_code%3ABR&per-page=1")
tryurl("F_page2", "https://api.openalex.org/fields?per-page=200&page=2")
tryurl("F_cursor", "https://api.openalex.org/fields?per-page=200&cursor=*%3A%3A")
tryurl("q1", "https://api.openalex.org/works?search=colonial+legacy+science&sort=cited_by_count%3Adesc&per-page=15", "lit/raw/q1.json")
tryurl("T_groupby", "https://api.openalex.org/works?filter=fields_of_study.fields.id:https://openalex.org/fields/25&group_by=authorships.country_code&group_by=publication_year&per-page=2", "data/raw/test_g_groupby.json")
print("DONE")
