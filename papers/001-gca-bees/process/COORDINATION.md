# COORDINATION.md — ARIS4C-001 · 跨会话协调

> 最后更新：2026-09-26 16:07 · 窗口A（段4 双语稿直写收官：EN 7 块 ~245 行 + ZH 7 块镜像 + EN_notes 数字溯源表全落盘；32 条引用逐条核（Crossref 复核补全 8 条 DOI 完整书目）；段5 收官窗口A 认领待启动）。**任何会话在启动新 ARIS 段前必读本文件。**
> 本篇为 017→001 重跑队列第 2 篇（017 已闭环）。沙盒仅 `RESEARCH_BRIEF.md` + 本文件 + `stage1_prompt.txt`。

## 自动驱动体系（2026-09-26 13:23 部署，用户要求全自动跑完 23 篇）
- **常驻看门狗**：`D:\Software\ARIS4C-local\watchdog_loop.ps1`（powershell pid 3460，后台 task xe7t76）——无 aris.exe 时拉起一个驱动器周期（`DRIVER_SPEC.md`，单周期 ≤25min），有 aris.exe 时 5min 轮询跳过；日志 `D:\Software\ARIS4C-local\results\watchdog.log`。
- **驱动器规范**：`D:\Software\ARIS4C-local\DRIVER_SPEC.md`（每周期：读状态→至多 1 个推进动作→落账退出；覆盖启动下一段/128K 接管补完/git 同步/启动下一篇，001→023 严格串行）。
- **看门狗会话死后仍存活**（Windows 孤儿进程，017 已验证 spawn 进程跨会话存活）；机器重启或看门狗进程死亡需人工重启（发「继续」即可，或自建计划任务：`schtasks /Create /F /SC MINUTE /MO 30 /TN "ARIS4C_Driver" /TR "powershell.exe -NoProfile -ExecutionPolicy Bypass -File D:/Software/ARIS4C-local/watchdog.ps1"`，一次型脚本 watchdog.ps1 已备好）。
- 驱动器的认领行会话名=「驱动器」；与人工会话共操时遵循同一认领纪律。

## 当前状态
- **段1（文献抽取 + 数据可行性画像）= 完成（门控已过）**（13:08 启动 → executor 13:33 死于 128K → 编排器接管补写 3 件产物，13:40 收官）
  - 四件产物全落盘且冻结：`lit/REGISTRY.md`（25 条目/32 引用）+ `data/DATA_PROFILE.md`（A=1/B=16/C=8，estimand ①/② 判定，M1–M5 可估性）+ `lit/LIT_NOTES.md`（32 条汇编）+ `stage1_summary.md`
  - 核心结论：estimand ① 走相关级元分析（Finke 2023 核心）；estimand ② 降级方案（Oxman 2026 原始数据 + Perry 2013 组级）；主确认性对比 M1 vs M4
- **段2（指标构建 + 跨任务协方差结构估计）= 完成（接管收官 15:15，门控已过）**
  - run#1（13:56）死于 413（新死因第 1 例，Git Bash 误解析 cmd 风格命令成全盘递归）；run#2（14:29，PID 3800）14:54:16 死于 **128K 溢出（第 5 例，log 3207）**；死前取数 + 统计窗口抽取完成；剩余 3 件交付物由编排器按 aris-128k-takeover 直写补完（第 7 次接管，未重跑 LLM）
  - 六件交付物全落盘：`results/corr_pairs.csv`（16 行）/ `results/s2_meta.json`（M1 vs M4 检验）/ `results/s2_precision.json`（Oxman 三层 precision）/ `data/oxman2026/PROFILE.md` / `results/stage2_results.json` / `stage2_summary.md`
  - **主对比结果**：M4 任务局部零结构**被拒**（RL1–RL2 元分析 r=0.56 [0.32,0.74] p<.001；RL1–NP r=0.277 [0.16,0.38] p<.001；跨研究 简单→逆转 r=0.571 [0.37,0.72] p<.001）；M1 共同因子**部分支持**（方向全正 + 正定行列式 Expt1 0.5915/Expt2 0.4972；RL2–NP 边弱：4/4 单实验 ns、合并 r=0.185 p=.028）→ 层级结构（RL1 强极、RL2 部分）
  - M2/M3 不可估（已记录理由）；M5 两阶段可估（学习侧因子 + Perry 组级 opt-out χ²=25.349 df=10 P=.005）；Finke SI=组级 GLMM 无逐个体数据→维持 B 级
  - Oxman precision（探索性）：信息量追踪强（stage OLS β=0.0894 p<.0001）；个性效应弱/混杂（调整信息量后 liar +25% p=3.2e-05，方向谨慎）；个体差异不支持（56 跟随者 Δ p=0.827，符号检验 p=0.894）
