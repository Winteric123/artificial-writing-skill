# CCR 2026 Translational Mechanisms and Therapy full-text language assets

## Purpose and source discipline

This reference was curated on 2026-09-07 from the complete main text of five original research articles published in the CCR category `Translational Mechanisms and Therapy`. It supports full-manuscript vocabulary, phrase, sentence, and paragraph construction across oncology, immunotherapy, targeted therapy, genomics, transcriptomics, bioinformatics, basic experiments, and statistical reporting.

Use these materials as functional language patterns, not as source sentences to copy. Reconstruct every sentence from the user's own design, population, model, endpoint, estimate, and uncertainty. Never transfer a number, comparator, assay, or mechanistic link from these articles into another manuscript.

This focused set contains no commentary, editorial, author reply, rebuttal, or response-only correspondence. Such genres remain ineligible for corpus updates.

## Five-paper evidence map

| PMID | Study form | Strongest language domains | Maximum supported inference |
|---|---|---|---|
| 41817317 | Randomized perioperative radiation study with tumor immune profiling and survival correlations | Brain metastasis, radiation, bulk RNA-seq, TCR-seq, immune deconvolution, adjusted survival analysis | Prognostic association and radiation-associated immune change; not treatment-response prediction |
| 41837748 | Engineered anti-CTLA-4 antibodies assessed in vitro, in mouse models, nonhuman primates, and exploratory cross-trial human biomarker data | Immunotherapy engineering, Fc biology, T-cell phenotyping, antitumor activity, pharmacokinetics, toxicology | Preclinical comparative activity and translational pharmacodynamic observations; not clinical superiority or comparative safety |
| 41649868 | Mutant-selective EGFR inhibitor evaluated in cell systems, xenografts, intracranial models, and an early phase I/II dose-escalation cohort | Acquired resistance, targeted therapy, signal inhibition, brain penetration, preliminary clinical response | Preclinical efficacy plus preliminary single-arm clinical activity; not established patient benefit |
| 42148884 | Historical real-world cohort, pharmacovigilance analysis, human pathology, and mechanistic cell and mouse experiments | Immune-related secondary malignancy, competing-risk incidence, TFH-B-cell signaling, causal triangulation | Association with recorded lymphoma incidence plus biological plausibility; not proof that PD-1 blockade caused lymphoma |
| 42507545 | Large retrospective real-world DNA/RNA cohort with temporal, TCGA, and trial-based validation analyses | 9p21 loss, targeted DNA sequencing, whole-transcriptome RNA-seq, immune deconvolution, TTNT, biomarker interpretation | Clinicogenomic and outcome associations; not a validated predictive biomarker without a treatment interaction |

## Modality coverage boundary

The five papers directly support language for:

- targeted tumor and matched-normal DNA sequencing;
- whole-exome sequencing and Sanger confirmation;
- bulk RNA sequencing and whole-transcriptome profiling;
- T-cell receptor repertoire sequencing;
- circulating tumor DNA profiling;
- pathway and gene-set enrichment analysis;
- computational immune-cell deconvolution from bulk RNA-seq;
- conventional and multiplex immunohistochemistry or immunofluorescence;
- flow-cytometric immune phenotyping;
- cell-line, patient-derived cell, syngeneic, xenograft, orthotopic intracranial, and nonhuman-primate experiments.

They do **not** contain primary single-cell RNA-seq, spatial transcriptomics, or mass-spectrometry proteomics workflows. Therefore:

- do not relabel bulk RNA-seq as single-cell transcriptomics;
- do not call multiplex tissue imaging `spatial omics`;
- do not call immunoblotting, IHC, cytokine assays, or flow cytometry `proteomics`;
- do not infer cell states at single-cell resolution from computational deconvolution;
- add single-cell, spatial, or proteomic wording from another verified source set before claiming corpus support for those modalities.

## Evidence-first language selection

Before choosing a phrase, label the evidence unit:

