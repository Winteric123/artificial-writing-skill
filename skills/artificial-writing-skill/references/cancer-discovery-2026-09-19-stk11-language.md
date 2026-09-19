# Cancer Discovery: STK11 core-framework reading and language

Reading date: 2026-09-19. Two supplied original-research main PDFs were read, including every main figure/caption and the 2018 main table. This is first-pass main-text reading and evidence/language curation, **not a separate acceptance source recheck**. Both quality records remain not_reviewed. External supplements were not supplied. Physical PDF page numbers below are 1-based.

## PMID 26069186 — 2015

**Co-occurring genomic alterations define major subsets of KRAS-mutant lung adenocarcinoma with distinct biology, immune profiles, and therapeutic vulnerabilities.** Cancer Discovery 5(8):860–877. DOI: 10.1158/2159-8290.CD-14-1236. [Identity](https://pubmed.ncbi.nlm.nih.gov/26069186/).

Source: nihms-684461.pdf, 35 physical pages, author manuscript. Publication year is 2015, not the later PMC-availability year. SHA-256: 2337083294ccd5fd43e3c26b26afc031c090d9e826ef8f5fd390bf7b790a4722.

### Classification and scientific interpretation

Primary: co-mutation-associated molecular subtyping. Secondary: genomic/copy-number landscape, bulk transcriptomics and microRNA, targeted total/phosphoprotein RPPA, immune phenotype, recurrence associations, cell-line pharmacology and rescue/knockdown. Direct KRAS/STK11 relevance; user-designated highlight.

Question: whether co-occurring alterations explain heterogeneity within KRAS-mutant LUAD and reveal distinct biological and therapeutic contexts. The sequence is multi-cohort subtype discovery → molecular/functional characterization → immune and recurrence associations → cell-line vulnerability. Expression-defined KL/KP/KC clusters are not interchangeable with mutation-only KLm/KPm/KPLm labels. Not every KL tumor has a detected STK11 mutation, and genotype definitions overlap.

Evidence ceiling: reproducible subtype associations and perturbation-supported cell-line dependencies, not a prospectively validated clinical classifier or HSP90 treatment recommendation. Bulk immune signatures do not directly enumerate cell types. RPPA is targeted antibody-based profiling, not untargeted mass-spectrometry proteomics. No single-cell or spatial-omics dataset is established by this paper.

### Coverage

| Unit | Physical pages | Reading result |
|---|---|---|
| Abstract; Introduction | 2; 2–3 | Heterogeneity, knowledge gap, integrative objective |
| Results | 3–12 | Subtypes, genetic context, functional LKB1/NRF2, immune phenotype, recurrence, pharmacology |
| Discussion and closing synthesis | 12–16 | Cohort/context dependence, interpretation and translational limits; no separate Conclusion heading |
| Methods | 16–18 | Cohorts/platforms, statistics and experimental assays; supplementary detail remains outside supplied scope |
| Significance | 22 | Functional translational summary, not a clinical indication |
| Figure 1 | 23–24 | NMF/consensus subtypes and validation; figure and caption inspected |
| Figure 2 | 25–26 | Co-alterations, triple-mutant context and clonality; figure and caption inspected |
| Figure 3 | 27–28 | LKB1 genetic/protein/pathway status; figure and caption inspected |
| Figure 4 | 29–30 | KEAP1/NRF2 and proteostasis programs; figure and caption inspected |
| Figure 5 | 31–32 | Immune expression/protein findings; figure and caption inspected |
| Figure 6 | 33 | Recurrence and overall survival; figure and caption inspected |
| Figure 7 | 34–35 | Drug screen, isogenic perturbation and NQO1 context; figure and caption inspected |

No separate numbered main table. Figure-embedded numerical displays were included. Pages 19–21 are references, not additional evidence cohorts.

### Numerical and negative-result checks

| Finding | Analysis set / checked value | Source | Reuse boundary |
|---|---|---|---|
| Training/validation | TCGA 68; 384-gene NMF; three clusters; 18-gene classifier; validation 88 = 41 PROSPECT + 47 Chitale | pp3–4; Fig1 | External cohorts and platforms remain distinct; do not describe all patients as one training sample |
| Refractory cohort | BATTLE-2 expression cohort 36 versus genomically profiled 41 | pp4–5; Fig1–2 | Denominator depends on modality |
| Cluster sizes | TCGA KL 23, KP 30, KC 15 | Fig1–2 | Expression clusters, not mutually exclusive mutation-only groups |
| Co-alterations | TP53 P=3.8e-06; STK11 P=1.03e-05; ATM P=.002; KEAP1 P=.006 | pp4–6; Fig2 | Enrichment, not proof of functional cooperation; KRAS-allele distribution alone did not define clusters |
| Triple mutation | Permutation P=.0018 in training 68; .01692 in independent 77; .0693 in merged 176 | pp5–6; Fig2 | Preserve nonsignificance in merged cohort; do not claim universal mutual exclusivity or longitudinal acquisition |
| Functional LKB1 | Mutation-negative KL: RNA P=7.57e-06; protein trend P=.056; pAMPK P=.017; copy loss P=.006 | pp6–7; Fig3 | Mutation, RNA, protein, copy loss and pathway state are different measurements |
| Immune phenotype | PD-L1 RNA P=.000147; IHC comparison P=.039 | pp8–9; Fig5 | RNA/protein cohorts and assays are not identical |
| Recurrence versus OS | PROSPECT RFS n=40, one stage-IV case excluded; KP versus KL+KC P=.029; adjusted for adjuvant treatment/nodal status P=.03; merged-cohort OS P=.3 | pp9–10; Fig6 | RFS association does not establish OS benefit; no ICI-treated efficacy cohort here |
| HSP90 screen | Initial 19 lines (9 vs10); expanded 22 (10 vs12); 72-h viability | pp10–12; Fig7 | Cell lines are experimental units, not patients |
| Drug-specific findings | Ganetespib P=.0044; 17-AAG P=.0237; AUY922 P=.0523 | Fig7B | AUY922 difference did not meet .05; do not claim all three were significant |
| Perturbation | LKB1 restoration/knockdown, with compound/cell-line exceptions; NQO1 inhibition addresses part of 17-AAG sensitivity | pp11–12; Fig7D–F | Mechanism is contextual, not a universal HSP90-class clinical effect |

### Source conflicts and quarantined transfer

- p11 describes the knockdown/restoration IC50 direction inconsistently with Fig7D: Calu6 shLKB1 bars show lower IC50 than shScr, whereas the prose includes an increase formulation. Do not reuse a blanket statement that LKB1 knockdown increases IC50. Preserve the discrepancy and use panel-specific direction only when reopening the source.
- Several figure legends use the ambiguous phrase “standard deviation of the mean.” Do not silently convert this to SEM; specify only an unambiguous source statistic.
- ERN1/UPR findings include nonsignificant comparisons (e.g., Fig4H P=.0675); enrichment of a pathway does not make every component significant.
- Introductory statements about the historical absence of KRAS-directed therapies are time-bound 2015 context, not current clinical background.
- STK11 and KEAP1 are both on 19p; correlated regional loss does not by itself prove two independent causal events.

### STK11 writing-framework transfer

Use: cohort/platform map → subtype discovery and independent reproduction → co-mutation and functional-state disambiguation → immune associations → clinical endpoint separation → experimental vulnerability. Do not import unavailable data modules into the user's STK11 paper.

Reusable section entries below are synthetic abstractions, not source quotations. Bracketed slots require the user's own supported data.

## PMID 29773717 — 2018

**STK11/LKB1 Mutations and PD-1 Inhibitor Resistance in KRAS-Mutant Lung Adenocarcinoma.** Cancer Discovery 8(7):822–835. DOI: 10.1158/2159-8290.CD-18-0099. [Identity](https://pubmed.ncbi.nlm.nih.gov/29773717/).

Source: nihms967902.pdf, 26 physical pages, author manuscript. Publication year is 2018, not 2019 PMC availability. SHA-256: 0e632e402ade9ee9f42d3baccd2408c323f507333f533ef391c892b8c0ffbf0f.

### Classification and scientific interpretation

Primary: immunotherapy outcome and resistance mechanism. Secondary: mutation/co-mutation genomics, TMB, PD-L1 and LKB1 IHC, retrospective response/survival, small trial biomarker subset, CRISPR knockout and syngeneic mouse immunotherapy, flow cytometry. Direct STK11 mutation/functional deficiency; user-designated highlight.

Clinical association is supported across several analysis contexts, with model perturbations supporting a tumor-cell-intrinsic contribution in the studied models. The small CheckMate-057 subgroup does not settle clinical prognostic versus predictive status. STK11 mutation is not a universal no-benefit marker for every stage or immunotherapy regimen. Human cohorts, assay definitions and mouse models remain separate. No primary single-cell/spatial/global-proteomics dataset.

### Coverage

| Unit | Physical pages | Reading result |
|---|---|---|
| Abstract; Introduction | 1; 1–2 | Clinical resistance problem and co-mutation hypothesis |
| Results | 2–6 | SU2C/CM057 response and survival, LKB1 function, TMB/PD-L1, PD-L1-positive validation, knockout models |
| Discussion; closing synthesis | 6–8; 8 | Clinical/mechanistic integration, limitations; no separate Conclusion heading |
| Methods | 8–11 | Patient selection, mutation/assay definitions, endpoints, censoring and models |
| Figures 1–3 | 20–22 | Response denominators, survival curves and LKB1 composite; all panels/captions inspected |
| Figures 4–6 | 23–25 | PD-L1/TMB, PD-L1-positive cohort, knockout model response and immune cells; all panels/captions inspected |
| Table 1 | 26 | Cohort characteristics and assay/evaluable populations inspected |

### Numerical and negative-result checks

| Finding | Analysis set / checked value | Source | Reuse boundary |
|---|---|---|---|
| SU2C cohort | 174 = 62 MDACC + 56 MSK + 56 DFCI; 165 PD-1 monotherapy, 9 combinations | pp2–3; Table1 | Not an exclusively monotherapy population |
| ORR versus survival denominator | ORR evaluable 173; KL 4/54=7.4%, KP 20/56=35.7%, K-only 18/63=28.6%; P<.001 | Fig1A | Survival uses 174 with K-only n=64; do not silently use the same denominator |
| CM057 | 44 total, nivolumab 24/docetaxel 20; nivolumab KL 0/6, KP 4/7, K-only 2/11 (P=.047); docetaxel 0/3, 0/6, 2/11 (P=.65) | p3; Fig1B | Tiny post hoc subgroups; not proof of treatment interaction |
| SU2C KL versus STK11 WT | PFS HR1.87 (95% CI1.32–2.66), P<.001; medians1.8/2.7 months | pp3–4; Fig2 | Retain comparator and survival analysis set |
| Overall survival | HR1.99 (1.29–3.06), P=.0015; medians6.4/16.0 months | Fig2 | Association under exposure, not randomized STK11-specific effect |
| Functional deficiency | IHC subset12 mutant+34 WT; composite survival population61 deficient/38 proficient | pp4; Fig3 | Composite survival set is not the IHC-only 46 |
| Composite survival | PFS HR1.80 (1.15–2.82), P=.0094; OS2.03 (1.13–3.65), P=.016 | Fig3 | Keep functional composite definition distinct from mutation-only status |
| FMI | 924 LUAD, including346 KRAS mutant; TMB <6, 6–<20, ≥20 mutations/Mb | pp4–5; Fig4 | Dataset thresholds, not universal clinical cutoffs |
| PD-L1-positive cohort | 66=11 STK11 mutant+55 WT; ORR0/11 vs19/55=34.5%, P=.026 | p5; Fig5 | Zero responses in 11 does not mean no patient can ever benefit |
| PD-L1-positive PFS | HR4.76 in prose, rounded4.8 in figure; CI2.0–11.1; P=.00012; medians1.7/19.3 months | p5; Fig5C | Preserve rounding and small-cohort uncertainty |
| PD-L1-positive OS | HR14.3; lower CI3.4; upper CI conflict50.0 versus66.7 | p5 versus Fig5D | Quarantine a single definitive CI; see source conflict below |
| PD-L1 strata interaction | P=.48 for PFS and .59 for OS | p5 | No significant interaction is not proof of no effect modification |
| PD-L1-negative KRAS subset | n=46; KP DCR7/10=70%, P=.034; ORR30%, P=.11 | pp5–6 | Preserve significant DCR versus nonsignificant ORR |
| Mouse experiments | Isogenic LKR13/LKR10 Stk11 loss; reduced PD-1/PD-L1 response and CD8 infiltration | p6; Fig6 | No neutrophil enrichment in these models; do not force agreement with other models |

### Definitions, conflict and transfer boundaries

- KL includes STK11-mutant cases with or without TP53 co-mutation; KPL belongs to KL. K-only means STK11/TP53-intact within the stated grouping, not free of every other genomic alteration.
- Mutation/functional criteria differ across SU2C, CM057 and FMI. LKB1 protein loss is not synonymous with a detected STK11 mutation.
- PD-L1 assays differ: E1L3N, 28-8, SP142 and 22C3 occur in distinct cohorts. Do not merge TPS thresholds and assay performance without validation.
- **Unresolved source conflict:** PD-L1-positive OS upper 95% CI is 50.0 in p5 prose and 66.7 in Fig5D; HR14.3 and lower limit3.4 agree. Report the conflict or withhold the disputed interval; never pick one invisibly.
- PFS and OS had different censoring cutoffs (Methods). Reuse the endpoint-specific censoring concept, not this study's historical dates.
- Mouse curves terminate relative to experimental endpoints; measured intervals and conditions must match when comparing growth.
- No comprehensive safety analysis supports claims of tolerability from this paper.
- The clinical association plus animal perturbation supports a coherent hypothesis, not a universally validated patient-selection rule.

### STK11 writing-framework transfer

Use: co-mutation groups → evaluable response set → survival → mutation versus functional deficiency → immune/biomarker context → independent clinical population → perturbation experiments → prediction/prognosis limits. Retain negative findings and source inconsistencies.

## Section-indexed language

The companion [catalog](cancer-discovery-section-language-catalog.csv) contains article-level, section/function/domain/unit/tier/source-location entries. These original frames are not harvested source sentences and require adaptation to supplied evidence. No separate Conclusion heading is invented: closing synthesis is mapped functionally to Conclusion. Loading this asset does not establish a journal-wide Cancer Discovery style profile.

### Curated entries by article and section

Each row's source locator identifies the evidence/rhetorical context, not verbatim attribution of the synthetic wording. Term rows may group related conventional terminology. All constraints apply to the entire four-entry pack.

#### 26069186 — Abstract — integrative objective

Source: p2 Abstract. Use constraint: 仅写实际检测过的组学；分子相关性与细胞系干预分开。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-001 | vocabulary | molecular heterogeneity 分子异质性; integrative profiling 整合分子谱分析; subtype-associated vulnerability 亚型相关脆弱性 |
| CD-STK11-002 | collocation | jointly characterize [genomic and expression features]; resolve heterogeneity within [driver-defined disease] |
| CD-STK11-003 | sentence_frame | We integrated [data modalities] across [cohorts] to delineate [subtypes] and assess their [biological/clinical] correlates. |
| CD-STK11-004 | paragraph_architecture | Define heterogeneous population → state integrated approach → report principal subtype-level finding → give bounded experimental implication. |

#### 26069186 — Introduction — gap and rationale

Source: pp2–3 Introduction. Use constraint: 不要沿用2015年对KRAS可靶向性的历史判断；may不等于已证实因果。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-005 | vocabulary | co-occurring alteration 共发生改变; lineage differentiation 谱系分化; context dependence 背景依赖 |
| CD-STK11-006 | collocation | beyond the initiating driver; within a genetically defined disease subset; an unresolved source of variation |
| CD-STK11-007 | sentence_frame | Although [driver] defines a clinically relevant group, variation in [co-alterations] may distinguish biologically different subsets. |
| CD-STK11-008 | paragraph_architecture | Established driver → residual heterogeneity → plausible co-alteration context → specific question and study scope. |

#### 26069186 — Methods — subtyping and validation

Source: pp16–18 Methods; Fig1. Use constraint: 只能写真实执行的方法；独立验证与训练集重抽样不同；cophenetic可保留英文避免术语歧义。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-009 | vocabulary | consensus clustering 一致性聚类; non-negative matrix factorization 非负矩阵分解; cophenetic correlation 共表型相关系数; external validation 外部验证 |
| CD-STK11-010 | collocation | select the number of clusters using [criterion]; apply a fixed classifier to [independent cohort]; harmonize expression within [platform] |
| CD-STK11-011 | sentence_frame | Subtypes were derived in [training set] using [algorithm] and evaluated in [independent sets] without redefining the classifier. |
| CD-STK11-012 | paragraph_architecture | Specify eligible samples/platforms → preprocessing → cluster selection/stability → fixed assignment rule → independent evaluation. |

#### 26069186 — Methods — experimental perturbation

Source: pp16–18 Methods; Fig7. Use constraint: 不要把细胞系数或技术复孔当患者数；不要从原文方向冲突生成通用IC50结论。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-013 | vocabulary | isogenic rescue 同源背景回补; knockdown 敲低; concentration–response curve 浓度反应曲线; half-maximal inhibitory concentration 半数抑制浓度 |
| CD-STK11-014 | collocation | restore [protein] expression; compare matched perturbation and control; quantify viability after [duration] |
| CD-STK11-015 | sentence_frame | Drug sensitivity was evaluated in [cell lines] using [assay], with [rescue/knockdown] experiments to test the contribution of [factor]. |
| CD-STK11-016 | paragraph_architecture | Define experimental unit → genotype/control → exposure and viability readout → curve fitting → uncertainty and replication. |

#### 26069186 — Results — genomic and immune characterization

Source: pp3–9; Figs1–5. Use constraint: KL表达分型不等于STK11突变组；RPPA不是全局质谱蛋白组；表达特征不等于实测细胞比例。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-017 | vocabulary | co-mutation enrichment 共突变富集; functional deficiency 功能缺失; protein abundance 蛋白丰度; inflammatory signature 炎症表达特征 |
| CD-STK11-018 | collocation | enriched in [subtype]; associated with reduced [pathway readout]; concordant at the [RNA/protein] level |
| CD-STK11-019 | sentence_frame | [Subtype] was enriched for [alteration], whereas its [immune/program] profile differed from that of [comparator]. |
| CD-STK11-020 | paragraph_architecture | Subtype definition and denominator → genomic contrast → orthogonal functional measurement → immune association → qualification for discordant assays. |

#### 26069186 — Results — negative endpoints and drug specificity

Source: pp9–12; Figs6–7. Use constraint: 保留OS与AUY922阴性结果；RFS不能改写成OS获益；不要以一个药物代表全类。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-021 | vocabulary | recurrence-free survival 无复发生存; adjusted association 调整后关联; nonsignificant difference 未达显著差异; compound-specific response 化合物特异反应 |
| CD-STK11-022 | collocation | persist after adjustment for [covariates]; fail to meet the prespecified threshold; differ across compounds |
| CD-STK11-023 | sentence_frame | The association was evident for [endpoint A], but not for [endpoint B]; sensitivity to [compound] was evaluated separately in [experimental system]. |
| CD-STK11-024 | paragraph_architecture | State analysis set → endpoint/comparator → estimate and uncertainty → null endpoint → separate experimental finding and its limits. |

#### 26069186 — Discussion — interpretation and alternative explanation

Source: pp12–16 Discussion. Use constraint: 跨队列横断面差异不能写为同一患者的克隆演化；共缺失不证明独立因果。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-025 | vocabulary | genotype–phenotype relationship 基因型表型关系; regional co-deletion 区域共缺失; translational hypothesis 转化假设 |
| CD-STK11-026 | collocation | consistent with a context-dependent dependency; not fully captured by mutation status; warrant prospective evaluation |
| CD-STK11-027 | sentence_frame | These findings suggest that [functional state] adds information beyond [mutation status], although [confounding/assay limitation] remains relevant. |
| CD-STK11-028 | paragraph_architecture | Integrate convergent modalities → distinguish mutation from function → discuss discordant findings → consider regional loss/selection → propose bounded validation. |

#### 26069186 — Conclusion — closing synthesis and significance

Source: pp15–16 closing; p22 Significance. Use constraint: 源文无独立Conclusion；Significance为原文独立单元，可作次级功能；不得宣称已验证HSP90临床疗效。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-029 | vocabulary | biologically distinct subset 生物学不同亚群; subtype-informed hypothesis 亚型导向假设; therapeutic vulnerability 治疗脆弱性 |
| CD-STK11-030 | collocation | provide a framework for [stratification]; nominate [dependency] for further study; within [defined population] |
| CD-STK11-031 | sentence_frame | Together, these analyses support a subtype-informed framework for [question] and nominate [experimental dependency] for further investigation. |
| CD-STK11-032 | paragraph_architecture | Principal classification insight → bounded biological implication → required clinical validation. |

#### 29773717 — Abstract — clinical and mechanistic summary

Source: p1 Abstract. Use constraint: 人群关联与模型干预分别陈述；不要将标题的resistance套用于所有STK11患者及方案。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-033 | vocabulary | primary resistance 原发耐药; genomic correlate 基因组相关因素; tumor-intrinsic mechanism 肿瘤内在机制 |
| CD-STK11-034 | collocation | associate with diminished response to [regimen]; evaluate across [clinical cohorts]; test in isogenic models |
| CD-STK11-035 | sentence_frame | [Alteration] was associated with [clinical outcome] in [population], and matched model experiments supported a contribution to [phenotype]. |
| CD-STK11-036 | paragraph_architecture | Clinical question → distinct human/model approaches → principal association → model finding → bounded implication. |

#### 29773717 — Introduction — biomarker problem

Source: pp1–2 Introduction. Use constraint: 未定义的功能作用应保留不确定性；不能替用户新增实验目标。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-037 | vocabulary | response heterogeneity 反应异质性; co-mutational context 共突变背景; immune escape 免疫逃逸 |
| CD-STK11-038 | collocation | account for variation within [driver-defined group]; complement existing biomarkers; motivate functional testing |
| CD-STK11-039 | sentence_frame | The contribution of [co-alteration] to treatment-response heterogeneity remains incompletely defined, particularly within [molecular context]. |
| CD-STK11-040 | paragraph_architecture | Treatment benefit and nonresponse → limitations of current biomarker → co-mutation rationale → clinical and functional objectives. |

#### 29773717 — Methods — cohort and assay definitions

Source: pp8–10 Methods; Table1. Use constraint: KL可含KPL；K-only不是无其他突变；不同PD-L1克隆或队列定义不能自动合并。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-041 | vocabulary | response-evaluable population 反应可评价人群; nonsynonymous variant 非同义变异; H-score 组织化学评分; assay-specific cutoff 检测特异阈值 |
| CD-STK11-042 | collocation | assign overlapping genotypes using [hierarchy]; retain assay-specific thresholds; distinguish mutation from protein loss |
| CD-STK11-043 | sentence_frame | Patients were classified using [variant rules], and [response/survival] analyses used their respective evaluable populations. |
| CD-STK11-044 | paragraph_architecture | Eligibility → variant/overlap hierarchy → assay and cutoff → endpoint-specific denominator → missing-data handling. |

#### 29773717 — Methods — survival and multiplicity

Source: pp10–11 statistical methods. Use constraint: 只有实际完成的模型/校正才能写入；CI、Wald或log-rank P不能混搭。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-045 | vocabulary | endpoint-specific censoring 终点特异删失; Cox proportional hazards model Cox比例风险模型; interaction test 交互作用检验; multiplicity correction 多重性校正 |
| CD-STK11-046 | collocation | estimate survival using [method]; censor at [endpoint-specific date]; adjust for multiple comparisons using [method] |
| CD-STK11-047 | sentence_frame | Associations were summarized as hazard ratios with [confidence level] intervals, using prespecified comparators and endpoint-specific censoring rules. |
| CD-STK11-048 | paragraph_architecture | Define time origin/event → censoring and evaluable population → estimator/model → covariates → multiplicity and subgroup status. |

#### 29773717 — Results — response, survival and function

Source: pp2–5; Figs1–5; Table1. Use constraint: ORR173与生存174分开；0/11不是永远无获益；OS CI冲突数值禁止生成确定句。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-049 | vocabulary | objective response rate 客观缓解率; disease control rate 疾病控制率; functional loss 功能缺失; confidence interval 置信区间 |
| CD-STK11-050 | collocation | among [n] response-evaluable patients; compared with [reference genotype]; directionally consistent but imprecise |
| CD-STK11-051 | sentence_frame | Responses occurred in [numerator]/[denominator] patients in [group A] and [numerator]/[denominator] in [group B]; the survival analysis included [separate n]. |
| CD-STK11-052 | paragraph_architecture | Cohort/evaluable flow → response fractions → survival estimate → mutation/function distinction → biomarker stratum → uncertainty. |

#### 29773717 — Results — model perturbation

Source: p6; Fig6; Methods. Use constraint: 限定具体小鼠/克隆；本模型无中性粒细胞富集，不可据其他文献补写；accompanied不证明免疫细胞为中介。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-053 | vocabulary | isogenic knockout 同源背景敲除; syngeneic tumor model 同系肿瘤模型; intratumoral CD8 cells 肿瘤内CD8细胞 |
| CD-STK11-054 | collocation | attenuate response under [treatment]; compare edited and control tumors; accompany a change in [immune compartment] |
| CD-STK11-055 | sentence_frame | Under matched experimental conditions, loss of [gene] reduced [treatment response] and was accompanied by [measured immune change]. |
| CD-STK11-056 | paragraph_architecture | Genetic perturbation validation → tumor response → endpoint/timing → immune readout → model-specific negative observation. |

#### 29773717 — Discussion — prognostic versus predictive interpretation

Source: pp6–8 Discussion. Use constraint: 亚组间一个显著一个不显著不等于交互显著；模型因果不能自动上升为人群预测标志物。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-057 | vocabulary | prognostic association 预后关联; treatment-effect modification 治疗效应修饰; limited subgroup power 亚组效能有限 |
| CD-STK11-058 | collocation | does not distinguish prognosis from prediction; supports a mechanistic contribution in [model]; requires a treatment interaction |
| CD-STK11-059 | sentence_frame | Although the clinical and experimental findings are coherent, the available comparator data do not establish [biomarker] as a treatment-predictive marker. |
| CD-STK11-060 | paragraph_architecture | Reconcile human/model findings → retain assay/genotype heterogeneity → discuss small comparator subset → delimit prediction → validation need. |

#### 29773717 — Conclusion — closing translational implication

Source: p8 closing Discussion. Use constraint: 原文无独立Conclusion；不能以研究框架模板替代临床决策。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| CD-STK11-061 | vocabulary | resistance-associated phenotype 耐药相关表型; context-specific biomarker 背景特异标志物; validation cohort 验证队列 |
| CD-STK11-062 | collocation | identify a candidate contributor to [resistance]; support further evaluation in [defined setting] |
| CD-STK11-063 | sentence_frame | These results identify [factor] as a candidate contributor to [phenotype] and support validation under clearly specified treatment and genomic contexts. |
| CD-STK11-064 | paragraph_architecture | Principal association → bounded model support → unresolved clinical prediction and prospective testing. |

