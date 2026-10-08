# STAGE2_FREEZE — ARIS4C-006 段2冻结文档（2026-09-30）

> 冻结依据：RESEARCH_BRIEF.md 冻结设计 + stage2_prompt.txt。本 run 0 次 API 查询；
> 数字来自在盘 data/s2_pilot_works.json（前 run 抓取）+ 本地计算 data/s2_analysis.py（结果 data/s2_pilot_results.json）。

## 一、8 冻结项

### F1 样本（主人群）
- OpenAlex authorships 关联至少一个 CN 机构（authorships.institutions.country_code:CN）；
  4 领域 field_id：math=26 / physics=31 / nursing=29 / medicine=27。
- 描述为 China-based scholarly system；不从姓名推断国籍/族裔/公民身份。
- 面板规模（2010–2024 在盘 counts）：math 142,544 / physics 340,328 / nursing 42,464 / medicine 1,610,478（合计 2,135,814 works）。

### F2 时间窗
- 主窗 2010–2024（发表年）；敏感性 2000–2009（子集）；pilot 窗 2019–2024。

### F3 解析阈值（5A–5D）
- 5A 直接汉字：ChineseNames 最长匹配（2 字复姓优先）→ tier1；sort key=姓氏拼音（surnames.py 多音字专音覆盖，其余按字 givenname.csv 拼接、去声调）。
- 5B 罗马化：2 token 且恰 1 token ∈ 姓氏拼音集（1806 姓→391 拼音）→ tier2；双 token 均命中→取 token0（姓前优先，flag both-match）；3 token 先试 2-token 复姓拼音。
- tier3（未命中/仅启发式）不进确证模型。5D 闸：blind 100 条 CN 署名（先取后看），tier1+2 精度 ≥0.90 且姓氏覆盖 ≥50%。
- Pilot 实测（4×100 works，2603 署名，100% 罗马化、0 汉字名）：tier2=2071（覆盖 79.6%），tier3=532，both-match flag=613（占 t2 的 29.6%）。

### F4 暴露估计器（本 run 重算，接入人口频率）
- Obs(work)=1 当且仅当全部署名解析成功（t1/t2）且姓氏拼音键在列出顺序上非降序。
- Exp(work)=h_n(p)：p=familyname.csv n.1930_2008 归一化（1806 姓）；h_n=Σ_{s1≤...≤sn} Π p_{s_i}（DP 计算，n≤64）= 从人口分布随机抽 n 个姓氏恰呈字母序的概率；并列自动调整、随团队规模递减（n=2 约 0.5）。
- 语境 Level C=journal×field×year；cell 有效 n<30 退化 field×year。
- ExcessAlpha(c)=(Obs−Exp)/(1−Exp)；Stage 3 正式暴露用 cross-fitted / leave-one-work-out / lagged（pilot 最大 journal cell LOO 敏感度 max|Δ|=0.093，n=6）。
- **均匀 A–Z 永不是有效零假设**：s3_openalex.py 旧 chance（Πv!/n!）为占位，自本 run 弃用。

### F5 主结果
- Tier 1 ① Y(i,t)=作者 t 年多作者作品中 (pos−1)/(n_auth−1) 的均值（0=第一，1=末位）；② 给定团队构成/语境下 P(first)；③ 通讯作者占比（覆盖 ≥30% 才启用）。

### F6 模型层级
- 主模型（Stage 3 冻结只跑一次）：Y(i,t)=β1·Rank(i)+β2·AlphaExp(i,t−1)+β3·Rank×AlphaExp+controls+FE+ε(i,t)。
- Rank 与 AlphaExp 标准化；FE=领域×年+作者（≥2 年者）；controls=log 姓氏人口份额/团队规模/职业年龄/前期产出 lag。焦点系数=β3。

### F7 排除规则
- 单作者→出估计器+主 Y（留作负对照集）；两作者→出主惯例估计（敏感性保留，§4 已验稳定）；无机构国码→出 CN 面板；tier3 解析→出确证模型；ORCID 优先消歧。

### F8 多重性
- 主检验 1 个（β3，不校正）；Tier 1 次级 3×β3→Holm；8 个负对照只报告；Tier 2 探索性→FDR q=0.1 显式标注。

## 二、Pilot 证据表（详见 data/s2_pilot_results.json §1–§4）
| # | Pilot | 本 run 证据 | 判定 |
|---|-------|------------|------|
| 1 | P1 覆盖 | counts 142,544/340,328/42,464/1,610,478；filter 形态 primary_topic.field.id:<fid> probe OK | PASS |
| 2 | P2 语境变异 | field 级 ExcessAlpha：math +0.162 / physics −0.021 / nursing +0.001 / medicine −0.015；journal×field×year 220 cells（最大 n=6）var=0.173、range 1.948、p50 −0.0002 | PARTIAL（field 级分化清晰；journal 级判定延至 Stage 3 全面板） |
| 3 | P3 解析 | 2603 署名 100% 罗马化；t2 覆盖 79.6%≥50%；both-match 29.6% 已 flag；50 条抽查入 §3 | PASS（5D 正式 blind 闸在 Stage 3） |
| 4 | P4 消歧诊断 | 延至 Stage 3 入口闸（见 §三） | DEFERRED |
| 5 | P5 基线复现 | ChineseNames 23 首字母占比在盘（unknown=0），宿主已复现 | PASS（继承） |
| 6 | P6 稳定性 | 排除两作者：Pearson=0.990，max|Δex| =0.047（n2=35/14/4/5） | PASS |
| 7 | P7 closest prior | 段1 已判（无已组合最近先例） | PASS（继承） |

## 三、P4 消歧诊断 = Stage 3 入口闸
- 执行时机：全面板构建完成后、主模型拟合前（先于任何确证结果）。
- 内容：OpenAlex 作者身份 split/merge 压力测试；检验诊断量（署名名方差、机构/国码冲突率、ORCID 覆盖率）是否与姓氏首字母 Rank 呈强单调相关；ORCID 优先消歧子集复核。
- 失败处置：收窄（限高置信消歧子集）或停止该论文，不硬凑结果。

## 四、Stage 3 面板抽取预算
- 每领域页数=ceil(count/200)：math 713 / physics 1702 / nursing 213 / medicine 8053，合计 10,681 > 5,000 上限。
- 确定性子采样规则：published 升序，每 k=3 页取 1 页（k 显式记录）→ 预估 238+568+71+2685=3,562 查询（≤5,000，余量 ~1,438）。
- 每查询 per-page=200；429 backoff (0,30,60,120,240)；自诊断 filter zzz.gte:1。

## 五、Deviations（本 run）
1. probe 记录 key 'primary_topic.field.id:%s' 为 cosmetic 显示 bug，无数据影响（宿主已验证）。
2. 4×100 样本 raw_author_name 100% 罗马化（0 汉字名）→ 5A 本 run 无样本、5B 为主路径；5A 汉字路径保留供 Stage 3（中文期刊 raw 名）。
3. "团队规模加权" 实现为：per-work chance 依赖团队规模 h_n + 语境层按 work 平均（即团队构成加权）；按 n 加权的变体列为 Stage 3 敏感性分析。
4. 双 token 均命中姓氏拼音（613/2071=29.6%）按 token0=姓处理并 flag（§3）；Stage 3 以 ORCID 关联+跨文献一致性消歧。
5. 工具环境：write_file 工具静默不落盘 → 脚本改经 PowerShell here-string 落盘执行（已记 data/progress_s2fix.txt）。
6. 抓取 sort=publication_year:desc → 4×100 样本偏 2024 最新（pilot 局限，§2 语境构成已体现）。