1. **System:** patient, real-world database, clinical-trial cohort, human specimen, patient-derived cell, engineered cell line, mouse model, or nonhuman primate.
2. **Measurement:** directly measured, pathologist assessed, clinician documented, sequencing derived, computationally estimated, or inferred from a perturbation.
3. **Endpoint:** molecular inhibition, immune activation, tumor growth, tumor-free status, objective response, TTNT, survival, cumulative incidence, pharmacokinetics, or toxicity.
4. **Analysis status:** primary, prespecified sensitivity, adjusted, exploratory, subgroup, cross-trial, temporal validation, or external validation.
5. **Claim tier:** descriptive, associative, prognostic, mechanistic, predictive, or comparative efficacy.

Use the lowest defensible claim tier. Orthogonal evidence can strengthen biological plausibility, but it does not repair confounding in a historical cohort or create a randomized treatment comparison.

## Vocabulary and collocation bank

### Typical-section mapping

Technical terms can appear in several manuscript sections. Use this table as typical-use metadata, then select rhetorical frames from the exact target section in [ccr-phrase-patterns.md](ccr-phrase-patterns.md).

| Vocabulary group | Typical sections |
|---|---|
| Oncology and tumor biology | Abstract; Introduction; Methods; Results; Discussion; Conclusion |
| Immunotherapy and immune mechanisms | Abstract; Introduction; Methods; Results; Discussion; Conclusion |
| Targeted therapy and drug resistance | Abstract; Introduction; Methods; Results; Discussion; Conclusion |
| Genomics, transcriptomics, and bioinformatics | Abstract; Introduction; Methods; Results; Discussion |
| Basic and translational experiments | Introduction; Methods; Results; Discussion; Conclusion |
| Efficacy, activity, and safety endpoints | Abstract; Methods; Results; Discussion; Conclusion |
| Statistical reporting | Abstract; Methods; Results; Discussion; Conclusion |

The mapping is nonexclusive. Preserve one term across sections, but select section-specific verbs, uncertainty, and information order.

### Oncology and tumor biology

- `biomarker-defined molecular subset` - 生物标志物界定的分子亚群
- `driver-defined subgroup` - 驱动基因界定亚组
- `actionable genomic alteration` - 可靶向基因组改变
- `co-occurring alteration` / `mutually exclusive alteration` - 共现 / 互斥改变
- `biallelic loss` / `homozygous deletion` - 双等位基因缺失 / 纯合缺失
- `concordant codeletion` / `discordant deletion` - 一致性共缺失 / 不一致缺失
- `focal deletion` / `broad deletion` - 局灶性 / 广泛性缺失
- `genomic context` / `clinicogenomic landscape` - 基因组背景 / 临床基因组图谱
- `tumor microenvironment` / `immune microenvironment` - 肿瘤 / 免疫微环境
- `immune-excluded phenotype` - 免疫排斥表型
- `immune-cell infiltration` - 免疫细胞浸润
- `brain metastasis microenvironment` - 脑转移微环境
- `intracranial tumor burden` - 颅内肿瘤负荷
- `malignant pleural effusion-derived cells` - 恶性胸腔积液来源细胞
- `tumor-infiltrating lymphocytes` - 肿瘤浸润淋巴细胞
- `treatment-naive` / `previously treated` / `heavily pretreated` - 初治 / 既往治疗 / 多线治疗
- `acquired resistance` / `on-target resistance` - 获得性耐药 / 靶内耐药
- `resistance-associated alteration` - 耐药相关改变
- `molecularly selected population` - 分子筛选人群
- `histology-specific association` - 组织学特异性关联
- `clinically annotated cohort` - 具有临床注释的队列
- `real-world treatment cohort` - 真实世界治疗队列

### Immunotherapy and immune mechanisms

