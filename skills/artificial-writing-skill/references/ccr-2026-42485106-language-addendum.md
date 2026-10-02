# Post hoc multimodal treatment-effect modeling in TRIDENT

## PMID 42485106

Identity: Skoulidis et al., Utilizing Machine Learning to Identify Multimodal Signatures for Patients Who Would Benefit from the Addition of Tremelimumab to Durvalumab and Chemotherapy (TRIDENT). Clinical Cancer Research. 2026;32(19):4461–4473. DOI 10.1158/1078-0432.CCR-25-3729. The supplied source is a 13-page OnlineFirst-style PDF with SHA-256 4844b3589ded1523689287e2216b87d50240e0ff44a9581c55c6e6972dfdffee.

Date and reading boundary: the supplied PDF states posted first 2026-07-22; a separate publisher/PubMed-facing record reports 2026-08-21. The records are not merged here. The historical main-text read was completed on 2026-09-08. This addendum was created from that reading plus a bounded source check on 2026-10-02; it is not a new exhaustive reread or independent acceptance review. Page numbers are one-based physical PDF pages. Supplementary material was not independently reviewed.

Evidence boundary: TRIDENT is a post hoc heterogeneous-treatment-effect analysis of randomized POSEIDON data. Its modeled contrast is tremelimumab plus durvalumab and chemotherapy versus durvalumab and chemotherapy, not either experimental arm versus chemotherapy alone. STK11 is one of several influential features in a multivariable model, not a standalone interaction estimate, causal mechanism, or externally validated single-gene rule.

Reuse guidance: every unit below is synthetic or conventional, not a quotation. Replace brackets only with verified study-specific evidence. Preserve the treatment contrast, 24-month RMST estimand, modality-specific analysis set, full-set estimate, model-ranked subgroup definition, and absence of external validation. Do not infer individual treatment benefit, treatment safety, or an STK11-specific indication.

### Abstract background

- `Average treatment effects may conceal clinically relevant heterogeneity in the incremental benefit of an added treatment component.` 研究缺口；物理 pp. 1–3。使用 may，且必须明确增量治疗成分及共同背景方案。

### Abstract methods

- `We used post hoc multimodal modeling to rank patients by the estimated survival effect of adding [component] to [shared regimen].` 方法概括；物理 pp. 1–5。estimated effect 为模型输出，不是观测到的个体反事实。

### Abstract results

- `The model-ranked subgroup had a larger estimated treatment effect than the full analysis set, while STK11 was one of several influential genomic features.` 结果概括；物理 pp. 1 and 6–9，Table 1 on p. 6 and Figure 3 on p. 9。不得省略 full-set 比较或把 influential 改为 independently predictive。

### Abstract conclusion

- `The internally validated signature is hypothesis-generating and requires independent external validation before treatment selection.` 限定结论；物理 p. 10。不能把嵌套交叉验证写成外部验证。

### Abstract frames

- `Using [modalities] from a randomized trial, we estimated conditional treatment effects for [explicit contrast] and evaluated model-ranked subgroups within modality-specific analysis sets.` 摘要结构；物理 pp. 1–6。随机化来源不使后验、数据自适应签名成为确证性结论。

### Introduction vocabulary

- `incremental treatment contrast` 增量治疗对比；物理 pp. 1–3。本文为在相同 durvalumab 加化疗背景上增加 tremelimumab。
- `heterogeneous treatment effect` 异质性治疗效应；物理 pp. 2–3。不同于一般预后风险分层。
- `conditional average treatment effect` 条件平均治疗效应；物理 p. 3。本文以 24 个月 RMST 差定义，不等于个体已观测获益。

### Introduction frames

- `A population-average effect may not identify subgroups with different effects under the same treatment contrast.` HTE 动机；物理 pp. 2–3。必须保持同一对比，不得跨用化疗单药对照结果。
- `We examined whether baseline multimodal features could rank patients by the estimated benefit of adding [treatment component].` 研究目的；物理 pp. 2–3。could rank 为模型问题，不预设临床可用性。

### Methods vocabulary

- `24-month restricted-mean-survival-time contrast` CATE 结局尺度；物理 p. 3。不能替换成中位 OS 差或未经说明的生存概率差。
- `super T-learner` HTE 元学习架构；物理 pp. 3–4。属于本文模型方法，不是治疗名称。
- `repeated nested cross-validation` 重复嵌套交叉验证；物理 p. 5。属于内部验证，不能称独立测试。
- `modality-specific analysis set` 模态特异分析集；物理 pp. 5–6。临床、影像、基因组及组合模型的患者数不同。
- `post hoc Bayesian model averaging` 后验模态模型聚合；物理 p. 5。post hoc 在此描述模型聚合步骤，也要与研究总体后验性质区分。
- `permutation-based feature importance` 置换特征重要性；物理 pp. 5 and 8–9。重要性不等同于因果效应或单变量交互。

