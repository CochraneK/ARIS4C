# Takeover (window A): sentence-level context extraction from on-disk fulltexts
# Perry opt-out group stats / Raine + Evans correlations / Finke SI docx per-bee check
import re
import zipfile

BASE = "D:/Software/ARIS4C-local/001-gca-bees/data"
RES = "D:/Software/ARIS4C-local/001-gca-bees/results"


def sentences(text):
    text = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(s.strip()) > 20]


def extract(path, patterns, outpath, maxn=50, minlen=40):
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    sents = sentences(text)
    rx = re.compile(patterns, re.I)
    hits, seen = [], set()
    for s in sents:
        if rx.search(s) and len(s) >= minlen:
            key = s[:50]
            if key not in seen:
                seen.add(key)
                hits.append(s)
        if len(hits) >= maxn:
            break
    with open(outpath, "w", encoding="utf-8") as f:
        f.write("\n".join(f"{i+1}. {h}" for i, h in enumerate(hits)))
    print(f"{outpath.split('/')[-1]}: {len(hits)} sentences")


extract(f"{BASE}/perry2013/fulltext.txt",
        r"opt.?out|safe option|difficult (trial|choice)|percentage|proportion of",
        f"{RES}/s2_perry_ctx.txt", maxn=50)
extract(f"{BASE}/raine2012/fulltext.txt",
        r"correlat|spearman|\br\s*=\s*-?0\.",
        f"{RES}/s2_raine_ctx.txt", maxn=40)
extract(f"{BASE}/evans2017/fulltext.txt",
        r"correlat|spearman|pearson|\br\s*=\s*-?0\.",
        f"{RES}/s2_evans_ctx.txt", maxn=40)

docx = f"{BASE}/finke2023/si_2_10071_2022_1741_MOESM1_ESM.docx"
try:
    z = zipfile.ZipFile(docx)
    xml = z.read("word/document.xml").decode("utf-8", errors="replace")
    txt = re.sub(r"<[^>]+>", " ", xml)
    txt = re.sub(r"\s+", " ", txt)
    heads = re.findall(r"Table S\d+[^\s]{0,80}", txt)[:20]
    with open(f"{RES}/s2_finke_si_check.txt", "w", encoding="utf-8") as f:
        f.write("docx text length: %d\n" % len(txt))
        f.write("table headers: " + " | ".join(heads) + "\n\n")
        f.write("first 1500 chars:\n" + txt[:1500] + "\n")
    print("finke si: %d chars, %d table headers" % (len(txt), len(heads)))
except Exception as e:
    print("finke si error:", e)
