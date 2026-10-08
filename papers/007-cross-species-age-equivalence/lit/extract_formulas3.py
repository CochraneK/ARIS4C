# -*- coding: utf-8 -*-
"""Convert all inline-formulas (MathML) in lu2023.xml to text; keep those near
age-transformation keywords. Small stdout."""
import re

t = open("lit/lu2023.xml", encoding="utf-8", errors="ignore").read()

def mml2text(s):
    # strip namespaces/tags, keep mtext/mi/mn/mo content
    s = re.sub(r"<mml:mrow[^>]*>", "", s)
    s = re.sub(r"</mml:mrow>", "", s)
    s = re.sub(r"<mml:msup[^>]*>", "", s)
    s = re.sub(r"</mml:msup>", " ^ ", s)
    s = re.sub(r"<mml:msub[^>]*>", "", s)
    s = re.sub(r"</mml:msub>", " _ ", s)
    s = re.sub(r"<mml:mfrac[^>]*>", "( / ", s)
    s = re.sub(r"</mml:mfrac>", ")", s)
    s = re.sub(r"<mml:msqrt[^>]*>", "sqrt(", s)
    s = re.sub(r"</mml:msqrt>", ")", s)
    s = re.sub(r"<mml:munder[^>]*>", "", s)
    s = re.sub(r"</mml:munder>", " _ ", s)
    s = re.sub(r"<mml:mover[^>]*>", "", s)
    s = re.sub(r"</mml:mover>", " ^ ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip()

txt = re.sub(r"<[^>]+>", " ", t)
txt = re.sub(r"\s+", " ", txt)

KEYS = re.compile(r"log-?linear|relative age|clock [23]|formula \(|maxim um|maximum lifespan|gestation|sexual maturity|age transformation|log\(age|ln\(|log\(", re.I)

out = []
for m in re.finditer(r"<inline-formula[^>]*>(.*?)</inline-formula>", t, re.S):
    pos = txt.find(m.group(1)[:15])  # rough
    ftxt = mml2text(m.group(1))
    if len(ftxt) < 3:
        continue
    # context in raw xml: find surrounding text window
    s = max(0, m.start() - 500)
    e = min(len(t), m.end() + 500)
    ctx = re.sub(r"<[^>]+>", " ", t[s:e])
    ctx = re.sub(r"\s+", " ", ctx)
    if KEYS.search(ctx):
        out.append((m.start(), ftxt, ctx))

print("kept:", len(out))
for pos, f, c in out[:24]:
    print("---")
    print("F:", f[:200])
    print("C:", c[:320])
