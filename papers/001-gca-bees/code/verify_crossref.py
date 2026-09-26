import json, time, urllib.request

UA = {"User-Agent": "aris4c-stage1 (research; mailto:local@example.org)"}

def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode())

# doi | expected_first_author_frag | expected_year | expected_title_frag
DOIS = [
 ("10.3758/bf03328341", "Bermant", 1966, "Discrimination training and reversal"),
 ("10.1016/s0003-3472(86)80157-9", "Gould", 1986, "Pattern learning by honey bees"),
 ("10.2307/4422", "", 1986, "Optimal diet, minimal uncertainty"),
 ("10.1007/bf01997235", "Benatar", 1995, "Selection on a haploid genotype"),
 ("10.1007/s003590050360", "Scheiner", 1999, "Tactile learning"),
 ("10.1037/0735-7036.114.1.86", "Chandra", 2000, "Heritable variation for latent inhibition"),
 ("10.1007/s100710000068", "Ben-Shahar", 2000, "reversal learning test and division of labor"),
 ("10.1006/nlme.2000.3996", "Scheiner", 2001, "Genotype, Foraging Role"),
 ("10.1023/a:1012227308783", "Chandra", 2001, "Quantitative Trait Loci"),
 ("10.1101/lm.44602", "Komischke", 2002, "Successive Olfactory Reversal"),
 ("10.1073/pnas.0732090100", "Chen", 2003, "Topological pattern recognition"),
 ("10.3389/fnbeh.2010.00048", "Mota", 2010, "Multiple reversal olfactory"),
 ("10.3389/fnbeh.2010.00186", "Hadar", 2010, "Memory Formation in Reversal"),
 ("10.1007/s10905-014-9465-1", "Carr-Markell", 2014, "Reversal-Learning Abilities"),
 ("10.1016/j.beproc.2015.03.001", "Muszynski", 2015, "Relational learning in honeybees"),
 ("10.1098/rspb.2016.2149", "Benaets", 2017, "deformed wing virus"),
 ("10.7717/peerj.5918", "P\u00e9rez", 2018, "Appetitive reversal learning"),
 ("10.1073/pnas.1314571110", "", 2014, "selectively avoid difficult choices"),
 ("10.1007/s10071-022-01741-2", "Finke", 2023, "Individual consistency"),
 ("10.1007/s00265-026-03744-2", "Oxman", 2026, "recruitment effort when dance"),
 ("10.1007/s10071-026-02076-y", "Golan", 2026, "cognitive judgement bias"),
 ("10.1073/pnas.1408039111", "Cheeseman", 2014, "clock-shifted bees"),
 ("10.3389/fevo.2019.00177", "Hendriksma", 2019, "Foraging Decisions"),
 ("10.1371/journal.pone.0045096", "Raine", 2012, "Trade-Off between Learning Speed"),
 ("10.1038/s41598-017-00389-0", "Evans", 2017, "Fast learning in free-foraging"),
 ("10.1523/jneurosci.15-03-01617.1995", "Hammer", 1995, "Learning and memory in the honeybee"),
 ("10.3389/fpsyg.2013.00162", "Pahl", 2013, "Numerical Cognition in Bees"),
 ("10.3819/ccbr.2012.70005", "Roberts", 2012, "Information Seeking in Animals"),
 ("10.3389/fnhum.2014.00443", "Fleming", 2014, "How to measure metacognition"),
 ("10.3389/fetho.2023.1246370", "Qu", 2023, "Uncertainty monitoring"),
 ("10.1207/s15516709cog0000_50", "Hills", 2006, "Animal Foraging and the Evolution"),
 ("10.1371/journal.pone.0111805", "Veldwijk", 2014, "Opt-Out Option in Discrete Choice"),
]

out = []
for doi, ea, ey, et in DOIS:
    try:
        d = get("https://api.crossref.org/works/" + urllib.request.quote(doi, safe=""))
        m = d["message"]
        ti = (m.get("title") or ["?"])[0]
        yr = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
        au = m.get("author") or [{}]
        fa = (au[0].get("family") or au[0].get("name") or "?")
        ok = "OK"
        if ea and ea.lower() not in fa.lower():
            ok = "AUTH?"
        if ey and yr and int(yr) != ey:
            ok = "YEAR?"
        if et.lower()[:15] not in ti.lower():
            ok = "TITLE?"
        out.append("%s | %s | %s | %s | %s" % (ok, doi, yr, fa, ti[:80]))
    except Exception as e:
        out.append("FAIL | %s | %r | expected %s %s" % (doi, e, ea, et))
    time.sleep(0.4)

try:
    d = get("https://api.datacite.org/dois/10.5281/zenodo.17771502")
    d3 = d["data"]["attributes"]
    out.append("OK | 10.5281/zenodo.17771502 | %s | %s | %s" % (
        d3.get("titles", [{}])[0].get("title", "?")[:60],
        (d3.get("creators") or [{}])[0].get("name"),
        d3.get("publisher")))
except Exception as e:
    out.append("FAIL | 10.5281/zenodo.17771502 | %r" % e)

with open("results/crossref_check.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("CHECKED", len(out))
for l in out:
    print(l)
