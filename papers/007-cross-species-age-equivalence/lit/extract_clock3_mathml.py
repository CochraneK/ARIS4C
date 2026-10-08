# -*- coding: utf-8 -*-
"""Print plain text of the Clock-2/Clock-3 methods region (formulas inline as text)."""
import re

t = open("lit/lu2023.xml", encoding="utf-8", errors="ignore").read()
P = re.sub(r"<[^>]+>", " ", t)
P = re.sub(r"\s+", " ", P)
i0 = P.find("loglog transformation of relative age for clock 2")
print("i0:", i0)
seg = P[i0:i0+4600]
print(seg)
