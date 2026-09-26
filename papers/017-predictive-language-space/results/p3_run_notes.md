# P3 run notes (stage4, orchestrator takeover) — 2026-09-26 06:23 BJT

## 执行方式
- 段4 ARIS executor run 死于 128K 溢出（段3 同款事故）。编排器按 stage4_prompt.txt 冻结规格确定性补完。
- run_p3.py 经 9 轮后台运行：8 次崩溃 + 1 次成功（run#9，1m49s，远快于 30min 预算，**未使用任何降级路径**）。
- 7 处单点修复（均在 run_p3.py 带 `# FIX` 注释）：
  1. C4 `Qi.T @ Qj` → `Qi @ Qj.T`（(Kp,m) 行=code 列=语言，逐组合对语言取均值）
  2. C5 `u` 更新 `R.sum(1)*v` → `R @ v`
  3. C5 `v` 更新 `R @ u2` → `R.T @ u2`
  4. C7 `rate` 二维 (Ki,Kj) → `.ravel()` 对齐 1-D 参照向量
  5. C6 TSNE `n_iter` → `max_iter`（sklearn 1.9.1 已移除 n_iter）
  6. C6 `xh` `.ravel()` → `.reshape(-1, 2)`（保二维供 `.sum(1)`）
  7. seed 循环 `obsm[tr, CPI] & obsm[tr, CPJ]` → `np.ix_` 网格化（双 1-D fancy 索引不可广播）
- 1 处编辑事故：run#6 的 ravel 修复写入错误缩进（8 空格 vs 循环内 12 空格）→ py_compile 拦截，未实际运行（假失败，靠脚本/日志 mtime 对比确诊）。
- 1 处环境事故：matplotlib 字体缓存 `AppData\Local\matplotlib\fontlist-v3.11.0.json` 为 09-08 陈旧文件（无 DejaVu 条目）→ 备份 .bak-20260926 后 `_load_fontmanager(try_read_cache=False)` 重建 + 渲染测试。

## 冻结设计偏差
- C4 "seed 42" 为 no-op：c4_fit 为纯确定性 SVD（30 轮 soft-impute rank3，无随机初始化），seed 参数仅留接口。
- C6 support = 高斯核平均密度（非概率），logloss/brier 为代理指标（soft label clip 后计算）；p3_design.json item3 已注明。
- 其余与 p3_design.json（14 键冻结）完全一致；宇宙冻结值经 probe 硬断言复验：pairs=4000 cells=17053 gaps=32 rare=484 ge50=14726 DEC=1705。

## 结果要点（run#9 stdout 39 行全落盘 p3_run_stdout.log）
- C5 全局收敛 3999/4000（1 对未达 1e-10，按 100 轮截断值计）。
- ④ seed 稳定性触发：C6_manifold（stab 0.103 < 0.5）；C1/C3/C4/C5 均 0.963–1.000。
- ⑤ 稀有标定触发：C6_manifold（sp 0.065 < 0.5）、C7_energy（sp 0.034 < 0.5）。
- 共识集 n=1428，gap_hits=32（32 个真空格全部入共识）；C4 在共识集 rank min/med/max = 1/720/3611（1=最低分）。
- C1/C3/C4/C5 两两 full Spearman 0.972–0.996（高一致）；凡含 C6/C7 的对均 <0.13。
- C7 logloss 0.2700 显著差于其余 ~0.027（brier 0.0603 vs 0.0000）。

## 产物
- results/p3_results.json (5.8KB, 12 键) / p3_results.csv (10.4MB, 187583 数据行 = 11 帧[全局 6 + C4 seed 5] × 17053)
- figures/p3_comparison.png / p3_agreement.png / p3_calibration.png
- results/_w_cache.npz (48.7MB, C3 的 W 矩阵缓存，run#1 建、后续复用)
