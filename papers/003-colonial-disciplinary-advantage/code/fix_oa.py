import json, time, math, urllib.request, urllib.error, os
UA = {"User-Agent": "aris4c-003-stage1/0.1 (local research)"}
def get(url, path=None, tries=2):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                d = r.read()
            if path:
                open(path, "wb").write(d)
            return r.status, d
        except urllib.error.HTTPError as e:
            if i == tries - 1:
                return e.code, e.read()
            time.sleep(2 + i)
        except Exception as e:
            print("EXC", type(e).__name__, str(e)[:80]); time.sleep(2 + i)
    return None, None
def cnt(s, d):
    try:
        return json.loads(d).get("meta", {}).get("count")
    except Exception:
        return None
if os.path.exists("data/raw/test_g_authorships_country_code.json"):
    d = open("data/raw/test_g_authorships_country_code.json", encoding="utf-8").read()
    print("OLD_tG_head", d[:400])
F25 = "https://openalex.org/fields/25"
for name, f in [("CC1", "authorships.countries:BR"), ("CC2", "authorships.institutions.country_code:BR"),
                ("FF1", "topics.field.id:" + F25), ("FF2", "primary_topic.field.id:" + F25)]:
    s, d = get("https://api.openalex.org/works?filter=" + f + "&per-page=1")
    print(name, s, "count", cnt(s, d)); time.sleep(0.5)
CC = "authorships.countries"; FF = "topics.field.id"
s, d = get("https://api.openalex.org/works?filter=" + CC + ":BR," + FF + ":" + F25 + ",publication_year:2020"
           "&per-page=1&select=id,publication_year,cited_by_count,authorships,fields_of_study", "data/raw/test_a_schema.json")
if s == 200:
    r = json.loads(d)["results"][0]; a0 = r["authorships"][0]; f0 = r["fields_of_study"][0]
    print("tA rkeys", sorted(r.keys())); print("tA auth0", sorted(a0.keys()), "cc?", "country_code" in a0)
    print("tA fos0", sorted(f0.keys()), "f0", sorted(f0["fields"][0].keys()), "nfos", len(r["fields_of_study"]))
else:
    print("tA FAIL", s, d[:200])
time.sleep(0.6)
def count(filt, tag):
    s, d = get("https://api.openalex.org/works?filter=" + filt + "&per-page=1", "data/raw/count_%s.json" % tag)
    c = cnt(s, d)
    print(tag, s, ("10^%.1f" % math.log10(c)) if c and c > 0 else c)
    time.sleep(0.6)
count(CC + ":BR", "c1_br_all")
count(CC + ":BR," + FF + ":" + F25, "c2_br_mat")
count(FF + ":" + F25, "c3_mat_all")
count(FF + ":" + F25 + ",from_publication_date:1990-01-01", "c4_mat_1990p")
count(CC + ":GB," + FF + ":" + F25 + ",publication_year:1900-1919", "c5_uk_mat_1900s")
for gb in ["authorships.countries", "authorships.country_code", "authorships.institutions.country_code",
           "topics.field.id", "primary_topic.field.id"]:
    s, d = get("https://api.openalex.org/works?filter=" + CC + ":BR&group_by=" + gb +
               "&group_by=publication_year&per-page=2", "data/raw/test_g_%s.json" % gb.replace(".", "_").replace(":", "_"))
    try:
        j = json.loads(d); r0 = j["results"][0]
        print("tG OK", gb, "top", sorted(j.keys()), "r0", sorted(r0.keys()),
              "nested", "groups" in r0, sorted(r0["groups"][0].keys()) if r0.get("groups") else None)
        if "groups" in r0:
            break
    except Exception:
        print("tG BAD", gb, s, d[:150])
    time.sleep(0.5)
s, d = get("https://api.openalex.org/subfields?per-page=1")
print("subfields_total", s, cnt(s, d))
time.sleep(0.5)
KWS = ["tropical", "agricultural", "geology", "mining", "pharmaceutical", "pharmacology", "botany",
       "forestry", "zoology", "anthropology", "history", "economics", "ecology", "chemistry",
       "materials", "engineering", "computer", "physics", "mathematics", "environmental"]
for kw in KWS:
    s, d = get("https://api.openalex.org/subfields?search=" + kw + "&per-page=8", "data/raw/sub_%s.json" % kw)
    if s == 200:
        rs = json.loads(d).get("results", [])
        print("SUB", kw, len(rs), [(x["display_name"], x["id"].split("/")[-1]) for x in rs[:5]])
    else:
        print("SUB", kw, "FAIL", s)
    time.sleep(0.5)
print("DONE")
