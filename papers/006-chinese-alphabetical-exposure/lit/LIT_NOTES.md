# LIT NOTES — ARIS4C-006 stage 1（2026-09-29）
只记与冻结设计直接相关的点；完整题录与状态见 `lit/REGISTRY.md`（68 条候选池见 `lit/crossref_raw.json`）。

## D1 字母排序惯例（测量方法可借鉴处）
- cain2016alpha（Physiology News, VERIFIED+doi.org）：对"alphabetical author order"惯例的直接评述；确认部分学科论文**自报**字母序 → 惯例测量可用"名单模式检测 + 论文自报文本"双通道，后者可作独立验证源。
- sysrev_alpha_tab1/2a/2b（系统综述补充条目）：把字母序作为**二分类惯例**按 2009 指南测量论文 prevalence → 本设计将其连续化为 ExcessAlpha=(Obs−Exp)/(1−Exp)（团队规模加权+并列调整+cross-fitted），是其直接加强；二分类测量无法支撑 dose-response 交互，正是本课题的增量点。
- alphord1400（"Alphabetical Order", 1400, Crossref 目录条目）：概念史证据，非实证研究（relevance 1）。
- 借鉴清单：① 名单模式=全部解析姓氏呈字典升序（已实现）；② 显式声明文本证据；③ excess 连续标度；④ 2 作者≈50% 巧合 → 3+ 作者为稳健规范（冻结设计已含）。

## D2 作者位置与职业结果
- schneider2009cocit（Scientometrics）& zhao2008cocit（J Informetr）：first-author vs all-author 共被引——署名位置影响引用积累的既有量化证据 → Tier-1 近端结果"给定团队构成下的第一作者概率"有方法先例可借鉴。
- bornmann2026resp_a/b（Author Response, citation accuracy/noise）：引用噪声会污染署名位置估计 → Tier-2 引用轨迹必须领域×年标准化（冻结设计已含），且"top-10%/1% 占比"比绝对引用数稳健。
- 机制先验支持：署名位置→引用/晋升链条文献支持"近端结果先动、远端更小"的 dose-response 预期；晋升端公开数据稀缺 → Tier-2 以可观测机构转移/职业长度为骨干（冻结 Tier 2 定义已含）。

## D3 implicit egotism（仅作 Non-Goals 背景，用于区分主机制）
- simonsohn2010spurious：早期 name-similarity/implicit egotism 结果部分 spurious（p-hacking/选择偏差）→ 姓名偏好作为主机制的证据本身不稳，**支持**把主机制冻结为制度性暴露而非姓名偏好。
- pelham2020egotism（Encyclopedia 条目）& boyd2008selection：姓名偏好效应集中于**自我选择**场景（城市/配偶/名字选择），与署名排序场景机制不同 → 二者可用同一负对照集区分。
- 区分判据（对应冻结负对照）：若姓氏排序效应在**单作者文献**（无合作者排序通道）或保留姓氏分布的随机化排序中仍存在 → 倾向姓名偏好/声望机制，制度性排序暴露机制被削弱（即冻结证伪判据）。

## D4 中文姓名解析/罗马化/消歧
- pinyin1994a/b（Chinese Primer 附录）& mandarin2006（Modern Mandarin）：拼音罗马化规范与例外清单 → 5B 词典"标准拼音 + 专音例外（单 Shan/解 Xie/仇 Qiu/区 Ou 等）"的结构参照（`data/surnames.py` 已按此组织）。
- yalepinyin2019 & pinyinwade2019（Pinyin vs Yale vs Wade-Giles 对比）：**多罗马化体系并存**是 5B 覆盖缺口的主要来源 → 冻结设计中"有证据支持的遗留/地区罗马化"条目必须逐条注源；5C 置信度分层（Tier-3 启发式排除出确证样本）正是控制此类歧义的闸门。
- 消歧误差：Crossref/OpenAlex 的作者记录是"署名级"非"人级"，split/merge 错误不可避免 → 验收 #4 的消歧压力测试必须检查诊断变量是否与姓氏排序/频率相关（冻结误差审计已含）；本 run 的 CN 主人群限定"机构关联"而非姓名推断，降低族裔误分风险。

## D5 学术劳动力市场姓名偏倚（方法借鉴，机制不同）
- gaddis2017hispanic：名字作为感知/选择工具变量的测量设计（Hispanic 名感知研究）→ 名字"信号值"的量化思路可借鉴，但其机制是招聘端感知，非发表端排序暴露。
- baert2022names：实验名字选择的代表性论证 → 冻结负对照"保留经验姓氏分布的随机化姓氏排序"直接借鉴其分布保持逻辑（避免随机化引入分布失真）。
- derous2024resumes（audit 设计）& duguet2024callback（CRAN 统计包）：审计/简历筛选设计与 discrimination 统计工具 → callback 包可复用于 Tier-1 结果（第一作者概率等）的功效计算。
- 边界声明：D5 文献研究**招聘端**对名字的感知偏倚；本课题研究**发表端**排序惯例的暴露效应——仅方法借鉴，不作机制引用（Non-Goals 一致）。
