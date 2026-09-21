# ARIS4C019 · Post-Unlock Treatment Isolation Audit v0.1

**Audit date:** 2026-09-21  
**Stage:** post-outcome identification audit  
**Primary outcome already unlocked:** Life Ladder  
**Secondary outcomes remain locked:** Positive affect / Negative affect

> This audit was initiated after the first Life Ladder outcome look. It does **not** rewrite the pre-outcome freeze and must not be presented as preregistered. Its purpose is to test whether the frozen legal events can actually identify a statutory annual-leave effect rather than a broader labour/time-off package or contemporaneous shock.

## 1. Why this audit is necessary

The frozen event registry correctly identifies legal changes in statutory paid annual leave. That is not sufficient for treatment isolation.

A credible annual-leave-specific interpretation additionally requires that:

1. the legal intervention is reasonably separable from other simultaneous labour-policy changes;
2. the reference year is not an obvious transitory shock or rebound anchor;
3. the population affected by the law is sufficiently aligned with the population outcome;
4. the event is not dominated by a major macro shock in the event window.

The first outcome diagnostics exposed exactly this concern: the pooled mean is strongly influenced by Bahrain, while several events are embedded in comprehensive labour-law packages.

## 2. Headline-event isolation audit

| Event | Legal vehicle | Isolation class | Important co-treatment / shock | Consequence for interpretation |
|---|---|---|---|---|
| China 2008 | State Council Decree No. 514, Regulations on Paid Annual Leave of Employees | **Leave-specific regulation** | Global financial crisis overlaps post window | Cleanest annual-leave legal intervention in the frozen pool, but macro timing still weakens a single-event causal claim |
| Croatia 2010 | 2009 Labour Act | **Broad labour code** | Working time, rest and other employment rights changed within the same act; GFC overlap | Cannot attribute the event to annual leave alone |
| Kosovo 2010 | Law No. 03/L-212 on Labour | **Broad labour code** | Comprehensive regulation of employment relations | Cannot attribute the event to annual leave alone |
| Kuwait 2010 | Law No. 6/2010, private-sector Labour Law | **Broad labour code** | Contracts, termination, wages, hours/rest, OSH, collective labour relations and annual leave | Cannot attribute the event to annual leave alone |
| Bahrain 2012 | Law No. 36/2012, private-sector Labour Law | **Broad labour code + severe reference-year risk** | 2011 domestic unrest depressed activity; 2012 saw a broad macroeconomic rebound | The very large positive post gap is especially vulnerable to rebound/confounding and should not identify an annual-leave effect |
| Taiwan 2017 | 2016 Labor Standards Act amendments | **Bundled working-time reform** | Five-day work week, rest-day overtime, shift rest, national holidays, annual leave, enforcement changes | Better interpreted as a bundled work-time/time-off reform, not an annual-leave-only event |
| Luxembourg 2019 | Law of 25 April 2019 amending Labour Code | **Annual leave + public holiday bundle** | Same law increased annual leave to 26 days and added Europe Day as a legal public holiday; COVID overlaps later post years | Cannot cleanly separate the extra annual-leave day from the extra public holiday |
| Canada 2019 | Federal labour-standards modernization | **Broad federal labour-standards package** | Breaks, rest between shifts, schedule notice, personal/family-violence/medical leave and vacation changes; federal jurisdiction only; COVID overlap | Annual-leave-specific and population-wide interpretation are both weak |

Machine-readable flags are stored in `data/pilot0_event_isolation_flags.csv`.

## 3. Source anchors

### China

State Council Decree No. 514 is explicitly the *Regulations on Paid Annual Leave of Employees* and became effective on 2008-01-01.

- State Council Gazette: https://english.www.gov.cn/archive/state_council_gazette/2015/06/08/content_281475123272260.htm
- Regulation text mirror hosted by Shanghai Human Resources and Social Security: https://rsj.sh.gov.cn/cmsres/e5/e59dff3cca7b4acbbb0d01b5acc2e7dc/17bf163011fb8776ee5a396313e67451.pdf

### Croatia

The 2009 Labour Act is a general labour statute. Article 55 establishes at least four weeks of annual leave, while the same act regulates employment relations, working time and rest.

- Official Gazette: https://narodne-novine.nn.hr/clanci/sluzbeni/2009_12_149_3635.html

### Kosovo

