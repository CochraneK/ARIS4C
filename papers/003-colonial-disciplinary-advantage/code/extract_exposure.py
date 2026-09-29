# extract_exposure.py — parse COW colonial contiguity into ownership intervals + OWID cross-check profile
import csv, io, os, re, zipfile
from collections import defaultdict

EX = "data/raw/exposure"
RAW = EX + "/raw_csv"
os.makedirs(RAW, exist_ok=True)

# 1) extract all members incl. PDFs
zf = zipfile.ZipFile(os.path.join(EX, "cow_colonial_contiguity_v310.zip"))
for name in zf.namelist():
    if not name.endswith("/"):
        out = os.path.join(RAW, os.path.basename(name))
        if not os.path.exists(out):
            open(out, "wb").write(zf.read(name))
print("extracted:", os.listdir(RAW))

def pdf_text(path, maxlen=60000):
    b = open(path, "rb").read()
    # try pypdf
    try:
        from pypdf import PdfReader
        r = PdfReader(io.BytesIO(b))
        return "\n".join((p.extract_text() or "") for p in r.pages)[:maxlen]
    except Exception:
        pass
    # naive: extract text show operators
    out = []
    for m in re.finditer(rb"\((.*?)\)\s*Tj", b, re.S):
        out.append(m.group(1).decode("latin-1", "replace"))
    for m in re.finditer(rb"\[(.*?)\]\s*TJ", b, re.S):
        out.append("".join(x.decode("latin-1", "replace") for x in re.findall(rb"\((.*?)\)", m.group(1), re.S)))
    return "\n".join(out)[:maxlen]

ent = pdf_text(os.path.join(RAW, "Entities.pdf"), 80000)
open(os.path.join(EX, "entities_extracted.txt"), "w", encoding="utf-8").write(ent)
print("entities chars:", len(ent))
lines = [l.strip() for l in ent.splitlines() if l.strip()]
print("entities lines:", len(lines))
for l in lines[:50]:
    print("E>", l[:110])
codebook = pdf_text(os.path.join(RAW, "Colonial Contiguity Codebook.pdf"), 30000)
open(os.path.join(EX, "codebook_extracted.txt"), "w", encoding="utf-8").write(codebook)
print("codebook chars:", len(codebook))
for l in [l.strip() for l in codebook.splitlines() if l.strip()][:30]:
    print("CB>", l[:110])