- `PD-1 blockade` / `CTLA-4 blockade` - PD-1 / CTLA-4 阻断
- `immune-checkpoint inhibitor` - 免疫检查点抑制剂
- `Fc non-fucosylation` - Fc 非岩藻糖基化
- `peptide-masked antibody` - 肽掩蔽抗体
- `conditionally activatable therapeutic` - 条件性激活治疗分子
- `protease-mediated unmasking` - 蛋白酶介导的去掩蔽
- `tumor-localized activation` - 肿瘤局部激活
- `Fc gamma receptor co-engagement` - Fc gamma 受体共结合
- `APC-mediated T-cell priming` - 抗原呈递细胞介导的 T 细胞启动
- `effector-memory T cell` - 效应记忆 T 细胞
- `tumor-specific CD8-positive T cell` - 肿瘤特异性 CD8 阳性 T 细胞
- `conventional CD4-positive T cell` - 常规 CD4 阳性 T 细胞
- `regulatory T-cell depletion` - 调节性 T 细胞耗竭
- `Th1-like differentiation` - Th1 样分化
- `T follicular helper cell activation` - 滤泡辅助性 T 细胞激活
- `receptor-ligand axis` - 受体-配体轴
- `trophic signal` - 营养性支持信号
- `peripheral immune activation` - 外周免疫激活
- `dose-dependent cytokine induction` - 剂量依赖性细胞因子诱导
- `immune-related adverse event` - 免疫相关不良事件
- `context-dependent immune effect` / `double-edged effect` - 情境依赖性 / 双刃剑式免疫效应

### Targeted therapy and drug resistance

- `mutant-selective inhibitor` - 突变选择性抑制剂
- `fourth-generation EGFR tyrosine kinase inhibitor` - 第四代 EGFR 酪氨酸激酶抑制剂
- `C797S-mediated resistance` - C797S 介导的耐药
- `wild-type sparing` - 对野生型具有保留性 / 较低野生型抑制
- `target engagement` - 靶点结合或占有
- `on-target pathway suppression` - 靶向通路抑制
- `downstream signaling inhibition` - 下游信号抑制
- `dose-responsive suppression of phosphorylation` - 剂量响应性磷酸化抑制
- `antiproliferative activity` - 抗增殖活性
- `colony-forming capacity` - 克隆形成能力
- `blood-brain barrier penetration` - 血脑屏障穿透
- `intracranial exposure` - 颅内暴露
- `orthotopic brain-metastasis model` - 原位脑转移模型
- `central nervous system activity` - 中枢神经系统活性
- `synthetic-lethal vulnerability` - 合成致死脆弱性
- `PRMT5/MAT2A-directed strategy` - PRMT5/MAT2A 靶向策略
- `MTA accumulation` - 甲硫腺苷积累

### Genomics, transcriptomics, and bioinformatics

- `paired tumor-normal sequencing` - 肿瘤-正常配对测序
- `targeted DNA sequencing` - 靶向 DNA 测序
- `whole-exome sequencing` - 全外显子组测序
- `whole-transcriptome RNA sequencing` - 全转录组 RNA 测序
- `bulk transcriptomic profile` - bulk 转录组谱
- `T-cell receptor repertoire sequencing` - TCR 受体库测序
- `circulating tumor DNA dynamics` - 循环肿瘤 DNA 动态
- `somatic short variant` - 体细胞短变异
- `copy-number alteration` - 拷贝数改变
- `gene rearrangement or fusion` - 基因重排或融合
- `ploidy-aware copy-number model` - 倍体感知的拷贝数模型
- `circular binary segmentation` - 环状二元分割
- `stromal admixture` / `tumor purity` - 基质混合 / 肿瘤纯度
- `log2-transformed TPM` - log2 转换后的 TPM
- `trimmed mean of M values normalization` - TMM 标准化
- `voom-transformed expression data` - voom 转换表达数据
- `single-sample gene-set enrichment analysis` - 单样本基因集富集分析
- `pathway-level enrichment score` - 通路层面富集评分
- `computational immune deconvolution` - 计算性免疫去卷积
- `estimated immune-cell fraction` - 估计的免疫细胞比例
- `TCR diversity` / `TCR clonality` / `TCR density` - TCR 多样性 / 克隆性 / 密度
- `temporally distinct validation cohort` - 时间独立验证队列
- `biomarker-evaluable population` - 生物标志物可评估人群
- `technical confounding from low tumor purity` - 低肿瘤纯度导致的技术混杂

