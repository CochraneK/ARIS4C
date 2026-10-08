import re, html

raw = open("lit/lu2023.xml", encoding="utf-8", errors="replace").read()

# 1) find all <math ...>...</math> blocks
maths = re.findall(r'<math[^>]*>.*?</math>', raw, re.S)
print("math blocks found:", len(maths))

def mathml_to_text(m):
    # annotation-xml often holds LaTeX
    ann = re.findall(r'<annotation[^>]*>(.*?)</annotation>', m, re.S)
    out = []
    for a in ann:
        t = html.unescape(re.sub(r'<[^>]+>', '', a)).strip()
        if t: out.append("LATEX: " + t[:200])
    # fallback: mtext content
    txt = re.findall(r'<mtext[^>]*>(.*?)</mtext>|<mi[^>]*>(.*?)</mi>', m, re.S)
    flat = "".join(html.unescape(x[0] or x[1]) for x in txt)
    if flat.strip(): out.append("TEXT: " + flat[:200])
    return out or ["(empty)"]

# 2) find formula (5): locate display equations near "log-linear" or "Clock 3" in text flow
# get positions of formula-5 mention and log-linear in the raw xml
pos5 = [m.start() for m in re.finditer(r'formula \(5\)|Eq\. \(5\)|equation \(5\)', raw, re.I)]
posll = [m.start() for m in re.finditer(r'log[–\- ]linear age', raw, re.I)]
print("formula5 positions:", pos5[:5], "loglinear positions:", posll[:5])

# 3) for each math block, check if it's near (within 3000 chars) a log-linear/formula5 mention
targets = pos5 + posll
for i, m in enumerate(maths):
    s = m.start()
    near = [t for t in targets if abs(t - s) < 4000]
    tag = " <<NEAR-FORMULA5>>" if near else ""
    print(f"--- math[{i}] at {s}{tag}")
    for line in mathml_to_text(m):
        print("   ", line)

# 4) extract Methods paragraph text around formula (5) mentions (tag-stripped)
for p in pos5[:3]:
    seg = raw[max(0, p - 2500):p + 800]
    seg = re.sub(r'<math.*?</math>', ' [MATH] ', seg, flags=re.S)
    seg = re.sub(r'<[^>]+>', ' ', seg)
    seg = html.unescape(re.sub(r'\s+', ' ', seg)).strip()
    print("=== METHODS CONTEXT around formula(5) ===")
    print(seg[:1200])
    print()
