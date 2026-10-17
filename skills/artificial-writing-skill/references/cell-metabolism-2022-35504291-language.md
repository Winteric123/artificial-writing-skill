# Glutaminase inhibition, tumor metabolism and CD8 T-cell function

## PMID 35504291

Identity: Best et al., Glutaminase inhibition impairs CD8 T cell activation in STK11-/Lkb1-deficient lung cancer. Cell Metabolism 2022;34(6):874-887.e6. DOI 10.1016/j.cmet.2022.04.003; online 2022-05-02, issue 2022-06-07. [PubMed](https://pubmed.ncbi.nlm.nih.gov/35504291/). Supplied publisher-typeset main article, STAR Methods and embedded supplemental Figures S1-S6: 35 physical pages, SHA-256 9ee358e7d3b13c3806cc3d48761da5e1de5e583c07d54391a1aef18a00eb05c2. Main and embedded supplementary reading completed 2026-10-18. External Data S1 and repository source matrices were not supplied or reanalyzed. Article-level source learning; no journal-wide Cell Metabolism style or new STK11 highlight is established.

Classification: original mechanistic preclinical lung-cancer study integrating steady-state LC-MS metabolomics, isotope tracing, bulk RNA sequencing, flow cytometry, histology, genetic T-cell perturbation and human PBMC stimulation. Human TCGA/CCLE analyses are reanalyses. tSNE is applied to flow-marker measurements, not single-cell RNA sequencing; TCR V-beta repertoire measurement is flow cytometry, not TCR sequencing. K, KP, KK, KL and KKL are separately engineered genotypes, not interchangeable patient subgroups.

### Coverage and evidence reconstruction

| Source component | Physical pages | Actual review and inference boundary |
|---|---|---|
| Graphical abstract/highlights; Summary; Introduction | 1-3 | Read in full; graphical abstract inspected. Background clinical associations are cited prior work, not a new treated patient cohort. |
| Results and main Figures 1-6 with captions | 3-11 | All text read; Figures 1-6 visually inspected on pp4,5,6,7,8,10; captions include pp9,11. No main clinical efficacy table. |
| Discussion, therapeutic implications, limitations | 11-13 | Read in full. Combination survival was explicitly not evaluated. Anti-PD1-alone survival in S4G is a different experiment. |
| Acknowledgments, interests and references | 13-15 | Read for provenance; no new experimental findings inferred from citations. |
| STAR Methods and Key Resources Table | 16-21 | Read in full, including original assay details, repeated mouse samples, FDR and reagent/data accessions. Statistical wording has a source ambiguity described below. |
| Embedded supplement | 22-35 | Title/contents read; S1-S6 plots visually inspected pp24,26,28,30,32,34 and all captions read pp25,27,29,31,33,35. No separate Data S1 spreadsheet supplied. |

Question: do co-occurring Keap1 and Lkb1 losses impose the same tumor metabolic environment, and does glutaminase inhibition enhance anti-PD1 immune activity in an immune-competent autochthonous model?

| Evidence layer | Source-grounded result / implemented method | Boundary |
|---|---|---|
| Model latency | KK n19, KL n9, KKL n12; reported median latencies 71,48,49 days; Figure1 Mantel-Cox P<.0001 (pp3-4). | Tumor-model latency/survival is not survival after combination therapy or human prognosis. |
| Steady-state metabolomics | KK n5, KL n5, KKL n4 tumor samples; genotype-associated PCA separation and differential metabolite abundance. KL-v-KK Figure2 volcano labels 122 up,45 down,545 nonsignificant (pp4-5). | PCA separation does not prove a predictive classifier; abundance is not metabolic flux. Within-lung sampled pieces are not independent mice. |
| Isotope tracing | U-13C,U-15N-glutamine 15-minute pulse; UN/KL/KKL n5 mice per arm, four tissue/tumor pieces per mouse. Approximately60-70% labeled Gln pool; increased labeled Glu/Asp supports altered glutamine usage (pp4,6,20). | Isotopologue labeling supports a pathway interpretation within this experiment; it does not uniquely establish every possible biochemical route. |
| RNA / patient context | Original mouse bulk RNA-seq: n5 mice per tumor genotype,2 tumors/mouse, UN n6; TMM/voom-quality weights/limma, duplicateCorrelation for repeated tumors, BH FDR<.05 (pp19-20). TCGA and CCLE GLS1-expression comparisons are external reanalyses (pp6,21). | Bulk transcripts and human cell-line correlations do not directly measure patient intratumoral metabolic flux or clinical treatment benefit. |
| Genetic immune test | Adoptively transferred Gls1-deficient/control P14 CD8 cells; LCMV expansion assessed on days6,13; donor groups n10 and n9; expansion impaired after deletion (pp6-7,19). | Viral-antigen expansion supports a T-cell dependency but is not a tumor-specific response experiment. |
| Combination pharmacodynamics | KL treatment starts day20, harvest day29; CB-839 200mg/kg twice daily; vehicle/isotype, vehicle/anti-PD1, CB-839/isotype, CB-839/anti-PD1. Figure5 cohorts n6/6/4/6; short treatment showed no overall lung-weight or bulk CD45/CD3 change, while flow-defined TCR V-beta-family expansion and effector activation were reduced by combination (pp7-11,19,30-31). | Lung weight is a coarse burden measure; a short-term null does not establish equivalence. V-beta families are not sequence-resolved clonotypes. No combination OS experiment. |
| Effector phenotype | Figure6 cohorts generally n4/4/3/4; anti-PD1-associated IFN-gamma and GzmB activation was reduced with CB-839; vehicle/anti-PD1 vs combination P=.036 and .037 respectively (pp10-11). | Marker-defined activity and ex-vivo stimulation are not direct patient tumor killing. Multiple marker comparisons require their own reported testing context. |
| Human PBMC support | SEB-stimulated PBMCs, glutamine titration0-10mM, anti-PD1/isotype, IFN-gamma ELISA. Figure6D first significant displayed concentration0.37mM, P=.0042; higher concentrations P<.0001 (pp10-11,19,34-35). | Donor count not clearly specified in supplied main methods; this is an in-vitro human immune-cell assay, not a treated NSCLC cohort. |

The defensible conclusion is that the tested CB-839/anti-PD1 schedule impaired CD8 effector activation in these immune-competent Lkb1-deficient models despite the metabolic rationale. Tumor-cell metabolic dependence does not automatically predict a favorable immune combination. Dose/schedule alternatives, the relatively low immunogenicity of GEMMs and indirect TME cross-talk remain unresolved (p12).

### Source alerts and transfer limits

1. STAR Methods p21 juxtaposes one-way ANOVA with Kruskal-Wallis and couples Tukey/Dunn terminology in an ambiguous way; captions name ordinary one-/two-way ANOVA or unpaired t tests. Preserve the actual caption-specific test when reporting a result; do not copy the generic statistical sentence as an executable protocol.
2. The tracing LC-MS Methods p20 describes positive/negative ionization but later says the instrument scanned in negative mode for both. Reproduction requires instrument/source data clarification; learning assay language does not resolve that sentence.
3. Main p11 says anti-PD1 benefit occurs above0.37mM Gln, whereas Figure6D already labels a significant comparison at0.37mM. Use the plotted tested concentrations; do not invent a continuous biological threshold or silently call0.37 a validated cutoff.
4. Relative signal intensity, normalized abundance, Gln/Glu and fractional isotopic enrichment are distinct quantities. Main Figures2/3 and S1/S2 use different normalizations/cohorts; a shared metabolite name is not permission to pool numerical values.
5. S4G tests anti-PD1 alone versus isotype. The explicit limitation that combination OS was not evaluated governs any survival claim. Do not convert impaired immune pharmacodynamics into proven worse combination survival.
6. Data S1/source repositories remain outside the supplied PDF scope. Reading embedded S1-S6 does not certify spreadsheet-level raw values. Direct T-cell-autonomous causality is limited by TME cross-talk, and the LCMV experiment cannot remove all tumor-context alternatives.

All bracketed frames below are synthetic abstractions; terms are conventional. Physical pages locate the source logic. User-provided evidence must supply every slot.

### Abstract background
- `Tumor and immune cells may share metabolic requirements within [microenvironment].` 用于解释靶向代谢的细胞区室权衡；pp2-3。

### Abstract methods
- `We combined [metabolomic assay], [transcriptomic assay] and [functional perturbation] in [genetically defined models].` 仅列实际实施的模态，临床与小鼠分析分开；pp2-3,16-21。

### Abstract results
- `[genotype] was associated with [metabolic state], whereas [combination] reduced [immune function] under the tested conditions.` 用分层结果保留机制阳性与组合负向结果；pp2,7-11。

### Abstract conclusion
- `[metabolic dependency] may coexist with an immune-cell liability that constrains [combination strategy].` 前临床限制，不作患者治疗选择；pp2,12。

### Introduction vocabulary
- `autochthonous tumor model` 原位自发形成的工程肿瘤模型；p3。
- `compartment-specific metabolic dependency` 不同细胞区室的代谢需求；pp3,12。
- `immune-competent microenvironment` 保留免疫系统的微环境；pp3,12。

### Introduction frames
- `Although [target] supports tumor metabolism, its role in [immune population] may alter the effect of systemic inhibition.` 肿瘤依赖导向免疫副效应假设；pp3,12。
- `We compared [single-loss] and [combined-loss] models to distinguish shared from genotype-specific phenotypes.` 要求确有这些独立模型；p3。

### Methods vocabulary
- `steady-state metabolomics` 稳态代谢组，不等于通量；pp3,20。
- `fractional isotopic enrichment` 同位素分数富集；p20。
- `within-mouse repeated samples` 同鼠重复肿瘤样本；pp19-20。
- `marker-based TCR V-beta repertoire analysis` 流式V-beta面板，不能写作TCR测序；pp7,19。
- `authentic-standard confirmation` 标准品确认代谢物；p20。

### Methods frames
- `[metabolites] were profiled at steady state, and isotope tracing was used separately to examine [substrate utilization].` 分清丰度与动态示踪；pp3-6,20。
- `Correlations between repeated samples from the same [experimental unit] were accounted for using [implemented method].` 只能填实际使用的相关性处理；p20。
- `Metabolites were annotated using [mass/retention evidence], with [specified subset] confirmed against authentic standards.` 保留MSI2与MSI1确认层级；p20。
- `[cell state] was characterized by flow cytometry using [markers], followed by [dimensionality-reduction procedure].` 不升级为单细胞转录组；pp9,19。

### Results vocabulary
- `genotype-associated metabolic separation` 基因型相关的代谢分离；pp3-5。
- `substrate-to-product labeling` 底物到产物标记；pp4,6。
- `blunted effector differentiation` 效应分化减弱；pp9-12。
- `limited short-term burden change` 短程负荷变化有限；pp7,30-31。

### Results frames
- `[groups] separated in [exploratory representation], with differences in [specified features] supporting a genotype-associated metabolic pattern.` 探索性图谱与特征差异分开，无分类器验证暗示；pp3-5。
- `Despite similar steady-state abundance of [substrate], [group] showed greater labeling of [product] in the tracing experiment.` 仅在相应测量均存在时比较；pp4-6。
- `No change in [bulk endpoint] was detected over [interval], although [cell-specific assay] identified [functional difference].` 阴性总体指标不抹掉正交功能发现；pp7-11,30-31。
- `The increase in [marker] with [monotherapy] was attenuated when [second intervention] was added.` 需直接组合对照；不能由两组各自P值推断交互；pp10-11。
- `[cell subset] changed in [compartment], whereas the corresponding pattern was not detected in [other compartment].` 组织与外周区别，不直接证明统计交互；pp9,32-35。

### Discussion vocabulary
- `therapeutic window` 治疗窗（有效性与毒性之间的剂量或暴露范围），不等同于治疗时间窗；p12。
- `tumor-immune metabolic trade-off` 肿瘤与免疫代谢权衡；pp11-12。
- `combination effect under the tested schedule` 限于被测试的给药安排，未比较多个给药方案；p12。

### Discussion frames
- `Although [mechanistic rationale] supported the combination, the observed impairment of [immune function] limits that expectation under [tested conditions].` 机制合理性与实验反证并存；pp11-12。
- `The absence of a [survival/clinical] endpoint prevents inference about [patient or model benefit], despite the pharmacodynamic effect.` 没测量不等于阴性；p12。
- `An alternative dose or schedule could yield a different balance, but this possibility remains untested.` 保留作者未排除的替代安排；p12。

### Conclusion frames
- `These findings support evaluating both tumor-cell and immune-cell consequences before advancing [metabolic combination].` 研究用途；不把前临床药效学转成临床建议；p12。

### Results paragraph
- `Define the genotype-specific metabolic pattern; distinguish abundance from isotopic labeling; test the immune dependency genetically; report combination pharmacodynamics alongside bulk null findings; close with the endpoint that was not measured.` 合成结果架构；单时间点标记不是直接定量的绝对通量；pp3-12。

### Discussion paragraph
- `Return to the original combination hypothesis; explain the cell-compartment trade-off; reconcile the functional effect with unchanged short-term burden; state the missing survival endpoint and model limits; propose schedule testing as future work.` 合成讨论架构；pp11-12。
