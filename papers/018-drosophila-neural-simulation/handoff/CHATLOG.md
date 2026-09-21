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
