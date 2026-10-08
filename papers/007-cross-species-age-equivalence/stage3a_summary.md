# stage3a summary: Translating Time (TT) → tableE A4 行 (007)
## 1. 4 目标物种拟合（rank-OLS，data/tt_fit.csv，宿主验证，未重推）
| species | onset d PC | slope d/rank | r² | domain d PC |
|---|---|---|---|---|
| Human | 0.2200 | 11.5727 | 0.60774 | [19.1, 209.2] |
| Mouse | 7.1300 | 1.0809 | 0.59111 | [7.7, 26.0] |
| Cat | 10.6567 | 3.3270 | 0.78293 | [14.1, 61.7] |
| Rabbit | 8.9233 | 1.4439 | 0.58719 | [9.5, 34.7] |
## 2. 验证与域裁决（冻结结论）
- 180 拟合点中 54 个在发表 95% CI 外（30%）；rank-OLS 是 quasi-Newton 官方模型（r=0.993）的文档化简化，30% 违反属简化预期，如实报告；跨表不一致 = 0。
- 域纠正：13 列共享表 pair1=Rat(9.1–27.4)/Rhesus Macaque(22.9–108.4)，pair2=Mouse(7.7–26.0)/Human(19.1–209.2)；brief 原 "mouse 9.1–27.4 / human 22.9–108.4" 为 Rat/Macaque 域误标（宿主预提取错误），本 run 以 fit 输出为准。
## 3. A4 行（data/tableE.csv = 216 + 54 = 270 数据行）
- 方法：t_pc=a_years×365.25+gestation（tableA 按 species_id join）；r=(t_pc−onset_sp)/slope_sp；t_hum=0.22+11.5727·r；out_mid=t_hum/365.25；CI 用该物种 10 事件 (pc_median,lower95,upper95) 按 pc_median 轴线性插值（端点外线性外推），两端同法映射得 out_low/out_high。
- 4 映射物种（Human, Mouse, European rabbit, Cat / Domestic cat）→ 24 算值行，全部 out_of_domain（in/out：Human 0/6, Mouse 0/6, Cat 0/6, Rabbit 0/6；t_pc 384–44576 d 远超 11 事件发育窗）；input_note="out_of_domain=true; TT 11-event domain [L,U] d PC"。
- 5 未覆盖物种（Chimpanzee, Horse, Domestic pig, Dog, Meerkat）→ 30 行 out_low/out_high/out_mid 留空，input_note="species not in Translating Time 11-event subset"。
- 示例（Human q=0.9）：a_years=110.25 → t_pc=40548.8 d → out_mid=111.0166 y，out_low=102.5524，out_high=119.4808；human 行 ≈ a_years+0.767 y（恒等映射 sanity，与手算一致）。
## 4. 局限
- rank-OLS 为 quasi-Newton 模型简化（54/180=30% CI 违反，见 §2）。
- 全部 24 个 A4 算值行 out_of_domain：取值与 CI 均为自发育窗的线性模型外推，属外推性质。
- Mouse/Cat/Rabbit 末两事件 slope(lower95)>slope(upper95)，远外推致 CI 交叉（out_low>out_high）；为外推已知伪迹而非计算错误，Human 行不受影响。
