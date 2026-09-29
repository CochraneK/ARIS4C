# dump_ids.py — dump discipline IDs from stage1 fields.json + stage2 subfield/topic/concept probe raw
import json, os, glob

def show(tag, path, n=4):
    if not os.path.exists(path):
        print(tag, "MISSING")
        return
    j = json.load(open(path, encoding="utf-8"))
    res = j.get("results", []) if isinstance(j, dict) else j
    print(tag, "n=", len(res))
    for r in res[:n]:
        print("  ", r.get("id"), "|", r.get("display_name"))

print("== stage1 top-level fields ==")
fj = json.load(open("data/raw/fields.json", encoding="utf-8"))
res = fj.get("results", []) if isinstance(fj, dict) else fj
print("fields n=", len(res))
for r in res:
    print("  ", r.get("id"), "|", r.get("display_name"))
print("== stage2 subfields ==")
for p in sorted(glob.glob("data/raw/probes/s_*.json")):
    show(os.path.basename(p), p)
print("== stage2 topics ==")
for p in sorted(glob.glob("data/raw/probes/t_*.json")):
    show(os.path.basename(p), p, n=5)
print("== stage2 concepts ==")
for p in sorted(glob.glob("data/raw/probes/c_*.json")):
    show(os.path.basename(p), p)
print("DUMP DONE")
