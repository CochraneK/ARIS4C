import json

rows = json.load(open("results/openalex_raw.json", encoding="utf-8"))
out = []

def line(r, abn=400):
    out.append("%s | %s | %s | %s | OA:%s | %s | %s" % (
        r["year"], r["first_author"], (r["title"] or "")[:95],
        (r["source"] or "")[:32], "Y" if r["oa"] else "n", r["doi"],
        (r["oa"] or "")[:80]))
    out.append("ABS: " + (r["abstract"] or "(none)")[:abn])
    out.append("-" * 100)

out.append("=== A) AVILA rows (author/title) ===")
for r in rows:
    a = (r["first_author"] or "").lower()
    t = (r["title"] or "").lower()
    if "avila" in a or "avila" in t:
        line(r)

out.append("=== B) DYER as first/any author, bee-ish ===")
for r in rows:
    t = (r["title"] or "").lower()
    a = (r["first_author"] or "").lower()
    if ("dyer" in a or "dyer" in t) and any(
            b in t for b in ("bee", "honey", "apis", "cognit", "learn", "forag")):
        line(r)

out.append("=== C) TITLE contains opt ===")
for r in rows:
    if "opt" in (r["title"] or "").lower():
        line(r)

SEL_DOIS = ["10.3758/bf03328341", "10.1016/s0003-3472(86)80157-9",
            "10.1007/bf01997235", "10.1007/s003590050360",
            "10.1037//0735-7036.114.1.86", "10.1007/s100710000068",
            "10.1006/nlme.2000.3996", "10.1023/a:1012227308783",
            "10.1101/lm.44602", "10.1073/pnas.0732090100",
            "10.3389/fnbeh.2010.00048", "10.1007/s10905-014-9465-1",
            "10.1016/j.beproc.2015.03.001", "10.1098/rspb.2016.2149",
            "10.7717/peerj.5918", "10.1007/s10071-022-01741-2",
            "10.1007/s00265-026-03744-2", "10.1007/s10071-026-02076-y",
            "10.5281/zenodo.17771502", "10.3389/fevo.2019.00177",
            "10.1038/s41598-017-00389-0", "10.1371/journal.pone.0045096",
            "10.1073/pnas.1408039111", "10.3389/fpsyg.2013.00162"]
out.append("=== D) SELECTED full abstracts ===")
for d in SEL_DOIS:
    hit = [r for r in rows if r.get("doi") == d]
    if not hit:
        out.append("MISSING: " + d)
        continue
    line(hit[0], abn=700)

with open("results/digest.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("AVILA", sum(1 for r in rows if "avila" in (r["first_author"] or "").lower()
                  or "avila" in (r["title"] or "").lower()))
print("OPT_TITLES", sum(1 for r in rows if "opt" in (r["title"] or "").lower()))
print("DIGEST_LINES", len(out))
