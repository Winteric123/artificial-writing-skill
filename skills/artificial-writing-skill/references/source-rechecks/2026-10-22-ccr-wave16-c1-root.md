# CCR full-corpus six-gate source recheck — wave16-c1-root

Review date: 2026-10-22. Reviewer: `/root`. Method: same-agent source recheck of every main-text section and every main figure, table, and caption on the registered rendered PDFs. Text extraction was used only for navigation. No separate supplement was supplied. All six records received a bounded `passed` verdict; the source alerts below remain mandatory.

## PMID 33323401 — Efficacy and Biomarker Analysis of Camrelizumab in Combination with Apatinib in Patients with Advanced Nonsquamous NSCLC Previously Treated with Chemotherapy

- Source: publisher PDF, 10 pages, SHA-256 `4213d99a43342b117c98dc2e82b79d6726197b186ffd1a6e4a03659b27c176cd`; DOI `10.1158/1078-0432.CCR-20-3136`.
- Coverage: complete pp1–10; Figures 1–3 and Tables 1–3 on pp3–7 visually checked.
- Verified result: 94 response-evaluable patients had ORR 30.9%; all-treated ORR was 27.6%, median PFS 5.7 months, and median OS 15.5 months. In the 46-patient genotype set, STK11/KEAP1-altered versus double-wild-type tumors had ORR 42.9% versus 28.1% (`P=.33`), DCR 92.9% versus 65.6% (`P=.053`), and no significant overall PFS or OS difference. The nominal 12-month OS contrast is exploratory.
- Safety: grade 3–5 treatment-related adverse events 69.5%, with two treatment-related deaths.
- Boundary: single-arm estimates cannot identify component effects, reverse molecular resistance, or establish a predictive biomarker; a local safety prose/table discrepancy is governed by the table.
- Source sentence → type → scenario → template: “There was no significant difference in ORR between patients with PD-L1–positive tumors and patients with PD-L1–negative tumors.” → negative exploratory efficacy–biomarker comparison → nonsignificant biomarker subgroup result in a small single-arm study → `The [endpoint] was numerically [higher/lower] in [group A], but the between-group comparison was not statistically significant; given the small single-arm subset, this finding does not establish biomarker independence or a treatment interaction.`
- Gates: all six `pass`. Verdict: `passed` with the stated limits.

## PMID 33272981 — A Performance Comparison of Commonly Used Assays to Detect RET Fusions

- Source: publisher PDF, 14 pages, SHA-256 `36900a46c1604b8bda24c00911a33009effd465eb7e68f69384f8936b58d6edc`; DOI `10.1158/1078-0432.CCR-20-3208`.
- Coverage: complete pp1–14; Figures 1–4 on pp4, 6, 8, 10 and Tables 1–2 on pp5, 7 visually checked.
- Verified result: DNA sensitivity was 46/46 in a selected co-tested set and specificity 4,459/4,479; FISH sensitivity was 44/48 and selected specificity 18/25; IHC sensitivity was 61/70 and specificity 73/89. FISH detected 8/12 and IHC 6/12 NCOA4–RET fusions.
- Boundary: screened, RNA-confirmed, FISH, IHC, and plasma sets have different availability-selected denominators. Four responding low-IHC examples are not a population response rate. The Introduction reverses fusion architecture relative to the internally concordant Methods/Figure 1C and is quarantined.
- Source sentence → type → scenario → template: “FISH was 100% sensitive for both KIF5B-RET and CCDC6-RET fusions, yet, it missed 33.3% (4/12) of NCOA4-RET fusions due to poor signal separation.” → high aggregate performance with a variant-specific limitation → assay blind spot across fusion partners → `Although [assay] showed high aggregate sensitivity, performance was lower for [variant class], so the overall estimate should not be generalized across fusion partners or assay-availability settings.`
- Gates: all six `pass`. Verdict: `passed` with selected-denominator and partner-specific limits.

## PMID 33077574 — NRF2 Activation Promotes Aggressive Lung Cancer and Associates with Poor Clinical Outcomes

- Source: 13-page supplied PDF, SHA-256 `758747dacfc448ee96e212d42e64fbf07f8e0f125df525821154c53f81e7cf91`; DOI `10.1158/1078-0432.CCR-20-1985`.
- Coverage: complete pp1–13; Figures 1–5 on pp3, 5, 7, 8, 10 and Table 1 on p6 visually checked.
- Verified result: combined Keap1/Stk11 loss produced aggressive Kras-driven murine disease with 59-day median survival. In TCGA lung adenocarcinoma, the NRF2 signature was associated with OS after adjustment for KRAS/STK11 (HR 1.82, 95% CI 1.27–2.60; `P=.0011`). Associations in both OAK treatment arms favor a prognostic interpretation.
- Negative/predictive boundary: STK11 in the atezolizumab arm had `P=.051`; NRF2 signature-by-treatment interactions were nonsignificant in OAK (`P=.111`) and IMpower131 (`P=.60`) squamous analyses. Model causality cannot be transferred directly to patients.
- Source sentence → type → scenario → template: “While these data suggest that a low NRF2 signature score may be predictive of benefit from atezolizumab therapy in squamous lung adenocarcinoma, a formal test for the interaction between the NRF2 signature and treatment arm in affecting survival did not reach significance (LR test, P = 0.111).” → favorable within-arm direction with null formal interaction → apparent arm-specific efficacy/prognosis difference without effect modification → `Although the within-arm estimate suggested [direction], the biomarker-by-treatment interaction was not statistically significant; the finding therefore remains hypothesis-generating rather than treatment predictive.`
- Gates: all six `pass`. Verdict: `passed`; the null interaction governs predictive wording.

