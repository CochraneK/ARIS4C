# DATA_PROFILE — 003 殖民遗产与学科优势（段1 数据可行性画像）

- 冻结日期：2026-09-29（段1 收官；段2 未启动）
- 纪律：本文件**零 outcome 数值**——只记 schema / count 量级 / 可达性 / 候选清单 / 协议草案；H 检验统计量与效应值一律禁止出现在 pre-outcome gate 之前
- provenance：code/supp_search.py + code/fetch_oa.py 可复现；原始 JSON 落盘 lit/raw/、data/raw/（不入库）

## 1. 历史殖民暴露候选（要求 ≥2，本段不下载）

| 候选 | URL | 许可 | 粒度 | 访问状态 |
|---|---|---|---|---|
| COW project（cowcodes 殖民归属编码） | crow.ei.columbia.edu/cow | 公开使用 | country × year（殖民宗主国、独立年份） | 200 可达 |
| OWID colonialism 数据集 | ourworldindata.org（colonialism 条目） | CC BY | country × year（宗主国 + 独立年代） | 200 可达 |
| Easterly (2001) 殖民数据 | Duke/CEPR 页面 | 未注明 | country（宗主国类型 + 年份） | 403 bot 拦截，需人工下载 |
| World Bank WDI（对照变量用） | databank.worldbank.org | 公开 | country × year | 200 可达 |

- 判定：COW + OWID 满足 ≥2 候选；Easterly 作为第三交叉验证源需人工下载（bot 拦截）。
- 约束重申：现代 GDP/R&D/大学规模是历史过程的 **descendant**，不得机械当 baseline 混杂（RESEARCH_BRIEF 推断纪律）。

## 2. A 层：Country × discipline × year（主分析）

### 2.1 已验证 filter 路径与 count（OpenAlex，2026-09-29 实测）
- `authorships.countries:BR` → count = 3,894,723
- `authorships.countries:BR` + `topics.field.id:https://openalex.org/fields/25`（Materials）→ BR×Mat = 147,719
- Materials 全库 = 15,041,804；Mat ≥1990 = 12,906,406
- **GB × Mat 1900–1919 = 535** → OpenAlex 历史深度浅，A 层分析窗口现实约束 **≥1990**
- 参照：`authorships.countries:US` → count = 32,546,581

### 2.2 限流政策（实测后冻结）
- 0.2s 查询间隔 → 503 风暴（首跑 14 条查询仅 12 条 200）
- 冻结政策：**≥2s 间隔 + backoff (3,6,12,24) + 每查询 raw JSON 持久化**（lit/raw/supp_*.json，存在即跳过）→ 幂等重跑 14/14 全 200
- 无 key 限流：10 rps / 每日 10 万 results（官方口径，未压测触顶）

### 2.3 API 语义探针（段2 前必须复验 P2）
- 单维 `group_by` 可用：BR × `topics.field.id` → 5 组；top3：Social Sciences 1,136,328 / Medicine 899,654 / Agricultural & Biological Sciences 555,883
- 双 `&group_by=` **不嵌套**（5 个 test_g 探针文件全为扁平 year 分布）
- **同键多值 OR 语义未验证**：count(BR,US) 两轮均 503（None）→ 段2 首项复探
- 请求预算估算：单国×单学科分页拉取 200/页；BR×Mat≥1990 = 147,719 works ≈ 739 页（重）→ 段2 先冻结主 dyad/主国集再拉全量

### 2.4 学科字段候选与缺口
- 26 个 top-level fields 已探（lit/raw/ 有 raw）；subfield 探针 botany / mining / tropical 等 **0 命中** → 命名缺口，段2 必须 subfield 复探并建 crosswalk
- 高 IKES 候选（确认性学科）：History / Political Science / Law / Philosophy / Linguistics / Anthropology / Archaeology / Evolutionary Biology / Botany（缺口）/ Tropical（缺口）
- 对照学科（comparator）：Materials（fields/25）/ Computer Science / Physics / Mathematics / Chemistry / Engineering

