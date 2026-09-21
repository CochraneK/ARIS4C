# ARIS4C019 · Pilot-0 Callaway–Sant'Anna diagnostic

> Modern staggered-adoption group-time ATT diagnostic using the frozen primary event pool. This remains a Pilot-0 robustness layer, not a manuscript-level causal claim.

- differences version: **0.3.0**.
- Frozen treated countries: **8**.
- Common clean control universe: **66 countries**.
- Panel rows supplied to estimator: **1144**.
- Treated observations are hard-trimmed to the frozen legal-year window **T-4 through T+4**; mid-year transition T is excluded.
- Treatment cohorts (legal effective year -> treated-country count): **{2008: 1, 2010: 3, 2012: 1, 2017: 1, 2019: 2}**.
- Control group: **not_yet_treated**.
- Estimation method: **outcome-regression group-time ATT**, without post-treatment covariates.
- Bootstrap: **499**, seed **20260921**.
- Joint pre-treatment Wald diagnostic: **{'W': np.float64(610.858637), 'p_value': np.float64(0.0)}**.

## Simple aggregate output

~~~text
index SimpleAggregation                                                        
                        bootstrap simult. conf. band                           
                    ATT std_error              lower    upper zero_not_in_cband
    0          0.000466  0.251554          -0.350962 0.351894                  
~~~

## Dynamic/event aggregate output

~~~text
relative_period EventAggregation                                                     
                                 bootstrap simult. conf. band                        
                             ATT std_error              lower upper zero_not_in_cband
             -4         0.235033  0.236071                NaN   NaN                  
             -3        -0.113755  0.320899                NaN   NaN                  
             -2        -0.004368  0.221969                NaN   NaN                  
             -1         0.000000       NaN                NaN   NaN                  
              0        -0.192150  0.201662                NaN   NaN                  
              1        -0.053626  0.434704                NaN   NaN                  
              2         0.059607  0.252639                NaN   NaN                  
              3         0.193917  0.194793                NaN   NaN                  
              4        -0.039482  0.395303                NaN   NaN                  
~~~

## Interpretation boundary

- Cohorts contain only one to three treated countries, so country-level inference is intrinsically fragile.
- The common-control universe is deliberately conservative: a country must appear in every frozen event's clean donor pool.
- Cohort timing is the legal effective year and the universal base is T-1. Mid-year transition year T is removed, so post estimates begin at legal event time +1 without contaminating the reference period.
- This estimator does not rescue incompatible pre-trends; the first-outcome placebo diagnostics remain binding evidence.
- Positive/negative affect remain locked.