- **段3（试次级决策分析 + 稳健性）= 完成（run#1 15:30 死于 128K 第 6 例 → 窗口A 第 8 次接管收官 15:44，门控已过）**
  - 交付物：`code/s3_trial_model.py`（executor 遗留，修 2 处 statsmodels 新版 API bug 后跑通）+ `code/s3_robust.py`（新写，含 legacy groups= 回退）+ `results/s3_trial_model.json` + `results/s3_robustness.json` + `stage3_summary.md`
  - 试次级主模型（n=536 事件/213 蜂/325 trial）：focal 信息追踪 β=0.0106 [0.008,0.013] p<.001（稳健）；is_liar β=0.2346 [0.126,0.344] p=2.5e-05（稳健，log1p 尺度 +23%）；stage_test p=.207 ns；R2m=.112 R2c=.130
  - 潜 precision 代理：随机斜率 focal Var p=.080 边缘；47 蜂 hi/lo 分层 liar β 0.39 vs 0.18（Welch p=.23 ns；符号检验 hi p=.023；交互 p=.39）→ **仅探索性**；近期代理 recent_mean p=.008（探索性）、trial 位置 ns
  - 稳健性：Finke LOO——RL1-NP 全稳健 / RL1-RL2 稳健 / **RL2-NP 临界（drop_Expt3 后 ns，pooled p=.028 依赖单实验，稿件须如实呈现）**；corr_pairs 复算全 OK；Perry χ² 仅一致性核对（原始计数不在 OA）；未变换 OLS + 剔除单次事件（446 事件，is_liar p=1.1e-04）结论均不变
- **段4（双语稿件 EN+ZH）= 完成（窗口A 直写收官 16:07，未跑 LLM）**
  - 交付物：`paper/paper_EN.md`（7 块：标题+摘要+§1–§8+参考文献 32 条，~245 行）+ `paper/paper_ZH.md`（7 块中文镜像）+ `paper/paper_EN_notes.md`（数字→源 JSON 字段映射 + run provenance）
  - 稿件纪律：全部数字取自段2/3 冻结产物（s2_precision.json / s3_trial_model.json / s3_robustness.json / corr_pairs.csv）；RL2-NP 临界在摘要、§3.1、§5 行3、§7 共 4 处如实呈现；claims policy 逐字落实 §6.3 三条边界；只引冻结 32 条
  - 引用补全：写前 Crossref 复核 8 条书目不全的冻结 DOI（4/14/26–32，补全作者全名/完整题名，如 Hammer & Menzel 1995 实为双作者、Benatar 1995 完整题名、Qu 2023 完整题名）；未新增任何引用
- **段5（收官）= 窗口A 认领，待启动**（paper.json stage5_final + final_FROZEN.txt + git 同步交付物）