## PMID 33023953 — Transcriptional Subtypes Resolve Tumor Heterogeneity and Identify Vulnerabilities to MEK Inhibition in Lung Adenocarcinoma

- Source: publisher PDF, 13 pages, SHA-256 `b6d4ff9e13095da0c8c2ee1434e4cd196187ab8a15d55106dd5ad4a9cc280001`; DOI `10.1158/1078-0432.CCR-20-1835`.
- Coverage: complete pp1–13; Figures 1–4 on pp4, 6, 7, 9 visually checked.
- Verified result: the 113-gene MUC/PRO/MES states occurred across common driver genotypes; no single alteration uniquely defined them. PRO enrichment for functional STK11/KEAP1 deficiency is not equivalent to mutation status. MEK sensitivity was context-dependent across screens and preclinical models.
- Boundary: multiregion evidence included six patients and one metastasis pair. The 20-patient clinical combination subset lacks randomization and a treatment interaction; it cannot validate the subtype as a response predictor.
- Source sentence → type → scenario → template: “These transcriptional states lack discrete and causative mutational etiology as evidenced by similarly distributed oncogenic drivers, including KRAS and EGFR.” → expression-defined states without a unique genomic cause → a transcriptional phenotype spans genomic driver groups → `The expression-defined states occurred across [driver groups], indicating that no single genomic alteration uniquely accounted for the transcriptional classification.`
- Gates: all six `pass`. Verdict: `passed` with omics-layer and preclinical-to-clinical separation.

## PMID 33020056 — Genome and Transcriptome Biomarkers of Response to Immune Checkpoint Inhibitors in Advanced Solid Tumors

- Source: publisher PDF, 12 pages, SHA-256 `985527a4b3390415d4bd6ac1210d41fae3cec51fb72975c2f15107fc76fb9e92`; DOI `10.1158/1078-0432.CCR-20-1163`.
- Coverage: complete pp1–12; Table 1 on p4 and Figures 1–4 on pp5–8 visually checked.
- Verified result: exploratory WGS/RNA features, including TMB and immune-expression scores, showed cohort-specific associations. High CD274 expression had a univariable time-to-progression association but no OS association and no incremental joint-model information.
- Boundary: durable clinical benefit is not ORR; the reported time to progression is not standard radiographic PFS; M1–M2 is an expression score, not a counted-cell ratio. Table 1 sex counts sum to 72 rather than 82, Figure 3 prose conflicts with its displayed CD274 threshold direction, and a caption overgeneralizes a denominator; these fields are quarantined. Thresholds were cohort-informed, replication was inconsistent, and one lesion cannot establish acquired resistance.
- Source sentence → type → scenario → template: “The high CD274 expression did not provide any additional benefit in TTP or OS, indicating that any benefit from CD274 expression can be explained in our cohort by other predictive marker.” → univariable-positive marker without incremental value → transcriptomic association overlaps with correlated features → `Although [marker] showed a univariable association with [endpoint], it did not add independent information in the joint model, suggesting that the observed signal overlapped with other measured features.`
- Gates: all six `pass`. Verdict: `passed` with endpoint, denominator, threshold, and model boundaries.

## PMID 32241817 — Identification of Deleterious NOTCH Mutation as Novel Predictor to Efficacious Immunotherapy in NSCLC

- Source: publisher PDF, 13 pages, SHA-256 `7932e9af2e1e1bb002c983dc404407ecd42f2b8de6833d4f1912bd136ca3661d`; DOI `10.1158/1078-0432.CCR-19-3976`.
- Coverage: complete pp1–13; Figures 1–5 on pp4, 5, 7, 8, 10 and Table 1 on p11 visually checked.
- Verified result: the predicted-deleterious NOTCH class used truncating variants or PolyPhen-2 score ≥0.8. The PFS treatment interaction was significant (HR 0.73; `P=.012`), whereas the OS interaction was not (HR 0.86; `P=.255`).
- Boundary: predicted damage does not identify activation versus loss of function. Cohorts were heterogeneous and partly overlapping; no direct NOTCH perturbation tested mechanism. Docetaxel ORR is 9.3% in text versus 5.6% in Figure 5A, so the exact value is withheld.
- Source sentence → type → scenario → template: “However, this system fails to decipher the precise function of missense mutation as activation or deactivation.” → functional uncertainty of an in-silico variant classifier → predicted damaging variants without pathway-direction evidence → `Although [algorithm] classified the variants as potentially damaging, it did not resolve whether individual missense variants caused pathway activation or loss of function.`
- Gates: all six `pass`. Verdict: `passed` with classifier, endpoint, overlap, and source-conflict limits.
