# SUBJECT_FREEZE — 003 学科集合冻结（段2）

- 冻结日期：2026-09-29；依据：data/probes_stage2.md（段2 探针实测）+ DATA_PROFILE.md §2.4 候选清单
- 纪律：本文件只冻结"学科 ↔ OpenAlex 操作化 filter"映射与层级选择；不含任何 outcome 数值
- 原则：**subfield 优先 > concept > topic**（subfield 是 OpenAlex 分类学层级，稳定且与 topics.subfield.id filter 同构；concept/topic 为弥散标签，仅作无 subfield 学科的锚点或交叉验证）

## 1. 确认性学科集（高 IKES 候选，11 个）

| # | 学科 | 主操作化 filter（段3 面板构建用） | 交叉验证 filter | 验证状态 |
|---|---|---|---|---|
| 1 | History | `topics.subfield.id:https://openalex.org/subfields/1202` | — | subfield 路径段2 已证（3314 同路径） |
| 2 | Political Science | `topics.subfield.id:.../subfields/3320` | subfields/3312（邻接，敏感性用） | 同上 |
| 3 | Law | `topics.subfield.id:.../subfields/3308` | — | 同上 |
| 4 | Philosophy | `topics.subfield.id:.../subfields/1211` | — | 同上 |
| 5 | Linguistics | `topics.subfield.id:.../subfields/1203` \| `.../subfields/3310`（pipe OR，跨 A&H/SS） | — | 同上 |
| 6 | Anthropology | `topics.subfield.id:.../subfields/3314` | — | BR count 33,741（v_sub_anth_topics） |
| 7 | Archaeology | `concepts.id:https://openalex.org/C166957645` | topics T10087/T13372 | BR count 99,665（v_concept_arch） |
| 8 | Evolutionary Biology | `topics.subfield.id:.../subfields/1105`（Ecology, Evolution, Behavior and Systematics） | concepts.id C78458016 | 1105 路径已证 |
| 9 | Botany（段1 缺口→补） | `concepts.id:https://openalex.org/C59822182` | topics T12618/T13015；T12630(非洲)/T14310(拉美) 做区域敏感性 | BR count 149,275（v_concept_botany） |
| 10 | Tropical（段1 缺口→补） | `concepts.id:https://openalex.org/C185032368`（Tropical medicine） | topics T12778 | concepts.id 语法段2 已证 |
| 11 | Mining（补探） | `concepts.id:https://openalex.org/C16674752`（Mining engineering） | topics T11933；C108615695(Coal mining) 敏感性 | 同上；**data mining 系 topic（T10538 等）显式排除** |

## 2. 对照学科集（comparator，6 个，top-level field）

| # | 学科 | filter | 备注 |
|---|---|---|---|
| C1 | Materials Science | `topics.field.id:https://openalex.org/fields/25` | BR=147,719（段1 实测；段2 窗口探针复用） |
| C2 | Computer Science | `topics.field.id:.../fields/17` | 段1 fields.json |
| C3 | Physics and Astronomy | `topics.field.id:.../fields/31` | 同上 |
| C4 | Mathematics | `topics.field.id:.../fields/26` | 同上 |
| C5 | Chemistry | `topics.field.id:.../fields/16` | 同上 |
| C6 | Engineering | `topics.field.id:.../fields/22` | 同上 |

- 对照集选择依据（段1 RESEARCH_BRIEF）：工业化/实验科学主干，殖民期数据依赖弱，作为 H1/H2 的零效应对照。
- 全部 17 个学科（11 确认 + 6 对照）的 filter 字符串在段3 面板构建时统一加 `authorships.countries:XX`（多值 pipe）与窗口 `from_publication_date` 组合。

## 3. crosswalk 规则（段3 执行协议）
1. 每个学科只取**一个主 filter**（上表"主操作化"列）进面板；交叉验证 filter 只进敏感性分析，不进主表。
2. 同键多值一律 pipe `|`（段2 P2 判定）；filter 间 AND 用 comma。
3. 禁止使用 `fields_of_study.subfields.id`（4xx 非法）；禁止 `/fields?search=` 端点发现（行为异常，count=0 假象）。
4. 异名同词排除清单（硬编码进段3 脚本）：mining→排除 data mining 系 topic/concept；tropical→排除 cyclone/climate/forest 系。
5. 每学科拉取前先跑 `per-page=1` count 探针落盘（data/raw/probes/ 幂等），count=0 的学科×国组合记为 MISSING 而非 0 产出。

## 4. 缺口与风险声明
- **无 subfield 的 4 学科**（Archaeology/Evolutionary 用 1105 近似/Botany/Tropical/Mining）以 concept/topic 锚定，标签弥散度高于 subfield 学科；H2 单调性检验对这几科的置信度相应降级，论文须披露该操作化差异。
- Evolutionary Biology 用 subfield 1105（Ecology, Evolution, Behavior and Systematics）为**近似覆盖**（含 ecology 成分），C78458016 为纯度更高的交叉验证。
- Linguistics 跨两个 field（1203+3310）用 pipe OR 合并，存在重复计数可能（同一 work 同时挂两 subfield 时计 1 次——OpenAlex works 级 filter 天然去重，无双重计数风险，仅声明）。
- Tropical 锚定 tropical medicine 后，"热带农业"维度缺失（无对应 concept/topic 命中）——记为覆盖缺口，移入论文 limitations。

## 5. provenance
- ID 清单：data/raw/probes/{s,t,c}_*.json（段2 实测，2026-09-29）+ data/raw/{fields.json,sub_*.json}（段1）
- 复现：code/probe_stage2{,b,c,d}.py（幂等，raw 存在即跳过）+ code/dump_ids.py（ID 汇整）
- 所有 count 为 2026-09-29 时点值
