import time, os, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "aris4c006/1.0 (mailto:aris4c-006@polite.example)"}
def probe():
    try:
        req = urllib.request.Request("https://api.openalex.org/works?per-page=1&select=id", headers=UA)
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status == 200
    except Exception as e:
        print("probe-err", str(e)[:80])
        return False
for i in range(42):  # ~7h window, every 10 min
    t = time.strftime("%H:%M:%S")
    if probe():
        print("BUDGET-OK at", t)
        import s3_openalex
        s3_openalex.OUT = "data/feasibility_v2.json"
        s3_openalex.main()
        print("WAITER-DONE")
        break
    print("wait", i, t)
    time.sleep(600)
else:
    print("WAITER-TIMEOUT no success in window")
