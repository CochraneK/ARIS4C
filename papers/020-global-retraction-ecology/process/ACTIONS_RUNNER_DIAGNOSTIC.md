# GitHub Actions Runner Diagnostic · 2026-09-24

ARIS4C's `Build ARIS4C paper index` workflow currently fails before any workflow step starts.

Observed on run `35967502050`:
- attempt 1: failure;
- explicit re-run requested;
- attempt 2: failure;
- job: `Generate portfolio index`;
- `steps = null`;
- `logs_url = null`;
- run ends within seconds.

Therefore the failure is **upstream of repository code execution**. No Python command, checkout action, README generator, or ARIS4C-020 analysis step actually ran.

## Operational consequence

Do not classify scientific/code tasks as blocked merely because this workflow is red. Continue committing deterministic scripts and compact derived outputs.

## Recovery check

When GitHub-hosted execution becomes available again:
1. rerun the paper-index workflow;
2. confirm checkout produces normal step records/logs;
3. execute ARIS4C-020 regression tests;
4. execute the remaining OpenAlex enrichment shards from a networked runner;
5. regenerate portfolio surfaces.

The exact account/runner cause is not asserted here because the available GitHub connection cannot read account billing/Actions administration state.
