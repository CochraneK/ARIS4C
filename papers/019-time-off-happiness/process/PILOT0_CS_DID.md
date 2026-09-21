# ARIS4C019 · Pilot-0 Callaway–Sant'Anna diagnostic

> Modern staggered-adoption group-time ATT diagnostic using the frozen primary event pool. This remains a Pilot-0 robustness layer, not a manuscript-level causal claim.

- differences version: **0.3.0**.
- Frozen treated countries: **8**.
- Common clean control universe: **66 countries**.
- Panel rows supplied to estimator: **1144**.
- Treated observations are hard-trimmed to the frozen legal-year window **T-4 through T+4**; mid-year transition T is excluded.
- Treatment cohorts (first full-post year -> treated-country count): **{2008: 1, 2010: 1, 2011: 2, 2013: 1, 2017: 1, 2019: 1, 2020: 1}**.
- Control group: **not_yet_treated**.
- Estimation method: **outcome-regression group-time ATT**, without post-treatment covariates.
- Bootstrap: **499**, seed **20260921**.

## Simple aggregate output

~~~text
index SimpleAggregation                                                        
                        bootstrap simult. conf. band                           
                    ATT std_error              lower    upper zero_not_in_cband
    0         -0.001163  0.085873          -0.141566 0.139241                  
~~~

## Dynamic/event aggregate output

~~~text
relative_period EventAggregation                                                         
                                 bootstrap simult. conf. band                            
                             ATT std_error              lower     upper zero_not_in_cband
             -4        -1.011815  0.408540          -1.853757 -0.169873                 *
             -3         0.226032  0.089931           0.040698  0.411366                 *
             -2         0.031643  0.294240          -0.574743  0.638028                  
             -1         0.038744  0.086299          -0.139105  0.216593                  
              0         0.005807  0.085551          -0.170502  0.182116                  
              1        -0.219404  0.108052          -0.442085  0.003277                  
              2         0.066435  0.359747          -0.674952  0.807822                  
              3         0.147106  0.127546          -0.115748  0.409960                  
              4        -0.057503  0.130803          -0.327069  0.212063                  
~~~

## Interpretation boundary

- Cohorts contain only one or two treated countries, so country-level inference is intrinsically fragile.
- The common-control universe is deliberately conservative: a country must appear in every frozen event's clean donor pool.
- Mid-year legal reform years are removed for treated countries; package cohort timing is first full-post year.
- This estimator does not rescue incompatible pre-trends; the first-outcome placebo diagnostics remain binding evidence.
- Positive/negative affect remain locked.
