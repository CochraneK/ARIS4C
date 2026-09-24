# Aggregated Survival / Hazard Strategy · v1

ARIS4C-020 does **not** need to materialize every non-retracted OpenAlex work as an individual row to model time-to-retraction.

## Construction

For each publication-year × OpenAlex-field cohort:

- (N_0): eligible OpenAlex core works published in that cohort;
- (E_a): unique RWDB-linked works formally retracted at age (a) years;
- (R_a = N_0 - sum_{j<a} E_j): papers at risk at the start of age interval (a);
- discrete hazard (h_a = E_a / R_a);
- cumulative recorded-retraction incidence through age (a): (sum_{jle a} E_j / N_0).

Administrative follow-up ends at the frozen analysis cutoff.

This produces a compact cohort-age panel suitable for:
- fixed-horizon cumulative incidence;
- complementary-log-log or logit discrete-time hazard models;
- field/cohort interaction models;
- mass-event exclusion sensitivity.

## Important coverage boundary

The numerator initially contains RWDB works that:
1. have a usable OriginalPaperDOI;
2. match uniquely to OpenAlex;
3. have an OpenAlex field.

Therefore this is initially a **DOI/OpenAlex-linkable recorded-retraction hazard**, not yet the full RWDB population hazard.

Before headline use, report numerator coverage by publication cohort and repeat sensitivity analyses after:
- unmatched DOI adjudication;
- no-DOI identity recovery where feasible;
- eligible OpenAlex work-type freeze.

No multiplicative correction for missing events is applied without evidence that missingness is ignorable.

## Why this is preferable to downloading 100M+ control rows

The population at risk is represented exactly by grouped exposure counts when the estimand only requires cohort/field/time cells. Individual non-retracted records are needed only for analyses requiring work-level covariates or matched citation controls.

This keeps the primary survival design reproducible and substantially lighter.
