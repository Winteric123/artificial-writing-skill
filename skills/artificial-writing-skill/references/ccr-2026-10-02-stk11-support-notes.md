# CCR STK11 topic-support source checks (2026-10-02)

Integration update: the six topic-support recommendations below were adopted in the current membership map without changing core highlights or historical reading/review states. The audit below preserves the pre-integration catalog snapshot. New searchable single-paper language lives in [the PMID42456046 addendum](ccr-2026-42456046-language-addendum.md) and [the PMID42485106 addendum](ccr-2026-42485106-language-addendum.md); their dedicated manifest and generated catalog, rather than the proposed examples below, govern retrieval.

## Scope and status

This note audits six previously completed CCR main-text reads for possible STK11 topic-support use. It does not replace the original reading assets, alter the historical completion dates, certify a new six-gate acceptance review, or designate any paper as a core highlight.

- The registered PDF for every paper was reopened on 2026-10-02, and its SHA-256 matched both the private inventory and `source-version-register.csv`. Private local paths are intentionally omitted.
- The current check compared the existing scientific/language notes with selected full-text sections and visually inspected source pages, figures, and tables. It was a bounded same-agent source check, not a new exhaustive reread of every line.
- All six papers remain `reading_stage=main_text_deep_read_complete` and `review_status=not_reviewed`. Existing `pending` or `not_reaudited` gate values remain unchanged. Main-text completion does not imply supplement review or independent acceptance.
- Page numbers below are one-based physical PDF pages. Printed journal pages are added where useful. The quality register retains `supplement_status=not_supplied` for four papers and `not_recorded` for PMID 42456046 and PMID 42485106. This audit did not independently review separate supplements for any of the six. References to supplementary results in a main article are not supplement review.
- Suggested project membership is `topic_support` only. It is a recommendation for the STK11 writing map, not an implemented registration and not an automatic `core_highlight` promotion.

Status authorities: [CCR deep-reading ledger](ccr-deep-reading-ledger.md), [CCR reading-quality register](ccr-reading-quality-register.csv), and [source-version register](source-version-register.csv).

## Existing language-asset audit

Counts below describe the pre-update `ccr-section-language-catalog.csv` snapshot dated 2026-09-26. Multiword vocabulary/collocations are counted as `vocabulary`; paragraph structures are catalogued as `paragraph-model`.

