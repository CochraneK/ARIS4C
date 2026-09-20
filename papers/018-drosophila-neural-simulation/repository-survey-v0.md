# ARIS4C018 · Open-source Repository Survey v0

## Goal

Identify projects that can support a first reproducible simulation, not just collect links.

## Tier 1 · High-value infrastructure

| Repository | Role | Initial assessment |
|---|---|---|
| natverse/fafbseg | FAFB connectome access and analysis tooling | Useful infrastructure for connectome exploration |
| cobanov/awesome-fly | Resource index | Useful discovery map |

## Tier 2 · Requires deeper inspection

| Repository | Reason to inspect |
|---|---|
| fly-brain related repositories | Possible educational or simulation examples; verify provenance and maintenance |
| FlyWire-related tools | Potential bridge between connectome data and circuit analysis |

## Evaluation criteria

A candidate first simulation stack should have:

- runnable examples;
- public data access;
- clear biological interpretation;
- manageable computational requirements;
- reproducible environment.

## Current conclusion

Do not start from whole-brain simulation.

The likely first MVP should combine:

```
public circuit data
        ↓
small neural model
        ↓
stimulation
        ↓
observable computational behaviour
```

## Next investigation

Inspect FlyWire / hemibrain analysis workflows and identify the smallest circuit with a clear behavioural output.
