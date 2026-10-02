# PMID 40830141 精读记录

## 状态与来源边界

- 精读阶段：主文初次完整精读完成；尚未通过独立二次验收。
- 来源：15 个物理页的 Nature Communications 出版社开放获取版本；Table 1、Figures 1–6、全部主面板和图注均逐页视觉核验。
- 补充材料：本地未提供；Supplementary Figures/Data 中的更细治疗、基因和验证分析不能声称已精读。
- 内部一致性警告：Results/Figure 2 语境把 TMB-high 写作 `≥10 mut/Mb`，Methods 及部分治疗结果文字使用 `>19 mut/Mb`（低组相应 `≤19`）。两种阈值不可合并，正式引用前须回查分析数据/补充材料或作者勘误。

## 研究问题

肺大细胞神经内分泌癌（LCNEC）的真实世界一线化疗、化疗联合免疫治疗和免疫单药结局如何；基因组与转录组能否把 LCNEC 分成 SCLC-like 与 NSCLC-like 亚型；这些亚型及 `STK11` 等驱动改变是否与治疗结局或可靶向生物学脆弱性相关？

## 设计、研究对象与分析集

- 两个独立回顾性队列，合计 `n=590`。
  - Cohort 1：26 个机构，2014 年 1 月至 2023 年 12 月，接受一线系统治疗的 LCNEC `n=217`。
  - Cohort 2：Caris Life Sciences，2015 年 1 月至 2023 年 11 月，分子谱 LCNEC `n=373`；有一线治疗资料的子集 `n=146`。
- 病理：Cohort 1 由各中心本地病理判定，无统一中央复核；Cohort 2 有 `n=142` 子集中央复核，诊断一致率 94.3%。混合组织学排除。
- 治疗组：chemotherapy、chemoimmunotherapy、immunotherapy。Cohort 1 为 121、82、14；Cohort 2 治疗子集为 46、88、12。
- 分子平台：Cohort 1 使用不同机构 panel；Cohort 2 为 592-gene targeted sequencing `n=84` 或 WES `n=289`，并对全部 `n=373` 做 WTS。
- 基因组亚型定义：
  - SCLC-like：`TP53` 与 `RB1` 并发变异。
  - NSCLC-like：`RB1` 野生型且 `STK11`、`KRAS` 或 `KEAP1` 任一变异。
  - 不满足者为 unclassified；Cohort 1 若关键基因 panel 不完整则为 unknown。
- 模型/其他分析：OS、Cohort 1 rwPFS；Cohort 2 以 time on treatment（ToT）替代 PFS。Cox 调整性别、ECOG、年龄和 M 分期。另行训练 SVM 转录组分类器、分析连续样本、开展 GSEA、数字病理 TIL 估算及极小样本 FGL1 免疫荧光。
- 统计：未预先确定样本量；多项分子和转录组比较，需注意探索性与多重性。

## 覆盖记录（按 PDF 物理页）

| 物理页 | 已核验内容 |
|---:|---|
| 1 | 题名、摘要、Introduction 起始、文章/DOI/日期信息 |
| 2 | Results 队列特征；Table 1 全表和脚注；一线 OS 结果起始 |
| 3 | Figure 1 全面板/图注；OS、rwPFS、ToT 与毒性；分子亚型定义起始 |
| 4 | Figure 2 全面板/图注；基因组谱、可靶向事件、序列样本；SVM 方法起始 |
| 5 | Figure 3 全面板/图注；SVM 表现、再分类、TMB/PD-L1、基因生存关联、转录亚型起始 |
| 6–7 | Figure 4 全面板与跨页图注；ASCL1/YAP1、DLL3、FGL1/SPINK1；Discussion 起始 |
| 8–9 | Figure 5 全面板/图注；TIL、FGL1/SPINK1 证据；Figure 6 与拟议转化框架；局限 |
| 10–12 | 结论与 Methods：队列、测序、RNA、IHC/IF、数字病理、TMB/MSI、统计；TMB 阈值冲突位置 |
| 12–14 | 数据可用性、报告摘要、参考文献、作者贡献、利益冲突 |
| 15 | 补充材料链接、开放许可、作者/机构信息 |

## 临床治疗结果

- OS 在两队列的三类治疗间均无显著差异：
  - Cohort 1：chemotherapy 15.0 月、chemoimmunotherapy 12.0 月、immunotherapy 13.6 月，`p=0.71`。
  - Cohort 2：14.9、17.6、21.7 月，`p=0.38`。
- Cohort 1 rwPFS（可评估 `n=216`）：5.1、5.4、3.9 月。相对 chemoimmunotherapy，chemotherapy 调整后 HR `1.43 (1.04–1.99)`，`p=0.03`；immunotherapy HR 约 `1.3 (0.69–2.58)`。前两组中位数仅差 0.3 月，作者亦认为临床意义有限。
- Cohort 2 没有 rwPFS，ToT 为 2.4、7.5、6.3 月；chemotherapy 相对 chemoimmunotherapy HR `1.44`，`p=0.05`。ToT 同时受毒性、医生/患者选择和进展外停药影响，不能视作等价 PFS。
- Cohort 1 任意级治疗相关不良事件 52%；≥3 级为 chemotherapy 22%、chemoimmunotherapy 26%、immunotherapy 0%。免疫单药仅 `n=14`，0% 不能证明更安全。
- 治疗组比较为观察性且组间极不平衡；“OS 无显著差异”不证明三种策略等效。

## 基因组亚型与 STK11