## 本篇关键设定（来自 RESEARCH_BRIEF.md，唯一 idea 输入）
- 蜜蜂 *Apis mellifera* 学习/决策个体差异 → 哪个潜变量 + 试次级模型最能解释变异
- 双 estimands：① 跨任务个体协方差（辨别/逆转/负 patterning/opt-out 难度敏感/opt-out 增益/opt-out 迁移）② 试次级 opt-out 决策（客观难度 vs 近期奖惩 vs 潜 precision）
- 确认性模型 M1 单因子 / M2 两相关因子 / M3 两独立因子 / M4 任务局部联结 / M5 混合；探索性 predictive precision 仅当 M1–M5 可估
- Claims policy：只有 M1/M2 被模型比较明确支持才可谈 GCA；元认知/意识须独立证据链；神经推论标假设
- **数据仅公开已发表文献** + 登记表逐条核引用；无 GPU 纯 Python（venv `C:\Users\SCZ_2207\.workbuddy\binaries\python\envs\default\Scripts\python.exe`）；双语终稿 EN+ZH
- **禁读/复用旧仓库 `D:\Software\ARIS4C\papers\001-gca-bees\` 任何 code/data/results**（仅作背景，provenance 必须干净）

## 硬规则（防双跑 / 防网关竞争）
1. **同一时刻只允许 1 个 aris.exe 进程**（单模型网关 172.16.25.104:1026，并发诱发流空闲超时）。
2. 启动新段前必做：
   - `tasklist | grep -i aris` 确认为空；
   - 读本文件确认没有别的会话已认领下一段。
3. 认领后在本文件"认领记录"追加一行（会话/段/时间），完成后再追加完成行。
4. 任务 ID 不跨会话存活——监控一律用**日志落盘 + 进程查询**，勿依赖 TaskOutput。
5. **确定性产物脚本同样要认领**：跑段产物脚本前查认领记录 + `stat -c %y` 看目标产物是否 5 分钟内被别的窗口写过；是则让行或改文件名前缀。

## 128K 管道已验证的死因与修复（启动前必读，017 全量沉淀）
| 死因 | 触发 | 修复 |
|---|---|---|
| 128K 溢出 | thinking/reasoning token 累积；**edit_file 上下文累积**（017 段5b 同款：只读 2 小文件仍爆） | `ARIS_REASONING_EFFORT=low` + `ARIS_TOOL_OUTPUT_LINES=40` + 分块写 |
| stream idle timeout (120s) | 单次大文件写（>120s 无 token） | 分块写 ≤60–80 行/块（heredoc `>>` 追加） |
| bash timeout 毫秒陷阱 | 传 `timeout:60/300` 被当 60ms/300ms | 不传 timeout，必须传则 ≥300000 |
| LLM 流长停（≥600s） | 网关/模型侧 10 分钟无 token；`ARIS_STREAM_RETRY=3` 因已输出部分无法重试 | 600s 旋钮仅延长存活；靠分块小任务缩短单次响应；死亡后据日志落盘重跑（幂等） |
| 流长截断（reason='length'） | 单次输出超 max_tokens，写到一半被截断留残标；日志仍显示 Done | 写代码文件单块 ≤60 行；恢复按残标由编排器补完（**不必重跑 LLM**）；数值产物交叉验证后才可冻结 |
| **接管判定（017 技能 aris-128k-takeover）** | 死亡后剩余量小且源材料装得进编排器上下文 | **编排器直接按冻结 prompt 规格补完，不重跑 LLM**（写/译类段首选） |
| **413 请求体过大（001 段2 run#1 首例）** | 单条 bash 调用被 Git Bash 误解析成盘根全盘递归 find（371 万行进请求体；cmd 风格语法 `cd /d`/`for %f`/`find /c` 是诱因） | bash 禁复合/禁 cmd 语法/禁全盘递归，仅限 python 脚本+ls/wc/head/cat+唯一管道 head；长输出先写盘 |

## 标准启动范式（已验证，017 同款）
```
cd <001夹> && \
  ARIS_REASONING_EFFORT=low ARIS_TOOL_OUTPUT_LINES=40 \
  ARIS_STREAM_IDLE_TIMEOUT_SECS=600 ARIS_STREAM_RETRY=3 \
  "/d/Software/DSH/aris-bin/aris.exe" --permission-mode workspace-write \
  --dangerously-skip-permissions --output-format text prompt "$(cat stageN_prompt.txt)" \
  > results/stageN_run.log 2>&1
