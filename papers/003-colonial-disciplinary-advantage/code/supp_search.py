# -*- coding: utf-8 -*-
# stage1 接管补检（编排器确定性执行，2026-09-29）
# 目的：① 用 title.search 精准查询补 5 类检索方向（executor 原 search= 全文查询被高引噪声污染）
#       ② 新条目逐条 Crossref 核实（存在性+标题对齐）
#       ③ 补 2 个 API 语义探针（单维 group_by、同键多值 OR 语义）
# 纪律：不物化 outcome 矩阵；只记 schema/count/候选清单；输出写盘，对话只报关键数字
import json, time, csv, io, os, difflib, urllib.request, urllib.parse as up, urllib.error

UA = {"User-Agent": "aris4c-003-stage1-supp/0.1 (local research)"}
MAILTO = "aris4c-local-research@example.com"

def get(url, tries=5, timeout=45, backoff=(3, 6, 12, 24)):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.status, json.loads(r.read())
        except urllib.error.HTTPError as e:
            if i == tries - 1:
                return e.code, None
            time.sleep(backoff[min(i, len(backoff) - 1)])
        except Exception:
            time.sleep(backoff[min(i, len(backoff) - 1)])
    return None, None

# ---- 0) 已有 DOI 去重集 ----
have_doi = set()
try:
    with open("lit/extracted.tsv", encoding="utf-8") as f:
        for row in list(csv.DictReader(f, delimiter="\t"))[1:]:
            d = (row.get("doi") or "").strip()
            if d:
                have_doi.add(d.lower())
except Exception as e:
    print("HAVE_LOAD_ERR", str(e)[:80])

# ---- 1) 精准 title.search 查询（14 条，对应冻结 prompt 5 类方向）----
Q = [
    ("s01", 1, "geography of science"),
    ("s02", 1, "center-periphery"),
    ("s03", 1, "colonial legacy science"),
    ("s04", 2, "revealed comparative advantage"),
    ("s05", 2, "weighted citation impact"),
    ("s06", 2, "international co-authorship"),
    ("s07", 2, "co-authorship network"),
    ("s08", 3, "colonial origins"),
    ("s09", 3, "settler colonialism"),
    ("s10", 3, "colonization development"),
    ("s11", 4, "scientific specialization"),
    ("s12", 4, "knowledge production"),
    ("s13", 5, "academic rankings"),
    ("s14", 5, "university rankings"),
]

new_rows, ver_rows = [], []
idx = 0
for tag, cat, phrase in Q:
    u = ("https://api.openalex.org/works?filter=" + up.quote("title.search:" + phrase, safe=":")
         + "&sort=cited_by_count:desc&per-page=8&mailto=" + MAILTO)
    rawp = "lit/raw/supp_%s.json" % tag
    if os.path.exists(rawp):
        j = json.load(open(rawp, encoding="utf-8")); s = 200
    else:
        s, j = get(u)
        if s == 200 and j:
            json.dump(j, open(rawp, "w", encoding="utf-8"))
    rs = (j or {}).get("results", [])
    n_new = 0
    for w in rs:
        doi = (w.get("doi") or "").replace("https://doi.org/", "").strip().lower()
        if doi in have_doi:
            continue
        have_doi.add(doi)
        idx += 1
        authors = w.get("authorships", [])
        fa = authors[0].get("author", {}).get("display_name", "") if authors else ""
        title = (w.get("display_name") or "").strip()
        venue = ""
        try:
            venue = (w.get("primary_location") or {}).get("source", {}) or {}
            venue = venue.get("display_name", "") if isinstance(venue, dict) else ""
        except Exception:
            pass
        new_rows.append({
            "idx": idx, "cat": cat, "title": title, "year": w.get("publication_year"),
            "first_author": fa, "venue": venue, "doi": doi,
            "cited": w.get("cited_by_count"),
            "oa_url": w.get("id", ""), "src": tag,
        })
        n_new += 1
    print(tag, "cat%d" % cat, "phrase=%r" % phrase, "status", s, "hits", len(rs), "new", n_new)
    time.sleep(2.0)

# ---- 2) Crossref 逐条核实 ----
def tokens(s):
    return set(t for t in up.unquote(s.lower().replace("-", " ")).split() if len(t) > 2)

