# -*- coding: utf-8 -*-
"""Stage2: extract supplementary-materials / data URLs from lu2023 & crofts2023 XML (small stdout)."""
import re, sys

KEYS = ["moesm", "suppl", "mediaobjects", "zenodo", "bioproject", "esma",
        "s43587", "static-content", "researchgate", "github", "anage",
        "senescence", "clockfoundation", "gse"]
for f in ["lit/lu2023.xml", "lit/crofts2023.xml"]:
    t = open(f, encoding="utf-8", errors="ignore").read()
    urls = sorted(set(re.findall(r"https?://[^<>\s\"'<>]+", t)))
    print("==", f, len(urls), "urls total")
    n = 0
    for u in urls:
        lu = u.lower()
        if any(k in lu for k in KEYS):
            print(u)
            n += 1
        if n >= 38:
            print("...truncated...")
            break