Law No. 03/L-212 states that its purpose is to regulate rights and obligations arising from employment relationships and applies broadly across private and public sectors.

- Official Gazette: https://gzk.rks-gov.net/ActDetail.aspx?ActID=2735&langid=2
- Act text: https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=2735

### Kuwait

Law No. 6/2010 is classified by ILO NATLEX as a general labour/employment act. It covers contracts, termination, wages, working hours and weekly leave, annual paid leave, occupational safety, collective labour relations, inspection and penalties.

- ILO NATLEX: https://natlex.ilo.org/dyn/natlex2/r/natlex/fe/details?p3_isn=83616

### Bahrain

Law No. 36/2012 is a comprehensive private-sector Labour Law covering wages, hours/rest, leave, working conditions, injury, termination, disputes and occupational safety.

- ILO NATLEX: https://natlex.ilo.org/dyn/natlex2/r/natlex/fe/details?p3_isn=91026

The reference year is additionally problematic. IMF surveillance describes 2011 activity as disrupted by domestic unrest and reports a broad rebound in non-oil activity in 2012.

- IMF 2012 Article IV: https://www.imf.org/en/news/articles/2015/09/28/04/53/pn1239
- IMF 2013 Article IV: https://www.imf.org/en/news/articles/2015/09/28/04/53/pn1353

This is particularly relevant because the first donor-adjusted diagnostic uses 2011 as Bahrain's T-1 reference and Bahrain has both a very large pre-placebo RMS gap and a very large positive post gap.

### Taiwan

The Ministry of Labor describes the December 2016 amendments as reforms pertinent to the **Five-Day Work Week**. The package changed rest-day overtime, shift rest, the five-day work-week framework, national holidays, annual paid leave, complaint protection and penalties.

- Ministry of Labor: https://english.mol.gov.tw/21139/21156/21621/
- Labor Standards Act, Articles 37-38: https://laws.mol.gov.tw/Eng/PrintFLAWDAT0201.aspx?id=FL014930

### Luxembourg

The Law of 25 April 2019 simultaneously amended the legal-public-holiday provision to add Europe Day and raised the minimum annual leave to 26 working days.

- Official legislative dossier / Journal Officiel: https://wdocs-pub.chd.lu/docs/compilation/docpa/pdf/7399_Dossier_Complet.pdf
- Labour inspectorate annual-leave note: https://itm.public.lu/fr/questions-reponses/droit-travail/conges/a/a1.html

### Canada

The federal modernization package changed vacation entitlement together with breaks, minimum rest between shifts, schedule notice, personal leave, family-violence leave, medical leave and other standards.

- Government of Canada backgrounder: https://www.canada.ca/en/employment-social-development/news/2018/10/backgrounder-modernizing-labour-standards.html

## 4. Identification consequence

The current eight-event design **does not support a clean pooled causal claim about annual leave specifically**.

The event pool is better described as a heterogeneous collection of legal reforms in which annual-leave entitlement changed, often alongside other employment, working-time or time-off provisions.

Accordingly:

- do not relabel the frozen treatment retrospectively;
- keep the original eight-event results as a transparent feasibility/stress-test layer;
- do not use Bahrain's large positive gap as evidence for an annual-leave effect;
- distinguish an **annual-leave-specific estimand** from a **broader labour/time-off package estimand** in all subsequent work;
- treat China as the cleanest leave-specific event currently identified, while retaining its GFC timing caveat;
- search for additional stand-alone annual-leave reforms before attempting a manuscript-level annual-leave-specific pooled estimate.

## 5. Post-unlock decision

This audit changes the **interpretation and next data-collection priority**, not the frozen observed results.

### Track A — annual-leave-specific question

Continue searching for stand-alone statutory annual-leave reforms with:

1. exact legal date;
2. clear increase/decrease in entitlement;
3. no major same-law working-time/leave bundle;
4. >=2 observed Life Ladder years before and after;
5. acceptable donor support;
6. no obvious one-year reference shock.

### Track B — broader policy-package question

Retain the existing eight-event panel as exploratory evidence about reforms that changed annual leave within broader labour/time-off packages.

Track B must not be presented as isolating annual leave.

## 6. Outcome firewall

Positive affect and Negative affect remain locked. The identification problem in the primary Life Ladder analysis should be resolved or explicitly reframed before secondary outcomes are opened.
