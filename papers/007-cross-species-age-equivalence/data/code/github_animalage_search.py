# -*- coding: utf-8 -*-
"""GitHub repo search for Animal-Age baseline (small stdout)."""
import json, urllib.request

queries = ["animal-age cross-species", "animal age equivalence",
           "cross-species age mapping life history"]
for q in queries:
    url = "https://api.github.com/search/repositories?q=%s&per_page=8" % q.replace(" ", "+")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ARIS4C-research"})
        with urllib.request.urlopen(req, timeout=40) as r:
            d = json.loads(r.read().decode())
        print("== query:", q, "total:", d.get("total_count"))
        for it in d.get("items", [])[:8]:
            print("  -", it["full_name"], "|", (it.get("description") or "")[:90])
    except Exception as e:
        print("== query:", q, "FAIL", repr(e)[:120])
