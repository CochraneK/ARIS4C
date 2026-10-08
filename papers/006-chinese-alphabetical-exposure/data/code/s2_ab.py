import json,time,urllib.request as U,urllib.parse as P
UA={"User-Agent":"aris4c006/1.0 (mailto:aris4c-006@polite.example)"}
N=[0]
def get(u):
    last=None
    for b in (0,30,60,120,240):
        if b: time.sleep(b)
        try:
            N[0]+=1
            return json.load(U.urlopen(U.Request(u,headers=UA),timeout=120))
        except Exception as e:
            last=e
            if getattr(e,'code',0) in (400,404,422): break
    raise RuntimeError(str(last)[:50])
B="https://api.openalex.org/works?"; CN="authorships.institutions.country_code:CN"
F={"math":"26","physics":"31","nursing":"29","medicine":"27"}
out={"api_calls":N,"probe":{},"counts":{},"window_main":"2010-2024","window_pilot":"2019-2024","fields":{}}
def q(flt): return B+"filter="+P.quote(flt)+"&per-page=1&select=id"
form=None
for f in ("primary_topic.field.id:%s","topics.field.id:%s"):
    try:
        d=get(q(CN+","+f%"26"+",publication_year:2010-2024")); n=d["meta"]["count"]
        if n==0: raise RuntimeError("count0")
        out["probe"][f]="ok n=%d"%n; form=f; print("PROBE-OK",f,n); break
    except Exception as e:
        out["probe"][f]="fail "+str(e)[:45]; print("PROBE-FAIL",f,str(e)[:45])
if not form:
    json.dump(out,open("data/_s2_probe.json","w",encoding="utf-8"),ensure_ascii=False); raise SystemExit("NO-FORM")
for k,fid in F.items():
    d=get(q(CN+","+(form%fid)+",publication_year:2010-2024")); out["counts"][k]=d["meta"]["count"]; print("CNT",k,d["meta"]["count"])
json.dump(out,open("data/_s2_probe.json","w",encoding="utf-8"),ensure_ascii=False); print("COUNTS-DONE calls=%d"%N[0]); time.sleep(3)
SEL="&sort=publication_year:desc&per-page=100&select=id,display_name,publication_year,authorships,primary_location"
for k,fid in F.items():
    time.sleep(2)
    d=get(B+"filter="+P.quote(CN+","+(form%fid)+",publication_year:2019-2024")+SEL)
    out["fields"][k]={"meta_count":d["meta"]["count"],"results":d["results"]}; print("FETCH",k,len(d["results"]),"of",d["meta"]["count"])
json.dump(out,open("data/s2_pilot_works.json","w",encoding="utf-8"),ensure_ascii=False)
json.dump(out,open("data/_s2_probe.json","w",encoding="utf-8"),ensure_ascii=False); print("ALL-DONE calls=%d"%N[0])
