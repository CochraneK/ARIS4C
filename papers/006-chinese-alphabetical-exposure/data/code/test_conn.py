import sys, urllib.request
print(sys.version.split()[0], sys.executable)
r = urllib.request.urlopen("https://api.openalex.org/works?per-page=1&select=id", timeout=30)
print(r.status, r.read(80))
r2 = urllib.request.urlopen("https://api.crossref.org/works/10.1038/nature14562?select=DOI,title", timeout=30)
print(r2.status, r2.read(120))
