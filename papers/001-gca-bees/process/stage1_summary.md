# stage1_summary.md — 段1 收尾摘要（ARIS4C-001）

> 段1 = 文献抽取 + 数据可行性画像（门控：登记表冻结）。**门控已过：REGISTRY 2026-09-26 冻结（25 条目/32 引用）。**
> 完成方式：executor（aris.exe run zGtkH5）完成检索/核引用/REGISTRY 后死于 128K 溢出（13:33，log line 1807）；剩余 3 件写作类产物由编排器按段1 冻结规格接管补写（源材料全部在盘，未重跑 LLM）。

## 产物清单
| 文件 | 状态 |
|---|---|
| `lit/REGISTRY.md` | 冻结（25 条目全字段 + 5 轮检索日志 + 备注；executor 落盘） |
| `data/DATA_PROFILE.md` | 冻结（层级分桶 A=1/B=16/C=8；estimand ①/② 判定；M1–M5 可估性；段2 取数 P0–P3）（编排器接管） |
| `lit/LIT_NOTES.md` | 冻结（32 条一句话汇编；§A 登记表 25 + §B 背景/方法 7）（编排器接管） |
| `results/crossref_check.txt` | 32 条核引用（30 OK + 2 标记已修正）（executor 落盘） |
| `results/bees_cand.txt` / `digest.txt` / `candidates.txt` / `round4.txt` / `round5.txt` / `openalex_raw.json` | 检索中间产物（备查，openalex_raw 415KB 勿整读） |
| `code/fetch_round1–5.py` / `scan.py` / `verify_crossref.py` | 可复用脚本（OpenAlex 多轮检索 + Crossref 核实） |

## 段1 核心结论
1. **公开数据极薄**：A 级仅 1 条（Oxman 2026，Zenodo 10.5281/zenodo.17771502）；B 级 16 条（5 条"可能A"待段2核 SI）；C 级 8 条。
2. **estimand ①（跨任务个体协方差）**：原始数据级不可行 → 走相关级元分析（Finke 2023 核心 + Chandra 2000 + Raine 2012 跨物种）；Finke 2023 SI 若含逐个体数据则升 A 并解锁 M1/M2 完整拟合。
3. **estimand ②（试次级 opt-out）**：完整模型不可行 → 降级方案：Oxman 2026 原始数据（precision）+ Perry 2013 组级辅助。
4. **模型比较**：M4 可估，**主确认性对比 M1 vs M4**；M1/M2（及 M3 同数据需求）完整因子模型不可估；M5 改两阶段（学习个体因子 + block 级 opt-out）记为修改后 estimand；探索性 precision 仅 Oxman 2026。

## 遗留问题 / 段2 必办
- **P0**：下载 Oxman 2026 Zenodo 数据并画像；核实 Finke 2023 SI 是否含逐个体数据。
- **P1**：Perry 2013 OA 全文提取个体/block 比例（C→可能B）。
- **P2**：Raine 2012 / Evans 2017 / Pérez Claudio 2018 SI 核实。
- **引用纪律**：段2 只可引用 REGISTRY/LIT_NOTES 冻结 32 条；新增须补 Crossref 核并追加"段2 增补"小节。

## 教训（供后续段/篇）
- executor 的 "bash" 在本机是 **cmd.exe 语义**（for 循环/`;`/`2>/dev/null`/heredoc 全不可靠）→ 一律写 `.py` 脚本执行 API/数据处理（本段已验证全走通）。
- 128K 第 4 例：检索+核引用+REGISTRY 大文件写盘累积触发；REGISTRY 最后一次工具调用完整落盘（日志 diff 截断≠文件截断）→ 接管前先 `wc -l` + 读全件确认实际落盘量。