- Cohort 1 只有 `n=85` 具备足够基因数据：NSCLC-like `25 (29%)`、SCLC-like `19 (22%)`、unclassified `41 (48%)`；另 `n=132` 因关键基因检测不全而 unknown。
- Cohort 2：NSCLC-like `89 (23.9%)`、SCLC-like `136 (36.5%)`、unclassified `148 (39.7%)`。
- Cohort 2 可靶向改变合计写为 `22/373 (5.9%)`：列举 `KRAS G12C 13`、`EGFR 5`、`ERBB2 1`、`EML4::ALK 3`、`ETV6::NTRK2 1`。列举计数相加为 23，可能存在同一肿瘤重叠或主文计数不一致；未经补充数据不能自行消解。
- 高 TMB：Results 按 `≥10 mut/Mb` 报告 NSCLC-like `56.3% (49)`、SCLC-like `49.6% (67)`；但 Methods 另定义 `>19 mut/Mb`，需保持警告。
- 一线治疗的 rwPFS/OS 在 NSCLC-like、SCLC-like、unclassified 之间无显著差异。
- Cohort 1 中 `TP53` 或 `STK11` 变异与较差 OS 相关；Cohort 2 中包括 `STK11` 在内的已评估基因均未与 OS 显著相关。因此 `STK11` 生存信号没有在独立队列复制。
- `STK11` 同时被用于定义 NSCLC-like 亚型，故以该亚型作暴露的分析具有部分构造性/循环性；不能再把亚型差异独立归因于 `STK11`。

## 转录组分类与时间动态

- SVM 用 `2168` 个转录特征区分基因组标记的 NSCLC-like 与 SCLC-like。标记病例 `n=174` 中 80% 训练、`n=44` 验证；AUC `0.98`，准确率 `90.1%`。
- 对 `143` 个原 unclassified 肿瘤再分类：`101 (70.6%)` 为 SCLC-like，`42 (29.4%)` 为 NSCLC-like；UMAP 与预测标签呈聚类一致。
- 这是内部拆分验证，且特征选择/模型均来自同一数据环境；未进行独立外部或前瞻性验证，不能直接用于临床分类。
- 9 位患者有两个时间点样本：基因驱动总体保持，但 Cohort 2 可评估的 5 对中 4 对转录亚型发生变化。小样本提示“基因较稳定、转录状态更可塑”，不提供转变率的稳定估计。

## 转录亚型与候选靶点

- 合并 WTS 比较包括 SCLC `n=1643` 与 LCNEC `n=361`。ASCL1 在 SCLC-like LCNEC 更常见；YAP1 在各 LCNEC 组均存在。
- Figure 4 中 `STK11`/`KEAP1` 的“富集”比较是 SCLC-like LCNEC 相对于经典 SCLC，而不是证明其相对于 NSCLC-like LCNEC 更高；必须明确比较对象。
- SCLC 与 SCLC-like LCNEC 的 DLL3 表达高于 unclassified LCNEC；该结果支持进一步靶点研究，不等于药物疗效。
- NSCLC-like 相对 SCLC-like 的差异表达筛得 1061 个基因（名义 `p<0.05`、fold change >2），`FGL1` 与 `SPINK1` 富集，并在既往 75 例 LCNEC 数据集中作表达层面复现。
- FGL1 免疫荧光样本极小：NSCLC-like LCNEC 1/2、SCLC-like 0/1、NSCLC 3/3、SCLC 0/4 阳性，只能作为可行性/假设生成证据。
- 数字病理 TIL：LCNEC `n=16`，较 LUAD `n=353`、LUSC `n=63`、SCLC `n=122` 低；LCNEC 亚型仅 6/4/6，无法作稳定亚型比较。

## STK11 在本文中的角色

`STK11` 有三个不同角色，必须分开：第一，它与 `KRAS`/`KEAP1` 一起构成研究者定义 NSCLC-like LCNEC 的条件之一；第二，Cohort 1 单基因分析显示其与较差 OS 相关；第三，这一生存关联在 Cohort 2 未复制。故本文对 STK11 的最强贡献是分类框架和候选分子背景，而不是经过独立验证的预后或治疗预测标志物。

## 局限、偏倚与主张上限

- 回顾性治疗比较、组别极不平衡，治疗时点与方案选择受临床因素影响；不能由 OS 无显著差异得出方案等效。
- Cohort 1 无中央病理复核且平台异质；Cohort 2 虽有子集复核，仍不是所有病例。
- Cohort 1 大量病例因检测不全为 unknown，可能造成分子亚型选择偏倚。
- Cohort 2 用 ToT 代替 PFS，终点含义不同，两个队列不能直接合并。
- TMB 阈值在主文内部不一致；未经解析不得复用为统一 cutoff。
- SVM 是内部验证，且临床结局未因再分类显著分开；不可宣称临床效用已验证。
- `STK11` 单基因 OS 信号仅在 Cohort 1，Cohort 2 阴性；不能表述为稳健预后结论，更没有治疗交互证据。
- FGL1/SPINK1/DLL3 是表达与可成药性假设，不是疗效证据；FGL1 IF 与 LCNEC TIL 子集尤其小。
- 补充材料未提供，限制对基线平衡、模型全变量、所有敏感性和外部数据复现细节的核验。

## 可安全引用的结论

这项双队列回顾性研究描绘了 LCNEC 的治疗结局和基因—转录异质性，并提出经内部验证的转录分类及 FGL1、SPINK1、DLL3 候选靶点。`STK11` 是 NSCLC-like 定义的一部分，且仅在 Cohort 1 与较差 OS 相关、在 Cohort 2 未复制；因此不能据本文把 `STK11` 视为已验证的 LCNEC 预后或免疫治疗预测标志物。
