# -*- coding: utf-8 -*-
"""Extract Methods text around 'formula' / 'log-linear' / 'Clock 3' from lu2023.xml."""
import re

t = open("lit/lu2023.xml", encoding="utf-8", errors="ignore").read()
# strip tags to get plain text
txt = re.sub(r"<[^>]+>", " ", t)
txt = re.sub(r"\s+", " ", txt)
print("plain length:", len(txt))

for pat in [r"formula \(5\)", r"formula \(4\)", r"formula \(3\)", r"formula \(2\)",
            r"formula \(1\)", r"log-linear age", r"predicted maximum",
            r"predicted.*maximum lifespan", r"multivariate regression",
            r"age transformation", r"relative age"]:
    ms = list(re.finditer(pat, txt, re.I))
    print("== pattern:", pat, "hits:", len(ms))
    for m in ms[:3]:
        s = max(0, m.start() - 250)
        print("  ...", txt[s:m.end() + 300], "...")
    print()