Use `estimated`, `inferred`, or `deconvolved` for cell proportions derived from bulk RNA-seq. Reserve `measured` for direct assays.

### Basic and translational experiments

- `CRISPR/Cas9-engineered cell line` - CRISPR/Cas9 工程化细胞系
- `isogenic model` - 同基因背景模型
- `patient-derived cell model` - 患者来源细胞模型
- `syngeneic mouse model` - 同系小鼠模型
- `human target knock-in mouse` - 人源靶点敲入小鼠
- `subcutaneous xenograft` - 皮下异种移植模型
- `orthotopic intracranial xenograft` - 颅内原位异种移植模型
- `tumor rechallenge` - 肿瘤再挑战
- `treatment washout period` - 停药观察期
- `bioluminescence imaging` - 生物发光成像
- `multiplex immunofluorescence` - 多重免疫荧光
- `immunohistochemical H-score` - 免疫组化 H 评分
- `phospho-protein immunoblotting` - 磷酸化蛋白免疫印迹
- `flow-cytometric phenotyping` - 流式细胞表型分析
- `transwell coculture` - Transwell 共培养
- `receptor knockout experiment` - 受体敲除实验
- `SEB-stimulated peripheral blood mononuclear cell assay` - SEB 刺激的 PBMC 实验
- `nonhuman-primate toxicology study` - 非人灵长类毒理学研究
- `pharmacokinetic exposure` - 药代动力学暴露
- `pharmacodynamic readout` - 药效学读数
- `orthogonal experimental support` - 正交实验支持

### Efficacy, activity, and safety endpoints

- `half-maximal inhibitory concentration (IC50)` and `90% inhibitory concentration (IC90)`
- `area under the concentration-response curve`
- `tumor growth inhibition (TGI)`
- `tumor regression` / `durable tumor control`
- `tumor-free proportion` / `complete response in a mouse model`
- `best overall response (BOR)`
- `partial response`, `stable disease`, and `progressive disease`
- `time to next treatment (TTNT)`
- `progression-free survival (PFS)` and `overall survival (OS)`
- `restricted mean survival time`
- `cumulative incidence function`
- `highest nonseverely toxic dose (HNSTD)`
- `body-weight trajectory`
- `inflammation score`
- `peripheral cytokine induction`

TGI can exceed 100% when treatment produces regression relative to baseline under the study's calculation. Never rewrite a TGI above 100% as a response rate. An unchanged body-weight trajectory is a tolerability observation, not proof of safety. TTNT is a real-world surrogate and should not be silently relabeled as RECIST-assessed PFS.

### Statistical reporting

- `two-tailed P value`
- `false-discovery-rate-adjusted P value` / `FDR q value`
- `Dunnett-adjusted comparison with the reference group`
- `Bonferroni- or Sidak-adjusted multiple comparison`
- `Mann-Whitney U test` / `Kruskal-Wallis H test`
- `Fisher exact test` / `chi-square test`
- `one-way or two-way analysis of variance`
- `repeated-measures analysis of variance`
- `Spearman rank correlation`
- `Kaplan-Meier estimate` / `log-rank comparison`
- `Gehan-Breslow-Wilcoxon test`
- `Cox proportional hazards model`
- `multivariable-adjusted hazard ratio`
- `likelihood-ratio test`
- `competing-risk analysis` / `Gray test`
- `right-censoring`
- `risk-set adjustment`
- `left truncation` / `immortal-time bias`
- `prespecified sensitivity analysis`
- `subgroup analysis with limited power`
- `nominal significance without multiplicity control`
- `formal power calculation was not performed`

Report the estimate before the P value whenever an estimate exists. State the confidence interval with the HR, RR, OR, difference, or model coefficient. For subgroup treatment claims, require an interaction estimate or interaction test rather than comparing one subgroup's P value with another subgroup's P value.

## Section-specific phrase frames

### Introduction: clinical problem, mechanism, and gap

