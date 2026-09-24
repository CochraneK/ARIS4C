# ARIS4C 000 · TODO

## P0 · Scheduling

- [ ] Continue the current genuine Active paper until a bounded unit is checkpointed.
- [ ] When additional genuine execution capacity becomes available, promote the highest-progress Wait paper.
- [ ] Recalculate the queue after every material paper-state change.

## P1 · Portfolio integrity

- [ ] Keep `papers/dashboard.json` aligned with real execution rather than merely executable work.
- [ ] Keep Active WIP at 1 by default, but scale it up or down dynamically with model/agent/tool capability; 3 is only a conservative soft reference, not a hard cap.
- [ ] Ensure every paper switch passes the checkpoint-before-switch rule.
- [ ] Keep Block reasons explicit and actionable.

## P2 · Public/control surfaces

- [x] Resolve duplicate ARIS4C018 portfolio identity without deleting provenance: `018-drosophila-neural-simulation` is canonical; `018-drosophila-open-simulation` is retained as `portfolio_visible:false` with `superseded_by` metadata.
- [ ] Restore GitHub Actions runner execution. Since 2026-09-23/24, index/handoff/PDF/research workflows are failing before the first step starts; reruns reproduce the same zero-step failure.
- [ ] After runner execution is restored, regenerate README, README SVGs, Research Command Center, progress history, and 000 snapshot from canonical Git state; verify 023 is public and Today's curve shows the current Beijing date.
- [ ] Keep README and Research Command Center synchronized with canonical states.
- [ ] Keep 000 handoff current enough for a new agent/account/computer to resume safely.
