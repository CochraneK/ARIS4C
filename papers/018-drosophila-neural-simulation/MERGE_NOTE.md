# MERGE_NOTE — 018 双目录合并（2026-09-30）

## 背景

018 在 ARIS4C 曾存在**两个目录**：
- `papers/018-drosophila-open-simulation/`（open，12 文件，concept-scaffold，v0.4.26）
- `papers/018-drosophila-neural-simulation/`（neural，~94 文件，exploration-pilot4，v0.10.0，90% 进度）

open 目录的 paper.json 早已声明 `superseded_by: papers/018-drosophila-neural-simulation`、`portfolio_visible: false`，即 registry 层已指向 neural。
本次合并把 open 的**独有内容**（立宪章程 + 研究计划）正式折叠进 neural。open 目录的**物理删除已暂缓**（见文末「物理删除状态」）——内容层面 018 已收敛为单目录（neural 为正典）。

## 合并决定

**neural 为唯一正典（canonical 018）**，open 目录标记为 superseded（物理删除暂缓，见文末）。
依据：
- dashboard.json 的 "018" 条目已反映 neural 状态（90%，Pilot 4，R2.5 blocked）→ 无需改 registry。
- grep 确认无外部路径引用 open 目录。
- neural 是实质工作载体（~94 文件、Pilots 0-4 PASS），open 仅概念脚手架。

## 从 open 折叠进 neural 的内容

| open 内容 | 去向 | 说明 |
|---|---|---|
| `process/RESEARCH_PLAN.md` | → `neural/process/RESEARCH_PLAN.md` | 创立期 P1–P5 发现阶梯（atlas → 复现 → 耦合可视化 → 问题挖掘 → pilot），作为 neural 的「创始计划」保留 |
| 立宪章程（2 目标：仿真图谱 + 生成研究问题；同步愿景） | → `neural/README.md` 追加 "Founding charter" 小节 | open 的原始定位与目标 |
| `paper.json` 的 superseded_by / 概念定位 | → 本 MERGE_NOTE + neural paper.json 的 `merged_from` 字段 | 溯源留痕 |

open 的 handoff/（AGENT_HANDOFF、CHATLOG、CONTEXT、DECISIONS、README、SESSION_LOG、STATUS、TODO）与 process/STATUS.md 为**过程性脚手架**，无科学内容，不折叠（随 open 目录一并保留在磁盘，标记 superseded）。

## 两处冲突与裁决

| # | 冲突 | open | neural | 裁决 |
|---|---|---|---|---|
| 1 | 题名/定位 | "Open Simulation Atlas"，concept-scaffold，发现驱动综述（2 目标：atlas + 生成问题） | "Open Science & Neural Simulation / Fly Neuro Playground"，embodied simulation + Pilot 门 | **取 neural 定位**（embodied simulation + Pilot gates）；open 的 2 目标作为创始章程保留于 README，不覆盖 neural 现行定位 |
| 2 | 状态/进度 | concept registered，activity=wait，尚无科学结果 | 90%，active，Pilot 4，Pilots 0-4 PASS | **取 neural 状态**（90%/Pilot 4）；open 的 wait 状态作废 |

## 不变量（合并后必须保持）

- 018 在 portfolio 中**只出现一次**（neural 目录）；open 目录 `portfolio_visible: false`，不再作为 018 展示。
- dashboard.json "018" 条目不变（已指向 neural）。
- neural 的科学内容（Pilots 0-4、R2.5 结论）**不因合并改动**——合并只增不减（加 RESEARCH_PLAN + README 章程小节 + paper.json 溯源字段）。
- 重跑铁律：合并属目录/文档整合，不涉及复用旧代码/数据/结果。

## 物理删除状态（重要）

open 目录**当前仍保留在磁盘上**（`papers/018-drosophila-open-simulation/`，12 文件），仅标记为 superseded，**未做物理删除**。原因：

- 本次会话中两次执行 `git rm -r papers/018-drosophila-open-simulation`，**两次均**触发 papers/ 工作树大面积丢失（第一次 2070 文件、第二次 2198 文件），且 `git rm` 进程被 SIGTERM。
- 强相关：删除 open 目录的操作会触发该背景 wipe 事件。
- 依重跑铁律「若再发现 papers/ 大面积 'D'，先 git restore 再报用户，勿 commit 删除」，两次均已 `git restore -- papers/` 恢复，且**未 commit 任何删除**。
- 故物理删除暂缓，待与用户确认处理方式。

open 目录保留不影响 018 的正确性：registry/dashboard 指向 neural，open 的 paper.json 声明 `superseded_by=neural`、`portfolio_visible=false`。

## Provenance

- 合并日期：2026-09-30
- 执行者：小卫（WorkBuddy），用户 Kang 授权（AskUserQuestion 选项 4：018 双目录合并）
- 注：合并执行中两次遇 papers/ 工作树大面积丢失事件（2070 / 2198 文件），均 `git restore -- papers/` 恢复；open 目录物理删除因触发该事件而暂缓。详见 `.workbuddy/memory/2026-09-30.md`。
