import json, os, csv
ROOT = r"D:\Software\ARIS4C-local\006-chinese-alphabetical-exposure"
D = json.load(open(os.path.join(ROOT, "data/s2_pilot_works.json"), encoding="utf-8"))
print("D keys:", list(D.keys()))
print("fields keys:", list(D["fields"].keys()))
for k, v in D["fields"].items():
    print("field", k, "meta_count", v.get("meta_count"), "n_results", len(v.get("results", [])))
w = D["fields"]["math"]["results"][0]
print("work keys:", list(w.keys()))
print("work year:", w.get("publication_year"))
print("pl:", json.dumps(w.get("primary_location"), ensure_ascii=False)[:150])
a0 = w["authorships"][0]
print("auth0 keys:", list(a0.keys()))
print("auth0 raw:", a0.get("raw_author_name"), "| disp:", (a0.get("author") or {}).get("display_name"))
names = [(a.get("raw_author_name") or (a.get("author") or {}).get("display_name")) for a in w["authorships"]]
print("names[:5]:", names[:5])
with open(os.path.join(ROOT, "data/chinenames_pkg/familyname.csv"), encoding="utf-8") as f:
    rd = csv.DictReader(f)
    print("fam header:", rd.fieldnames)
    r1 = next(rd)
    print("fam row1:", r1)
with open(os.path.join(ROOT, "data/chinenames_pkg/givenname.csv"), encoding="utf-8") as f:
    rd = csv.reader(f)
    print("giv header:", next(rd))
    for i, row in enumerate(rd):
        if i < 3: print("giv row:", row)
        else: break
