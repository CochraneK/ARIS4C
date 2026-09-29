# stage1_summary — 003 殖民遗产与学科优势（殖民与学科优势的全球地理）

- 状态：**段1 完成**（executor 中途死亡，编排器接管补完；接管过程见 process/COORDINATION.md）
- 日期：2026-09-29；纪律：全程**零 outcome 数值**（country×field 产出/影响/协作矩阵未物化、未记录）

## 本段产物

| 文件 | 内容 | 验收 |
|---|---|---|
| lit/REGISTRY.md | 148 条文献登记表（原检索 50 + 编排器补检 98），逐条 Crossref 核实 | 148 条；VERIFIED 126 / VAM 15 / UNVERIFIED 5 / MISMATCH 2；重复记录 2（[076][111]）已标注 |
| lit/LIT_NOTES.md | ≥中相关性汇编（82 行/去重 81 条），按 ①–⑤ 主题 + 设计含义锚 | 见文件 |
| data/DATA_PROFILE.md | 暴露候选 / A–D 层可行性 / 字段路径+count / 限流政策 / IKES 草案 / H1–H6 判定 / gate 剩余输入 | 91 行，零 outcome |
| code/ | fetch_oa / fix_oa / debug_oa / parse_verify / probe_env / supp_search（6 个 .py，可复现） | 幂等 raw 缓存 |
| process/COORDINATION.md | 重跑账本（死亡→接管→验收→段2 排队） | 见文件 |
| RESEARCH_BRIEF.md | idea 输入（唯一冻结输入，未改动） | — |

## 可行性判定（摘要）

- **A 层**（country×discipline×year，主）：**可建**。filter 路径+count 已验证；窗口现实约束 **≥1990**（GB×Mat 1900–1919 仅 535 works）
- **B 层**（dyad 主网络）：**可建（降级）**——OpenAlex 无原生 dyad 端点，单国拉取+本地构边；BR×Mat≥1990 ≈ 147,719 works（≈739 页）重
- **C 层**（帝国中心小 N）：**可建**（精确推断协议）
- **D 层**（university×ranking year，二级）：**可建**（institution filter 待段2 探针；QS 403 需人工、THE/ARWU 200）
- 暴露数据：COW + OWID 双源可达（满足 ≥2）；Easterly 403 需人工下载

## H1–H6

| H | 判定 | 前置 |
|---|---|---|
| H1 | 数据可支撑 | 变换预选（log1p 候选）；稳健性集 [106]+[109]+[021] |
| H2 | 数据可支撑 | 学科集合冻结 + IKES 编码（含同模型独立性局限声明） |
| H3 | 需降级 | 前殖民数据缺失 → 殖民期制度质量代理 |
| H4 | 需降级 | dyad 重 → 先主 dyad 集（贸易版参照 [028]） |
| H5 | 数据可支撑 | C 层小 N 精确推断 |
| H6 | 数据可支撑 | D 层二级；波动基准 [147] |

## DESIGN_LOCKED 前剩余输入（段2 任务）

1. P2 复探：OpenAlex 同键多值 OR 语义（count(BR,US) 两轮 503 未决）
2. D 层 institution filter 探针
3. 学科集合冻结（botany/tropical subfield 复探 + crosswalk）
4. IKES 双盲编码 + 仲裁 + 冻结（声明同模型局限，不得声称"独立 Coder B"）
5. 暴露数据下载（COW/OWID 自动；Easterly 人工）
6. H1 变换预选；7. 窗口冻结（≥1990 vs ≥2000）；8. 主 dyad 集选择

## 遗留问题 / 已知缺陷

- **P2 OR 语义未验证**（两轮 503）→ 段2 首项
- 字段命名缺口：botany/mining/tropical subfield 0 命中 → 需复探
- [076] Balassa 1965 重复（no_DOI）；[111] Wolfe 2006 与 [001] 重复（dedup 脚本 `list(...)[1:]` 误删首行）——运行已完成不重跑，已在两处标注
- 原检索 50 条中 no_DOI 3（[003][006][037] → UNVERIFIED）+ 年份冲突 2（[025][042] → MISMATCH）——已标注，核心条目均经补检覆盖
- QS 403 bot 拦截 → 人工下载
- executor 死亡：stream reason='length'（128K 硬顶）假 Done；接管补完内容 = 98 条补检 + P1/P2 探针 + 四件交付物

## 给段2的建议（顺序）

1. 便宜探针先行：P2 复探 + D 层 institution probe（各 1 次 API 调用级）
2. 学科集合冻结（subfield 复探 + crosswalk 落盘）
3. IKES 双盲编码 + 仲裁（4 准则 × 1–5，随机置换证伪）
4. 暴露下载与合并（COW/OWID；Easterly 人工位留空）
5. 窗口/dyad 集/H1 变换冻结 → **DESIGN_LOCKED** → 段3 面板构建（OpenAlex 全量拉取 + 本地 dyad）
