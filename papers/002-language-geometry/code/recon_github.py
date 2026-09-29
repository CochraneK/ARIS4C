"""Stage1 recon: identify exact public sources + pin commit SHAs for TLI/GBI/WALS.
Saves JSON/README snapshots to data/raw/. Prints <=40 lines."""
import json, os, re, requests

UA = {"User-Agent": "aris4c-002-stage1-recon (research; contact: local)"}
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
os.makedirs(OUT, exist_ok=True)
G = "https://api.github.com"

def gh(path, **kw):
    r = requests.get(G + path, headers=UA, timeout=60, **kw)
    r.raise_for_status()
    return r

# 1) crossling-curated full tree (pin to main head)
main = gh("/repos/annagraff/crossling-curated/commits?per_page=1").json()[0]
print("crossling-curated main head:", main["sha"], main["commit"]["committer"]["date"])
tree = gh(f"/repos/annagraff/crossling-curated/git/trees/{main['sha']}?recursive=1").json()
paths = [t for t in tree.get("tree", []) if t["type"] == "blob"]
with open(os.path.join(OUT, "crossling_tree.json"), "w") as f:
    json.dump({"sha": main["sha"], "tree": paths}, f)
cd = [t for t in paths if t["path"].startswith("curated_data/")]
print(f"crossling blobs under curated_data/: {len(cd)}")
for t in cd:
    print(" ", t["path"], t.get("size"))
trunc = tree.get("truncated")
print("tree truncated:", trunc)