- `[Resistance alteration] is an increasingly recognized mechanism of acquired resistance to [therapy].`
- `Effective treatment options remain limited after emergence of [alteration].`
- `Strategies that preserve [desired on-target effect] while limiting [systemic or off-tumor effect] are needed.`
- `[Molecular event] frequently encompasses neighboring genes, complicating attribution of its clinical effects.`
- `The prognostic and treatment-specific implications of [marker] remain incompletely defined.`
- `Whether [immune population] contributes to [clinical event] during checkpoint blockade remains unclear.`
- `The brain-metastasis microenvironment may differ from extracranial disease in ways that alter local immunity.`
- `To address this gap, we integrated [clinical/genomic] analysis with [orthogonal experimental approach].`
- `We sought to distinguish [descriptive association] from [mechanistic or predictive hypothesis].`

Avoid opening with an unqualified `This is the first...` or `This is the largest...`. If priority or scale is important, define the searchable scope and verify it independently.

### Methods: population and specimen definition

- `Patients were included if they had [diagnosis], evaluable [assay], and documented [clinical variable].`
- `The analysis was restricted to specimens collected within [window] of [index event].`
- `Samples with estimated tumor purity below [threshold] were excluded because of reduced sensitivity for copy-number calling.`
- `The biomarker-evaluable population comprised randomized patients with interpretable tissue-based genomic profiling.`
- `The validation cohort was temporally distinct from the primary cohort.`
- `Clinical response was abstracted from treating-physician documentation rather than formal RECIST assessment.`
- `At the data cutoff of [date], [N] patients had received at least one dose.`

### Methods: omics and bioinformatics

- `Tumor and matched-normal specimens underwent targeted DNA sequencing, and tumor RNA underwent whole-transcriptome sequencing.`
- `Pathogenic or likely pathogenic short variants and prespecified copy-number alterations were retained for analysis.`
- `RNA abundance was expressed as log2(TPM + 1).`
- `Immune-cell fractions were estimated from bulk RNA-seq using [deconvolution method].`
- `Pathway enrichment scores were calculated for each sample using single-sample gene-set enrichment analysis.`
- `TCR repertoire diversity, clonality, and density were quantified separately.`
- `Copy-number segments were mapped to genes using [annotation release].`
- `Co-occurrence and mutual exclusivity were evaluated using [test] and log odds ratios.`
- `Multiple-hypothesis correction was performed using the false discovery rate.`

### Methods: preclinical and pharmacology

- `[Cell model] was engineered to express [specified mutant allele] and confirmed by [assay].`
- `Antiproliferative activity was summarized using IC50, IC90, and area-under-the-curve estimates.`
- `Pathway inhibition was assessed by changes in phosphorylated [target] and downstream [effectors].`
- `Mice with established tumors were assigned to [treatment groups] and monitored for tumor volume and body weight.`
- `Intracranial tumor burden was monitored longitudinally by bioluminescence imaging.`
- `A complete response was defined prospectively as [operational definition].`
- `Tumor rechallenge was used to assess the persistence of antitumor immune memory.`
- `Pharmacokinetic, pharmacodynamic, and toxicology endpoints were evaluated in nonhuman primates.`

Do not add randomization, blinding, biological replicates, technical replicates, humane endpoints, or exclusion rules unless the source methods state them.

### Methods: outcomes and statistics

- `TTNT was defined from first-line treatment initiation to the next line of therapy, death, or last follow-up and was censored at [time].`
- `Death was treated as a competing event in the cumulative-incidence analysis.`
- `Risk-set adjustment was used to mitigate left truncation and immortal-time bias.`
- `Patients sequenced more than [window] after treatment initiation were excluded from the delayed-entry analysis.`
- `The multivariable model included [covariates selected from the evidence ledger].`
- `No formal power calculation was performed; sample size was determined by the available retrospective cohort.`
- `The [time]-restricted analysis was prespecified as a sensitivity analysis.`

### Results: analysis set and denominator

- `Of [N screened], [N analyzed] met the prespecified inclusion criteria.`
- `After excluding samples with [technical criterion], [N] remained in the primary analysis.`
- `Among [N] evaluable patients, [n] had a partial response and [n] had stable disease.`
- `The outcome analysis included [N] patients with documented first-line therapy and eligible sequencing dates.`
- `Results are reported for the biomarker-evaluable rather than the intention-to-treat population.`

