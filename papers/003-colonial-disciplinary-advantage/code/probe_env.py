import os, sys
print("EXE:", sys.executable)
print("CWD:", os.getcwd())
print("PY:", sys.version.split()[0])
for d in ["data", "lit", "code", "results"]:
    print("DIR", d, os.path.isdir(d))
print("ROOT_FILES:", sorted(os.listdir("."))[:25])
try:
    import urllib.request as u
    r = u.urlopen("https://api.openalex.org/works?per-page=1&select=id", timeout=30)
    print("NET_OK", r.status)
except Exception as e:
    print("NET_FAIL", type(e).__name__, str(e)[:200])
try:
    import pandas, numpy, scipy, statsmodels
    print("PKGS_OK pandas", pandas.__version__)
except Exception as e:
    print("PKGS_FAIL", str(e)[:150])
