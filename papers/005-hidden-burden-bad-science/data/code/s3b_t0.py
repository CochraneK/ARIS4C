import csv, json, os
def head(p, n=8):
    with open(p, encoding="utf-8", errors="replace") as f:
        return " || ".join(l.strip() for l in [next(f, "") for _ in range(n)])
pts = ["RESEARCH_BRIEF.md", "stage3a_summary.md", "data/rw_e1_mapping.csv", "data/manifests/rw_csv_manifest.json", "data/stage3/e1_numerators.csv"]
print("1 exist_all:", all(os.path.exists(p) for p in pts))
n = sum(1 for _ in open("data/stage3/e1_numerators.csv", encoding="utf-8")) - 1
e1 = list(csv.DictReader(open("data/stage3/e1_numerators.csv", encoding="utf-8")))
wd = [r for r in e1 if (r.get("doi") or "").strip()]
print("2 rows:", n, "with_doi:", len(wd), "buckets:", sorted({r["bucket"] for r in wd}))
print("3 data/:", os.listdir("data"))
raw = [(f, os.path.getsize("data/raw/" + f)) for f in os.listdir("data/raw")] if os.path.isdir("data/raw") else []
print("4 raw:", sorted(raw, key=lambda x: -x[1])[:6])
print("5 manifest:", json.dumps(json.load(open("data/manifests/rw_csv_manifest.json", encoding="utf-8")))[:400])
print("6 e1 head:", head("data/stage3/e1_numerators.csv", 2)[:280])
print("7 mapping head:", head("data/rw_e1_mapping.csv", 5)[:400])
print("8 stage3a head:", head("stage3a_summary.md", 10)[:520])
