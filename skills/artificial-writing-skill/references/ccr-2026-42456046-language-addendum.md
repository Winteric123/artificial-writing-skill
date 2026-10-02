# Intratumoral immune heterogeneity and combined KEAP1/STK11 context

## PMID 42456046

Identity: Cipriani et al., Intratumoral Immune Heterogeneity Drives Divergent Outcomes to PD-(L)1 Blockade in Lung Cancer. Clinical Cancer Research. 2026;32(19):4396–4410. DOI 10.1158/1078-0432.CCR-26-1466. The supplied source is a 44-page publisher-hosted, line-numbered manuscript PDF with SHA-256 c795f9d233acd688cca4a87407fe7a0a2c8e863c69b8c9833d696982ced28855.

Reading boundary: the historical main-text read was completed on 2026-09-08. This addendum was created from the existing reading record plus a bounded source check on 2026-10-02; it does not constitute a new exhaustive reread or an independent acceptance review. Page numbers are one-based physical PDF pages. Separate supplementary material was not reviewed.

Evidence boundary: the paper derives a single-sample ITIH classifier from multiregion RNA sequencing and relates inferred states to survival in ICI-treated cohorts. The KEAP1/STK11 analysis uses a combined mutation-positive group and cannot establish an STK11-specific effect. Replication among treated cohorts supports outcome stratification, not treatment prediction without a comparator interaction. Digital pathology is orthogonal support but not an independent multiregion ground-truth validation set.

Reuse guidance: every language unit below is synthetic or conventional, not a quotation. Replace brackets only with verified study-specific evidence. Preserve the analysis set, endpoint, treatment context, uncertainty, and gene-combined boundary. Do not use these frames to claim that Hom-IE overcomes STK11, that ITIH selects therapy, or that the classifier has prospective clinical utility.

### Abstract background

- `Existing biomarkers incompletely capture spatially discordant immune states within the same tumor.` 背景缺口；物理 pp. 7 and 9。用于提出空间异质性问题，不把单次活检误写为已证实无效。

### Abstract methods

- `We trained a single-sample classifier against multiregion immune states and evaluated it using orthogonal pathology readouts and independent treated cohorts.` 设计概括；物理 pp. 7 and 10–13。这里的独立仅指临床队列，不表示存在独立多区域真值队列。

### Abstract results

- `The inferred immune state stratified overall survival across treated cohorts, whereas the combined KEAP1/STK11 group retained an adverse association within the favorable immune stratum.` 结果层级；物理 pp. 7–8 and 20–23，Figures 4–6 on pp. 42–44。必须保留 combined，不能拆成 STK11 单基因结论。

### Abstract conclusion

- `Single-sample immune-state inference may add resolution to established biomarkers, but treatment-selection utility requires comparative and prospective validation.` 有限结论；物理 pp. 24–27。前半句为关联性分层，后半句限制临床用途。

### Abstract frames

- `We derived [classifier] from [multiregion reference cohort], assessed [orthogonal evidence], and examined associations with [endpoint] across [treated cohorts].` 摘要结构；物理 pp. 7–8。不得把 examined associations 改为 predicted benefit，除非有适当比较组和交互分析。

### Introduction vocabulary

- `intratumoral immune heterogeneity` 核心概念；物理 pp. 7 and 9–10。需说明其操作定义基于同一肿瘤内免疫富集与免疫耗竭区域共存。
- `spatially discordant immune states` 空间不一致免疫状态；物理 pp. 9–10。不能替代遗传异质性或时间异质性。
- `partial representation of immune contexture` 现有标志物覆盖不完整；物理 p. 9。用于说明信息不足，不等同于证明 PD-L1 或 TMB 无预测价值。

### Introduction frames

- `A single tumor sample may not represent spatially heterogeneous immune states across the same lesion.` 研究动机；物理 pp. 9–10。使用 may，避免把采样偏倚写成每例必然发生。
- `We therefore examined whether multiregion immune patterns could be inferred at single-sample resolution and related to clinical outcome.` 目的句；物理 pp. 9–10。related to 表示关联，不升级为治疗效应预测。

### Methods vocabulary

- `multiregion reference state` 训练参照；物理 pp. 10–11。区域数与患者数是不同单位。
- `single-sample ITIH inference` 单样本推断；物理 pp. 10–11。推断状态不等同于实测全瘤空间状态。
- `sampling-depth-dependent heterogeneity detection` 采样深度相关检测；物理 p. 26。不能把更深采样下检出更多异质性解释为生物学发生率增加。
- `orthogonal digital-pathology assessment` 正交病理评估；物理 pp. 12–13 and 19。它支持免疫梯度，不复现多区域分子真值。
- `class-specific recall and precision` 类别特异性能；物理 pp. 11 and 18。须同时报告关注类别及其他类别表现，不能只报总体准确率。

### Methods frames

