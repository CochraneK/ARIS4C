import csv, json, os, time, urllib.request, urllib.error

MAILTO = "mailto=aris4c004@example.org"
SELFORMS = ["id,doi,title,publication_year,cited_by_count,authorships,concepts", ""]
DELAY = [0, 30, 60, 120, 240]
BUDGET = 600
PACE = 2.0
os.makedirs("data/raw/works", exist_ok=True)
os.makedirs("data/_raw", exist_ok=True)
QLOG = open("data/_raw/queries_2b.log", "a", buffering=1, encoding="utf-8")
PROG = open("data/_raw/fetch_progress_2b.txt", "a", buffering=1, encoding="utf-8")
ERR = open("data/_raw/fetch_err_2b.txt", "a", buffering=1, encoding="utf-8")
st = {"q": 0, "e429": 0, "stop": None, "form_drop": 0}
LAST = [0.0]
STORM = {"n": 0, "pauses": 0}

def pace():
    wait = PACE - (time.time() - LAST[0])
    if wait > 0:
        time.sleep(wait)
    LAST[0] = time.time()

def build_url(aid, sel, cur):
    u = "https://api.openalex.org/works?filter=author.id:%s&per-page=200" % aid
    if sel:
        u += "&select=" + sel
    return u + "&sort=publication_year:asc&cursor=%s&%s" % (cur, MAILTO)

def get(url, sid, page):
    last, nret = 0, 0
    for d in DELAY:
        if d:
            time.sleep(d)
        pace()
        st["q"] += 1
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "aris4c004@example.org"})
            r = urllib.request.urlopen(req, timeout=120)
            code, body = r.getcode(), json.loads(r.read().decode())
            nret = len(body.get("results", [])) if isinstance(body, dict) else 0
        except urllib.error.HTTPError as e:
            code, body = e.code, None
            if code == 429:
                st["e429"] += 1
            if code in (400, 404, 500, 502, 503):
                try:
                    msg = e.read().decode("utf-8", "replace")[:300]
                except Exception:
                    msg = "<unreadable>"
                ERR.write("%s|%s|p%d|%d|%s\n" % (time.strftime("%H:%M:%S"), sid, page, code, msg))
                ERR.flush()
        except Exception:
            code, body = 0, None
        last = code
        QLOG.write("%s,%s,%d,%d,%d\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), sid, page, code, nret))
        if code == 200:
            return 200, body
        if code in (429, 0):
            continue
        return code, body
    return last, None

def fetch_author(aid, form):
    works, pages, tr, status, cur = [], 0, 0, "ok", "*"
    sel = SELFORMS[form]
    while pages < 5:
        if st["q"] >= BUDGET:
            st["stop"], status = "budget", "budget"
            break
        code, body = get(build_url(aid, sel, cur), aid, pages + 1)
        if code == 400:
            return works, pages, tr, "err400"
        if code != 200 or body is None:
            status = "err%d" % code if code else "errnet"
            break
        works.extend(body.get("results", []))
        pages += 1
        cur = (body.get("meta") or {}).get("next_cursor")
        if not cur:
            break
    else:
        tr = 1
    return works, pages, tr, status

def save(aid, pages, works, tr, status):
    json.dump({"author_id": aid, "pages": pages, "works": works, "truncated": tr, "status": status},
              open("data/raw/works/%s.json" % aid, "w", encoding="utf-8"), ensure_ascii=False)

def run_author(aid):
    works, pages, tr, status = fetch_author(aid, 0)
    if status == "err400":
        st["form_drop"] += 1
        works, pages, tr, status = fetch_author(aid, 1)
    return works, pages, tr, status

rows = list(csv.DictReader(open("data/exposure_queue.csv", encoding="utf-8")))
done = set(f[:-5] for f in os.listdir("data/raw/works") if f.endswith(".json"))
failed, processed = [], 0
for row in rows:
    aid = row["author_id"].split("/")[-1]
    if aid in done:
        PROG.write("%s,skip,0,0,0,existing\n" % aid)
        continue
    if st["q"] >= BUDGET:
        st["stop"] = "budget"
        break
    if STORM["n"] >= 2 and STORM["pauses"] < 3:
        time.sleep(300)
        STORM["pauses"] += 1
        STORM["n"] = 0
    works, pages, tr, status = run_author(aid)
    if status in ("err429", "errnet"):
        STORM["n"] += 1
    elif status == "ok":
        STORM["n"] = 0
    processed += 1
    if works or status == "ok":
        save(aid, pages, works, tr, status)
        done.add(aid)
    else:
        failed.append(aid)
    PROG.write("%s,%d,%d,%d,%s\n" % (aid, pages, len(works), tr, status))
consec = 0
for aid in failed:
    if st["q"] >= BUDGET or st["stop"] == "budget":
        st.setdefault("stop", "budget" if st["q"] >= BUDGET else None)
        break
    if consec >= 3:
        break
    time.sleep(60)
    works, pages, tr, status = run_author(aid)
    if works or status == "ok":
        save(aid, pages, works, tr, status)
        done.add(aid)
        consec = 0
    else:
        consec += 1
    PROG.write("%s,%d,%d,%d,%s\n" % (aid, pages, len(works), tr, status + "_retry"))
if processed or not os.path.exists("data/_raw/fetch_manifest_2b.json"):
    json.dump({"queries_total": st["q"], "http429": st["e429"], "stop_reason": st["stop"],
               "sel_form_drop": st["form_drop"], "storm_pauses": STORM["pauses"],
               "ts": time.strftime("%Y-%m-%dT%H:%M:%S")},
              open("data/_raw/fetch_manifest_2b.json", "w"))
print("FETCH_DONE q=%d e429=%d stop=%s processed=%d failed_left=%d" % (st["q"], st["e429"], st["stop"], processed, len(failed)))