### Results: molecular and omics findings

- `[Alteration] was enriched in [group] and depleted in [comparator] after FDR correction.`
- `[Marker-positive] tumors had lower estimated [immune subset] fractions and lower enrichment scores for [pathway].`
- `The association was reproduced in a temporally distinct validation cohort.`
- `TCR diversity increased after [exposure], whereas clonality and density were not significantly altered.`
- `Higher [immune metric] was independently associated with [survival endpoint] after adjustment for [covariates].`
- `Expression of [gene] was lower in [deletion class], consistent with the physical extent of the deletion.`

Use `reproduced` or `was consistent` for a repeated association. Use `validated` only when the validation target, cohort independence, analysis plan, and success criterion justify it.

### Results: preclinical drug activity

- `[Agent] inhibited proliferation across [models], including cells harboring [resistance genotype].`
- `Treatment reduced phosphorylation of [target] and downstream [effectors] in a concentration-dependent manner.`
- `[Agent] achieved a TGI of [x%] at [dose], compared with [y%] for [comparator].`
- `Tumor regression was observed without a statistically significant change in body weight during the observation period.`
- `In the intracranial model, treatment reduced bioluminescent tumor burden and prolonged survival relative to [control].`
- `The modified antibody increased the proportion of tumor-free mice relative to the comparator.`
- `The antitumor effect was retained after conditional unmasking in vivo.`
- `Rechallenge of tumor-free mice provided evidence of durable antitumor immune memory.`

Use `greater antitumor activity in this model`, not `superior efficacy`, when evidence is limited to preclinical models.

### Results: clinical activity, association, and null findings

- `At data cutoff, preliminary antitumor activity was observed in the dose-escalation cohort.`
- `Three of [N] treated patients had a partial response; the uncontrolled sample does not support a comparative efficacy claim.`
- `[Exposure] was associated with a higher recorded cumulative incidence of [event] in the historical-cohort analysis.`
- `The crude relative risk was attenuated after adjustment for the secular trend but remained elevated.`
- `No statistically significant difference in TTNT was observed between the biomarker groups in the [treatment] cohort.`
- `BOR did not differ significantly across biomarker groups.`
- `The association weakened after multivariable adjustment, suggesting potential confounding by [covariates].`
- `The point estimate was elevated, but the confidence interval crossed the null and the P value was nonsignificant.`
- `Results differed across survival tests, limiting the robustness of the apparent association.`
- `The subgroup pattern was exploratory and should not be interpreted as evidence of treatment interaction.`

### Results: pharmacology and safety

- `Exposure increased approximately dose proportionally across [dose range].`
- `The HNSTD was higher for [agent A] than for [agent B] in the nonhuman-primate study.`
- `Peripheral cytokine induction was lower with [agent A] at the evaluated doses.`
- `Differences in dose and schedule precluded a definitive cross-trial comparison.`
- `No significant body-weight change was observed; broader safety conclusions require dedicated toxicology or clinical data.`

### Discussion: interpretation and mechanism

- `Taken together, these data support a model in which [perturbed pathway] contributes to [bounded phenotype].`
- `The knockout and coculture experiments support involvement of the [ligand/receptor] axis.`
- `The concordance of clinical, pathologic, and experimental observations increases biological plausibility.`
- `The net effect may depend on the receptor profile of the malignant cells and the balance between trophic and antitumor signals.`
- `The finding is consistent with resistance biology but does not establish a treatment-predictive biomarker.`
- `Radiation-associated changes in immune repertoire diversity may have prognostic relevance.`
- `Preclinical intracranial activity provides a rationale for prospective evaluation in patients with brain metastases.`
- `The results motivate biomarker-enriched trials of [therapeutic strategy].`

### Discussion: limitations linked to inference

