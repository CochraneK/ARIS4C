import json
R = json.load(open("data/s2_pilot_results.json", encoding="utf-8"))
print("keys:", sorted(R.keys()))
s1 = R["s1_panel_and_budget"]; print("s1 pages:", s1["pages_count_over_200"], "sum:", s1["sum_pages"], "k3:", s1["est_queries_k3"])
a = R["s2_excess"]["across_contexts"]; print("s2 n_cells:", R["s2_excess"]["n_cells"], "var:", a["var"], "range:", a["range"], "p50:", a["p50"])
s3 = R["s3_parsing"]; print("s3 tier:", s3["tier_dist"], "cov:", s3["t12_coverage_all"], "spot:", len(s3["spot_check_le50"]))
s4 = R["s4_stability"]; print("s4 pearson:", s4["pearson_r_excess_all_vs_ex2"], "maxdelta:", s4["max_abs_delta"])
print("spot[0]:", s3["spot_check_le50"][0])
