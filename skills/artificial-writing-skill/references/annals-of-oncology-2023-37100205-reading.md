# PMID 37100205 — spatial immune phenotyping in resectable NSCLC

## Identity and reading scope

- *Machine learning-based immune phenotypes correlate with STK11/KEAP1 co-mutations and prognosis in resectable NSCLC: a sub-study of the TNM-I trial*; M. Rakaee et al.; *Annals of Oncology* 2023;34:578-588; online 2023-04-24.
- PMID [37100205](https://pubmed.ncbi.nlm.nih.gov/37100205/); DOI [10.1016/j.annonc.2023.04.005](https://doi.org/10.1016/j.annonc.2023.04.005).
- Publisher-typeset PDF, 11 physical pages; SHA-256 `e293e86e112ed531582217f92e797225c086e70bfe0e695444ca71cf05e7e65b`.
- Main text, all five figures and Table 1 read, with visual inspection, on 2026-10-02 by `/root/intake_registry_audit`. First-pass complete, **review_status=not_reviewed**. Source inconsistencies below remain disclosed, not silently resolved.
- Separately linked supplementary figures/tables and detailed methods were not supplied and were not reviewed; **supplement_status=not_supplied**. Main-text descriptions of supplemental findings are not direct supplemental verification.

## Study question and design

The study asks whether quantitative spatial CD8 immune phenotypes can augment prognostic characterization of resected stage I-IIIA NSCLC, and which molecular features accompany non-inflamed tumors. It comprises two distinct cohorts: prospective Scandinavian TNM-I (453, enrolled 2016-2022) and retrospective northern-Norway UNN (481, surgery 1990-2010). These are not two prospective cohorts. Both were classified under updated stage/histology rules, but differ substantially in era, smoking, surgery, sex and histology.

CD8/pan-cytokeratin IHC whole-slide images were analyzed in QuPath with pathologist-supervised machine learning for tumor/stromal segmentation and cell detection. This is **spatial digital pathology**, not spatial transcriptomics, single-cell sequencing or an unsupervised deep-learning pipeline. Algorithms trained in TNM-I were applied to UNN without modification. However, the CD8 cutoffs were derived from quartiles of the **entire material**, so “independently locked external threshold validation” is too strong.

Molecular assays were limited to TNM-I subsets: targeted DNA panel n=215 (TSO500, 523 genes), targeted NanoString IO360 RNA expression n=132 (770 immune genes, 39 signatures). This is neither WES nor untargeted RNA-seq. The mutation plots separately analyze LUAD n=137 and LUSC n=68; these do not sum to all 215 because the complete cohort also contains other histologies. No copy-number variant analysis was included.

Outcome associations were tested **only in retrospective UNN**, because prospective follow-up was short. Prognostic associations are not evidence of treatment-predictive performance for ICI; these were primarily surgical cohorts, without a randomized ICI comparator or a gene-by-treatment interaction.

## Coverage map

| Content | Physical pages | Scope |
|---|---|---|
| Structured Abstract | 1 | Background/design/results/conclusion checked against full Results |
| Introduction, Patients and Methods | 2 | Cohort origins, assay subsets, classifier and cutoffs |
| Results, Figure 1 | 3 | Segmentation workflow, example IHC and phenotype distributions |
| Table 1, Results | 4 | Cohort differences, all rows/footnotes visually checked |
| Figure 2 | 5 | Immune signature scores, PD-L1 IHC, pathway contrasts/GSEA |
| Figure 3 | 6 | OncoPrints, genotype enrichment, TMB/CD8 negative associations |
| Figure 4 | 7 | Histology/stage distribution and targeted transcriptomic contrasts |
| Figure 5 | 8 | DSS/TTR curves, DSS adjusted forest plot and performance radar plots |
| Discussion, limitations, Conclusion | 7-9 | Cutoff uncertainty, no prospective outcome validation, prognosis versus prediction |
| Funding, disclosures, references | 10-11 | Surveyed; no embedded supplement |

## Central findings and numerical checks

| Finding | Population / result | Locator / boundary |
|---|---|---|
| Image-method agreement | Randomly selected n=100 excluding training set: stromal CD8 count ICC .99, intratumoral .98 versus manual annotations | p3; agreement is not clinical outcome prediction accuracy |
| Operational thresholds | Figure 1 labels desert: intratumoral <88 and stroma <814 CD8/mm2; altered: intratumoral >=88 and stroma <814; inflamed: both >= respective thresholds | p3 Figure 1B; labels do not explicitly resolve the fourth possible low-tumor/high-stroma quadrant; no invented rule |
| Phenotype frequencies | Total n=934: inflamed 24.4%, altered 51.3%, desert 24.3%; TNM-I 15%,58.1%,26.9%; UNN 33.5%,44.7%,21.8% | p3; pooled frequency not prospective-only |
| Immune expression | Adaptive signatures rise from desert to inflamed; macrophage and dendritic signatures associated, mast/neutrophil/NK signatures not individually associated | pp3-5; signatures are bulk targeted-expression measures, not direct cell counts |
| PD-L1 discordance | No association with checkpoint-gene RNA expression described; PD-L1 IHC >=50% tumors more often inflamed (25%) versus PD-L1-negative (8%) or 1-49% (10%), chi-square P<.001 | p4, Figure 2B p5; RNA and protein assays are not interchangeable |
| STK11 and KEAP1 | LUAD STK11 mutation frequency 21%, KEAP1 14%; inflamed-versus-non-inflamed ORs STK11 .39, Q=.04; KEAP1 .27,Q=.02 | pp4-6; reciprocal OR not calculated; figure/denominator alerts below |
| Co-occurrence | STK11/KEAP1 and TP53/KEAP1 co-occurrence in non-inflamed LUAD, reported P<.001 | p5 narrative referring to absent Figure S13; not a new functional interaction test |
| Other genotype signals | ATM OR4.1,Q=.03 and NF1 OR7.5,Q=.03 enriched in inflamed LUAD; no mutation association identified across LUSC phenotypes | pp4-6; tumor-type restriction retained |
| TMB negative evidence | Overall median8.6 mutations/Mb (range .6-41); no phenotype-specific median difference and no CD8-density difference between TMB<10 (n130) and >=10 (n85) | pp5-6 Figure 3D; no equivalence claim |
| Follow-up | TNM-I median25 months (IQR17-36), UNN83 (45-122) | p6; outcome models only UNN |
| UNN outcome | Inflamed/altered/desert five-year DSS71%/57%/46%, P=.002; five-year TTR64%/51%/41%, P=.003 | Figure5A p8; not OS or recurrence incidence |
| Adjusted DSS | Inflamed vs desert HR.61 (95%CI .41-.91), P=.016; altered vs desert HR.73 (.51-1.04), P=.079 | Figure5B p8, p7 prose; adjusted for pathological stage,histology,ECOG,gender |
| TTR model | Abstract reports HR.65,P=.02; detailed adjusted model resides in absent FigureS18 | p1,p7; no CI invented and not independently checked against S18 |
| Histology-specific outcome | Positive association in LUSC (DSS/TTR P=.01), not significant in LUAD | pp6-9; don't attribute aggregate prognostic effect specifically to STK11-mutant LUAD |
| Discrimination | DSS AUC: stage .66 vs immune phenotype .58; TTR .63 vs .56 | p7,Figure5C; modest discrimination, not a clinically decisive classifier |

## Source conflicts and restrictions

1. **Genomic phenotype counts:** p4 and Figure3C label inflamed LUAD n=72 and non-inflamed n=65. This is difficult to reconcile with only15% inflamed among all453 TNM-I cases (approximately68). No supplied supplementary cohort flow resolves the discrepancy. Retain the authors' quoted subgroup labels when necessary with this warning; do not derive patient-level counts or assert reconciliation.
2. **Q-value caption:** Figure3C caption says Q<.01, whereas Results gives .02,.04,.03,.03 for displayed genes. Quote gene-specific Results values with locator, not the caption threshold; do not call STK11 Q<.01.
3. **Stage count:** Table1 gives stageIIIA200 (83+117), while Figure4A labels210. Use Table1 for documented cohort composition with explicit discrepancy if exact stages matter.
4. **DSS rounding:** Abstract gives P=.01, full Results/Figure5B give P=.016. Use full model estimate and CI for precision; not evidence of two distinct analyses.
5. **Pathway contrast:** NF-kB direction depends on comparison; Figure2C has positive inflamed-versus-desert directed score, whereas Figure2D negative noncanonical-NF-kB enrichment is inflamed-versus-altered. Do not reduce this to an unqualified “all NF-kB activity is highest in desert tumors,” or infer a perturbation mechanism.

These conflicts constrain exact numerical reuse and prevent any claim of error-free independent acceptance. They do not justify deleting the study or concealing its main-text reading.

## Interpretation and STK11-topic role

Direct clinical-correlative evidence links individual STK11/KEAP1 mutations and their co-occurrence to less-inflamed spatial phenotypes in resected LUAD. The study does not demonstrate that these mutations cause exclusion, does not test an STK11 drug intervention, and does not establish ICI resistance clinically in this cohort. Its strongest transferable contribution is the multi-layer design: reproducible digital-pathology phenotype, molecular association, then separately bounded prognostic validation. The prognostic signal's restriction to LUSC matters particularly when using the LUAD mutation findings.

## Section language and safe transfer

All frames are synthetic. Conventional phrases are terminology, not verbatim quotation claims.

| Section/function | Unit | Expression/frame | Locator / usage |
|---|---|---|---|
| Abstract background | vocabulary | spatial immune phenotype; immune-cell exclusion | pp1-2; distinguish phenotype from mechanism |
| Abstract methods | sentence-frame | We classified [specimens] using [image-based assay] and examined molecular correlates in separately defined subsets. | pp1-2; do not imply paired data for all samples |
| Abstract results | sentence-frame | [Alteration] was enriched in [phenotype], whereas outcome associations were evaluated in [distinct cohort]. | pp4-8; genotype and survival analyses have different cohorts |
| Introduction | collocation | heterogeneity within anatomical stage | p2; define a rationale for an added biomarker |
| Introduction | paragraph-frame | Describe residual prognostic variation; motivate spatial rather than aggregate immune measurement; state classifier and molecular questions separately. | p2 |
| Methods | vocabulary | pathologist-supervised pixel classification; whole-slide image analysis | pp2-3; not unsupervised deep learning |
| Methods | sentence-frame | The classifier was applied without modification to [cohort], while [cutoffs] were derived from [specified material]. | pp2,8; disclose cutoff leakage/generalizability boundary |
| Methods | collocation | targeted immune-expression panel | pp2-3; not whole-transcriptome sequencing |
| Results | sentence-frame | Agreement with manual annotation was quantified using [agreement statistic] in [held-out sample]. | p3; not diagnostic sensitivity |
| Results | sentence-frame | After adjustment for [covariates], [phenotype] was associated with [endpoint] (HR [value],95% CI [limits]). | pp7-8; prognostic, not treatment-predictive |
| Results null | sentence-frame | No statistically supported association was identified between [measure] and [phenotype] in [analysis set]. | pp5-6; does not prove absence |
| Discussion | collocation | hypothesis-generating classification threshold | p8; no validated clinical cutoff implied |
| Discussion | sentence-frame | The molecular and survival analyses were conducted in different cohorts, limiting direct linkage of [genotype] to [clinical outcome]. | pp2,6-9; explicit synthesis, not source quotation |
| Discussion | paragraph-frame | Separate analytical agreement, biological association and clinical discrimination; retain histology-specific null results; close with prospective validation needs. | pp7-9 |
| Conclusion | sentence-frame | The approach provides a candidate framework for [risk characterization], requiring prospective validation before clinical use. | p9 |
| Figure/table | sentence-frame | The heatmap depicts [assay-specific score], not a direct measurement of [cell abundance/pathway activity]. | Figures2,4; avoid bulk-to-cell inference |

Safe hypothetical transfer: “In [N] resected LUADs, [gene] alterations were associated with [spatial phenotype]. Whether this association predicts benefit from [therapy] was not tested.” Unsafe: “STK11/KEAP1 mutations caused immune exclusion and predicted immunotherapy failure in the TNM-I trial.”
