# CITATION CHAIN AUDIT · v0.2

## Purpose

Close G2 using citation topology as a discovery/audit layer, not as a prestige ranking.

## Seed set

Primary method seeds:
- Graça da Silva & Tehrani 2016 — 10.1098/rsos.150645
- D-PLACE 2016 — 10.1371/journal.pone.0158391
- Mace & Pagel 1994 — 10.1086/204317
- Mace & Holden 2005 — 10.1016/j.tree.2004.12.002
- Greenhill et al. 2009 — 10.1098/rspb.2008.1944
- Currie et al. 2010 — 10.1098/rstb.2010.0014
- Nunn et al. 2006 — 10.1177/1069397105283401

## Backward / forward pass

Scite citation-graph traversal was run in both directions at depth 1.

The first multi-seed run hit the 350-edge cap because the Mace & Holden review dominated the returned neighborhood. Several other seeds therefore showed low direct edge coverage. A second targeted pass separated the folktale/D-PLACE seeds from the horizontal-transmission seeds and attached citation intent/snippets where available.

Important papers recovered or promoted by the citation chain:
- Evans et al. 2021, *The uses and abuses of tree thinking in cultural evolution*;
- Bromham et al. 2018, relatedness/proximity/covariation;
- von Cramon-Taubadel & Lycett 2018, divergence versus inter-group transmission;
- Neureiter et al. 2022, contact-aware language trees;
- Mace & Jordan 2011, macro-evolutionary cultural-diversity review;
- Ané 2008, hierarchical autocorrelation.

## Coverage caveat

The citation graph is **not** interpreted quantitatively:
- seed coverage was highly unequal;
- edge caps truncated dense neighborhoods;
- DOI resolution is incomplete for books/chapters/humanities sources;
- the Scite MCP monthly usage limit was exhausted after this audit.

Therefore:
- non-appearance is not evidence of irrelevance;
- edge count is not used as a literature importance score;
- ancient-text/source-critical literature continues to rely on publisher/corpus verification and manual citation chaining.

## G2 closure rule

G2 is considered PASS because:
- >=50 records were screened;
- >=25 relevant sources/resources were retained;
- skeptical/contrasting method literature is included;
- backward/forward citation-chain audit was executed and limitations recorded;
- a claim-to-evidence map now links C1–C7 to external/project evidence and explicit boundaries;
- search/tool constraints are frozen below.

Future additions are permitted as bibliography maintenance but may not silently change preregistered claims or the case universe.