| PMID | Existing asset | Single-paper catalog rows | Coverage judgment |
|---|---|---:|---|
| 38300729 | [Combinatorial genomic biomarker reading](ccr-2024-38300729-language.md) | 24: 9 vocabulary/collocations, 13 sentence frames, 2 paragraph models | Sufficient for article-specific STK11/TMB composite-biomarker writing; retain its source-alert block. |
| 38980931 | [KEAPness reading](ccr-2024-38980931-language.md) | 59: 28 vocabulary/collocations, 29 sentence frames, 2 paragraph models | Sufficient for genotype–functional-state and immune-exclusion writing; it is KEAP1/KEAPness-centered, not direct STK11 evidence. |
| 42456046 | [2026 immunotherapy full-text asset](ccr-2026-immunotherapy-fulltext-language.md) and [CCR phrase patterns](ccr-phrase-patterns.md) | 0 single-paper rows; 274 multi-paper rows mention the PMID | Broad terminology and section frames exist, but single-article traceability and the combined KEAP1/STK11 boundary are insufficient. A bounded addendum is supplied below. |
| 42485106 | [2026 immunotherapy full-text asset](ccr-2026-immunotherapy-fulltext-language.md) and [CCR phrase patterns](ccr-phrase-patterns.md) | 0 single-paper rows; 251 multi-paper rows mention the PMID | General ML/HTE terminology is strong, but no single-PMID language mapping separates STK11 feature importance from a gene-specific treatment interaction. A bounded addendum is supplied below. |
| 33077574 | [2021/2026 supplemental language asset](ccr-2026-09-12-supplement-language.md#pmid-33077574) | 44: 23 vocabulary/collocations, 19 sentence frames, 2 paragraph models | Sufficient for NRF2 functional-state, compound-mutant models, and prognostic-versus-predictive language. |
| 33323404 | [STK11/LKB1 radiotherapy language asset](ccr-2021-33323404-language.md) | 66: 30 vocabulary/collocations, 34 sentence frames, 2 paragraph models | Sufficient and unusually detailed; retain the clinical/preclinical evidence split and its unresolved source inconsistencies. |

## PMID 38300729

### Identity, source, and prior reading

- **Article:** [Combining Genomic Biomarkers to Guide Immunotherapy in Non-Small Cell Lung Cancer](https://pubmed.ncbi.nlm.nih.gov/38300729/). *Clinical Cancer Research*. 2024;30(7):1307–1318. Online first 2024-02-01; issue 2024-04-01. DOI: [10.1158/1078-0432.CCR-23-4027](https://doi.org/10.1158/1078-0432.CCR-23-4027). PMCID: PMC10982639.
- **Supplied source:** publisher-typeset PDF, 12 physical pages, SHA-256 `e6fe17f7403bcb66e94d6aaad03137c6ea95e62e0c04f5d84b33ac7f5554ad19`.
- **Historical main-read completion:** 2026-09-23. Existing asset: [ccr-2024-38300729-language.md](ccr-2024-38300729-language.md).
- **2026-10-02 bounded check:** text on physical pp. 1–5 and 7–10; visual recheck of Figure 2 (p. 7 / printed p. 1313) and Figure 4 (p. 9 / printed p. 1315). This check did not change `review_status=not_reviewed`.

### Structured evidence summary

- **Question/design:** retrospective clinicogenomic discovery/validation study of advanced NSCLC treated with anti-PD-(L)1 monotherapy. Discovery used WGS in 75 patients; validation used MSK-IMPACT tumor-normal panel data in 169 patients. Durable clinical benefit (DCB) was CR/PR or stable disease lasting at least six months, not ORR.
- **Rule:** at least one qualifying `STK11 OR KEAP1 OR EGFR` alteration plus TMB below 10 mutations/Mb. It is a logical-OR composite, not triple co-mutation. WGS and panel cohorts used different operational variant filters; the validation cohort could not reproduce PURPLE passenger-probability filtering.
- **Central result:** among composite-positive tumors, DCB occurred in 0/15 low-TMB versus 11/13 high-TMB discovery cases and 1/34 low-TMB versus 15/34 high-TMB validation cases (Abstract p. 1; Figures 2 and 4, pp. 7 and 9). In validation, the low-TMB composite was associated with shorter PFS (HR 2.62, 95% CI 1.62–4.22) and OS (HR 2.37, 95% CI 1.41–4.00). High-TMB altered tumors still had adverse OS in validation (HR 3.08, 95% CI 1.51–6.27), so high TMB did not uniformly “rescue” prognosis.
- **STK11-specific context:** discovery low-TMB STK11-altered cases had 0/9 DCB; validation low-TMB cases had 1/17 DCB. The validation exception carried STK11 E119*, TMB 6.1 mutations/Mb, PD-L1 TPS 60%, and ongoing PFS of 11 months at cutoff (Results p. 8 / printed p. 1314). Responding STK11+KRAS cases were few and all had high TMB.
- **Claim ceiling:** the study supports a hypothesis-generating, TMB-conditioned low-benefit association. It does not establish that STK11 alone universally causes ICI resistance or that withholding ICI is safe.

### Source alerts and STK11 use

- The Abstract reports 254 patients, whereas the stated cohorts sum to 244 (75+169). Preserve the discrepancy rather than silently repairing it.
- The study lacks a non-ICI comparator and a treatment-by-biomarker interaction; prognostic and treatment-specific components cannot be separated.
- The single responding low-TMB STK11 case prevents absolute “no benefit” wording. Survival directions also differ across cohorts in some high-TMB analyses.
- Suggested role: `tier=topic_support`; `stk11_relation=direct_analysis`; modules `sequence_context clinical_outcomes`.
- Best use: explain why a co-biomarker framework may be more specific than mutation status alone, while retaining assay definitions, DCB definition, rare-beneficiary cost, and prospective-validation requirement.

### Language-asset verdict

The existing single-paper asset is sufficient: it covers combinatorial-biomarker vocabulary, assay-specific mutation definitions, rare-benefit exceptions, survival language, safe sentence frames, and Results/Discussion paragraph logic. No additional catalog item is proposed here.

## PMID 38980931

### Identity, source, and prior reading

- **Article:** [Transcriptional Phenocopies of Deleterious KEAP1 Mutations Correlate with Survival Outcomes in Lung Cancer Treated with Immunotherapy](https://pubmed.ncbi.nlm.nih.gov/38980931/). *Clinical Cancer Research*. 2024;30(19):4397–4411. Online first 2024-07-09; issue 2024-10-01. DOI: [10.1158/1078-0432.CCR-24-0626](https://doi.org/10.1158/1078-0432.CCR-24-0626).
- **Supplied source:** publisher-typeset PDF, 15 physical pages, SHA-256 `93eb22b1aa149270f5e592b3317fe5c8cfe7b7681c1d67433d36378829838480`.
- **Historical main-read completion:** 2026-09-24. Existing asset: [ccr-2024-38980931-language.md](ccr-2024-38980931-language.md).
- **2026-10-02 bounded check:** text on physical pp. 1–3 and 5–13; visual recheck of Figure 4 (p. 8), Figure 5 (pp. 9–10), and Figure 6 (pp. 11–12). Status remains `not_reviewed`.

### Structured evidence summary

- **Question/design:** secondary biomarker study asking whether KEAP1-wild-type tumors can share a KEAP1-mutant-like transcriptomic state (“KEAPness”). The work spans TCGA discovery, SU2C and OAK/POPLAR clinical cohorts, and TRACERx421 multiregion evolutionary analysis.
- **Analysis sets:** TCGA included 9,229 pan-cancer tumors. Clinical RNA-seq comprised SU2C n=153 and atezolizumab-treated OAK/POPLAR n=439; endpoint denominators differed within SU2C. OAK/POPLAR also contained 452 docetaxel-treated patients. TRACERx421 included 347 patients and 947 regions; regions are not patients.
- **Functional classifier:** the 12-gene score used an outcome-informed cutoff optimized in 93 non-squamous SU2C patients with 2,000 bootstrap resamples, then carried forward. The exact clinical cutoff is not printed in the supplied main text. A TCGA z-score threshold is not a substitute.
- **Central result:** KEAPness-dominant tumors showed shorter PFS and OS in SU2C and atezolizumab cohorts and an immune-depleted phenotype. In pooled mutation-matched analysis, KEAPness and KEAP1-mutant groups had similarly adverse outcomes relative to KEAPness-free tumors (Figure 4, p. 8).
- **STK11 context:** STK11 was enriched in KEAP1-mutant tumors, but the reported KEAPness-versus-free STK11 comparison was not significant. TP53, KRAS, and STK11 appeared among shared positive-selection signals in non-squamous groups (Figure 5, pp. 9–10). This is context for convergent functional states, not an STK11 classifier or proof of STK11–KEAP1 epistasis.
- **Evolution/heterogeneity:** 31% of KEAPness tumors had at least one KEAPness-free region; RNA-derived immune patterns were supported by DNA-derived T-cell ExTRECT estimates (Figure 6, pp. 11–12). These are bulk/multiregion computational analyses, not single-cell or spatial-transcriptomic measurements.

### Source alerts and STK11 use

- Figure 4 risk sets sum to 314, while the Methods-matched genomic subsets sum to 312. The discrepancy is unresolved.
- Adverse associations also appear in docetaxel-treated patients, and no treatment interaction is shown. Do not call KEAPness an established ICI-specific predictive biomarker.
- The threshold was outcome-informed, covariate availability was limited, and “outperforms mutation-only classification” does not itself establish incremental discrimination or clinical utility.
- Suggested role: `tier=topic_support`; `stk11_relation=contextual_analysis`; modules `sequence_context functional_state clinical_outcomes immune_mechanism`.
- Best use: distinguish mutation status from downstream functional state and discuss convergent immune-excluded phenotypes; do not transfer KEAPness results into an STK11-only claim.

### Language-asset verdict

The single-paper asset is sufficient and well calibrated. It contains explicit genotype–phenotype vocabulary, endpoint-specific analysis-set language, outcome-informed cutoff framing, evolutionary and immune-inference terminology, and Results/Discussion paragraph models. No additional catalog item is proposed here.

## PMID 42456046

### Identity, source, and prior reading

- **Article:** [Intratumoral Immune Heterogeneity Drives Divergent Outcomes to PD-(L)1 Blockade in Lung Cancer](https://pubmed.ncbi.nlm.nih.gov/42456046/). *Clinical Cancer Research*. 2026;32(19):4396–4410. Online record 2026-08-04; issue 2026-10-01. DOI: [10.1158/1078-0432.CCR-26-1466](https://doi.org/10.1158/1078-0432.CCR-26-1466).
- **Supplied source:** 44-page publisher-hosted, line-numbered manuscript PDF; header classification remains `not_classified_by_header`. SHA-256 `c795f9d233acd688cca4a87407fe7a0a2c8e863c69b8c9833d696982ced28855`. Physical pp. 35–38 contain figure legends and pp. 39–44 the figure plates; do not substitute formal issue pagination for this supplied version.
- **Historical main-read completion:** 2026-09-08. Existing assets: [2026 immunotherapy full-text language](ccr-2026-immunotherapy-fulltext-language.md) and [CCR phrase patterns](ccr-phrase-patterns.md).
- **2026-10-02 bounded check:** text on pp. 6–12, 17–27, and 35–38; visual recheck of Figure 2 (p. 40), Figure 4 (p. 42), Figure 5 (p. 43), and Figure 6 (p. 44). Status remains `not_reviewed` with six gates `not_reaudited`.

### Structured evidence summary

- **Question/design:** retrospective computational/translational study deriving a single-sample classifier of intratumoral immune heterogeneity (ITIH) from multiregion TRACERx421 RNA-seq and applying it to ICI-treated cohorts.
- **Training/reference sets:** the classifier used 746 regions from 246 multiregion patients after stated exclusions (Methods p. 10). The prevalence analysis reports ITIH in 80/285 cases (Results p. 17; Figure 2, p. 40). These are distinct analysis sets and should not be merged.
- **Classifier performance:** for Hom-IE, recall was 0.694, precision 0.658, F1 0.676, and global accuracy 0.613 (p. 18). This supports bounded single-sample inference, not perfect recovery of multiregion ground truth.
- **Clinical cohorts:** cohort A n=291, cohort B n=439, and cohort C n=355, for 1,085 ICI-treated patients (Methods p. 12). Hom-IE tumors had longer OS across all three cohorts (Results pp. 20–21; Figure 4, p. 42). PD-L1 was available for 380 pooled cohort A/B patients; among PD-L1-low/negative tumors, Hom-IE median OS was 22.4 versus 10.8 months for non-Hom-IE (log-rank P=0.012; p. 21; Figure 5, p. 43).
- **Orthogonal support:** TCGA digital pathology included 863 NSCLC samples and an independent cohort-A subset included 64 specimens. The latter showed stepwise trends with P=0.07 and P=0.06 rather than conventionally significant confirmation (pp. 12 and 19; Figure 3).
- **STK11 context:** combined `KEAP1 and/or STK11` status was available for 155 cohort-A and 251 cohort-B patients. It was not enriched across ITIH groups, but the combined mutation-positive group retained adverse survival within Hom-IE LUAD (Results p. 23; Figure 6, p. 44). Figure 6 does not separate STK11 from KEAP1 and does not establish an STK11-specific effect.

### Source alerts and STK11 use

- All three main outcome cohorts were ICI treated. A supplementary cohort-B atezolizumab-versus-docetaxel comparison is referenced, but the supplement was not reviewed here. Main-text cohort replication alone supports outcome stratification, not an established treatment-predictive biomarker.
- There was no independent multiregion ground-truth validation cohort. Digital pathology supports immune gradients but is not the same target as multiregion molecular ITIH.
- PD-L1 was partly missing and pooled; cohort C lacked major covariates and could not support multivariable analysis. Treatment lines and contemporary regimens were heterogeneous.
- Suggested role: `tier=topic_support`; `stk11_relation=contextual_analysis`; modules `sequence_context functional_state clinical_outcomes immune_mechanism`.
- Best use: show that an adverse combined KEAP1/STK11 genomic context may persist inside an apparently favorable immune state. Do not write that Hom-IE overcomes STK11, that STK11 alone drove the result, or that ITIH is externally validated for treatment selection.

### Single-paper language addendum

These are synthetic transfer models supported by the cited context, not quotations. They are recorded here because the current catalog has no single-PMID entries for this article.

- **Methods vocabulary/collocations:** `multiregion-derived single-sample classifier`; `orthogonal digital-pathology support`; `sampling-depth-dependent heterogeneity detection`; `independent multiregion ground-truth validation`.
- **Methods frame:** `A classifier trained against multiregion immune states was applied to single-sample cohorts and evaluated against orthogonal pathology readouts.` Safe only when training target, sample unit, and orthogonal readout are stated; source context pp. 10–19 and Figures 2–3.
- **Results vocabulary/collocations:** `combined KEAP1/STK11 mutation status`; `favorable immune-state stratum`; `persistent adverse genomic association`.
- **Results frame:** `Within the [immune-state] stratum, the combined mutation-positive group retained an adverse survival association, although gene-specific effects were not separable.` Source context p. 23 and Figure 6 (p. 44).
- **Discussion frame:** `Replication across treated cohorts supports outcome stratification, whereas treatment-predictive utility requires a comparative interaction analysis and prospective validation.` Source context pp. 24–27.
- **Paragraph logic:** define multiregion ITIH → report classifier performance → add pathology support → replicate survival stratification → position PD-L1 and combined KEAP1/STK11 context → end with missing multiregion external validation and treatment-utility limits.

## PMID 42485106

### Identity, source, and prior reading

- **Article:** [Utilizing Machine Learning to Identify Multimodal Signatures for Patients Who Would Benefit from the Addition of Tremelimumab to Durvalumab and Chemotherapy (TRIDENT)](https://pubmed.ncbi.nlm.nih.gov/42485106/). *Clinical Cancer Research*. 2026;32(19):4461–4473. Issue 2026-10-01. DOI: [10.1158/1078-0432.CCR-25-3729](https://doi.org/10.1158/1078-0432.CCR-25-3729).
- **Date/version note:** the supplied OF1–OF13 PDF states “posted first” 2026-07-22, while a separately retrieved publisher/PubMed-facing online date was 2026-08-21. These dates arise from different records and are not merged here; formal online-date reconciliation remains outside this bounded source check.
- **Supplied source:** publisher OnlineFirst-style PDF with `XX:XX–XX` and OF pagination, 13 physical pages; register classification remains `not_classified_by_header`. SHA-256 `4844b3589ded1523689287e2216b87d50240e0ff44a9581c55c6e6972dfdffee`.
- **Historical main-read completion:** 2026-09-08. Existing assets: [2026 immunotherapy full-text language](ccr-2026-immunotherapy-fulltext-language.md) and [CCR phrase patterns](ccr-phrase-patterns.md).
- **2026-10-02 bounded check:** text on physical pp. 1–10; visual recheck of Table 1 (p. 6) and Figure 3 (p. 9). Status remains `not_reviewed` with six gates `not_reaudited`.

### Structured evidence summary

- **Question/design:** post hoc heterogeneous-treatment-effect analysis of the randomized POSEIDON source trial. TRIDENT compared the predicted OS effect of adding tremelimumab to durvalumab plus chemotherapy (`T+D+CT` versus `D+CT`), not the original trial's experimental arm versus chemotherapy-alone primary comparison.
- **Population/data attrition:** 974 POSEIDON participants entered TRIDENT, but the two modeled treatment arms contained 652 patients with clinical data. Radiomics analyses used 616, genomics 557, all three modalities 526, and the nonsquamous clinical-plus-genomic analysis set 345 patients (Figure 2, p. 4; Table 1, p. 6). Analysis-set-specific estimates cannot be compared as if derived from the same patients.
- **Estimand/model:** CATE was the predicted difference in 24-month restricted mean survival time under the two treatment options. Super T-learners used repeated nested cross-validation, with feature selection and tuning inside the procedure (Methods pp. 3–5).
- **Central result:** in nonsquamous analysis set 6, the clinical-plus-genomic model's top-ranked 50% had OS HR 0.56 (95% CI 0.33–0.97; P=0.04), compared with HR 0.88 (0.68–1.12) in the complete analysis set (Table 1, p. 6; Figure 3C, p. 9). The genomic-only model gave HR 0.58 (0.35–0.97) for its top 50%.
- **STK11 context:** EGFR, FGFR3, CDKN2A, KRAS, and STK11 status were the five highest-importance features in model 19 (Results p. 8; Figure 3C, p. 9). STK11 mutation was one component of a multivariable feature-importance ranking, not a standalone interaction estimate or validated single-gene treatment rule.
- **Negative/limiting findings:** a performant squamous signature was not obtained; adding radiomics to clinical/genomic data did not improve performance; no external validation cohort or independent test set was available (Discussion p. 10).

### Source alerts and STK11 use

- Randomization of the source trial does not make the post hoc, data-adaptive signature confirmatory. Nested cross-validation is internal validation, not external validation or individual treatment utility.
- The fixed top-50% selection is model-defined. Feature importance reflects contribution to model prediction and cannot be interpreted as a causal STK11 mechanism or gene-specific treatment interaction.
- Missing modalities changed analysis sets; the sample was too small for a hold-out set; centrally detected EGFR findings differed from local eligibility testing; gene-level mutation coding ignored variant-level heterogeneity.
- Suggested role: `tier=topic_support`; `stk11_relation=contextual_analysis`; modules `sequence_context clinical_outcomes`.
- Best use: illustrate multivariable treatment-effect heterogeneity and hypothesis generation for CTLA-4 addition. Do not state that STK11 mutation alone predicts tremelimumab benefit or that TRIDENT externally validated such selection.

### Single-paper language addendum

These are synthetic transfer models, not quotations, and are not yet catalogued as single-PMID entries.

- **Methods vocabulary/collocations:** `post hoc heterogeneous-treatment-effect modeling`; `24-month restricted-mean-survival-time CATE`; `super T-learner`; `analysis-set-specific modality availability`; `repeated nested cross-validation`; `permutation-based feature importance`.
- **Methods frame:** `Conditional treatment effects were defined as the predicted difference in [time-horizon] restricted mean survival under the two randomized treatment options.` Source context pp. 2–5.
- **Results frame:** `Among the model-ranked top [fraction], the estimated treatment effect was larger than in the full analysis set, while [gene] remained one of several influential features.` Source context Table 1 (p. 6) and Figure 3 (p. 9).
- **Interpretation frame:** `Feature importance supports multivariable subgroup generation but does not establish a standalone treatment interaction for any single genomic variable.` Source context pp. 8–10.
- **Discussion frame:** `The signature is internally validated and hypothesis-generating; independent external validation is required before patient-level treatment selection.` Source context p. 10.
- **Paragraph logic:** define treatment contrast and CATE → disclose modality-dependent attrition → describe nested validation → report full-set and top-ranked effects together → interpret multiple features → retain negative squamous/radiomics findings → close with the external-validation boundary.

## PMID 33077574

### Identity, source, and prior reading

- **Article:** [NRF2 Activation Promotes Aggressive Lung Cancer and Associates with Poor Clinical Outcomes](https://pubmed.ncbi.nlm.nih.gov/33077574/). *Clinical Cancer Research*. 2021;27(3):877–888. Online first 2020-10-19; issue 2021-02-01. DOI: [10.1158/1078-0432.CCR-20-1985](https://doi.org/10.1158/1078-0432.CCR-20-1985). PMCID: PMC10867786.
- **Supplied source:** register classification `not_classified_by_header`, 13 physical pages (article pp. 1–12 plus publisher-information p. 13), SHA-256 `758747dacfc448ee96e212d42e64fbf07f8e0f125df525821154c53f81e7cf91`.
- **Historical main-read completion:** 2026-09-12. Existing asset: [ccr-2026-09-12-supplement-language.md#pmid-33077574](ccr-2026-09-12-supplement-language.md#pmid-33077574).
- **2026-10-02 bounded check:** key text on pp. 1–11; visual recheck of Figure 1 (p. 3 / printed p. 879), Figure 4 (p. 8 / printed p. 884), and Figure 5 (p. 10 / printed p. 886). Status remains `not_reviewed`.

### Structured evidence summary

- **Design:** compound-mutant GEMMs and isogenic cells were integrated with TCGA DNA/RNA analyses and OAK/IMpower131 biomarker cohorts. The primary molecular object is NRF2 pathway activation, with STK11 as a co-occurring genomic and experimental context.
- **Mechanistic layer:** combined Keap1 loss, Stk11 loss, and Kras activation produced early, multifocal, aggressive lung tumors and reduced redox stress relative to specified model comparators (Figures 1–2, pp. 3–5). This supports model-specific cooperation, not a universal human three-gene causal rule.
- **Functional-state layer:** a 96-gene NRF2 signature captured pathway activation beyond KEAP1/NFE2L2 mutation status. In TCGA LUAD, high signature was associated with worse OS after adjustment for KRAS and STK11 (HR 1.82, 95% CI 1.27–2.60; P=0.0011; Results p. 6, Figure 3).
- **Clinical layer:** in OAK nonsquamous tumors, STK11 mutation was adverse in atezolizumab (HR 1.54, 95% CI 0.998–2.38; P=0.051) and docetaxel (HR 2.28, 1.52–3.43; P=7.3×10^-5) arms (Figure 4, p. 8). The atezolizumab result does not meet the conventional significance threshold. STK11-mutant and NRF2-high tumors still showed atezolizumab benefit comparable to the evaluable population.
- **Squamous layer:** NRF2-low LUSC showed favorable arm-wise patterns in OAK and IMpower131, but formal treatment-by-signature interactions were not significant (P=0.111 and P=0.60; Results p. 9 / Figure 5 p. 10).

### Source alerts and STK11 use

- NRF2 signature, KEAP1 mutation, and STK11 mutation are related but non-interchangeable variables. Do not label every NRF2-high tumor as KEAP1-mutant or STK11-null.
- Adverse associations in both atezolizumab and docetaxel arms support a substantial prognostic component and do not establish universal ICI resistance.
- Bulk immune signatures are inferred contexture, not direct single-cell composition. Referenced supplements were not independently reviewed.
- Suggested role: `tier=topic_support`; `stk11_relation=direct_analysis`; modules `sequence_context functional_state clinical_outcomes immune_mechanism`.
- Best use: link STK11 genomic context to NRF2 functional state while separating engineered-model causality from patient-level association and treatment prediction.

### Language-asset verdict

The existing single-paper asset is sufficient. It covers compound-mutant models, gene rescue, redox measurements, functional signatures, nested-model comparison, prognostic-versus-predictive wording, and cross-layer Results/Discussion paragraph logic. No additional catalog item is proposed here.

## PMID 33323404

### Identity, source, and prior reading

- **Article:** [STK11/LKB1 Mutations in NSCLC Are Associated with KEAP1/NRF2-Dependent Radiotherapy Resistance Targetable by Glutaminase Inhibition](https://pubmed.ncbi.nlm.nih.gov/33323404/). *Clinical Cancer Research*. 2021;27(6):1720–1733. Online first 2020-12-15; issue 2021-03-15. DOI: [10.1158/1078-0432.CCR-20-2859](https://doi.org/10.1158/1078-0432.CCR-20-2859). PMCID: PMC8138942.
- **Supplied source:** NIH author manuscript, 27 physical pages, SHA-256 `62ed98bd908b24800e28f8759c3cff246129b27a141da6582b794f6468a97630`.
- **Historical main-read completion:** 2026-09-24. Existing asset: [ccr-2021-33323404-language.md](ccr-2021-33323404-language.md).
- **2026-10-02 bounded check:** targeted text recheck of clinical and experimental claims; visual recheck of Figure 1 (p. 18), Figure 4 (p. 21), Figure 5 (p. 22), Table 3 (p. 25), and Table 5 (p. 27). Status remains `not_reviewed`.

### Structured evidence summary

- **Clinical layer:** retrospective definitive-radiotherapy cohort of 194 stage I–III NSCLC patients, with 164 stage III patients in the central analysis and only 12 STK11-mutant cases. One-year LRR was 25.0% (95% CI 4.8–53.1) versus 10.8% (6.5–16.5), P=0.0108 (Results p. 7; Figure 1 p. 18; Table 2 p. 24).
- **Survival layer:** univariable DFS HR was 2.530 (1.375–4.657; P=0.0029; Table 3 p. 25). Univariable OS HR was 2.198 (1.097–4.405; P=0.0263; Table 4 p. 26). The age-adjusted, two-variable OS model gave HR 2.123 (1.060–4.252; P=0.0337; Table 5 p. 27). This was not comprehensive multivariable control.
- **Negative result:** one-year distant-metastasis estimates were 66.7% versus 39.3%, but P=0.1129 (Results p. 7; Figure 1D p. 18). Do not report a demonstrated increase in distant failure.
- **Mechanistic layer:** isogenic restoration/knockdown experiments support model-specific LKB1/KEAP1–NRF2 redox contributions to radiation response (Figure 3, p. 20). Xenograft irradiation benefited the KEAP1-restored model but not clearly the LKB1-restored model (Figure 4, p. 21).
- **Therapeutic-hypothesis layer:** CB-839 increased clonogenic radiosensitivity in vitro (Figure 5, p. 22). No patient treatment, clinical dose, or in-vivo CB-839-plus-radiotherapy efficacy arm was tested.

### Source alerts and STK11 use

- The clinical sequencing panels did not assess KEAP1. KEAP1/NRF2 dependence comes from experimental models and cannot be described as clinically adjusted STK11/KEAP1 co-mutation evidence.
- The stage III cohort predates routine consolidation durvalumab and has no non-radiotherapy comparator or treatment interaction. It supports an association after RT, not a validated RT-specific predictive marker.
- Endpoint denominators differ (LRR/DM n=162 versus DFS/OS n=164). Table 5 adjusts for age only. Small subgroups and wide intervals limit precision.
- Existing notes correctly retain unresolved DCFDA/MitoSOX, restored-LKB1 DER, xenograft-denominator, and protocol-volume discrepancies. Exact conflicting values should remain withheld or qualified.
- Suggested role: `tier=topic_support`; `stk11_relation=direct_analysis`; modules `sequence_context functional_state clinical_outcomes`.
- Best use: illustrate a clinical-association → isogenic-mechanism → preclinical-vulnerability evidence chain while keeping causal strength and treatment era separate at every step.

### Language-asset verdict

The existing single-paper asset is sufficient. It covers competing-risk language, endpoint-specific denominators, isogenic perturbation, clonogenic survival, dose-enhancement terminology, negative-result retention, clinical-versus-preclinical evidence, and paragraph architectures. No additional catalog item is proposed here.

## Recommended topic-support registration

These recommendations do not implement membership or priority changes.

| PMID | Suggested tier | STK11 relation | Suggested modules | Principal contribution |
|---|---|---|---|---|
| 38300729 | `topic_support` | `direct_analysis` | `sequence_context clinical_outcomes` | TMB-conditioned composite resistance-marker framework and rare-beneficiary caution. |
| 38980931 | `topic_support` | `contextual_analysis` | `sequence_context functional_state clinical_outcomes immune_mechanism` | Genotype–functional-state discordance, KEAPness, immune exclusion, and convergent evolution. |
| 42456046 | `topic_support` | `contextual_analysis` | `sequence_context functional_state clinical_outcomes immune_mechanism` | Immune-state heterogeneity and persistence of adverse combined KEAP1/STK11 context. |
| 42485106 | `topic_support` | `contextual_analysis` | `sequence_context clinical_outcomes` | Post hoc multivariable treatment-effect heterogeneity in which STK11 is one model feature. |
| 33077574 | `topic_support` | `direct_analysis` | `sequence_context functional_state clinical_outcomes immune_mechanism` | NRF2 functional state, compound-mutant models, and prognostic-versus-predictive separation. |
| 33323404 | `topic_support` | `direct_analysis` | `sequence_context functional_state clinical_outcomes` | Radiotherapy outcome association, redox mechanism, and preclinical glutaminase vulnerability. |

## Directory and catalog handoff

Only the two single-paper addenda for PMIDs 42456046 and 42485106 are new language material in this note. They are not searchable language recommendations until the main maintenance pass:

1. registers this file as a routed topic-support/source-note asset;
2. maps each addendum item to one PMID with section, rhetorical function, domain, unit type, evidence tier, source asset/line, and synthetic-not-quotation provenance;
3. uses context locators rather than claiming literal PDF phrase matches for synthetic frames;
4. rebuilds the CCR section catalog and cross-journal language index, then runs the reading-quality, library, provenance, unit, skill, and Wisp-discovery checks required by the maintenance workflow.

Do not count these two addenda as new article reads, new standardized-section corpus papers, or core highlights. If the topic-support recommendations are adopted, link this note in `source_refs` while retaining the original article-level language assets as the primary language sources.