for r in new_rows:
    doi = r["doi"]
    if not doi:
        ver_rows.append({"idx": r["idx"], "doi": "", "http": "", "cr_title": "", "cr_year": "",
                         "cr_author": "", "verdict": "UNVERIFIED", "note": "no_DOI"})
        continue
    s, j = get("https://api.crossref.org/works/" + up.quote(doi, safe=""), tries=2, timeout=30)
    if s != 200 or not j:
        ver_rows.append({"idx": r["idx"], "doi": doi, "http": s or 0, "cr_title": "", "cr_year": "",
                         "cr_author": "", "verdict": "UNVERIFIED", "note": "crossref_%s" % s})
        time.sleep(0.12)
        continue
    m = j.get("message", {})
    cr_title = (m.get("title") or [""])[0]
    cr_year = (m.get("issued", {}).get("date-parts", [[None]])[0][0])
    cr_auth = (m.get("author") or [{}])[0].get("family", "")
    ratio = difflib.SequenceMatcher(None, r["title"].lower(), cr_title.lower()).ratio()
    fa = (r["first_author"] or "").split()[-1].lower() if r["first_author"] else ""
    am = fa and cr_auth.lower() in fa or fa in cr_auth.lower()
    if ratio >= 0.75:
        v = "VERIFIED" if am else "VERIFIED_author_mismatch"
    else:
        v = "MISMATCH"
    ver_rows.append({"idx": r["idx"], "doi": doi, "http": 200, "cr_title": cr_title[:90],
                     "cr_year": cr_year, "cr_author": cr_auth, "verdict": v,
                     "note": ("tr=%.2f" % ratio)})
    time.sleep(0.12)

# ---- 3) API 语义探针 ----
os.makedirs("data/raw", exist_ok=True)
s1, j1 = get("https://api.openalex.org/works?filter=authorships.countries:BR&group_by=topics.field.id&per-page=5&" + "mailto=" + MAILTO)
if s1 == 200 and j1:
    gb = j1.get("group_by", [])
    print("P1 group_by=topics.field.id (BR):", s1, "entries", len(gb), "top3",
          [(g.get("key_display_name") or g.get("key"), g.get("count")) for g in gb[:3]])
    json.dump(j1, open("data/raw/supp_gb_field.json", "w", encoding="utf-8"))
else:
    print("P1 FAIL", s1)
time.sleep(0.3)
s2, j2 = get("https://api.openalex.org/works?filter=authorships.countries:US&per-page=1&" + "mailto=" + MAILTO)
c_us = (j2 or {}).get("meta", {}).get("count")
time.sleep(0.3)
s3, j3 = get("https://api.openalex.org/works?filter=authorships.countries:BR,US&per-page=1&" + "mailto=" + MAILTO)
c_brus = (j3 or {}).get("meta", {}).get("count")
print("P2 OR-semantics: count(BR)=3894723 count(US)=", c_us, "count(BR,US)=", c_brus,
      "| sum-approx" if c_brus and c_us and abs(c_brus - (3894723 + c_us)) < 0.05 * (3894723 + c_us) else "| NOT-sum")

# ---- 4) 写盘 ----
cols_new = ["idx", "cat", "title", "year", "first_author", "venue", "doi", "cited", "oa_url", "src"]
cols_ver = ["idx", "doi", "http", "cr_title", "cr_year", "cr_author", "verdict", "note"]
with open("lit/extracted_supp.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols_new, delimiter="\t")
    w.writeheader(); [w.writerow({k: r.get(k, "") for k in cols_new}) for r in new_rows]
with open("lit/verification_supp.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols_ver, delimiter="\t")
    w.writeheader(); [w.writerow({k: r.get(k, "") for k in cols_ver}) for r in ver_rows]
n_v = sum(1 for v in ver_rows if v["verdict"].startswith("VERIFIED"))
n_m = sum(1 for v in ver_rows if v["verdict"] == "MISMATCH")
n_u = sum(1 for v in ver_rows if v["verdict"] == "UNVERIFIED")
print("DONE new=%d verified=%d mismatch=%d unverified=%d" % (len(new_rows), n_v, n_m, n_u))
print("FILES lit/extracted_supp.tsv lit/verification_supp.tsv data/raw/supp_gb_field.json")
