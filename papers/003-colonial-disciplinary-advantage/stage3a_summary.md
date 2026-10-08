# ARIS4C-003 段3a 收官（A 层全量计数 + topup）— 宿主代写 2026-09-30

## 结果
- A 层全量抓取完成：2958/2958 格，fails=0，DONE @ 10:17:50（topup run 收尾）
- A 层 = 174 国 × 17 学科 = 2958 格（from_year=1990）
- v2（per-page=200）为正典；v1（per-page=1）留存对照

## 在盘交付物
- data/panel/a_layer_count.csv — 2959 行（2958+表头）；schema: iso,country,discipline,filter_path,from_year,count,years_json
- data/panel/a_layer_count_v1_20260929.csv — v1 留存（2959 行）
- data/panel/a_layer_drift_report.txt — v1 vs v2 漂移报告
- data/panel/b_smoke.md — B 层冒烟（PT-BR Mining count=58）
- data/raw/panel_a2/ — 2958 个 raw JSON（group_by = 扁平 list {key:年份,count}，1990 起；抽样 8–38 组）
- data/raw/panel_b/ — 2 个冒烟文件（PT__BR__mining__p1/p2.json，3 段命名；derive 脚本自动忽略）

## 漂移（v1 per-page=1 vs v2 per-page=200，meta.count）
- n_compared=2547，max_drift=0.3333（CF Philosophy 3→4，小计数），mean_drift=0.00109
- cells_drift_gt_1pct=65，gt_10pct=3 → 可接受，v2 为正典

## 关键教训（3b 继承）
- group_by 返回组数 ≤ per-page 值：per-page=1 只得 1 个年度组（3a 根因，已按 200 重抓）
- B 层全量抓取 per-page=200（panel_b_full.py 已冻结）

## 配额实证
- 单日 2958 查询无 429 阻断（fails=0）→ 日配额 ≫ 1000（旧假设 1000/天与实证矛盾，以实证为准）

## 移交 3b
- 冻结规格：stage3b_prompt.txt（S1 panel_b_full.py：287 跨境 dyad × 17 学科 = 4879 格 → S2 panel_b_derive.py → S3 收官）
- 脚本：code/panel_b_full.py（91 行，per-page=200，分页至 meta.count，幂等）+ code/panel_b_derive.py（宿主已语法预检，无 2026 不兼容残留）
- 纪律：≤40 调用；启动后 30 分钟轮询；panel_b/ 内 3 段命名旧冒烟文件由 derive 自动忽略
