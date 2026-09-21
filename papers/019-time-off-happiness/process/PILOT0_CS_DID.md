# ARIS4C019 · Pilot-0 Callaway–Sant'Anna diagnostic

> Modern staggered-adoption group-time ATT diagnostic using the frozen primary event pool. This remains a Pilot-0 robustness layer, not a manuscript-level causal claim.

- differences version: **0.3.0**.
- Frozen treated countries: **8**.
- Common clean control universe: **66 countries**.
- Panel rows supplied to estimator: **1197**.
- Treatment cohorts (first full-post year -> treated-country count): **{2008: 1, 2010: 1, 2011: 2, 2013: 1, 2017: 1, 2019: 1, 2020: 1}**.
- Control group: **not_yet_treated**.
- Estimation method: **outcome-regression group-time ATT**, without post-treatment covariates.
- Bootstrap: **499**, seed **20260921**.

## Simple aggregate output

~~~text
index SimpleAggregation                                                        
                        bootstrap simult. conf. band                           
                    ATT std_error              lower    upper zero_not_in_cband
    0          0.152199   0.07291           0.013607 0.290791                 *
~~~

## Dynamic/event aggregate output

~~~text
relative_period EventAggregation                                                        
                                 bootstrap simult. conf. band                           
                             ATT std_error              lower    upper zero_not_in_cband
            -12         0.024923  0.057940          -0.118002 0.167847                  
            -11        -0.071201  0.098389          -0.313905 0.171503                  
            -10         0.050167  0.070937          -0.124819 0.225154                  
             -9        -0.071541  0.090664          -0.295190 0.152108                  
             -8         0.052759  0.027994          -0.016297 0.121815                  
             -7         0.067284  0.092919          -0.161927 0.296496                  
             -6        -0.008671  0.177105          -0.445549 0.428208                  
             -5        -0.097404  0.093737          -0.328634 0.133826                  
             -4        -0.586448  0.334261          -1.410998 0.238102                  
             -3         0.225910  0.087473           0.010134 0.441687                 *
             -2         0.032381  0.298135          -0.703054 0.767815                  
             -1         0.036377  0.090159          -0.186026 0.258781                  
              0         0.003525  0.085837          -0.208218 0.215267                  
              1        -0.227326  0.116086          -0.513684 0.059032                  
              2         0.056587  0.368892          -0.853390 0.966565                  
              3         0.140847  0.134930          -0.191997 0.473691                  
              4        -0.061772  0.122381          -0.363660 0.240115                  
              5         0.006101  0.193408          -0.470996 0.483198                  
              6         0.110746  0.123887          -0.194856 0.416348                  
              7         0.135190  0.242737          -0.463589 0.733968                  
              8         0.243309  0.173945          -0.185774 0.672393                  
              9         0.159243  0.080408          -0.039106 0.357591                  
             10         0.610059  0.455432          -0.513392 1.733510                  
             11         0.551939  0.307300          -0.206105 1.309982                  
             12         0.399270  0.457053          -0.728180 1.526721                  
             13         1.009199  0.118453           0.717000 1.301398                 *
~~~

## Interpretation boundary

- Cohorts contain only one or two treated countries, so country-level inference is intrinsically fragile.
- The common-control universe is deliberately conservative: a country must appear in every frozen event's clean donor pool.
- Mid-year legal reform years are removed for treated countries; package cohort timing is first full-post year.
- This estimator does not rescue incompatible pre-trends; the first-outcome placebo diagnostics remain binding evidence.
- Positive/negative affect remain locked.
