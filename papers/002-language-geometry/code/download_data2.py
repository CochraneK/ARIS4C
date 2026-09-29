"""Fetch remaining WALS/Glottolog CLDF files (cldf/ subdir), append MANIFEST."""
import hashlib, json, os, re, datetime
import requests

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW = os.path.join(BASE, "data", "raw")
UA = {"User-Agent": "aris4c-002-stage1 data download (research; mailto:local@example.org)"}
TODAY = datetime.date.today().isoformat()
GH = "https://api.github.com"
pins = json.load(open(os.path.join(RAW, "pins.json")))

def fetch(repo, path, dest):
    ref = pins[repo][0]
    r = requests.get(f"{GH}/repos/{repo}/contents/{path}",
                     headers={**UA, "Accept": "application/vnd.github.raw"},
                     params={"ref": ref}, timeout=300)
    r.raise_for_status()
    data = r.content
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "wb").write(data)
    url = f"https://raw.githubusercontent.com/{repo}/{ref}/{path}"
    return {"file": os.path.relpath(dest, BASE), "url": url,
            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
            "fetched": TODAY, "pin": ref}

jobs = [
    ("cldf-datasets/wals", "cldf/languages.csv", os.path.join(RAW, "wals", "languages.csv")),
    ("cldf-datasets/wals", "cldf/parameters.csv", os.path.join(RAW, "wals", "parameters.csv")),
    ("cldf-datasets/wals", "cldf/values.csv", os.path.join(RAW, "wals", "values.csv")),
    ("cldf-datasets/wals", "cldf/codes.csv", os.path.join(RAW, "wals", "codes.csv")),
    ("cldf-datasets/wals", "cldf/StructureDataset-metadata.json",
     os.path.join(RAW, "wals", "StructureDataset-metadata.json")),
    ("glottolog/glottolog-cldf", "cldf/languages.csv", os.path.join(RAW, "glottolog", "languages.csv")),
    ("glottolog/glottolog-cldf", "cldf/classification.nex", os.path.join(RAW, "glottolog", "classification.nex")),
    ("glottolog/glottolog-cldf", "cldf/cldf-metadata.json", os.path.join(RAW, "glottolog", "cldf-metadata.json")),
]
mf = os.path.join(RAW, "MANIFEST.tsv")
rows = open(mf).read().strip().splitlines()[1:]
have = {l.split("\t")[0] for l in rows}
for repo, path, dest in jobs:
    rel = os.path.relpath(dest, BASE)
    if rel in have:
        print("have", rel); continue
    try:
        m = fetch(repo, path, dest)
        rows.append("\t".join(str(m[k]) for k in ["file", "url", "sha256", "bytes", "fetched", "pin"]))
        print("ok", rel, m["bytes"])
    except Exception as e:
        print("FAIL", rel, e)
open(mf, "w").write("\n".join(rows) + "\n")
print("manifest rows:", len(rows))
