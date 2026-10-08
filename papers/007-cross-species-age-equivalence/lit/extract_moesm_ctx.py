# -*- coding: utf-8 -*-
"""Show raw context around MOESM mentions in lu2023.xml / crofts2023.xml (small stdout)."""
import re

for f in ["lit/lu2023.xml", "lit/crofts2023.xml"]:
    t = open(f, encoding="utf-8", errors="ignore").read()
    print("==", f, "MOESM mentions:", len(re.findall(r"MOESM\d+[_A-Z]*", t)))
    shown = 0
    for m in re.finditer(r"MOESM\d+[_A-Z]*", t):
        s = max(0, m.start() - 220)
        ctx = t[s:m.end() + 80].replace("\n", " ")
        print("---")
        print(ctx)
        shown += 1
        if shown >= 8:
            break
