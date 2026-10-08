# stage3b summary (004) — 真实 focal pilot CPE + M1-strict + M3 探索 + Gate D

## T1 M1-strict 敏感性（code/sim_m1s.py → m1s_results.csv / m1s_lookahead_log.json）
- 判据：用回退判据。理由：works_index.jsonl 中 concepts 为扁平规范 ID（2 样例 work 验证，无 level/depth 字段），主判据（最深概念层级）不适用。
- 回退判据（预注册）：替代 work 的 year<y、非 focal、与删除 work 共享出现率 ≤30%（≤11290/37636 works）的稀有概念；全图稀有概念 16969 个；seed=20260918。
- 饱和对比（recovery_frac≥0.999 行占比）：原 M1 60/64（93.8%）→ M1s 7/64（10.9%），显著缓解。
- M1s recovery_frac 均值（a=0.25/0.5/0.75/1.0）：0.981/0.981/0.973/0.965；min=0.9236（a=1.0）。
- no-look-ahead：64/64 条 worst_gap=-1（<0），0 条 None（m1s_lookahead_log.json）。

## T2 M3 发现延迟探索（code/sim_m3.py → m3_results.csv / m3_lookahead_log.json）
- 【observed-alternative 标注】delay 为实测非 focal 历史的代理，非 oracle；focal 在场可能加速/改变这些替代，延迟估计有偏（方向不假设）。
- 中位延迟（16 focal 的中位延迟再取中位）：各 a 均 0.00 年；frac_alt_within_5/10/20（focal 中位再取中位）≈ 0.828/0.871/0.898（按 a 范围 0.825–0.831 / 0.858–0.872 / 0.882–0.906）；missing 率（focal 中位再取中位）≈ 0.091（按 a 范围 0.081–0.105）。
- 总 work-concept 对 219142，missing 28629（13.1%）；所用替代 work 年份 1914–2026（log 每条 observed_alternative=true）。
- M3 不并入 CPE 表（延迟语义不同），以 frac_alt_within_* 序列独立报告。

## T3 CPE pilot（code/cpe_pilot.py → cpe_results.csv，768 行 = 4 model × 16 focal × 4 a × 3 metric）
- M0/M2 行为直接图测量（V_cf=V_obs+delta，delta 取自 3a CSV）；M1/M1s 行在 3a 无图级 delta，用线性恢复分解 cpe=(1−recovery_frac)×cpe_M0（显式假设，非完整图反事实，见 limitations）。
- 符号分布（每 model×metric 64 行，cpe 真实符号，neg 全为 0，无符号异常）：M0 deg/lcc/reach 全 64pos。M1 deg/lcc/reach 各 4pos/60zero（共 12 小 pos，幅度为 M0 的 0.2–0.7%，与 M1 饱和一致）。M1s deg/lcc/reach 各 57pos/7zero。M2 deg 64pos；lcc 56pos/8zero；reach 56pos/8zero。
- 实践显著性（|cpe|>5%×V_obs，独立 significant 列）：M0 deg 64/64、lcc 2/64、reach 15/64；M1 0/192；M1s deg 7/64、lcc 0/64、reach 5/64；M2 deg 64/64、lcc 0/64、reach 11/64。
- 单调性（focal 内 CPE 随 a 不减，相邻 a 对严格递减记违反）：M0/M1/M2 各 0；M1s deg/lcc/reach = 4/1/1，共 6/144 对，可解释为 (1−r) 随 a 非单调微变。
- M0 a=1.0 规模：deg mean 859.6（104–6796）；lcc mean 755.2（71–5338）；reach mean 25311.5（71–30717）。

## T4 Gate D 判定（§22 检查单）
- (1) M0+M1 实现：PASS — 3a 产物在盘（m0_results.csv、m1_results.csv、sim_m0.py、sim_m1.py）。
- (2) bounded M2：PASS — 3a 产物在盘（m2_results.csv、m2_lookahead_log.json）。
- (3) 恢复行为测试：PASS — 3a 合成基准 4 断言全 PASS（36/36、24/24、81/81、no-look-ahead canary PASS）+ 本段真实 pilot：M1s 饱和 93.8%→10.9% 显著缓解；CPE 单调违反仅 6/144 且可解释；无符号异常。
- (4) 无 look-ahead：PASS — 3a lookahead_audit.json verdict=PASS；本段 m1s 64/64 条 worst_gap<0、m3 log 全部 observed_alternative=true。
- 总判定：Gate D PASS。备注：M1 族判别力弱（M1 CPE 幅度≤0.7%×M0；M1s 幅度 0.1%–7.6%×M0），主分析应依赖 M0/M2/M3 族，M1 族作敏感性参照——如实声明，不静默。

## limitations
- M3 为 observed-alternative 代理：focal 在场可能使延迟估计有偏（方向不假设），非 oracle。
- 3a 合成基准三网络结果完全相同（star-local 指标只依赖局部结构），3a 已记录，本段未重做。
- betweenness 为 k=200 近似（仅用于 focal 选择/分层，未重算）。
- M1/M1s 的 CPE 行为线性恢复分解估计，非完整图反事实模拟。

## 2026-10-08 宿主侧验收修正（2 处，其余数字复核无误）
- sign 列 bug：cpe_pilot.py 原 sign_of 以 |cpe|≤5%×V_obs 判 'zero'，把实践显著性混入 CPE 符号（383/768 行与 cpe 真实符号不符）。已修：sign=cpe 严格符号，阈值移入独立 significant 列；cpe_results.csv 已重生成（宿主侧 fix run，log: results/stage3b_fix_cpe_rerun.log）。原 T3 符号分布行照抄了该错误列，已替换为真实符号 + 实践显著性两行。
- T2 行 frac_alt/missing 范围（0.819–0.824 等、0.100–0.114）无法从 m3_results.csv 复现，已替换为经核数值（focal 中位再取中位 + 按 a 范围）。
- 本 summary 其余数字均经宿主侧独立复核与盘上文件一致：m1s 饱和 7/64、均值、min=0.9236；m3 总对 219142/missing 28629（13.06%）且 n_used 190513+28629=219142 交叉验证一致；单调违反 6/144；M0 a=1.0 规模；m1s log 64/64 worst_gap=-1；m3 log 16/16 observed_alternative=true、年份 1914–2026。

DONE stage3b 004