- `Historical treatment eras may introduce temporal confounding that cannot be eliminated by sensitivity analysis.`
- `Administrative claims lacked sufficient histologic detail to classify all lymphoma events.`
- `Pharmacovigilance reports are vulnerable to reporting and surveillance biases and do not provide an incidence denominator.`
- `The single-arm dose-escalation cohort was small and lacked a standard-of-care comparator.`
- `Cross-trial biomarker comparisons used different doses and schedules and are therefore exploratory.`
- `TTNT is an imperfect surrogate for PFS and may overestimate treatment benefit.`
- `Filtering low-purity tumors improved copy-number reliability but may have excluded immune-rich tumors.`
- `Subgroup analyses of deletion length had limited power and generalizability.`
- `A significant prognostic association does not establish prediction of treatment benefit.`
- `Discordant results across statistical tests reduce confidence in the robustness of the finding.`

### Translational Relevance

- `These findings provide a rationale for prospective evaluation of [agent or combination] in [molecularly selected population].`
- `The biomarker may support risk stratification, but treatment selection requires evidence of a biomarker-by-treatment interaction.`
- `The preclinical therapeutic window warrants evaluation in a controlled clinical study.`
- `The mechanistic findings identify a candidate pathway for intervention without establishing clinical utility.`

### Conclusion

- `In [population or model], [bounded primary finding] supports [specific next step] but does not establish [unsupported claim].`
- `Prospective studies are needed to quantify the event frequency and define clinicopathologic risk factors.`
- `Further work should integrate complete genomic annotation with standardized clinical endpoints.`

## Drug-efficacy wording ladder

| Evidence level | Preferred wording | Do not upgrade to |
|---|---|---|
| Biochemical or cell assay | `bound`, `inhibited phosphorylation`, `reduced viability`, `showed antiproliferative activity` | patient efficacy |
| Mouse tumor model | `reduced tumor growth`, `induced regression`, `increased the tumor-free proportion`, `prolonged survival in the model` | clinical benefit or clinical superiority |
| Nonhuman-primate study | `showed a higher HNSTD`, `reduced peripheral immune activation at the tested doses` | safe in patients |
| Early single-arm clinical cohort | `preliminary activity was observed`, `n of N patients had a partial response` | superior, effective, or practice changing |
| Retrospective treatment cohort | `was associated with shorter TTNT`, `the adjusted association weakened` | caused resistance or predicted benefit |
| Historical incidence comparison | `was associated with a higher recorded incidence` | caused the adverse event |
| Randomized treatment comparison | `improved` or `reduced` only when the endpoint, estimate, uncertainty, and analysis support it | broad class-wide benefit |

## Synthetic full-sentence models

These sentences are newly constructed calibration models, not quotations.

### Immune repertoire and prognosis

`Higher TCR diversity was independently associated with longer survival in the analyzed brain-metastasis cohort, whereas the study did not test a biomarker-by-treatment interaction; the finding is therefore prognostic rather than predictive.`

### Engineered immunotherapy

`In the human CTLA-4 knock-in mouse model, Fc non-fucosylation increased the proportion of tumor-free animals relative to the ipilimumab-like comparator, while peptide masking reduced peripheral immune activation at the evaluated doses.`

`These preclinical findings support further evaluation of the engineered antibody but do not establish greater efficacy or safety in patients.`

### Fourth-generation targeted therapy

`JIN-A02 suppressed mutant EGFR signaling and induced regression in C797S-containing xenograft models, including an orthotopic intracranial model.`

`Partial responses in the ongoing dose-escalation cohort constitute preliminary activity in a small, uncontrolled population and should not be presented as comparative benefit.`

### Immunotherapy-associated secondary malignancy

`PD-1 blockade was associated with a higher recorded incidence of lymphoma in a historical-cohort analysis; complementary pathology and perturbation experiments support biological plausibility but do not eliminate temporal or surveillance confounding.`

### Multiomic real-world biomarker

`CDKN2A/MTAP codeletion was associated with distinct genomic, transcriptomic, and immune features and with shorter TTNT in selected treatment cohorts, although attenuation after multivariable adjustment and heterogeneous treatment-specific patterns limit a predictive interpretation.`

