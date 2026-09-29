import json, os, time, math, urllib.request, urllib.parse as up
UA = {"User-Agent": "aris4c-003-stage1/0.1 (local research)"}
os.makedirs("lit/raw", exist_ok=True); os.makedirs("data/raw", exist_ok=True)
def get(url, path, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                d = r.read()
            open(path, "wb").write(d)
            return json.loads(d)
        except Exception as e:
            print("ERR", path, type(e).__name__, str(e)[:100]); time.sleep(2 + i)
    return None
def works(q): return "https://api.openalex.org/works?" + up.urlencode(q)
Q = [("q1","colonial legacy science",15),("q2","geography of science center periphery empire",15),
("q3","revealed comparative advantage",15),("q4","international co-authorship network bibliometrics",15),
("q5","field weighted citation impact indicator",12),("q6","colonialism dataset colonial duration independence",15),
("q7","settler colonies European empires historical data",15),("q8","scientific specialization field structure countries",15),
("q9","university ranking QS THE ARWU bibliometrics",15),("q10","academic reputation ranking methodology",12)]
for n, s, per in Q:
    j = get(works({"search": s, "sort": "cited_by_count:desc", "per-page": str(per)}), f"lit/raw/{n}.json")
    print(n, len(j.get("results", [])) if j else -1, (j or {}).get("meta", {}).get("count")); time.sleep(0.35)
f1 = get("https://api.openalex.org/fields?per-page=200", "data/raw/fields1.json")
f2 = get("https://api.openalex.org/fields?per-page=200&cursor=*%3A%3A", "data/raw/fields2.json")
FL = (f1 or {}).get("results", []) + (f2 or {}).get("results", [])
json.dump(FL, open("data/raw/fields.json", "w", encoding="utf-8"))
mats = [f for f in FL if "material" in f["display_name"].lower()]
print("fields_total", len(FL), "mats", [(m["id"], m["display_name"]) for m in mats][:8]); time.sleep(0.35)
mat = next((m for m in FL if m["display_name"].lower() == "materials"), mats[0] if mats else None)
MID = mat["id"] if mat else None
print("MID", MID)
def count(filt, tag):
    j = get("https://api.openalex.org/works?filter=" + up.quote(filt, safe=",:") + "&per-page=1", f"data/raw/count_{tag}.json")
    c = (j or {}).get("meta", {}).get("count", 0)
    print(tag, ("10^%.1f" % math.log10(c)) if c else 0); time.sleep(0.35)
count("authorships.country_code:BR", "c1_br_all")
count(f"authorships.country_code:BR,fields_of_study.fields.id:{MID}", "c2_br_mat")
count(f"fields_of_study.fields.id:{MID}", "c3_mat_all")
count(f"fields_of_study.fields.id:{MID},from_publication_date:1990-01-01", "c4_mat_1990p")
count(f"authorships.country_code:GB,fields_of_study.fields.id:{MID},publication_year:1900-1919", "c5_uk_mat_1900s")
u = works({"filter": "authorships.country_code:BR,publication_year:2020", "per-page": 1,
           "select": "id,publication_year,cited_by_count,authorships,fields_of_study"})
j = get(u, "data/raw/test_a_schema.json")
if j:
    r = j["results"][0]; a0 = r["authorships"][0]; f0 = r["fields_of_study"][0]
    print("tA rkeys", sorted(r.keys()))
    print("tA auth0", sorted(a0.keys()), "country_code?", "country_code" in a0)
    print("tA fos0", sorted(f0.keys()), "field0keys", sorted(f0["fields"][0].keys()))
u2 = "https://api.openalex.org/works?filter=" + up.quote(f"fields_of_study.fields.id:{MID}", safe=",:") \
     + "&group_by=authorships.country_code&group_by=publication_year&per-page=2"
j2 = get(u2, "data/raw/test_g_groupby.json")
if j2:
    r0 = j2["results"][0]
    print("tG r0keys", sorted(r0.keys()), "nested?", "groups" in r0,
          "groups0keys", sorted(r0["groups"][0].keys()) if r0.get("groups") else None)
print("DONE")
