import json, urllib.request, urllib.parse, time
UA = {"User-Agent": "aris4c006/1.0 (mailto:aris4c-006@polite.example)"}
def probe(name, url):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=40) as r:
            body = r.read(300)
            print(name, r.status, body[:200])
    except Exception as e:
        print(name, "ERR", str(e)[:120])
probe("crossref_search", "https://api.crossref.org/works?query.bibliographic=alphabetical+author+order&rows=2&select=DOI,title,author,container-title,issued,URL")
time.sleep(1)
probe("s2_search", "https://api.semanticscholar.org/graph/v1/paper/search?query=implicit+egotism+name+letters&limit=2&fields=title,year,externalIds,venue")
time.sleep(1)
probe("github_raw", "https://raw.githubusercontent.com/zhengxiaotian/ChineseNames/master/README.md")
time.sleep(1)
probe("cr_chinenames", "https://cran.r-project.org/web/packages/ChineseNames/index.html")
