# Six-paper co-alteration scope, 2026-10-07

Article-level topic curation after the complete first supplied-PDF reads, with targeted source-context reopening by the assigned readers. This is not independent six-gate acceptance, external-supplement reading or an exhaustive gene-pair map. Sequence co-mutation and broad genomic co-alteration are distinct. Descriptive or negative analyses can qualify as analyzed; individual covariates, protein expression and drug combinations do not by themselves qualify.

The authoritative machine records are in [coalteration-annotations.json](coalteration-annotations.json); see [classification rules](coalteration-topics.md) and [batch overview](ccr-2026-10-07-intake.md).

## PMID 34074656

[PubMed](https://pubmed.ncbi.nlm.nih.gov/34074656/) — CDKN2A Alterations and Response to Immunotherapy in Solid Tumors

Sequence co-mutation: not_identified; broad co-alteration: analyzed.

Actual evidence:

物理p8 Discussion报告本研究TCGA BLCA分析中，CDKN2A纯合删除样本的43%同时删除9p21.3邻近干扰素基因簇的一部分或全部。这是实际描述性共删除结果，可判广义共改变analyzed，但不是序列共突变。没有在所供全文识别到独立的序列双突变结果，因此窄义co_mutation为not_identified。

Physical PDF contexts reopened for this topic check: 8.

Boundary: 旁邻区域共删除不等于序列共突变；43%的分母是CDKN2A纯合删除TCGA BLCA样本，不是全部TCGA样本或ICI病例。该共删除与免疫耐药关系仅假说，不增添treatment_outcomes或immune_context作为已实测共删除效应。gene_contexts只登记CDKN2A，不凭基因簇笼统名补造具体IFNA/IFNB/IFNG配对；p2 CDKN2A/CDKN2B文献背景不是本篇新共删除结果。没有STK11直接证据。not_identified不是全文生物学阴性保证。

[Full reading note](ccr-2021-34074656-reading.md). Main-read/review/supplement states are unchanged.

## PMID 33272981

[PubMed](https://pubmed.ncbi.nlm.nih.gov/33272981/) — A Performance Comparison of Commonly Used Assays to Detect RET Fusions

Sequence co-mutation: not_identified; broad co-alteration: analyzed.

Actual evidence:

p5实际描述4例EGFR激活突变肺癌（2例exon19 deletion、2例L858R）在EGFR TKI治疗背景下检测到RET融合；p3比较RNA阳性GroupC与RNA阴性GroupD的其他并存驱动改变比例0%与60%，P=.0006；p5 Table1及p6 Figure2A给出实际共驱动景观。故广义共改变analyzed，但EGFR序列变异+RET融合不是两个序列突变，不能升级窄义co_mutation。

Physical PDF contexts reopened for this topic check: 3, 4, 5, 6.

Boundary: 序列变异加融合属于广义共改变，不是序列双突变；融合两端基因不能作为两次独立事件。4例EGFR/RET观察支持耐药背景，不能从单次检测推定同克隆、因果协作或所有病例均有本研究配对前后测序证明新获得。6/151是作者定义的non-RET driver集合，含激素表达，不可整体称6例基因共改变；选择仅EGFR/RET作为明确基因组合。Table1脚注列ERBB2扩增为非RET驱动示例，但未逐例定位，故本建议不新增RET/ERBB2特定共改变配对或copy_number_gain标签。BRAF/RET互斥在p3属于阴性对照选择依据，不当作新的无偏互斥检验。RET单基因context表示与未逐一转录的驱动指标比较，不推定所有GroupD结构变异都是功能融合。无直接STK11分析。

[Full reading note](ccr-2021-33272981-reading.md). Main-read/review/supplement states are unchanged.

## PMID 32241817

[PubMed](https://pubmed.ncbi.nlm.nih.gov/32241817/) — Identification of Deleterious NOTCH Mutation as Novel Predictor to Efficacious Immunotherapy in NSCLC

Sequence co-mutation: analyzed; broad co-alteration: analyzed.

Actual evidence:

- TP53_KRAS_comparison: TP53 and KRAS co-mut versus mono-mut + WT in EGFR/ALK-WT atezolizumab-treated POPLAR/OAK subset
- PFS_univariable: HR0.75,95%CI0.45-1.26,P=.273
- OS_univariable: HR0.78,95%CI0.41-1.46,P=.430
- multivariable_coefficients_for_pair: not displayed

Physical PDF contexts reopened for this topic check: 4, 11.

Boundary: 该共突变标签由实际TP53/KRAS双突变对照分析和逐样本图谱支持；两项结局比较均不显著，不是因果协同或治疗交互。这里只保留明确的TP53/KRAS基因对，不从Figure1扁平基因名单生成所有组合。NOTCH1/2/3分组本身是家族突变分类/并集，不等于同一肿瘤的三突变；STK11和KEAP1单独协变量共同入模并非STK11/KEAP1共突变分析，因此不在此记录加入该基因对。未从统计Methods提及fraction of CNA而推定实际CNV共变异结果。非穷尽基因对标注，外部补充未读。

[Full reading note](ccr-2020-32241817-reading.md). Main-read/review/supplement states are unchanged.

## PMID 31694835

[PubMed](https://pubmed.ncbi.nlm.nih.gov/31694835/) — Organoid Cultures as Preclinical Models of Non-Small Cell Lung Cancer

Sequence co-mutation: not_identified; broad co-alteration: analyzed.

Actual evidence:

- same_gene_context: PDXO426 KRAS G13C mutation plus KRAS amplification, reported in patient/PDX/organoid
- cross_gene_context: PDXO426 KRAS amplification and CDKN2A deletion, stated on physical p8
- comparison_scope: nine long-term model groupings,23 related specimens; genomic/source concordance and selected preclinical drug testing

Physical PDF contexts reopened for this topic check: 7, 8.

Boundary: KRAS序列突变+扩增不是同基因双序列突变，故不加same_gene_compound，也不标co_mutation_status=analyzed。KRAS与CDKN2A分别含扩增/缺失成分，不能改写为双点突变。Fig3A是不同标本之间突变一致性/总量热图，不是逐基因共突变oncoPrint；主文列TP53/DDR2/KRAS/KEAP1/CUL3/NOTCH等是跨模型出现的基因清单，不能任意配对。p8的FGFR1扩增属于另一个PDXO274模型，不与PDXO426的KRAS/CDKN2A拼成三基因背景。药物组合和磷蛋白共抑制不算基因组共变异。单模型药敏不证明KRAS/CDKN2A合作机制或患者治疗获益。未定位序列共突变只限本次主文判断，未提供S3等补充可含其他变异，不构成全文库或生物学不存在断言。

[Full reading note](ccr-2020-31694835-reading.md). Main-read/review/supplement states are unchanged.

## PMID 35802677

[PubMed](https://pubmed.ncbi.nlm.nih.gov/35802677/) — DNA Methylation Profiling Identifies Subgroups of Lung Adenocarcinoma with Distinct Immune Cell Composition, DNA Methylation Age, and Clinical Outcome

Sequence co-mutation: analyzed; broad co-alteration: analyzed.

Actual evidence:

Physical p7 Figure3: each column is one of88 tumor samples, with aligned EGFR/KRAS/TP53/STK11/KEAP1/ATM mutation annotation rows. This is an actual per-sample multi-gene descriptive landscape, not merely six separate marginal tests. The p7 prose additionally describes subgroup6 as TP53-mutant without mutations in the other five drivers.

Physical PDF contexts reopened for this topic check: 7.

Boundary: Analyzed qualifies only as a descriptive patient/sample-level genomic landscape. No pair-specific enrichment, interaction, common clone, causal synergy, STK11 co-mutation survival effect or treatment prediction is established. Six flat gene contexts must not be expanded into all possible positive pairs. The separate single-gene DNAm-age and immune comparisons are not the basis for the co-mutation label. Methylation/immune composition and IHC are not genomic alteration types. No copy-number or fusion type added; external SupplementaryS7 not independently inspected.

[Full reading note](ccr-2022-35802677-reading.md). Main-read/review/supplement states are unchanged.

## PMID 34921025

[PubMed](https://pubmed.ncbi.nlm.nih.gov/34921025/) — HER3 Augmentation via Blockade of EGFR/AKT Signaling Enhances Anticancer Activity of HER3-Targeting Patritumab Deruxtecan in EGFR-Mutated Non-Small Cell Lung Cancer

Sequence co-mutation: analyzed; broad co-alteration: analyzed.

Actual evidence:

Physical p4 explicitly calls MYCN/RB1/TP53 sequence variants and MYC amplification concomitant to the EGFR-mutant context. Figure1C p5 maps baseline variants per patient. Figure3A p7 maps EGFR-activating variants, T790M, EGFR/MET/HER2 copy gains and additional alterations in posttreatment samples; Figure3B shows patient-specific T790M acquisition and MET/HER2 copy changes.

Physical PDF contexts reopened for this topic check: 4, 5, 7.

Boundary: EGFR activating plus T790M variants are same-gene compound status, not a two-gene co-mutation; no cis/trans phasing is established. EGFR mutation plus EGFR/MET/ERBB2 copy gain is broad co-alteration, not two sequence mutations. Figure3 annotates posttreatment measurements and marks pre-existing events with asterisks; do not call every displayed alteration acquired. Missing gray cells are not wild-type. Gene contexts are selected, not an exhaustive or all-pairs map; no STK11 label. HER3 protein augmentation, EMT expression, ADC combinations and small-cell histologic conversion are not themselves genomic co-alterations. This supports resistance-context description and HER3-association analysis, not a validated co-mutation treatment-prediction rule.

[Full reading note](ccr-2022-34921025-reading.md). Main-read/review/supplement states are unchanged.
