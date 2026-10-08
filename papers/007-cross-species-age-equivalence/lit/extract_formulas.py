# -*- coding: utf-8 -*-
"""Find formula elements (inline-formula/MathML) in lu2023.xml; print context + MathML text."""
import re

t = open("lit/lu2023.xml", encoding="utf-8", errors="ignore").read()
print("len", len(t))
for tag in ["inline-formula", "display-formula", "<m:oMath", "alttext", "annotation-xml"]:
    print("count", tag, len(re.findall(re.escape(tag), t)))

# extract alttext attributes (MathML often carries alttext with plain formula)
alts = re.findall(r'alttext="([^"]+)"', t)
print("ALTTEXT count:", len(alts))
for a in alts[:40]:
    print("ALT:", a)
