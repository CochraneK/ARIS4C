"""Stage1 Group C: download TLI/GBI/WALS/Glottolog from public sources,
pin commit SHAs, record SHA256 + URLs + date in data/raw/MANIFEST.tsv."""
import hashlib, io, json, os, datetime
import requests

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW = os.path.join(BASE, "data", "raw")
os.makedirs(RAW, exist_ok=True)
UA = {"User-Agent": "aris4c-002-stage1 data download (research; mailto:local@example.org)"}
TODAY = datetime.date.today().isoformat()
GH = "https://api.github.com"
GHTREE = {  # repo -> (branch, head sha known from recon)
    "annagraff/crossling-curated": ("main", "255632bc62ce05674f1af195b88efea5aef7afce"),
}

def gh_head(repo):
    r = requests.get(f"{GH}/repos/{repo}/commits?per_page=1", headers=UA, timeout=60)
    r.raise_for_status()
    c = r.json()[0]
    return c["sha"], c["commit"]["committer"]["date"]

manifest = []
def fetch(url, dest, sha_pin=None):
    """Download via api.github.com contents endpoint (raw accept),
    because the local proxy cannot reach raw.githubusercontent.com."""
    import re as _re
    m = _re.match(r"https://raw\.githubusercontent\.com/([^/]+)/([^/]+)/(.+)", url)
    repo = f"{m.group(1)}/{m.group(2)}"
    ref, path = m.group(3).split("/", 1)
    api_url = f"{GH}/repos/{repo}/contents/{path}"
    r = requests.get(api_url, headers={**UA, "Accept": "application/vnd.github.raw",
                                       "Referer": url},
                     params={"ref": ref}, timeout=300)
    r.raise_for_status()
    data = r.content
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as f:
        f.write(data)
    h = hashlib.sha256(data).hexdigest()
    manifest.append({"file": os.path.relpath(dest, BASE), "url": url,
                     "sha256": h, "bytes": len(data), "fetched": TODAY,
                     "pin": sha_pin or ""})
    return data

shas = {}
for repo, (br, known) in GHTREE.items():
    sha, dt = gh_head(repo)
    shas[repo] = (sha, dt)
    print(repo, "head:", sha[:12], dt, "(recon-known:", known[:12], ")")
for repo in ("cldf-datasets/wals", "glottolog/glottolog-cldf"):
    sha, dt = gh_head(repo)
    shas[repo] = (sha, dt)
    print(repo, "head:", sha[:12], dt)

CL = shas["annagraff/crossling-curated"][0]
WALS = shas["cldf-datasets/wals"][0]
GLO = shas["glottolog/glottolog-cldf"][0]
R = lambda repo, path: f"https://raw.githubusercontent.com/{repo}/{shas[repo][0]}/{path}"

for p in ["curated_data/TLI/statisticalTLI/full/statisticalTLI_full_densified_small.csv",
          "curated_data/TLI/statisticalTLI/full/statisticalTLI_full_densified_large.csv",
          "curated_data/TLI/logicalTLI/full/logicalTLI_full_densified_small.csv",
          "curated_data/GBI/statisticalGBI/statisticalGBI_densified.csv",
          "curated_data/GBI/logicalGBI/logicalGBI_densified.csv",
          "curated_data/TLI/statisticalTLI/cldf/StructureDataset-metadata.json",
          "curated_data/GBI/statisticalGBI/cldf/StructureDataset-metadata.json"]:
    d = os.path.join(RAW, "crossling", os.path.basename(p))
    fetch(R("annagraff/crossling-curated", p), d, CL)
for p in ["languages.csv", "parameters.csv", "codes.csv", "values.csv",
          "metadata.json", "feature_groups.csv"]:
    d = os.path.join(RAW, "wals", p)
    try:
        fetch(R("cldf-datasets/wals", p), d, WALS)
    except Exception as e:
        print("skip wals", p, e)
for p in ["classification.csv", "l25.csv", "languages.csv", "metadata.json"]:
    d = os.path.join(RAW, "glottolog", p)
    try:
        fetch(R("glottolog/glottolog-cldf", p), d, GLO)
    except Exception as e:
        print("skip glottolog", p, e)

with open(os.path.join(RAW, "MANIFEST.tsv"), "w") as f:
    f.write("\t".join(["file", "url", "sha256", "bytes", "fetched", "pin"]) + "\n")
    for m in manifest:
        f.write("\t".join(str(m[k]) for k in ["file", "url", "sha256", "bytes", "fetched", "pin"]) + "\n")
json.dump(shas, open(os.path.join(RAW, "pins.json"), "w"))
print(f"downloaded {len(manifest)} files")
for p in ["crossling/statisticalTLI_full_densified_small.csv", "wals/languages.csv",
          "glottolog/classification.csv"]:
    fp = os.path.join(RAW, p)
    if os.path.exists(fp):
        first = open(fp, encoding="utf-8", errors="replace").readline()[:200]
        print(p, "|", first.replace("\n", " "))
