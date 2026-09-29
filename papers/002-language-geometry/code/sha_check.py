# sha_check.py - 段3 开工 sha256 核验：8 件 CSV vs data/raw/MANIFEST.tsv（每件 1 行输出）
import hashlib
import os

from common import BASE, RES

CSV8 = [
    "data/raw/crossling/statisticalTLI_full_densified_small.csv",
    "data/raw/crossling/statisticalTLI_full_densified_large.csv",
    "data/raw/crossling/logicalTLI_full_densified_small.csv",
    "data/raw/crossling/statisticalGBI_densified.csv",
    "data/raw/crossling/logicalGBI_densified.csv",
    "data/raw/wals/values.csv",
    "data/raw/wals/languages.csv",
    "data/raw/glottolog/languages.csv",
]


def main():
    man = {}
    with open(os.path.join(BASE, "data", "raw", "MANIFEST.tsv"), encoding="utf-8") as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) >= 3:
                man[p[0].replace("\\", "/")] = p[2]
    ok_all = True
    lines = ["sha256 check (8 CSVs vs data/raw/MANIFEST.tsv) - 002 stage3"]
    for rel in CSV8:
        h = hashlib.sha256()
        with open(os.path.join(BASE, *rel.split("/")), "rb") as fh:
            for blk in iter(lambda: fh.read(1 << 20), b""):
                h.update(blk)
        act = h.hexdigest()
        ok = man.get(rel) == act
        ok_all = ok_all and ok
        tag = "OK" if ok else "FAIL"
        lines.append("%s\t%s\tact=%s" % (tag, rel, act))
        print("%s\t%s\tact=%s" % (tag, rel, act), flush=True)
    lines.append("ALL_OK=%s" % ok_all)
    print("ALL_OK=%s" % ok_all, flush=True)
    with open(os.path.join(RES, "sha256_check_stage3.txt"), "w", encoding="utf-8") as out:
        out.write("\n".join(lines) + "\n")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