## 3. B 层：Country-pair × discipline × year（主网络）
- OpenAlex **无原生 dyad 端点**；降级路径 = 单国 filter 拉 works + 本地从 authorships 构 co-authorship dyad 边
- 量级：BR×Mat≥1990 = 147,719 works ≈ 739 页 → 重；段2 先定主 dyad 集（建议按暴露类型配对 3–5 对），再评估全量
- 判定：**可建（降级）**
## 4. C 层：Imperial-center × discipline × year（小 N 二级）
- 同 A 层路径（`authorships.countries` + `topics.field.id`），无额外端点依赖
- 小 N 协议：帝国中心取小集合（GB/FR/DE/NL/BE/PT/ES/IT 等，最终以暴露表冻结为准）；推断用**精确推断**（binomial/permutation），不用渐近 p 值
- 判定：**可建（小 N）**

## 5. D 层：University × discipline × ranking year（二级三角）
- institution filter 路径**未探**（段2 必验：`authorships.institutions.id` 或 `primary_location.institution.id`）
- 排名数据可达性（仅记录，未下载）：QS 403（bot 拦截，需人工）/ THE 200 / ARWU 200
- 锚定文献：ARWU 原文 [137]；排名系统跨国差异 [139]；方法批评 [144]；波动性 [147]
- 判定：**可建（二级）**——排名数据永远只做三角验证，不进主分析

## 6. 学科确认性集合 + IKES 双盲编码协议（草案，段2 冻结）
- 候选清单见 §2.4；冻结前须完成：subfield 复探（botany/tropical 缺口）+ field↔discipline crosswalk
- 双盲流程：Coder A / Coder B 两轮独立编码 → 分歧 >1 分触发第三轮仲裁（输入含双方评分与理由）
- **独立性局限（必须声明）**：本 run executor/reviewer 同模型（内网 DeepSeek-Flash-V4-正式版），Coder A/B 为同模型同程序两次独立抽取，双盲弱于真双模型，**不得声称“独立 Coder B”**；论文中须原样披露
- 量表：4 准则 × 1–5 分——(1) 学科殖民史嵌入度 (2) 中心—外围分工 (3) 对殖民地数据/材料的依赖 (4) 制度路径依赖
- provenance：冻结 `ikes_scores.csv` + 编码元数据（prompt 版本 / 模型版本 / 时间戳 / 输入顺序）
- 证伪：随机置换检验（打乱 country×discipline 配对，IKES 均值应回落到置换基线）

## 7. H1–H6 数据支撑判定

| H | 判定 | 说明 |
|---|---|---|
| H1 | 数据可支撑 | `alpha_ct` 固定效应；**变换须在查暴露关联前预选**（log1p 候选，段2 冻结） |
| H2 | 数据可支撑 | 待学科集合冻结 + IKES 编码完成（单调性检验） |
| H3 | 需降级 | 前殖民国家/制度数据缺失（前 1500 机构）→ 降级为“殖民期制度质量”代理，或移入讨论 |
| H4 | 需降级 | dyad 构建重（见 §3）→ 先跑主 dyad 集，全量视预算 |
| H5 | 数据可支撑 | C 层小 N 精确推断（§4） |
| H6 | 数据可支撑 | D 层二级三角；波动敏感性以 [147] 为基准 |

## 8. DESIGN_LOCKED（pre-outcome gate）前剩余输入
1. P2 复探：同键多值 OR 语义（count(BR,US)）
2. D 层 institution filter 探针
3. 学科集合冻结（含 botany/tropical subfield 复探 + crosswalk）
4. IKES 双盲编码完成 + 仲裁 + 冻结
5. 暴露数据下载（COW/OWID 自动；Easterly 人工）
6. H1 变换预选（log1p vs 有界对称）
7. 分析窗口冻结（≥1990 vs ≥2000）
8. 主 dyad 集选择（B 层范围）

## 9. 声明
- 本文件为段1 交付物：仅含 schema、count、可达性、候选清单与协议草案
- 全程**零 outcome 数值**（无任何 country×discipline 产出/影响/协作数值被物化或记录）
- 所有 count 为 2026-09-29 时点值，可由 code/ 脚本复现
