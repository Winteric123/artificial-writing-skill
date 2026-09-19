# Nature: STK11/KEAP1 dual-checkpoint framework and language

Reading date: 2026-09-19. First-pass main-text reading, figure/table inspection, numerical/evidence checks and section-language curation complete. A separate acceptance source recheck has **not** been performed: review_status=not_reviewed.

## PMID 39385035 — 2024

**CTLA4 blockade abrogates KEAP1/STK11-related resistance to PD-(L)1 inhibitors.** Nature 635:462–471. DOI: 10.1038/s41586-024-07943-7. [Article](https://www.nature.com/articles/s41586-024-07943-7), [identity](https://pubmed.ncbi.nlm.nih.gov/39385035/).

Source: s41586-024-07943-7 (1).pdf, 42 physical pages; supplied corrected version with 2025 correction notice in the publication. SHA-256: 43eb81bea1e19a6b5060c6216c1ea74f1d3250e8c984529fa1157ac36a073a5c. Original publication year remains 2024; online 2024-10-09.

[Author correction, 2025-02-27](https://www.nature.com/articles/s41586-025-08767-9): author-name correction and bottom-right Fig1a KEAP1-mutant OS numbers at risk at 24/30 months changed from 1 to 0. The supplied figure was visually checked and shows 0 at both positions. The corresponding STK11 curve is a different panel; do not change it by analogy. A correction notice is version metadata, not a learning-corpus article.

### Classification and scientific interpretation

Primary: clinical-to-mechanistic dual-checkpoint immunotherapy. Secondary: STK11/KEAP1 co-mutations, clinical genomics, retrospective chemoimmunotherapy, exploratory randomized-trial biomarker subgroups, pooled in-vivo CRISPR/Tuba-seq, syngeneic/genetically engineered models, mouse scRNA-seq, human bulk immune deconvolution and multiplex immunofluorescence, flow cytometry, CD4/CD8/myeloid depletion, iNOS pharmacology. Direct STK11 context; user-designated highlight.

Question: whether adding CTLA4 blockade can address the immune context and reduced responsiveness associated with STK11 and/or KEAP1 alterations. Human associations and POSEIDON exploratory subgroup analyses are linked to experimental interventions; they are not one interchangeable evidence tier.

**STK11 and/or KEAP1 means the union**, including either single-mutant and double-mutant cases. It is not the double-mutant subgroup. Clinical benefit of TDCT versus chemotherapy and the numerical comparison against DCT are distinct. The latter OS CI includes 1. Individual STK11-only and KEAP1-only subgroup uncertainty must not be hidden behind pooled results.

### Coverage and supplementary scope

| Unit | Physical pages | Reading result |
|---|---|---|
| Abstract and introductory rationale | 1 | Clinical resistance problem, multimodal strategy, translational conclusion |
| Main Results, integrated discussion and closing | 2–8 | Human outcomes, trial biomarker subgroup, model resistance and immune mediators; no standalone Conclusion heading |
| Figures1–4 and captions | 2,4,5,7 | All main panels visually inspected and checked against text |
| Online Methods | 11–17 | Cohorts, endpoints, variant calling, CRISPR/Tuba-seq, models, scRNA, deconvolution, depletion and statistics |
| Declarations/data and other article metadata | 17–19 | Data availability and scientific context; not additional efficacy cohorts |
| ED Figures1–4 | 20–25 | Chemo/chemoimmunotherapy, trial outcomes, gene-specific and KRAS-stratified analyses |
| ED Figures5–8 | 26–32 | Tuba-seq/alternative combinations, mouse scRNA, human immune profiles, treated immune-cell states |
| ED Figures9–11 | 33–35 | Chemotherapy/immune changes, depletion controls, POSEIDON design and biomarker population |
| ED Tables1–2 | 36–37 | Baseline/missingness and genotype-specific TMB; image-only tables visually read |
| Reporting Summary | 38–42 | Experimental/statistical reporting and data-exclusion inconsistency below |

All embedded ED figures/tables and their captions were read. Separate external supplementary files, including referenced supplementary tables, were not supplied; supplement_status remains **partially_reviewed**, not fully reviewed. Reading a cited result in the main text is not reading the external file.

### Design and denominator ledger

- Retrospective 22-institution cohort: 871 total, CP432 and PCP439; treatment-era/nonrandomized comparisons and survival ≥14-day inclusion require selection/confounding caution.
- In PCP, STK11 OS119 mutant+320 WT=439; PFS119+317=436. KEAP1 OS42+103=145; PFS42+102=144. Joint-genotype response set is141, not439.
- The CP baseline table records missing STK11 status in6/432. Many KEAP1/TMB values are missing; missingness is not wild type or low TMB.
- FMI genomic cohort8592, including3224 KRAS-mutant. Fig1d caption's8836 conflicts with plotted group counts summing8592; do not publish a definitive PD-L1 denominator without disclosing this.
- POSEIDON:1013 randomized,637 nonsquamous,612 mutation-evaluable. STK11-mutant87 and KEAP1-mutant37 overlap in14, yielding110 in the union. Union arms TDCT42/DCT43/CT25; WT arms166/160/176. Tissue-only38, tissue+ctDNA334, ctDNA-only240 are assay populations, not independent patient cohorts.
- POSEIDON subgroup HRs are unstratified Cox estimates. Retrospective Fig1 HRs are multivariable-adjusted for age, ECOG and brain metastases, whereas displayed P values are log-rank tests; do not label them adjusted Cox P values.
- Variant definitions differ between real-world all-nonsynonymous criteria and trial functional/OncoKB criteria. Harmonization cannot be assumed.

### Central numerical checks

| Finding | Estimate / denominator | Source | Safe interpretation |
|---|---|---|---|
| PCP STK11 PFS | HR1.60 (95% CI1.24–2.07), log-rank P=.002; medians4.8/7.0 months | p2 Fig1a | Retrospective adverse association |
| PCP STK11 OS | HR1.55 (1.18–2.05), P=.014; medians11.1/16.7 months | p2 Fig1a | Not a randomized STK11-specific treatment effect |
| PCP STK11 ORR | 30.5% mutant versus40.9% WT; labeled NS | Fig1a | Do not upgrade to significant because survival differs |
| PCP KEAP1 | PFS HR2.07 (1.35–3.17); OS2.24 (1.42–3.54); ORR14.3%/43.0%, P<.0001 | Fig1a | Preserve gene/assay subset rather than pooling with STK11 |
| Joint-genotype ORR | WT48.6%, STK11-only29.6%, KEAP1-only28.6%, double7.1%; n72/27/14/28 | ED1b | Response-evaluable141, not all PCP439 |
| Mutation/TMB context | STK11/KEAP1 union25.2% overall and32.4% KRAS-mutant; median TMB WT5.22, STK11-only7.83, KEAP1-only13.05, double7.83 | Fig1b–d | STK11/KEAP1 alteration does not imply low TMB; KEAP1-only PD-L1 pattern differs |
| Union DCT versus CT | PFS HR1.00 (.57–1.77); OS.90 (.53–1.52) | Fig2 | No observed benefit is not statistical equivalence |
| Union TDCT versus CT | PFS HR.52 (.28–.95); OS.50 (.29–.87) | Fig2a–b | Exploratory randomized-trial biomarker subgroup, not an independently validated predictive rule |
| Union TDCT versus DCT | OS HR.64 (.40–1.04), medians15.8/7.3 months; PFS.71 (.43–1.17) | Fig2a–b | Both CIs cross1; do not say statistically proven superiority over DCT |
| Response and duration | ORR42.9%/30.2%/28.0%; median DoR13.6/12.7/3.3 months for TDCT/DCT/CT | Fig2a; ED2b | DoR is responder-conditional; spider plots show38/38/25, not the full42/43/25 |
| STK11-only exploratory outcome | TDCT vs CT OS.56 (.30–1.03); vs DCT.63 (.35–1.08) | ED3b | Individual STK11 subgroup uncertainty remains even when union CI excludes1 |
| Pooled CRISPR | 1813 sgRNAs/162 genes; Stk11/Keap1 among strongest enriched resistance hits | Methods; Fig3a–c | Experimental selection, not clinical mutation prevalence |
| Tuba-seq | 22 tumor suppressors+6 inert vectors;16–19 analyzed mice/group | Fig3d–e; ED5 | Multiple tumors nested within mice; tumors are not independent animal replicates |
| iNOS inhibition | KLK no-outgrowth7/7 with dual ICB versus2/7 with L-NIL plus dual ICB | Fig4e | Model-specific outgrowth endpoint, not seven clinical cures |
| Immune depletion | CD8 required in studied KK/KL5 models; CD4 and myeloid effects differ by model | Fig4c–d; ED10 | Do not generalize one cell-depletion result across all genotypes/models |

### Omics, basic experiments and statistical language boundaries

- Direct scRNA-seq is **mouse**, K/KK/KLK with two mice/group in ED6;10x5′, mm10 alignment, CellRanger/Seurat/Harmony/SingleR, UMAP and module scores. GEO GSE267321. Cell numbers do not replace biological mouse replication.
- Human TCGA/ICON immune inference uses bulk RNA-based deconvolution, including MCP-counter/quanTIseq/xCell, not directly measured human scRNA cell fractions.
- Human mIF ratio comparison has13 mutant-union versus19 WT; CD8 abundance has14 versus27 (ED7a). Different evaluable subsets must be kept separate.
- ICON n57 uses LKB1-deficient22/proficient35 and NRF2-high8/low49 signature groups; this is not the same partition as STK11-mutant8/KEAP1-only10/WT39.
- Multiplex imaging is not spatial transcriptomics; flow, immunoblot and iNOS readouts are not global proteomics.
- Preserve immune-cell denominators: live cells versus CD45-positive cells; relative ratios can rise through denominator depletion without an absolute numerator increase.
- Regulatory T cells were not depleted by dual ICB in these experiments. TH1/Treg ratio change must not be rewritten as Treg elimination.
- Mouse time to tumor volume ≥1200 mm³ is a surrogate event endpoint, not human OS. Control-group stopping times differ by experiment.
- Explanatory myeloid depletion is not a therapeutic recommendation to remove myeloid cells: some myeloid cells contributed to combination efficacy in the studied setting.
- Cross-subgroup significance patterns alone do not demonstrate a genotype-by-treatment interaction. Exploratory subgroup evidence and model causality remain distinct.

### Unresolved source conflicts: restricted from factual templates

1. **Fig1d denominator:** caption8836 versus plotted6427+1027+571+567=8592 and genomic cohort8592. Retain panel-specific figures; withhold an unqualified single PD-L1 cohort size.
2. **Alternative checkpoint model:** p6 prose labels KLK, but Methods p16, ED5h panel and caption pp26–27 label KL5. The visual panel confirms KL5 wording, but the source discrepancy remains; do not silently “correct” the entire paper.
3. **Tuba-seq duration:** p6/Fig3 timeline and ED5 refer to3 weeks after12-week growth/15-week readout; Methods p14 states2 weeks/14 weeks. Withhold exact duration as a reusable protocol fact pending clarification.
4. **Exclusions:** Reporting Summary p39 says no data excluded; Methods p15 describes excluding low-transduction mice below the stated tumor-cell threshold. Do not reuse an unrestricted no-exclusion statement.
5. Corrected Fig1a risk-table entries are version-controlled separately from these unresolved conflicts.

### STK11 writing-framework transfer

Use: real-world adverse association → disaggregate STK11 and KEAP1 → exploratory randomized regimen contrast → unbiased resistance screen → controlled genotype models → immune states → mediator-depletion/rescue logic → bounded clinical hypothesis. Cite experimental interventions only for the exact models/conditions, not all patients.

## Section-indexed language

Use [nature-section-language-catalog.csv](nature-section-language-catalog.csv) for section/function/domain/unit/tier/source-location retrieval. Entries are synthetic writing/translation frames, not copied sentences. Conclusion maps to the article's closing discussion, not an invented heading. This one-paper source set is not a Nature-wide style profile.

### Curated entries by article and section

Each row's source locator identifies the evidence/rhetorical context, not verbatim attribution of the synthetic wording. Term rows may group related conventional terminology. All constraints apply to the entire four-entry pack.

#### 39385035 — Abstract — multilevel evidence summary

Source: p1 Abstract. Use constraint: STK11和/或KEAP1是并集；不能把TDCT对CT结果改为TDCT对DCT显著。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| NAT-STK11-001 | vocabulary | dual checkpoint blockade 双检查点阻断; biomarker-defined subgroup 标志物定义亚组; innate immune effector 固有免疫效应细胞 |
| NAT-STK11-002 | collocation | integrate exploratory trial findings with functional models; overcome resistance in [specified model]; associate with [outcome] |
| NAT-STK11-003 | sentence_frame | We combined [clinical analyses] with [experimental systems] to evaluate whether [intervention] addresses [genotype-associated phenotype]. |
| NAT-STK11-004 | paragraph_architecture | Clinical problem → multilevel design → separate clinical/model findings → bounded translational conclusion. |

#### 39385035 — Introduction — regimen-specific gap

Source: p1 Introduction. Use constraint: 背景信息不能宣称当前所有试验结论；历史TRITON提及需另核最新状态。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| NAT-STK11-005 | vocabulary | regimen-specific resistance 方案特异耐药; immune contexture 免疫构成; actionable hypothesis 可检验干预假设 |
| NAT-STK11-006 | collocation | move beyond a uniformly resistant phenotype; distinguish single-gene and combined contexts; motivate combination testing |
| NAT-STK11-007 | sentence_frame | Whether [additional intervention] alters the adverse outcome pattern associated with [genomic context] remains an important question. |
| NAT-STK11-008 | paragraph_architecture | Known adverse association → regimen distinction → mechanistic uncertainty → clinical/model testing strategy. |

#### 39385035 — Methods — trial subgroup and real-world analysis

Source: pp11–13 Methods; Fig2; ED11. Use constraint: 可评价不等于ITT；回顾性调整HR与试验非分层HR分开；基线缺失不能归为WT。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| NAT-STK11-009 | vocabulary | mutation-evaluable subset 突变可评价亚集; unstratified Cox model 非分层Cox模型; multivariable adjustment 多变量调整; duration of response 缓解持续时间 |
| NAT-STK11-010 | collocation | define [either-gene union] separately from [double-mutant subset]; retain endpoint-specific cutoffs; analyze responders for [DoR] |
| NAT-STK11-011 | sentence_frame | Biomarker analyses were restricted to [evaluable set], with [union/single/double] groups defined explicitly and regimen comparisons reported separately. |
| NAT-STK11-012 | paragraph_architecture | Randomized population → biomarker-evaluable flow → operational variant criteria → endpoints/comparators → exploratory inference. |

#### 39385035 — Methods — single-cell and inferred immune states

Source: pp15–17 Methods; ED6–7. Use constraint: 两只小鼠/组不能以细胞数扩充生物学重复；mIF不是空间转录组；不同方法输出不等价。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| NAT-STK11-013 | vocabulary | batch integration 批次整合; cell-type annotation 细胞类型注释; module score 模块评分; digital deconvolution 数字反卷积 |
| NAT-STK11-014 | collocation | annotate clusters using [markers/reference]; integrate batches with [method]; infer immune composition from bulk profiles |
| NAT-STK11-015 | sentence_frame | [Mouse] single-cell profiles were analyzed using [workflow], whereas immune composition in [human cohort] was inferred from bulk expression data. |
| NAT-STK11-016 | paragraph_architecture | Biological sample and species → capture/QC → batch handling → annotation → abundance/signature testing → orthogonal validation. |

#### 39385035 — Methods — screening and mediator perturbation

Source: pp13–16 Methods; Figs3–4. Use constraint: 不得把Tuba-seq肿瘤数当独立小鼠；源文疗程/排除标准冲突不得照抄。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| NAT-STK11-017 | vocabulary | pooled genetic screen 混合遗传筛选; inert control guide 惰性对照向导; nested tumor sampling 嵌套肿瘤采样; depletion efficiency 清除效率 |
| NAT-STK11-018 | collocation | quantify guide enrichment relative to [control]; account for tumors nested within mice; verify depletion before interpreting efficacy |
| NAT-STK11-019 | sentence_frame | [Candidate genes] were tested by [screen], followed by genotype-controlled treatment and immune-cell perturbation experiments. |
| NAT-STK11-020 | paragraph_architecture | Screen controls and readout → follow-up model → intervention/depletion check → response endpoint → mediation limits. |

#### 39385035 — Results — clinical efficacy and uncertainty

Source: Fig1–2; ED1–4; ED11. Use constraint: union TDCT/DCT OS .64(.40–1.04)不能写显著优效；DCT/CT HR1不证明等效。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| NAT-STK11-021 | vocabulary | numerically favorable estimate 数值上有利的估计; null-crossing interval 跨无效值区间; responder-conditional duration 缓解者条件下持续时间 |
| NAT-STK11-022 | collocation | favor [regimen] numerically; retain uncertainty around the direct comparison; show no evidence of equivalence |
| NAT-STK11-023 | sentence_frame | [Regimen A] had a numerically favorable [endpoint] estimate versus [regimen B] (HR [value], 95% CI [lower–upper]), but the interval included 1. |
| NAT-STK11-024 | paragraph_architecture | Define genotype/analysis set → named regimen contrast → effect/uncertainty → distinguish CT and DCT comparisons → exploratory limitation. |

#### 39385035 — Results — immune composition and necessity

Source: Fig4; ED6–10. Use constraint: 比例增加不等于绝对增殖；Treg未被清除；小鼠无肿瘤长出不是临床治愈；保留未显著比较。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| NAT-STK11-025 | vocabulary | relative sparing 相对保留; myeloid enrichment 髓系富集; effector-memory CD4 cells 效应记忆CD4细胞; iNOS-expressing cells 表达iNOS的细胞 |
| NAT-STK11-026 | collocation | increase the [numerator/denominator] ratio; attenuate efficacy after [depletion]; vary across genetically defined models |
| NAT-STK11-027 | sentence_frame | [Intervention] altered [measured immune state]; depletion of [cell population] attenuated efficacy in [model], supporting a context-specific contribution. |
| NAT-STK11-028 | paragraph_architecture | Immune-state comparison → absolute/relative denominator → perturbation validation → efficacy change → cross-model qualification. |

#### 39385035 — Discussion — convergence and limitations

Source: pp6–8 integrated discussion. Use constraint: 不要宣称已证实所有STK11患者应加CTLA4；不得用动物显著性填补临床CI跨1。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| NAT-STK11-029 | vocabulary | convergent evidence 相互印证证据; biological plausibility 生物学合理性; exploratory signal 探索性信号; context-specific requirement 背景特异依赖 |
| NAT-STK11-030 | collocation | support rather than establish clinical prediction; separate population association from model necessity; require prospective confirmation |
| NAT-STK11-031 | sentence_frame | The convergence of [clinical observations] and [model interventions] supports [hypothesis], but does not eliminate uncertainty in [direct treatment comparison]. |
| NAT-STK11-032 | paragraph_architecture | Principal clinical signal → experimentally tested mechanism → gene/model heterogeneity → source/selection limitations → prospective comparison. |

#### 39385035 — Conclusion — closing hypothesis

Source: p8 closing discussion. Use constraint: 无单独Conclusion标题；这里是写作框架，不是处方建议或已验证治疗预测规则。

| Entry ID | Unit | Reusable language or architecture |
|---|---|---|
| NAT-STK11-033 | vocabulary | therapeutic rationale 治疗研究依据; prospective confirmation 前瞻性确认; genotype-informed strategy 基因型导向策略 |
| NAT-STK11-034 | collocation | provide a rationale for testing [combination]; prioritize validation in [defined setting]; preserve regimen-specific uncertainty |
| NAT-STK11-035 | sentence_frame | These findings provide a rationale for testing [strategy] in [defined molecular context], while prospective evidence is needed to establish its clinical utility. |
| NAT-STK11-036 | paragraph_architecture | Bounded cross-level synthesis → defined population/regimen → next validation requirement. |

