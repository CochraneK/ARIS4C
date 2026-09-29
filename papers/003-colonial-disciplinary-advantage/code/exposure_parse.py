# exposure_parse.py (part 1) — COW Entities.pdf -> ownership intervals -> exposure pair table
import csv, io, json, os, re
from collections import defaultdict

EX = "data/raw/exposure"
RAWC = EX + "/raw_csv"

def pdf_text(path, maxlen=1000000):
    b = open(path, "rb").read()
    try:
        from pypdf import PdfReader
        r = PdfReader(io.BytesIO(b))
        return "\n".join((p.extract_text() or "") for p in r.pages)[:maxlen]
    except Exception as e:
        print("pypdf fail:", str(e)[:80])
    out = []
    for m in re.finditer(rb"\((.*?)\)\s*Tj", b, re.S):
        out.append(m.group(1).decode("latin-1", "replace"))
    for m in re.finditer(rb"\[(.*?)\]\s*TJ", b, re.S):
        out.append("".join(x.decode("latin-1", "replace") for x in re.findall(rb"\((.*?)\)", m.group(1), re.S)))
    return "\n".join(out)[:maxlen]

ent = pdf_text(os.path.join(RAWC, "Entities.pdf"))
open(os.path.join(EX, "entities_full.txt"), "w", encoding="utf-8").write(ent)
print("entities_full chars:", len(ent))

YR = r"(?:1[7-9]\d{2}|20\d{2})"
rows, names = [], {}
for line in ent.splitlines():
    toks = line.split()
    if len(toks) < 6 or not toks[0].isdigit():
        continue
    for i in range(1, len(toks) - 2):
        if re.fullmatch(YR, toks[i]) and re.fullmatch(YR, toks[i + 1]):
            code, name = int(toks[0]), " ".join(toks[1:i])
            if code not in names:
                names[code] = name
            rows.append((code, name, int(toks[i]), int(toks[i + 1]), " ".join(toks[i + 2:])))
            break

def classify(status):
    m = re.match(r"^Became colony of (\d+)$", status)
    if m:
        return "colony", int(m.group(1))
    m = re.match(r"^Became part of (\d+)$", status)
    if m:
        return "part", int(m.group(1))
    m = re.match(r"^Occupied by (\d+)$", status)
    if m:
        return "occupied", int(m.group(1))
    return "other", None

print("parsed rows:", len(rows), "distinct entities:", len(names))
colony = defaultdict(list)   # (metropole, entity) -> [(b, e)]
occupied = defaultdict(list)
part = defaultdict(list)
status_kinds = defaultdict(int)
for code, name, b, e, status in rows:
    kind, other = classify(status)
    status_kinds[kind] += 1
    if kind == "colony":
        colony[(other, code)].append((b, e))
    elif kind == "occupied":
        occupied[(other, code)].append((b, e))
    elif kind == "part":
        part[(other, code)].append((b, e))
print("status kinds:", dict(status_kinds))
print("colony pairs:", len(colony), "occupied pairs:", len(occupied), "part pairs:", len(part))

def merge(ivs):
    ivs = sorted(ivs)
    out, cb, ce = [], None, None
    for b, e in ivs:
        if cb is None:
            cb, ce = b, e
        elif b <= ce + 1:
            ce = max(ce, e)
        else:
            out.append((cb, ce)); cb, ce = b, e
    if cb is not None:
        out.append((cb, ce))
    return out