### Methods frames

- `Conditional treatment effects were defined as the predicted difference in [time horizon] restricted mean survival under the two specified treatment options.` 估计目标；物理 p. 3。需写明两个治疗选项和时间窗。
- `The modeled contrast isolated the addition of [component] to a shared background regimen rather than comparing the experimental combination with chemotherapy alone.` 对比边界；物理 pp. 1–3。不得借用 POSEIDON 的其他随机对比替代 TRIDENT 对比。
- `Feature selection, hyperparameter tuning, and performance evaluation were separated within repeated nested cross-validation.` 内部验证框架；物理 pp. 4–5。不能声称独立外部验证或完全消除过拟合。
- `Each model was evaluated in the patients with all modalities required for that analysis set.` 缺失数据边界；物理 pp. 5–6。跨模型 HR 不宜视为同一患者集上的直接优劣比较。

### Results vocabulary

- `model-ranked top-benefit subgroup` 模型排序高获益亚组；物理 pp. 6 and 8–9。top 50% 或 top 30% 为模型定义阈值，不是已确证临床界值。
- `full-analysis-set effect estimate` 全分析集效应估计；物理 pp. 6–8，Table 1 on p. 6。应与筛选亚组估计并列呈现。
- `modality-dependent attrition` 模态依赖样本缩减；物理 p. 6。不能把 974、652、616、557、526 或 345 当作同一分析分母。
- `multivariable feature-importance ranking` 多变量特征重要性排序；物理 pp. 8–10。STK11 位于多个变量共同构成的模型中。

### Results frames

- `Among the model-ranked top [fraction], the hazard ratio was [estimate], compared with [estimate] in the complete analysis set.` 亚组与全组并列；物理 pp. 6 and 8–9。两估计必须来自对应分析集和同一治疗对比。
- `STK11 was among several influential features in the multivariable model, without a standalone gene-by-treatment interaction estimate.` STK11 安全句式；物理 pp. 8–10，Figure 3 on p. 9。不能写成 STK11 mutation predicts benefit。
- `A performant signature was not identified in the squamous analysis set.` 阴性结果；物理 pp. 8 and 10。不能由样本小直接推断真实无异质性。
- `Adding radiomic features did not improve predictive performance over the clinical-plus-genomic model in the evaluated analysis set.` 模态阴性结果；物理 p. 10。仅限该特征工程、影像条件与分析集。

### Discussion vocabulary

- `data-adaptive treatment-effect subgroup` 数据自适应治疗效应亚组；物理 pp. 8–10。不同于预先设定且确证的生物标志物亚组。
- `internally validated performance estimate` 内部验证性能估计；物理 p. 10。不能简称 validated signature 而省略层级。
- `external-validation gap` 外部验证缺口；物理 p. 10。嵌套交叉验证不能填补该缺口。
- `gene-level mutation encoding` 基因层级突变编码；物理 p. 10。未建模变异亚型和共突变结构。

### Discussion frames

- `Randomization in the source trial does not make a post hoc, data-adaptive signature confirmatory.` 设计边界；物理 pp. 1 and 8–10。用于区分治疗分配随机化与模型发现流程。
- `Feature importance supports multivariable subgroup generation but does not establish a standalone treatment interaction for any single genomic variable.` 解释边界；物理 pp. 8–10。尤其适用于 STK11、KRAS、EGFR、FGFR3 和 CDKN2A。
- `Nested cross-validation provides internal performance estimation rather than evidence of external clinical predictive accuracy.` 验证层级；物理 pp. 5 and 10。保留作者所述 hypothesis-generating 状态。
- `Differences among modality-specific models are difficult to interpret when data availability changes the analysis population.` 跨模型比较限制；物理 pp. 6 and 10。不能把性能差异完全归因于新增模态。

### Conclusion frames

- `The signature warrants independent validation before it is used for patient-level treatment selection.` 最小结论；物理 p. 10。不得推导临床处方规则。
- `STK11 may contribute to a multivariable treatment-effect model without constituting a validated single-gene biomarker.` STK11 定位；物理 pp. 8–10。使用 may 并保留 multivariable。

### Results paragraph

- `Report analysis-set attrition and the explicit treatment contrast; present the full-set effect; quantify the model-ranked subgroup effect; identify multiple influential features without isolating STK11; retain the negative squamous and radiomics findings.` 结果段落逻辑；物理 pp. 6–9，Table 1 and Figure 3。不得选择性只报显著 top-ranked 亚组。

### Discussion paragraph

- `Interpret the model as post hoc HTE exploration; distinguish feature importance from gene-specific interaction; separate nested internal validation from external validation; explain modality-dependent populations and gene-level encoding; end with independent prospective confirmation.` 讨论段落逻辑；物理 pp. 8–10。适用于研究写作校准，不是个体治疗决策模板。
