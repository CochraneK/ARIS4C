# -*- coding: utf-8 -*-
"""Stage2: download lu2023 supplementary data (MOESM1-4) from Springer MediaObjects.
Saves under data/suppl/. Prints HTTP status + size per file, nothing else.
"""
import os, sys, urllib.request

BASE = ("https://static-content.springer.com/esm/"
        "art%3A10.1038%2Fs43587-023-00462-6/MediaObjects/")
PREFIX = "43587_2023_462_MOESM{n}_ESM"
outdir = "data/suppl"
os.makedirs(outdir, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (research snapshot; contact via ARIS4C)"}

for n in [1, 2, 3, 4]:
    for ext in ["xlsx", "csv", "zip"]:
        url = BASE + PREFIX.format(n=n) + "." + ext
        dest = os.path.join(outdir, "43587_2023_462_MOESM%d_ESM.%s" % (n, ext))
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            print("cached", dest, os.path.getsize(dest))
            continue
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            with open(dest, "wb") as f:
                f.write(data)
            print("OK", url, len(data))
            break
        except Exception as e:
            print("FAIL", url, repr(e)[:120])
            if os.path.exists(dest):
                os.remove(dest)
