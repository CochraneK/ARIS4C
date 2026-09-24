# ARIS4C018 · Research conversation log

Public-safe record of material human ↔ ChatGPT / external-agent conversations. This is **not** hidden chain-of-thought and must not contain secrets.

## 2026-09-19 · Historical bootstrap distilled from surviving ARIS4C context

- **Surface:** ChatGPT / ARIS4C project conversations
- **Participants:** Cochrane Kang + AI research assistants
- **Research thread:** An exploration project mapping the open Drosophila neuroscience ecosystem and developing a behaviour-neural dual-view sandbox. Pilot 0 validates the perturb-simulate-visualize-measure pipeline with an explicitly non-biological toy ring-attractor model; Pilot 1 will reproduce maintained published components such as FlyGym or flyvis before biological claims.
- **User operating preference:** Continue in GO mode when requirements are clear; persist important state to Git rather than relying on chat memory alone.
- **Outcome:** The current repository state, process files, dashboard state, and handoff package are treated as the recoverable source of truth.
- **Backfill limitation:** Earlier chats are summarized rather than reproduced verbatim where a complete export is unavailable.

### Prospective logging rule

For every future material conversation, append:
- date/session and agent/surface;
- the research question or requested change;
- concise faithful summary;
- important user correction/constraint;
- decision/result;
- affected files/commits where known.

## 2026-09-21 · Pilot 2B closed-loop milestone

User requested continued GO-mode execution on ARIS4C018.

Public-safe summary:
- reproduced the official legacy embodied visual-neural interface;
- reproduced a bounded moving-target closed loop using the published engineered decoder equations;
- explicitly separated biological/connectome-constrained neural activity from the engineered neural-to-control decoder;
- did not label the bounded run as successful following because target separation increased;
- added independent decoder tests, claim-boundary documentation, modern FlyGym migration audit, and a synchronized trace schema;
- next work is full trace capture and stronger baseline/full-condition reproduction.

## 2026-09-21 · Pilot 2C synchronized trace milestone

- Pilot 2C workflow completed successfully.
- CI generated, shape-validated, and committed a deterministic 100-frame real-model trace.
- Trace contains 25 selected visual cell types per eye plus decoder/body/target state.
- Replay UI now consumes committed scientific trace rather than toy fallback data.
- Trace computation cost (~9m16s for 0.20s baseline + 0.20s loop) makes naive legacy 3s CI expansion unattractive.
- Work moved to a reusable FlyGym 2.x Retina -> current flyvis adapter before spending full-duration legacy compute.


## 2026-09-21 · Pilot 3 migration closure and Pilot 4 launch

User continued GO-mode execution.

Public-safe summary:
- current-stack synchronized trace generation and semantic validation passed;
- current trace was committed by CI and contains 40 real visual/neural updates;
- legacy/current semantic trace parity passed;
- one replay implementation now handles both provenance-labeled real traces;
- FlyGym 1.x→2.x migration was closed at the bounded engineering scope;
- a matched static-target cross-version diagnostic was frozen before inspecting results;
- legacy/current dependency stacks run in isolated CI jobs and a third job compares only pre-specified engineering metrics;
- no post-hoc equivalence threshold, version winner, or biological interpretation is permitted from the first matched diagnostic.

## 2026-09-24 · deletion-ready Git handoff requested

- **Surface:** ChatGPT / ARIS4C project conversation
- **Participants:** Cochrane Kang + AI research assistant
- **User request:** Persist all material ARIS4C018 work to Git, make the project compliant with the ARIS4C handoff standard, and prepare for deletion of the current chat.
- **Repository audit result:** Canonical Git state is 90% / Pilot 4 localization. Pilots 0–3, Pilot 4 matched diagnostic, R1 and R2 are already committed. R2.5 is implemented but has not scientifically executed because GitHub Actions currently fails before job steps begin.
- **Corrections made:** Added the missing R2 narrative result; refreshed project README; reconciled historical TODO items; refreshed handoff CONTEXT/TODO/DECISIONS/SESSION_LOG; verified the current runner blocker.
- **Continuation rule:** Do not rely on this chat. Start from `handoff/README.md` and `handoff/AGENT_HANDOFF.md`, then execute the frozen R2.5 gate when a runner becomes available.
- **Safety/claim boundary:** No hidden chain-of-thought, credentials, or private material were committed; only public-safe research continuity information is retained.
