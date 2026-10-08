# -*- coding: utf-8 -*-
"""bioRxiv januel2026 file list, verbose."""
import json, urllib.request

url = "https://api.biorxiv.org/details/biorxiv/2025.07.31.667772"
try:
    req = urllib.request.Request(url, headers={"User-Agent": "ARIS4C-research"})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read().decode()
    print("HTTP OK, bytes:", len(raw))
    d = json.loads(raw)
    coll = d.get("collection", [])
    print("collection size:", len(coll))
    for k in coll:
        f = k.get("files", {})
        print("ver:", k.get("version"), "date:", k.get("date"))
        print("  pdf:", f.get("pdf"), f.get("pdf_size"))
        print("  supp:", f.get("supplementary"))
except Exception as e:
    print("FAIL", repr(e)[:300])