## Synthetic paragraph models

### Integrated Results paragraph

`Among [N] eligible tumors, [marker] was present in [n (%)] and was enriched in [molecular context] after FDR correction. Bulk RNA-seq showed lower enrichment scores for [immune pathway], and computational deconvolution estimated lower fractions of [cell population] in marker-positive tumors. In the treatment cohort, [marker] was associated with shorter [endpoint] in univariable analysis (HR, [x]; 95% CI, [a-b]), but the association attenuated after adjustment for [covariates]. BOR did not differ significantly between groups. Together, these findings define a clinicogenomic phenotype but do not establish treatment-specific predictive value.`

### Preclinical-to-clinical paragraph

`The candidate agent inhibited [mutant target] signaling in engineered and patient-derived models and reduced tumor burden in both subcutaneous and intracranial xenografts. No significant body-weight change was observed during the study period. At the clinical data cutoff, [n/N] patients in the dose-escalation cohort had a partial response. These observations support continued clinical evaluation, although the small single-arm cohort precludes conclusions about comparative efficacy or safety.`

### Mechanistic triangulation paragraph

`The clinical database analysis identified a higher recorded incidence of [event] after [exposure]. Multiplex tissue imaging localized [cell population] within the malignant compartment, and receptor knockout experiments attenuated [functional readout] in vitro and in vivo. This triangulation supports a biologically plausible [cell-cell or ligand-receptor] mechanism; however, the observational comparison remains susceptible to temporal, surveillance, and residual confounding.`

## Paper-specific numerical calibration checks

Use these only when auditing or summarizing the same article, and re-open the source before publication.

- **PMID 41817317:** breast brain-metastasis TCR diversity retained a multivariable survival association (adjusted HR 0.25; 95% CI 0.115-0.54; Dunnett-adjusted P = 0.0009). In a separate lung cohort, Mantel-Cox P = 0.0445 but Gehan-Breslow-Wilcoxon P = 0.1550, so `robustly validated` is not supported.
- **PMID 41837748:** in the MC38 model, 90% of mice receiving the non-fucosylated antibody versus 30% receiving the ipilimumab-like comparator were tumor-free. The NF-PB HNSTD was threefold higher than NF in nonhuman primates, but human cross-trial cytokine comparisons were exploratory and used different schedules.
- **PMID 41649868:** JIN-A02 produced TGI values of 115.9% and 168.2% at 10 and 30 mg/kg, respectively, versus 49.3% with osimertinib in the specified model. At the 2025-07-22 cutoff, 3 of 23 treated patients had a partial response and 7 had stable disease.
- **PMID 42148884:** the claims analysis included 8,661 historical platinum-only and 7,009 platinum-plus-ICI patients. The reported crude lymphoma relative risk of approximately 3.9 was conservatively attenuated to about 2.5 after accounting for a secular incidence trend; this was not a fully adjusted causal estimate.
- **PMID 42507545:** the primary cohort contained 16,947 tumors and the temporal validation cohort 10,996. In exploratory IFNK-stratified analyses, one HR was 1.89 (95% CI 1.33-2.69; P < 0.001), whereas another was 1.59 (95% CI 0.95-2.68; P = 0.079); do not simplify heterogeneous subgroup results into a universal predictive claim.

## Mandatory misuse checks

Before using this reference, reject or revise any sentence that:

- calls one of these five articles a commentary or reply;
- calls the five-paper set a single-cell, spatial-omics, or proteomics corpus;
- converts computationally estimated cell fractions into directly measured cell counts;
- converts TGI into objective response rate;
- treats absence of mouse weight loss as clinical safety;
- treats an HNSTD comparison as a patient safety comparison;
- treats cross-trial cytokine differences as randomized evidence;
- treats a partial response in dose escalation as proof of comparative efficacy;
- treats historical-cohort incidence as causal risk;
- treats a prognostic survival association as treatment prediction;
- treats a nominal subgroup P value as an interaction test;
- treats TTNT as equivalent to RECIST-assessed PFS;
- calls a repeated association `validated` without defining the validation target and independent cohort.