- `The classifier was trained on [number] regions from [number] multiregion patients after the stated eligibility exclusions.` 样本单位框架；物理 p. 10。不要把 746 个区域写成 746 名患者。
- `Patients with only one sampled region were excluded because the reference heterogeneity state required spatial comparison.` 排除标准；物理 p. 10。该条件属于训练参照队列，不自动适用于临床应用队列。
- `Performance was summarized by class using recall, precision, F1 score, and global accuracy.` 模型性能报告；物理 pp. 11 and 18。避免仅用一个指标宣称验证成功。
- `Digital pathology was used as an orthogonal immune readout rather than as an independent multiregion ground-truth dataset.` 验证边界；物理 pp. 12–13, 19, and 26。不得把正交支持写成外部空间分子验证。

### Results vocabulary

- `Hom-IE survival stratum` 免疫状态分层；物理 pp. 20–23。它是模型定义组，不是随机化治疗亚组。
- `PD-L1-low/negative subgroup` PD-L1 低或阴性亚组；物理 pp. 21–22，Figure 5 on p. 43。PD-L1 数据仅在部分合并队列可用。
- `combined KEAP1/STK11 mutation status` 合并基因状态；物理 p. 23，Figure 6 on p. 44。该变量是 KEAP1 and/or STK11，不能拆基因。
- `persistent adverse genomic association` 持续不良基因组关联；物理 p. 23。属于 LUAD 中 Hom-IE 层内生存关联，不证明独立机制。

### Results frames

- `For [target class], recall was [value], precision was [value], and the F1 score was [value], while global accuracy was [value].` 性能结果句；物理 p. 18。需同时说明目标类别及整体性能，不能把 0.613 总体准确率省略后称高准确。
- `The immune-state groups separated overall survival across the three treated cohorts, with cohort-specific estimates reported separately.` 跨队列结果；物理 pp. 20–21，Figure 4 on p. 42。复制的是关联方向，不是共同治疗效应大小。
- `Among patients with available PD-L1 data, the favorable immune state retained an outcome association within the low/negative stratum.` 分层关联；物理 pp. 21–22，Figure 5 on p. 43。保留 available 和 pooled analysis 边界。
- `Within the favorable immune-state stratum, the combined mutation-positive group had shorter survival, although gene-specific effects were not separable.` STK11 相关安全句式；物理 p. 23，Figure 6 on p. 44。不得改写为 STK11 alone drove resistance。

### Discussion vocabulary

- `treated-cohort outcome stratification` 治疗队列结局分层；物理 pp. 24–27。不同于治疗选择或预测性验证。
- `multiregion external-validation gap` 多区域外部验证缺口；物理 p. 26。单区域临床复制不能填补这一真值验证缺口。
- `gene-combined genomic context` 合并基因组背景；物理 pp. 23 and 27。不得转成单基因因果标签。
- `comparative interaction requirement` 比较性交互要求；物理 pp. 25–27。用于限制治疗预测表述，不能暗示文中已完成该分析。

### Discussion frames

- `Replication across ICI-treated cohorts supports outcome stratification but does not by itself establish a treatment-predictive biomarker.` 预测与预后分离；物理 pp. 24–27。需要适当对照与交互分析后才能提高证据等级。
- `The combined genomic analysis cannot distinguish the contribution of STK11 from that of KEAP1.` 基因边界；物理 p. 23，Figure 6 on p. 44。适用于本文合并变量，不概括其他研究。
- `Orthogonal pathology findings support immune gradients without substituting for independent multiregion molecular validation.` 证据类型分离；物理 pp. 19 and 26。不要把趋势性病理结果写成确定性复现。
- `Partially missing biomarkers, heterogeneous treatment settings, and limited covariates constrain clinical transportability.` 外推限制；物理 pp. 26–27。尤其保留 cohort C 无法多变量调整的事实。

### Conclusion frames

- `The findings support further validation of single-sample immune-state stratification rather than immediate treatment assignment.` 结论边界；物理 pp. 26–27。不得导出免疫单药、强化或降阶治疗建议。
- `Prospective comparative studies are needed before the classifier is used to select or de-escalate therapy.` 临床验证需求；物理 pp. 25–27。文中治疗策略讨论属于假说，不是已验证用途。

### Results paragraph

- `Define the multiregion reference and classifier performance; report orthogonal pathology support; present cohort-specific survival associations; examine PD-L1 strata; close with the combined KEAP1/STK11 result and its nonseparable gene boundary.` 结果段落逻辑；物理 pp. 17–23，Figures 2–6 on pp. 40–44。不得把关联序列改写为机制链或治疗效应链。

### Discussion paragraph

- `Relate spatial immune heterogeneity to outcome stratification; distinguish orthogonal support from multiregion validation; separate treated-cohort replication from predictive utility; retain sampling, missing-covariate, and combined-gene limitations; end with prospective comparative validation.` 讨论段落逻辑；物理 pp. 24–27。适用于证据校准写作，不是临床决策模板。
