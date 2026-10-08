# -*- coding: utf-8 -*-
"""Show structure of a few inline-formula elements (content may be image refs)."""
import re

t = open("lit/lu2023.xml", encoding="utf-8", errors="ignore").read()
ms = list(re.finditer(r"<inline-formula.*?</inline-formula>", t, re.S))
print("formulas found:", len(ms))
for m in ms[:5]:
    print("==")
    print(m.group(0)[:400])
# find the Methods section text near 'log-linear'
txt = re.sub(r"<[^>]+>", " ", t)
txt = re.sub(r"\s+", " ", txt)
i = txt.find("Methods")
print("methods at", i)
# locate 'Universal clocks' methods subsection
for key in ["Construction of the universal", "universal clock", "age transformation",
            "log-linear", "Clock 3"]:
    idxs = [m.start() for m in re.finditer(key, txt, re.I)]
    print("key", repr(key), "n=", len(idxs), "first 3:", idxs[:3])
