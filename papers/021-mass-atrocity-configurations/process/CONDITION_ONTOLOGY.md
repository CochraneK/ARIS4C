# ARIS4C021 · Condition Ontology v0.1

## Purpose

Provide a MECE-oriented causal-role ontology for candidate mass-atrocity conditions while keeping raw source variables separate from analytic conditions.

This file defines candidate concepts, not empirical conclusions.

## O · Opportunity structure
- O-AUT · autocracy / weak executive constraints
- O-TRANS · abrupt regime transition / collapse
- O-CONFLICT · internal armed conflict / civil war

## M · Elite motive / exclusionary project
- M-IDEO · exclusionary ruling-elite ideology
- M-ETH · salient ethnic character / minority position of ruling elite
- M-EXCL · institutionalized political exclusion

## T · Proximate trigger
- T-UPH · acute political upheaval
- T-COUP · coup / attempted seizure of power
- T-ESC · rapid conflict escalation

## V · Target vulnerability
- V-DISC · prior organized discrimination
- V-VIOL · prior targeted violence against a group
- V-EXCL · low political access / exclusion of targeted population

## C · Coercion and impunity
- C-REP · severe state repression
- C-IMP · impunity / weak accountability
- C-CAP · coercive capacity available to perpetrators

## X · External constraint / integration
- X-TRADE · trade openness / economic international integration
- X-MON · external monitoring / international constraint
- X-SUP · external sponsorship/support where sourceable without post-treatment leakage

## H · Historical path dependence
- H-PRIOR · prior genocide/politicide
- H-ATRO · prior mass atrocity
- H-REC · recurrent unresolved violent conflict

## Replication core

The first model is restricted to:
- H-PRIOR
- T-UPH
- M-IDEO
- O-AUT
- M-ETH
- X-TRADE

Do not add extension variables until replication is locked.

## Atlas display semantics

A condition tile has five independent fields:
- family;
- calibration;
- role;
- robustness;
- provenance.

Allowed post-analysis role labels:
- Necessary;
- Sufficient-path component;
- INUS component;
- Protective-path component;
- Unstable;
- No supported role.

A tile must never say simply “causes genocide”.
