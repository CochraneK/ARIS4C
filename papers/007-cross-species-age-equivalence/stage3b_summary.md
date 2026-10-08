# ARIS4C-007 Stage 3b Summary — A5 生存等价（终版）
日期 2026-09-30；本 run=fix2（仅 T6+T7）；T1/T3'/T4'/T5 承接前 run（宿主已核盘）
## 9 物种 tier 与锚点（全 Tier2 两锚点 Gompertz：S(m)=0.5, S(amax)=0.001；amax=anAge 快照）
| 物种 | m(y) | m 区间 | amax(y) | tier/DEV |
|---|---|---|---|---|
| Human | 76.4 | 68.8-84 | 122 | Tier2-dev1（人表 WAF 拦截） |
| Mouse / Mouse  / Wild mouse | 3.0 | 2.7-3.3 | 4 | Tier2-dev2（DEV-2） |
| Cat / Domestic cat | 15.0 | 13.5-16.5 | 30 | Tier2（DEV-3） |
| Chimpanzee | 45.0 | 40-50 | 59 | Tier2（DEV-3） |
| Dog | 13.0 | 11.7-14.3 | 20 | Tier2（DEV-3） |
| Domestic pig | 8.0 | 6-10 | 27 | Tier2（DEV-3/5 农场口径） |
| European rabbit | 8.0 | 7-8.9 | 9 | Tier2（DEV-3/6 m 钳制低于 amax） |
| Horse | 29.0 | 28-30 | 57 | Tier2（DEV-3） |
| Meerkat | 13.0 | 12-14 | 20 | Tier2（DEV-3） |
## 结果：tableC.csv 402 数据行（箱宽 mouse 30 天/其余 1 岁）+ tableC_summary.json 各物种 λ/δ；tableE.csv 324 数据行 = 270（A0-A4）+ 54 A5（9 物种 × 6 分位；method=A5；out_unit=human_eq_years）；幂等：检出前次超时孤儿进程残留 54 A5 行，删除后重算重写；Human sanity max|out_mid−a_years|=0.000 岁（≤1 岁通过，恒等映射）；A5 out_mid 范围检查 bad=0（0-122 岁）
## 偏差清单（host-prior 定案）
DEV-2：鼠无可引用 Gompertz 参数 → 两锚点 Tier2-dev2，不再重试；Human（Tier2-dev1）：SSA/CDC/WHO 全 WAF 拦截（2 run × 3 路 403/FAIL）→ 人表两锚点（m=US LEAB 2021 76.4 岁），不再重试
DEV-3：7 物种（cat/chimp/dog/pig/rabbit/horse/meerkat）m 均 host-prior 中位（圈养优先、留区间）；DEV-5：猪 m 用农场口径 6-10y；DEV-6：兔 m=8.0 贴近 amax=9.0（钳制低于 amax）
## 局限：全物种 Tier2 两锚点 Gompertz（无可引用完整人表/鼠 Gompertz 参数），为真生存曲线近似；人曲线为两锚点合成 period 风格，非真实 life table；圈养中位寿命存在圈养选择偏差
DONE stage3b 007
