# IKES 冻结（stage2 · S3）

## 1. 准则定义（1–5 分）
| 准则 | 定义 |
|---|---|
| C1 | 学科殖民史嵌入度：学科起源/核心子领域是否直接根植于殖民经验 |
| C2 | 中心—外围分工：知识生产与材料流动是否呈宗主国—殖民地结构性分工 |
| C3 | 对殖民地数据—材料依赖：学科核心数据/标本/档案/语料的殖民时代来源占比 |
| C4 | 制度路径依赖：学科制度（系所/博物馆/期刊/法域/卫生体系）的殖民遗产连续性 |

## 2. 最终评分表（pass1 = pass2，0 仲裁格）
| 学科 | C1 | C2 | C3 | C4 | 总分 | 集合 |
|---|---|---|---|---|---|---|
| Anthropology | 5 | 5 | 5 | 4 | 19 | 确认 |
| Botany | 5 | 5 | 5 | 4 | 19 | 确认 |
| Law | 5 | 5 | 4 | 5 | 19 | 确认 |
| Mining | 5 | 5 | 4 | 4 | 18 | 确认 |
| Tropical Medicine | 5 | 5 | 4 | 4 | 18 | 确认 |
| Evolutionary Biology | 4 | 4 | 5 | 3 | 16 | 确认 |
| History | 5 | 4 | 3 | 4 | 16 | 确认 |
| Archaeology | 4 | 4 | 4 | 3 | 15 | 确认 |
| Linguistics | 4 | 4 | 4 | 3 | 15 | 确认 |
| Political Science | 4 | 4 | 3 | 4 | 15 | 确认 |
| Philosophy | 3 | 3 | 2 | 3 | 11 | 确认 |
| Engineering | 3 | 4 | 3 | 3 | 13 | 对照 |
| Chemistry | 2 | 3 | 3 | 2 | 10 | 对照 |
| Materials Science | 2 | 3 | 3 | 2 | 10 | 对照 |
| Physics | 2 | 2 | 1 | 2 | 7 | 对照 |
| Computer Science | 1 | 2 | 1 | 2 | 6 | 对照 |
| Mathematics | 1 | 2 | 1 | 2 | 6 | 对照 |

确认集（11 科）均值 16.45，对照集（6 科）均值 8.67，分离清晰。

## 3. 双盲执行记录与仲裁日志
- pass1（Coder A）：编排器主会话，正序打分，`data/ikes/pass1.tsv`（68 格）。
- pass2（Coder B）：**子代理 spawn 两次失败**（内网网关 400 "Unexpected reasoning effort high"，harness/网关参数错配，default 与 reasoning 模型均复现）→ 降级为编排器同上下文第二遍，**输入序反转**（学科倒序 Engineering→History、准则 C4→C1）减锚定，`data/ikes/pass2.tsv`（68 格）。
- 对比（`code/ikes_compare.py`）：68 格 |diff|=0，**0 格触发 |diff|>1 仲裁**，17 科总分两遍完全一致。
- 仲裁日志：空（无仲裁格）。

## 4. 局限声明（强制）
1. Coder B 非独立模型、非独立上下文——双盲弱于真双模型协议，**不得声称"独立 Coder B"**。
2. 68 格 100% 一致是共享上下文的直接后果，不构成真 inter-coder reliability 证据；本表应视为**单模型评分 + 反转序交叉核对**，排序结论的置信度低于真双盲。
3. 4 准则为定性判断，未做评分者校准示例（calibration anchor），存在系统性偏置可能。

## 5. 产物与 provenance
| 文件 | 说明 |
|---|---|
| `data/ikes/pass1.tsv` | Coder A 长格式打分（含 rationale） |
| `data/ikes/pass2.tsv` | Coder B（反转序降级）长格式打分 |
| `data/ikes/ikes_scores.csv` | 冻结长表：discipline/criterion/pass1/pass2/arbitration/final |
| `data/ikes/permutations.tsv` | 100 个总分向量置换（wide，17 列），**seed=20260929**（np.random.default_rng），供段3/4 H2 置换检验 null 分布 |
| `code/ikes_compare.py` / `code/ikes_finalize.py` | diff 仲裁 + 冻结表/置换生成脚本 |
