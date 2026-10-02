# PMID 40830141 语言资产

以下表达从文章的论证结构中抽象而来，不是长段原文复制。页码均为本地出版社 PDF 物理页。

## Section-aware vocabulary and collocations

| 表达 | 适用部分 | 功能 | 来源锚点 | 安全迁移 |
|---|---|---|---|---|
| `retrospective comparative-effectiveness analysis` | Methods/Discussion | 标示治疗比较的真实世界属性 | p1–3、p9–10 | 不可使用 efficacy-equivalence 语言 |
| `time on treatment as a surrogate endpoint` | Methods/Results | 区分 Cohort 2 终点与 PFS | p3、p12 | 必须说明受非进展停药影响 |
| `genomically defined molecular subtype` | Methods/Results | 描述基于关键基因组合的分类 | p3–5 | 若基因是定义条件，不可把亚型关联再次独立归因于该基因 |
| `internally validated transcriptomic classifier` | Results | 准确描述训练/验证均来自同一数据环境 | p4–5 | 不得改写为 externally validated 或 clinical-grade |
| `stable genomic drivers but shifting transcriptomic states` | Results/Discussion | 概括连续取样的小样本观察 | p4–5 | 必须注明仅 9 位患者且可评估对数更少 |
| `hypothesis-generating therapeutic vulnerability` | Discussion | 校准表达型候选靶点 | p6–9 | 不可从表达差异推断药物有效 |

## Synthetic sentence frames

- Results：`No statistically significant OS difference was detected among the three treatment groups; however, the retrospective design and marked group-size imbalance preclude an equivalence claim.`
- Results：`The association of [gene] with survival was observed in Cohort 1 but was not reproduced in Cohort 2.`
- Methods：`Tumors were classified as [subtype] when they met the prespecified genomic rule of [rule], with incompletely profiled cases labeled unknown.`
- Classifier：`The model showed high performance in an internal held-out set, but external and prospective validation remains necessary before clinical use.`
- Biomarker caution：`Conflicting TMB thresholds in the main text should be reconciled before the prevalence or outcome estimates are reused.`

## Paragraph logic

多模态结果段可按：两个队列的治疗结局 → 基因组定义与 unknown 比例 → 转录分类器内部表现 → 连续样本中的稳定/可塑性 → 转录亚型与候选靶点 → 外部验证及因果边界。每一步都应标明其分析集，不把临床、WTS、IF 与数字病理样本混为一体。

STK11 专题段可按三个角色拆开：`STK11` 作为 NSCLC-like 分类条件；Cohort 1 的单基因 OS 关联；Cohort 2 未复制。最后明确没有随机治疗交互证据。这个结构能避免分类定义造成的循环归因。

## Unsafe transfer

- 不要把“OS 无显著差异”写成三种治疗等效。
- 不要把 ToT 当作与 PFS 完全相同的终点。
- 不要将内部验证 SVM 称为外部验证或可直接临床部署。
- 不要把 Cohort 1 的 `STK11` 结果忽略 Cohort 2 阴性后写成已重复验证。
- 不要把基于表达的 FGL1/SPINK1/DLL3 候选写成已证实靶向疗效。
- 不要合并 `≥10 mut/Mb` 与 `>19 mut/Mb` 两个不一致的 TMB-high 定义。

## Indexed language units

- `treatment cohorts → genomic rules and unknown cases → internal classifier performance → longitudinal stability → candidate targets → validation ceiling`
