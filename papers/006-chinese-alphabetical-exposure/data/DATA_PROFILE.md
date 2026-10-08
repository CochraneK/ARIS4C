# DATA PROFILE — ARIS4C-006 stage 1（快照日期 2026-09-29）
venv python 3.13（C:\Users\SCZ_2207\.workbuddy\binaries\python\versions\3.13.12，即 brief 所指 default venv）；所有外部 API 均带 backoff (0,30,60,120,240)；零 outcome 计算（未跑 β3、未冻结 Stage 2）。

## 0. 环境事件（影响多项 verdict）
- **OpenAlex：共享出口 IP 免费每日预算耗尽** → 429 "Insufficient budget … resets at midnight UTC"（retryAfter≈8483s，2026-09-29 上午实测）。全部 OpenAlex 查询阻塞。
  后台 waiter（`data/s3_waiter.py`，10min 轮询×7h 窗口）已启动：预算恢复即自动执行 `data/s3_openalex.py` 全管线，结果落 `data/feasibility_v2.json`。finisher 的 75min 轮询在写盘时点未取回（FEAS-PENDING）；waiter 窗口在写盘时仍活跃，**Stage 2 前必须复核该文件**。
- Crossref：可用（批量检索秒级；单条 DOI 复核被限流至 ~20-40s/条）。CRAN：可用（秒级）。Semantic Scholar：429。WebSearch(DuckDuckGo) 后端：不可达。

## 1. OpenAlex CN 关联 authorships 覆盖 — verdict: 阻塞（未判）
- 来源 URL: `https://api.openalex.org/works?filter=authorships.country_code:CN,type:article,primary_topic.field.id:<math|medicine>,publication_year:2018-2022&per-page=200&select=id,doi,title,publication_year,authorships,primary_topic`（3 种 filter 变体自动探测: authorships.country_code:CN → authorships.institutions.country_code:CN → institutions.country_code:CN；禁 group_by>per-page 已遵守）
- 计划测量: 有序 authorships / raw_author_name 覆盖 / is_corresponding 覆盖 / 机构国家码覆盖 / CJK raw 名占比。
- 量级: 未取到（429）。局限: 共享 IP 预算, UTC 午夜重置。
- 复跑: `python data\s3_waiter.py`（或预算恢复后直跑 `python data\s3_openalex.py`）。

## 2. ChineseNames 源 — verdict: 部分
- 来源 URL: `https://cran.r-project.org/web/packages/ChineseNames/index.html`（CRAN 包确认存在, **Version 2025.8**, 页面抓取成功 @2026-09-29）。
- 下载: 页面 tarball 为相对链接 `../../../src/contrib/ChineseNames_2025.8.tar.gz`，脚本拼接出非法 URL（idna 编码错误）→ 下载失败未解压。正确 URL: `https://cran.r-project.org/src/contrib/ChineseNames_2025.8.tar.gz`。
- 许可/姓氏人口频率表结构/拼音罗马化字典结构: **未核**（未解压）。复跑: 修复 `data/chinenames_check.py` 的 URL 拼接（strip 前导 `../..`）后重跑，自动解压+打印 DESCRIPTION+计算期望首字母占比（验收标准 5 的离线复现逻辑已实现，回退词典 `data/surnames.py`）。
- 局限: 包内是否同时含频率表+拼音字典待解压确认；若数据仅 .rda，纯 Python 需 pyreadr（未预装, 需 pip）。

## 3. 字母排序估计器试算 — verdict: 阻塞（未判）
- 设计（不冻结参数）: 4 语境（math/physics 高暴露候选 + nursing/medicine 低暴露候选）× 50 篇（2015-2023, CN 关联, type:article, 共 ≤200 篇）；仅统计全部作者均为可解析 CJK 姓名的多作者论文；ObservedAlphaRate / ExpectedChance（团队规模加权, 含并列的 multiset chance = ∏m_i!/n!）/ ExcessAlpha=(Obs−Exp)/(1−Exp)。
- 代码: `data/s3_openalex.py` item3 段（随 OpenAlex 恢复自动执行）。量级: 未取到。局限: 同 #1。

## 4. 姓名解析器可行性（5A/5B）— verdict: 部分（代码就绪, 实测待数据）
- 5A: 最长匹配已实现（`data/surnames.py`, ~170 姓氏 = 单姓 + 24 复姓 + 15 多音字专音[单/解/仇/区/查等]）。在 ≤100 条真实 raw_author_name 上的解析率: 待 OpenAlex 样本（`data/s3_openalex.py` item4 段, 自动执行）。
- 5B 罗马化字典覆盖缺口: 未测（需罗马化姓名样本）；D4 文献提示 Yale/Wade-Giles 遗留变体为主要缺口来源（见 LIT_NOTES D4）。
- 局限: 本次词典为可行性占位，**最终基线必须来自 ChineseNames 冻结源**（冻结设计要求）。

## 5. 作者-年面板规模 — verdict: 阻塞（未判）
- 1 个 count query: 同 #1 filter, `per-page=1&select=id` → meta.count（已写入 `data/s3_openalex.py` filter_discovery 段）。
- 面板行数估计: author-yr rows ≈ works_count × 平均 CN 署名数/work（样本均值法, 代码已实现 item5 段）。量级: 未取到。局限: 同 #1。

## 6. 7 条 pilot 验收标准的段 1 可判性
- #1 OpenAlex 覆盖: 段1 可初判 → 本次**阻塞**（预算）。
- #2 语境间 excess 变异: 段1 可初判（4 语境试算）→ **阻塞**。
- #3 解析器高精度: 段1 仅能做冒烟+解析率；正式精度需预注册验证样本与最低精度/覆盖要求（Stage 2 冻结前完成设计）→ **部分**（代码就绪）。
- #4 消歧诊断与姓氏排序不相关: 需完整面板+压力测试 → 段2。
- #5 ChineseNames 期望首字母占比离线复现: 段1 可判 → **部分**（源确认 v2025.8, 复现未竟, 逻辑已实现）。
- #6 估计器对两作者剔除/歧义名稳定: 段1 可初判（两作者显式建模 + 歧义标记已在代码内）→ **阻塞**（随 #2）。
- #7 未发现最接近先前工作: 段1 可判 → **完成**（REGISTRY closest_prior: 未找到; 限 Crossref 单源, 需双源复核）。