```
- env：`ARIS_REASONING_EFFORT=low`+`ARIS_TOOL_OUTPUT_LINES=40` 防 128K；`ARIS_STREAM_IDLE_TIMEOUT_SECS=600`+`ARIS_STREAM_RETRY=3` 流超时备份旋钮（挡不住流长停，靠分块写）。
- run_in_background=true；prompt 已明令：分块写、不传 bash timeout、总调用 ≤25、失败重试 ≤2 次后记录继续、Windows 用脚本文件勿 `python -c` 换行。
- **stdout 必须重定向落盘**（后台任务输出随会话丢失）。

## 分段规划（依据 RESEARCH_BRIEF 流水线）
- **段1**（本段）：文献抽取 + 数据可行性画像（门控：登记表冻结）
- **段2**（待段1 门控）：指标构建 + 跨任务协方差结构估计（M1–M5 可估性确认；若需公开原始数据在此下载+画像）
- **段3**：试次级决策分析（opt-out 回归：客观难度 vs 近期奖惩 vs 潜 precision）+ 稳健性
- **段4**（双语稿件，按 017 经验**评估是否直接编排器写**）：EN 稿 + ZH 稿（只读冻结产物，数字逐项对齐）
- **段5**（编排器收官，无 LLM）：paper.json stage5_final + final_FROZEN.txt + git 同步交付物（排除 .log/npz/>5MB/草稿）

## 认领记录
| 时间 | 会话 | 段 | 事件 |
|---|---|---|---|
| 13:08 | 窗口A（本会话） | 段1启动 | 网关空闲（0 个 aris.exe）；`stage1_prompt.txt` 冻结（OpenAlex 首选 + Crossref 核引用，登记表门控，A/B/C 统计量层级分桶，estimand ①/② 可行性判定，禁读旧仓库）；后台启动段1（task zGtkH5，aris.exe PID 20800，log=`results/stage1_run.log`） |
| 13:10 | 窗口A（本会话） | 段1存活核查 | 进程存活（PID 20800）、日志 22KB 新鲜增长、128K 死亡检查=0；启动初期一次 bash exit 255（路径瞬态报错）已自愈；executor 正做文献检索（Chittka/Dyer/Srinivasan 等），REGISTRY 尚未写盘；继续后台运行，待产物落盘后验收 |
| 13:33 | 窗口A（本会话） | 段1死亡分诊 | aris.exe 退出（task zGtkH5 failed）；log 216KB line 1807 = 128K 溢出（131073>131072，同款第 4 例）；executor 死前 REGISTRY.md 已完整落盘（79 行，日志 diff 截断≠文件截断）+ crossref_check 32 条核完 + M1–M5 判定已出（仅在日志）；缺口=DATA_PROFILE/LIT_NOTES/stage1_summary 三件 |
| 13:40 | 窗口A（本会话） | 段1接管收官 | 按 aris-128k-takeover 技能编排器直接补写（源材料在盘，未重跑 LLM）：DATA_PROFILE.md + LIT_NOTES.md + stage1_summary.md 落盘，四件产物全冻结，门控通过；段2 可启动（prompt 需写入 cmd shell 教训 + 只引冻结 32 条 + P0 取数清单） |
| 13:51 | 驱动器 | 段1接管竞态·让行 | 驱动器周期（13:34–13:51）读 13:33 状态诊断段1死亡（128K 溢出）拟接管；写认领行时回读发现窗口A 已于 13:33–13:43 完成同一接管并收官（三件补写落盘：DATA_PROFILE 44 行 / LIT_NOTES 46 行 / summary 30 行，残标全=0）→ 按认领纪律让行，未写任何产物；驱动器重复行 2 条（13:33:02/13:44）已移除，账本恢复严格时序；交叉验证已做且一致（bees_cand 条目行=67=登记表述；crossref_check 33 行=32 引用+1 标记行，30 OK+2 标记已修正；REGISTRY 残标=0）；下一周期：起草 stage2_prompt（并入窗口A 三点注记：cmd.exe 教训 / 只引冻结 32 条 / P0–P2 取数清单）并启动段2 |
| 13:54 | 窗口A（本会话） | 段2启动 | 网关空闲（0 个 aris.exe，驱动器 13:54:05 退出 exit=0 已确认）；`stage2_prompt.txt` 冻结（P0 取数 Oxman Zenodo 10.5281/zenodo.17771502 + Finke 2023 SI 核实；corr_pairs.csv 指标抽取；主确认性对比 M1 vs M4 按相关模式检验操作化（3 变量时 M1 饱和）；M5 两阶段修改后 estimand；探索性 precision 仅 Oxman 2026；cmd.exe shell 教训；只引冻结 32 条；≤30 调用）；后台启动段2（log=`results/stage2_run.log`）。**段2 已认领，下周期驱动器勿重复启动** |
| 13:59 | 驱动器 | 跳过（幂等） | 步骤0 命中：`_driver_last_run`=13:53:35（距今 156s<30min）→ 记「跳过」直接退出，本周期无推进动作；监控佐证（只读）：aris.exe×2=驱动器自身（PID 12632）+段2 executor（PID 20860，275MB 存活），`stage2_run.log` 增长中（1575B→2768B，mtime 13:57:25，tail 见 executor 正读 5 件冻结文件），128K 死亡检查=0；段2 窗口A 13:54 已认领，驱动器不重复启动；下周期继续分支 A 监控（>25min 无增长才死因分诊） |
| 14:29 | 窗口A（本会话） | 段2 run#1 死亡分诊 + run#2 认领 | run#1（PID 20860，13:56 启动）13:59:41 死于 **413 Payload Too Large**（新死因第 1 例，非 128K）：executor 第 2 个 bash 调用（cmd 风格 `cd /d … && for %f … do @find /c`）被 Git Bash 误解析成 C 盘根全盘递归列表（3718885 行进请求体）→ 网关 413 请求体过大；死于第 3 分钟，**零产物损失**（data/lit/results 无新文件）；v2 prompt 已冻结（413 纪律 + Git Bash shell 模型修正）；run#1 日志已存档 `results/stage2_run1_413.log`；驱动器周期 21756（14:03:03 起）卡死 24min 零落账，看门狗 14:28:03 KILL；网关确认 0 个 aris.exe → **窗口A 立即启动 run#2（log=`results/stage2_run.log`），run#2 已认领，驱动器勿重复启动** |
| 14:38 | 窗口A（本会话） | 段2 run#2 启动验收 | task KWH1Dm；PID 归属确认（看门狗日志 14:29:04 START driver pid=1676 → **驱动器=1676 / executor=3800**，铁律 1 允许的 2 进程组合，驱动器走分支 A 监控不重复启动）；14:31 初验：进程存活 / 日志 965B 增长 / 死亡签名=0；14:38 复查：日志 338KB 健康增长，executor 按纪律分块写 Python（自判 "85 行 → 2 chunks (45+40)"）、主动跳过读 run#1 旧日志（省上下文）；死亡签名 6 命中逐条核过 = 全为 prompt 回显/executor 思考（无真实 413/128K 死亡）；**run#2 继续后台执行，下周期驱动器只做分支 A 监控（>25min 无增长才死因分诊）** |
| 14:55 | 窗口A（本会话） | 段2 run#2 死亡分诊 + 处置认领 | run#2（PID 3800，14:29 启动）14:54:16 死于 **128K 溢出（131073>131072，同款第 5 例**，log 3207）：上下文累积（5 件冻结文件 + 写 fetch/analyze 脚本 + 读 s2_stat_windows.txt 窗口 100+ 行）撑爆；死前已推进显著（code/ 新脚本 + results/s2_stat_windows.txt 等落盘，详见分诊）；Finke 2023 SI 返回 **HTTP 403**（executor 已按 prompt 降级路径处理）；驱动器 1676 被看门狗 14:54:04 KILL（25min 预算）；网关现 0 个 aris.exe → **窗口A 认领段2处置（B-2 接管评估中），驱动器勿动段2** |
| 15:15 | 窗口A（本会话） | 段2接管收官 | 按 aris-128k-takeover 直写补完（未重跑 LLM）：`code/s2_meta.py`+`s2_precision.py`+`s2_finalize.py` 新写并运行 → 六件交付物全落盘（corr_pairs.csv 16 行 / s2_meta.json / s2_precision.json / PROFILE.md / stage2_results.json / stage2_summary.md）；**主对比 M1 vs M4：M4 被拒、M1 部分支持**（层级结构：RL1 强极）；M2/M3 不可估已记录；M5 两阶段 + Oxman precision 完成（个体差异不支持）；Finke SI 判级=B（组级 GLMM 无逐个体数据）；数值全部可追溯（ref_id+文件/表，复算 p 与论文一致）；**段2 门控通过，段3（试次级决策分析+稳健性）为下一段，窗口A 起草中，驱动器勿动** |
| 15:21 | 窗口A（本会话） | 段3启动 | 网关空闲（tasklist 无 aris.exe；驱动器 16908 15:20 预算点退出）；`stage3_prompt.txt` 冻结（试次级混合模型 log1p effort ~ is_liar + focal + stage + (1|ID) + 潜 precision 个体异质性 + 近期奖惩代理；稳健性全套：Finke 留一法 meta / corr_pairs 复算 / Perry χ² 自洽性 / Oxman 变换+样本敏感性；只引冻结 32 条；段2 双死因纪律沿用；≤30 调用）；后台启动段3（log=`results/stage3_run.log`）。**段3 已认领，驱动器勿重复启动** |
| 15:31 | 窗口A（本会话） | 段3 run#1 死亡分诊 + 处置认领 | run#1（executor PID 9356，15:21 启动）15:30:30 死于 **128K 溢出（第 6 例，log 1756-1757：131073>131072）**：读 6 件冻结输入 + 写脚本累积撑爆（与段2 run#2 同款死法）；死前已写完 `code/s3_trial_model.py`（233 行，尾部完整无残标，未运行）；results/ 无 s3 产物 → 剩余=确定性（跑脚本+稳健性+summary）→ **窗口A 按 aris-128k-takeover 接管（第 8 次），驱动器 17232 勿动段3** |
| 15:44 | 窗口A（本会话） | 段3接管收官 + 段4认领 | 第 8 次接管收官（未重跑 LLM）：① executor 遗留 `s3_trial_model.py` 修 2 处 statsmodels 新版 API bug 后跑通（bug1：formula API 的 m.params 含 "ID Var" 随机效应方差参数→只取列名参数；bug2：m.random_effects 是 dict→isinstance 分支）→ `s3_trial_model.json` 完整；② 新写 `s3_robust.py`（~130 行；exclude_single_event 需 legacy `groups=` API 回退——新版 from_formula 报 "'groups' is a required keyword argument"）→ `s3_robustness.json` 完整（fitted=true）；③ `stage3_summary.md` 落盘。**主结果**：n=536/213 蜂/325 trial；is_liar β=0.2346 [0.126,0.344] p=2.5e-05；focal β=0.0106 [0.008,0.013] p<.001；stage p=.207 ns；R2m=.112；precision 调制仅探索性（Welch p=.23/交互 p=.39，符号检验 hi p=.023）；稳健性 RL2-NP 临界（drop_Expt3 后 ns）须如实呈现。**段3 完成；窗口A 认领段4（双语稿直写，不跑 LLM），驱动器见本行勿动段4**。驱动器状态：3460 看门狗存活；17232（15:21:04 起）15:43:59 PowerShell 核对仍存活，看门狗 15:46:04 按 25min 预算 KILL；Bash tasklist 对隐藏会话 aris 进程有假阴性（15:40 误报无 aris），进程核对一律用 PowerShell Get-Process 落盘再读 |
| 16:07 | 窗口A（本会话） | 段4收官 + 段5认领 | 段4 双语稿窗口A 直写收官（未跑 LLM）：`paper/paper_EN.md`（7 块 ~245 行：标题+摘要（2462 字符完整，Read 工具 2000 字符行截断≠文件截断）+§1 引言 5 小节/§2 数据+表1 全 16 行/§3 跨任务协方差（M4 拒绝表+M1 部分支持+M2/M3 不可估+M5 两阶段+段2 三层表）/§4 试次级（表2+随机斜率+47 蜂分层+近期代理）/§5 稳健性表3（RL2-NP 临界行3）/§6 讨论+claims policy 三边界/§7 局限 10 条/§8 provenance+参考文献 32 条）+ `paper/paper_ZH.md`（7 块中文镜像，数字与 EN 逐项一致）+ `paper/paper_EN_notes.md`（数字→源字段映射 + run provenance，含 8 次接管记录）；写前 Crossref 复核 8 条书目不全冻结 DOI（4/14/26–32，未新增引用）。**段5 收官由窗口A 认领（paper.json stage5_final + final_FROZEN.txt + git 同步），驱动器勿动段5** |
