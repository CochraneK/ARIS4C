# stage3a summary (004, fix run: 仅补 T5/T6/真实 summary)
主 run 已完成 T0–T4，产物在盘未动；本 fix run 仅执行 T5 合成基准、T6 no-look-ahead 审计与真实 summary。所有数字均溯源至 data/stage3/ 下在盘文件。

## T1 图清单 (graph_manifest.json)
- n_authors=31733, n_active=164, n_coauth_edges=848052, n_works=37636, n_concepts=50, n_ac_edges=6380, integrity=OK
- betweenness: k=200, seed=42 (betweenness_full.json，未重算)

## M0 naive deletion (m0_results.csv, 16 focal × 4 a = 64 行)
- 示例 Clayton (physics, A5000945647, t0=1924, a=0.25): n_works_deleted=143, deg_delta=-368, lcc_delta=-108, reach_delta=-108, affected_nodes=108

## M1 observed alt-path recovery (m1_results.csv) — LIMITATION
- 饱和: 60/64 行 recovery_frac≥0.999 (min=0.993, mean=1.000)；top-50 concept ≥1 共享判据过松，M1 近似恒恢复
- 如实记为 limitation；判据收紧留给段3b，本 run 未修改 M1

## M2 bounded dynamic reconnection (m2_results.csv)
- 保守重连: n_replaced min=0, max=930, mean=101.4；deg_delta 与 M0 逐行相同 (64/64)——替换不恢复 focal 自身度，只恢复连通

## T5 synthetic star-loss benchmark (benchmark_results.csv, benchmark_report.md)
- 3 网络 (er / sbm / star_er，各嵌 200 度 star hub, t0=1980, seed=20260918)，与真实数据同一 simcore_3 代码路径
- (a) M0 降幅最大: PASS 36/36 (M2 在 deg 上 12/36 检查与 M0 并列，设计使然)
- (b) M1/M2 部分恢复 (总降幅严格 < M0): PASS 24/24
- (c) 降幅随 a 单调不减: PASS 81/81
- (d) no-look-ahead canary: PASS (M2 full/pre 视图 12/12 决策一致; M1 受限视图 144/144 一致)
- 关键数 (a=1.0 M0): 三网络均 deg=-200, lcc=-600, reach=-600；M1 n_recoverable=n_deleted (200/200，与真实数据 60/64 饱和一致)

## T6 no-look-ahead audit (lookahead_audit.json)
- verdict: PASS。静态证据行号: simcore_3.py L4-5, 92-94, 117, 120; sim_m1.py L5, 29, 33, 44; sim_m2.py L7, 47, 68
- 运行时: m1 64/64 条 worst_gap<0 (全为 -1); m2 64/64 条 max_year_used≤t0 (取值 1863–1938)

DONE stage3a 004
