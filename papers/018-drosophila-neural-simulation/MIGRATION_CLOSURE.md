# ARIS4C018 · FlyGym 1.x → 2.x Migration Closure

Date: 2026-09-21

## Closure state

**Migration engineering gate: CLOSED / PASS.**

The following layers have each passed independently and in composition:

| Layer | Evidence |
|---|---|
| current FlyGym body compile / physics | Pilot 1 |
| current Retina readout | Pilot 3A |
| one-to-one FlyGym2 ↔ flyvis retinal mapping | Pilot 3A |
| current pretrained flyvis state | Pilot 3A |
| audited decoder equations | decoder unit CI |
| current HybridTurningController integration | strict Pilot 3B |
| target-driven current embodied closed loop | strict Pilot 3B |
| synchronized current BODY/TARGET/DECODER/BIO trace | Pilot 3C |
| legacy/current semantic trace parity | trace parity CI |
| one replay implementation for both provenances | replay UI |

## Canonical workflows

- Pilot 3A: `35555729841`
- strict Pilot 3B: `35556093444`
- Pilot 3C: `35556733779`
- trace parity: `35559603116`

## What is closed

The question:

> Can ARIS4C018 execute its bounded embodied visual-neural-decoder-body pipeline on the maintained FlyGym 2.x stack and preserve an auditable replay contract?

Answer:

**Yes, at the current bounded engineering scope.**

## What is not closed

Migration closure does not establish:

- numerical equivalence between FlyGym 1.x and 2.x;
- replication of the published 3 s condition;
- biological validity of the engineered decoder;
- successful target following;
- a novel neuroscience finding.

## Next stage

Pilot 4 is a **matched cross-version regression**.

It freezes the same static target, spawn, duration, update rate, decoder parameters and tracking cells on both stacks and reports diagnostic differences without a post-hoc equivalence threshold.

Any mismatch is localized in this order:

1. Retina geometry/order;
2. frozen retinal stimulus → flyvis;
3. decoder pure function;
4. controller semantics;
5. embodied trajectory.

Migration is therefore no longer the active project question.
