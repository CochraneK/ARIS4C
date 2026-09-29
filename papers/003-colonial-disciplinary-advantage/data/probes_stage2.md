# PROBE_REPORT_STAGE2 — 段2 便宜探针结果（S1/S2/S5）

- 日期：2026-09-29（段2 executor 死于 21:51 128K 溢出；本报告由编排器接管汇整，数字逐字抄自 data/raw/probes/ raw JSON）
- raw：data/raw/probes/ 42 文件（38 个 .json + 4 个 .err4xx）；可由 code/probe_stage2{,b,c,d}.py 幂等复现
- 纪律：零 outcome——本报告只含 schema 级 count / filter 可达性 / ID 清单，无任何 country×discipline 产出或关联统计量
- 限流政策沿用段1：≥2s 间隔 + backoff(3,6,12,24) + raw 持久化幂等

## S1-P2：同键多值 OR 语义（段1 遗留 UNVERIFIED → 本段判定）

| tag | filter | 结果 |
|---|---|---|
| p2_br | `authorships.countries:BR` | count=3,894,723 |
| p2_us | `authorships.countries:US` | count=32,546,581 |
| p2_br_us_comma | `authorships.countries:BR,US` | 4xx（"A filter value contai..."——逗号被解析为 filter 分隔符，第二段 "US" 非法） |
| p2_br_us_pipe | `authorships.countries:BR\|US` | count=36,209,582 |

**判定：OR 语义（并集去重）。** 36,209,582 ∈ [max(3,894,723; 32,546,581), 3,894,723+32,546,581=36,441,304)；若 AND 则 ≤min=3,894,723，排除。推得 |BR∩US|=36,441,304−36,209,582=231,722（同时有 BR 与 US 署名的 works）。
**工程结论：同键多值一律用 pipe `|`；comma 仅用于 filter 间 AND。**

## S1-D：institution filter 键（D 层前置验证）

| tag | filter | 结果 |
|---|---|---|
| d_inst_cc | `institutions.country_code:BR` | count=3,894,507（**有效**） |
| d_auth_inst_cc | `authorships.institutions.country_code:BR` | count=3,894,507（**有效**，与上行同 count） |
| d_inst_countr | `institutions.countries:BR` | 4xx "institutions.countries is not a valid field" |
| d_primary_inst_cc | `primary_location.institution.country_code:BR` | 4xx "primary_location.institution.country_code is not a valid field" |
| d_inst_name / d_inst_name3 | `authorships.institutions.display_name.search:university` | 匿名 rate limit ×3（**UNVERIFIED**；不影响 D 层——country_code 路径已可用） |

**D 层冻结路径：`authorships.institutions.country_code:XX`**（与 A 层 authorships.countries 同构，可组合）。

## S5：分析窗口候选（BR × fields/25 Materials）

| tag | filter 追加 | count | 保留率 |
|---|---|---|---|
| w_br_mat_all | — | 147,719 | 100% |
| w_br_mat_1990 | `from_publication_date:1990-01-01` | 143,887 | 97.4% |
| w_br_mat_2000 | `from_publication_date:2000-01-01` | 136,212 | 92.2% |

段1 证据：GB×Mat 1900–1919 仅 535 条（OpenAlex 历史深度浅）。两窗口均现实可行；取舍见 DESIGN_LOCKED。

## S2：学科命名缺口复探（fields/25 层 → subfields/topics/concepts 降级）

### 2.1 端点行为备忘
- `/fields?search=<q>`：6 个查询（philosophy/linguistics/political science/law/archaeology/evolutionary biology）全部 count=0——该端点 search 行为不可依赖（段1 已落盘 26 个 top-level fields 于 data/raw/fields.json，以之为准）。
- `/subfields?search=<q>` 与 `/subfields?filter=display_name.search:<q>`：均可用（后者为 s_mining2 验证）。
- `fields_of_study.subfields.id`：**非法 filter 字段**（v_sub_anth_fos 4xx）——works 侧只能走 `topics.*` 与 `concepts.id`。

### 2.2 确认性学科 ID 清单（补缺结果）

| 学科 | subfield | topic | concept | 段2 works 级验证（BR） |
|---|---|---|---|---|
| History | **1202**（段1） | — | — | 路径同 3314 已证 |
| Political Science | **3320** + 3312（sociology 邻接） | — | — | 路径已证 |
| Law | **3308** | — | — | 路径已证 |
| Philosophy | **1211** | — | — | 路径已证 |
| Linguistics | **1203**（A&H）+ 3310（SS，跨域） | — | — | 路径已证 |
| Anthropology | **3314**（段1） | — | — | 33,741（v_sub_anth_topics） |
| Archaeology | 0 命中 | T10087/T13372 | **C166957645** | 99,665（v_concept_arch） |
| Evolutionary Biology | **1105**（Ecology, Evolution, Behavior and Systematics，段1） | — | C78458016 | 1105 路径已证；C78458016 语法同证 |
| Botany（段1 缺口） | 0 命中 | T12618/T13015/T12630(非洲)/T14310(拉美) | **C59822182** | 149,275（v_concept_botany）；T12618=1,185（v_topic_botany） |
| Tropical（段1 缺口） | 0 命中 | T12778（唯一热带医学 topic） | **C185032368**（Tropical medicine） | 语法同证 |
| Mining（补探） | 0 命中（s_mining/s_mining2） | T11933（Mining and Resource Management） | **C16674752**（Mining engineering）/ C108615695（Coal mining） | 语法同证 |

注：`/topics?search=mining` 的 10 条结果中 data mining 系（T10538/T11710/T12016 等）为**异名同词**，必须排除；采矿学科锚点只取 C16674752 + T11933。"tropical" 在 topic 层弥散（cyclone/climate/forest），学科锚点只取 tropical medicine（C185032368 + T12778）。

### 2.3 对照学科（comparator）
26 个 top-level fields 全在 data/raw/fields.json；对照集六个直接可用 `topics.field.id`（段1 已验证 filter 路径）：Materials=fields/25（BR=147,719 段1 实测）、Computer Science=fields/17、Physics and Astronomy=fields/31、Mathematics=fields/26、Chemistry=fields/16、Engineering=fields/22。

### 2.4 works 级有效/无效 filter 路径汇总（段2 实测）
- 有效：`topics.field.id`（段1）、`topics.subfield.id`（v_sub_anth_topics=33,741）、`topics.id`（v_topic_botany=1,185）、`concepts.id`（v_concept_botany=149,275 / v_concept_arch=99,665）、`authorships.countries`（P2）、`authorships.institutions.country_code`（D 层）
- 无效：`institutions.countries`、`primary_location.institution.country_code`、`fields_of_study.subfields.id`（均 4xx）
- UNVERIFIED：`authorships.institutions.display_name.search`（匿名 rate limit ×3；D 层不依赖它）
