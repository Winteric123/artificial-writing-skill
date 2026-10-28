# Five user-supplied JTO lung-cancer papers: full-text intake

## Scope and identity

- Intake date: 2026-10-25 (Asia/Shanghai).
- The supplied folder was named `补充CCR`, but all five articles are from *Journal of Thoracic Oncology* (JTO). Journal identity, not the folder name, controls registration.
- All supplied main-PDF pages and all main figures, tables and captions were read and visually checked. Separately hosted supplements were not supplied and are not marked reviewed.
- The supplied versions are four NIH author manuscripts and one corrected proof. A supplied manuscript or proof is not silently relabeled as a publisher Version of Record.
- These five records expand the formal JTO corpus. They do not expand the CCR corpus and they are not automatically STK11 highlights.
- Review outcomes are article specific. A completed main-text read does not by itself establish a six-gate pass.

The [reading manifest](jto-supplement-2026-10-25-reading-manifest.csv) records identifier, DOI, supplied version, archive filename, SHA-256, page count, main-display pages and review status. The [independent source recheck](source-rechecks/2026-10-25-jto-supplement.md) records the six gates. The [source-linked sentence catalog](jto-supplement-2026-10-25-sentence-patterns.json) keeps each verified source sentence, paper, physical-page locator, result or method type, use scenario, synthetic rewrite template and evidence boundary together.

## Shared interpretation rules learned from this batch

1. Do not call article-level evidence integration a paired multi-omics cohort unless the same patients or specimens contributed the asserted layers. Independent DNA, RNA, protein, spatial and clinical cohorts must remain distinct.
2. A small P value does not make a weak correlation biologically strong. Report direction and magnitude together.
3. A significant result in one subgroup and a nonsignificant result in another does not demonstrate subgroup heterogeneity without a formal interaction test.
4. A retrospective association observed during immune-checkpoint treatment is treatment-context evidence, not a validated predictive biomarker without an appropriate comparator and treatment-by-marker interaction.
5. When adjusted and unadjusted results differ, the adjusted result governs the principal inference; a residual numerical trend may be described only as such.
6. `P>0.05` does not establish equivalence or absence of mechanism. Multiple concordant negative assays may narrow a mechanism only within the tested branch.
7. Cells retained after single-cell quality control are analytic units, not independent patients or animals. Pooling and biological replicate structure must be reported separately.
8. Targeted RPPA, Luminex, Olink or multicolor immunofluorescence panels must not be upgraded to unbiased proteomics or spatial proteomics.
9. Exploratory cutoffs, internally cross-validated models and small discovery sets are not externally validated clinical thresholds.
10. When source prose conflicts with a figure, table, caption or another part of the main text, preserve the conflict as an alert and quarantine the disputed formulation rather than silently repairing it.

## PMID 32068166 — STING pathway expression identifies NSCLC with an immune-responsive phenotype

### Source and coverage

- Citation: Della Corte CM, et al. *J Thorac Oncol.* 2020;15(5):777-791. DOI `10.1016/j.jtho.2020.01.009`.
- Supplied version: NIH author manuscript, 24 physical pages, SHA-256 `9b9f54e353accac94f93a2a194a22d15a3fb8fd94ab6bc75f91a112bb5ef956f`.
- Coverage: complete supplied main text; Figures 1-5 and Table 1 visually checked. External supplementary material was not supplied.

### Evidence reconstruction

The paper integrates institution-specific LUAD and LUSC cohorts, TCGA cohorts, BATTLE-2 expression data and preclinical platinum-treatment models. Transcriptomics, targeted RPPA, genomic context and immune measures are not uniformly available for the same patients. It is therefore a multi-cohort, multilayer analysis rather than a completely paired patient-level multi-omics study.

STING, cGAS and STING-associated chemokine expression tracked an inflamed immune phenotype. STING-low LUAD was enriched for `STK11`, whereas STING-high LUAD was enriched for `TP53`. The `STK11` association was not absolute: 18 of 73 `STK11`-mutant tumors were STING-high, and those tumors were more frequently `TP53` altered than STING-low `STK11`-mutant tumors. Platinum-related pathway changes were model and genotype dependent.

### Results logic and boundaries

- The central clinical evidence is cross-sectional association between pathway expression and immune features; it is not patient-level validation of treatment benefit.
- CD8 and CD4 differences included directional but nonsignificant comparisons (`P>0.1`). These may be described as trends only.
- The murine combination experiment did not establish every claimed pairwise superiority comparison, and high-dose cisplatin caused more than 15% weight loss.
- No patient immune-checkpoint outcome cohort was used to validate STING as a treatment-predictive biomarker.

### Mandatory source alerts

- The PROSPECT LUAD denominator appears as 152 in the Figure 1B label but 120 in nearby body or caption text; Table 1 supports 152 RNA profiles and 120 RPPA profiles.
- TCGA LUAD appears as 511 in Figure 2A and 515 in the caption.
- TCGA LUSC appears as 482 in Figure 4E and 501 in the body or Table 1.
- The abstract total of 1320 is not transparently reconciled with table-derived transcript totals.
- A Figure 3 caption uses stronger combination-superiority language than the pairwise tests reported in the body.

Safe writing should use assay-specific denominators and avoid copying a disputed total. This article remains `needs_correction` for live sentence reuse even though its supplied main text was fully read.

## PMID 33096269 — Neoadjuvant chemotherapy and immune-cell infiltration in resectable NSCLC

### Source and coverage

- Citation: Gaudreau PO, et al. *J Thorac Oncol.* 2021;16(1):127-139. DOI `10.1016/j.jtho.2020.09.027`.
- Supplied version: NIH unedited author manuscript, 20 physical pages, SHA-256 `fadea5c8cdb06950f6558baca576a871b67996ae6cfe6a7b59d08234fb224bc6`.
- Coverage: complete supplied main text; Figures 1-4 and all captions visually checked. The separate supplementary methods, 12 tables and at least 11 figures were not supplied.

### Evidence reconstruction

The study compares neoadjuvant-chemotherapy-treated and treatment-naive resectable NSCLC across partly overlapping assay sets: flow cytometry, multiplex immunofluorescence, bulk microarray, T-cell receptor sequencing, targeted cytokine assays and whole-exome sequencing. The 511-patient total is not the denominator for every assay, and the platforms do not form one fully paired multi-omics cohort.

Baseline clinical differences motivated adjusted analyses. Higher CD8 and CD8-positive CD103-positive infiltration remained significant after adjustment. Some initially positive immune comparisons weakened after adjustment. Microarray gene-set enrichment supported immune-program differences but did not directly measure cell counts. TCR richness and clonality did not differ significantly. The nominal TMB difference lost significance after adjustment, whereas smoking history remained associated.

### Results logic and boundaries

- A univariate association that becomes nonsignificant after adjustment should be written as attenuated and not robust to covariate adjustment.
- An mIF result that becomes significant only after adjustment should identify both the model and covariates; it is not interchangeable with the unadjusted comparison.
- GSEA, mIF, flow cytometry and TCR-seq are complementary but nonidentical measurements.
- The study did not test immune-checkpoint efficacy and did not validate a predictive biomarker.

### Mandatory source alerts

- Whole-exome sample counts differ between the abstract (18 treated and 73 untreated) and the Methods or Results (40 treated and 61 untreated).
- TCR counts appear as 16 treated and 63 untreated in the abstract or Methods but 15 treated and 63 untreated in the Results.
- One adjusted P value appears as 0.008 in Figure 2B and 0.009 in the body or caption.
- Multiple nominal immune comparisons are presented without a unified main-text multiplicity strategy.
- Important covariate and quality-control details reside in the unavailable supplement.

The supplied main text is complete, but unresolved denominator conflicts make the live review state `needs_correction`.

## PMID 37247843 — Aneuploidy, chromosome 9p loss and ICI outcomes

### Source and coverage

- Citation: Alessi JV, et al. *J Thorac Oncol.* 2023;18(11):1524-1537. DOI `10.1016/j.jtho.2023.05.019`.
- Supplied version: NIH author manuscript, 23 physical pages, SHA-256 `0f39d09184c05db03aea23d920f2a0bf5bd94b3c973d8eb400f1f885d08cbff5`.
- Coverage: complete supplied main text; Figures 1-6 and Table 1 visually checked. Supplementary Methods, Figures 1-30 and Tables 1-11 were not supplied.

### Evidence reconstruction

The study combines a 2293-case targeted-genomic cohort, a 765-case two-center immune-checkpoint cohort, smaller nonrandomized chemotherapy or never-ICI comparator analyses, an independent 404-sample mIF cohort and external TCGA transcriptomic deconvolution. The genomic, mIF and RNA evidence layers are separate cohorts rather than a single paired multi-omics dataset.

Higher fraction of arm alterations (FAA) was associated with lower response rates and shorter PFS and OS during ICI treatment. Chromosome 9p loss was associated with adverse ICI outcomes after adjustment. The 1q-gain association did not remain independent after adjustment for TMB, PD-L1 and FAA. FAA had only weak or very weak correlations with PD-L1 and TMB, despite small P values. A model combining PD-L1, TMB and FAA improved internal cross-validated discrimination, but it was not externally validated.

The small chemotherapy and never-ICI analyses support possible treatment-context specificity, but they are not randomized controls and no formal treatment-by-marker interaction was reported. FAA and 9p loss should therefore be described as candidate treatment-outcome-associated markers, not validated predictive biomarkers.

### Mixed and negative results

- Several mIF compartments supported an immune-depleted pattern, whereas other immune-cell and ratio comparisons were nonsignificant.
- TCGA deconvolution likewise contained positive and negative cell-state comparisons.
- `1q` gain was associated with outcome in unadjusted analysis but not after full adjustment.
- The never-ICI FAA OS estimate was imprecise (`HR 1.50`, 95% CI `0.60-3.79`).

### Mandatory source alerts

- ORR and durable clinical benefit are binary outcomes, but parts of the abstract or Results label adjusted estimates as hazard ratios while the Methods and Figure 4 indicate logistic regression or odds ratios. The disputed effect-size label is quarantined.
- The main text uses both “natural logarithmic transformation” and “normal transformation.”
- The 9p and 1q analysis denominators (606 and 675) are smaller than the 765-patient ICI cohort and are not fully reconciled in the main text.
- Subgroup-specific P values do not establish heterogeneity without interaction testing.

With the disputed effect-size sentence quarantined and the prediction boundary explicit, the bounded six-gate review is `passed` for the supplied main PDF.

## PMID 40056978 — Selective CCR8-positive Treg depletion and dendritic-cell-mediated antitumor immunity

### Source and coverage

- Citation: Chen P, et al. *J Thorac Oncol.* 2025;20(8):1050-1074. DOI `10.1016/j.jtho.2025.02.029`.
- Supplied version: corrected proof / article in press, 25 physical pages, SHA-256 `b683b381659b29b4bf8039165c8826982c26f586cf782c74233c91fb85ab8471`.
- Coverage: complete supplied main text; Figures 1-7 and all captions visually checked. Supplementary Figures 1-11 and Tables 1-3 were not supplied.

### Evidence reconstruction

This is a multimodal immune-mechanism study. Its principal evidence is four mouse lung-cancer models, longitudinal pooled-tumor scRNA-seq and scTCR-seq, targeted flow cytometry, five-color immunofluorescence, Luminex measurements and functional depletion, coculture, inhibition and rescue experiments. Human evidence comes from public cohorts, a local 16-patient RNA cohort and an ongoing nine-patient exploratory trial analysis. These layers must not be represented as a paired human multi-omics cohort.

Combination anti-CCR8 and anti-PD1 therapy reduced tumor growth in four models and improved survival in the LLC and KL models. Tumor CCR8-positive Treg cells decreased without a comparable decrease in blood and spleen Treg cells. The measured safety evidence is limited to body weight and selected circulating cytokines; it does not establish absence of systemic toxicity.

Longitudinal single-cell data supported early changes in NK, dendritic, plasmacytoid dendritic and B-cell states followed by cytotoxic and memory T-cell accumulation. Three tumors per treatment were pooled before sequencing, so retained cell counts cannot be treated as independent animal replicates.

Functional experiments support a CCR8-positive Treg–CCL5-positive dendritic cell–CD8 T-cell axis. However, in vivo CD11c-DTR depletion was broad dendritic-cell depletion rather than CCL5-positive-DC-specific depletion, and a DC-specific CCL5-loss model was not used. The human Olink analysis included nine patients, used `P<0.1` as a screening threshold and had no reported multiplicity correction or external validation.

### Negative and borderline results

- M1/M2 macrophage ratios did not differ significantly across treatment groups.
- IL-10 and TGF-beta did not change significantly in the tested Treg-DC experiment; this does not prove cytokine independence.
- CCL5-negative DC proportions did not differ between immune-sensitive and resistant models.
- CCL5 stimulation did not significantly alter the tested CD4 T-cell activation or proliferation readouts.
- NK-associated measurements did not support a dominant immunosuppressive branch, although NK depletion still impaired antibody-mediated Treg depletion.
- Two spatial-distance comparisons were borderline (`P` approximately 0.0556) and must remain directional or borderline, not significant.

### Mandatory source alerts

- Figure 5B shows a strong CCL5-CCL8 correlation but only a weak, nonsignificant positive CCL5-CCL1 direction (`R=0.190`, `P=0.307`); prose that groups both as positive associations must not imply that both are statistically supported.
- “Without systemic toxicity” exceeds the measured weight and selected-cytokine evidence.
- The Figure 7 “clinical efficacy and potential biomarker” heading exceeds a single partial response and a nine-patient exploratory panel.
- High-dimensional assays do not share a unified reported multiplicity-control strategy, and several central denominators or depletion experiments rely on the unavailable supplement.

The main text is fully read, but the unresolved supplement-dependent checks and source overstatements keep the live state `needs_correction`.

## PMID 40850615 — CEACAM7 expression, DNA methylation and LUAD prognosis

### Source and coverage

- Citation: Hulbert A, et al. *J Thorac Oncol.* 2026;21(1):124-134. DOI `10.1016/j.jtho.2025.08.015`.
- Supplied version: NIH author manuscript, 19 physical pages, SHA-256 `fe387a43d63d502d2fc524ce6026f611caefff3558d3e35b2945c8bb98c49011`.
- Coverage: complete supplied main text; Figures 1-5 and Table 1 visually checked. Supplementary Figures 1-5 were not supplied.

### Evidence reconstruction

This retrospective public-data study integrates TCGA RNA expression, TCGA 450K DNA methylation, clinical survival and independent GTEx normal-tissue expression. The core African American LUAD analysis contains 52 patients, divided at the median into 26 high- and 26 low-expression cases; adjusted models use 50 cases because two stage or covariate values are missing. The exact paired methylation-RNA denominator is not clearly reported in the main text, and GTEx samples are not patient-matched TCGA normal tissues.

CEACAM7 was one of six genes upregulated in the reported African American LUAD differential-expression result and was the highlighted candidate associated with survival. The adjusted mortality estimate was large but very imprecise (`HR 38.86`, 95% CI `3.94-383.68`), indicating instability in a small exploratory cohort. No significant CEACAM7 survival difference was observed in White LUAD or African American LUSC. Without a formal race-by-marker interaction, this pattern does not establish race specificity.

Five chromosome 19 CpG probes were negatively correlated with CEACAM7 expression and passed univariate screening. Only three of five remained significant after covariate adjustment. The selection, cutoff and Cox modeling occurred in the same small dataset without external validation. Low normal-lung or blood expression in GTEx motivates further assay study but does not establish liquid-biopsy sensitivity, specificity or clinical utility.

### Mandatory source alerts

- The abstract and Discussion call CEACAM7 the “only” upregulated gene, while the Results and Figure 2 list six upregulated genes. Safe wording is “one of six upregulated genes and the highlighted survival-associated candidate.”
- Table 1 reports an impossible low-expression age IQR of `59.5 (51.5-38)`. It is retained as a source error and not guessed or repaired.
- Figure 3 shows stage IV versus stage III significance, stage IV versus stage I only a trend and stage IV versus stage II no significance; stronger prose is quarantined.
- Discussion mismatches the Figure 4 survival groups: 22.24 and 37.29 months belong to the two high-CEACAM7 strata, whereas both low-CEACAM7 medians were not reached.
- Results misassign several Figure 5 K-O panel letters. Probe names and adjusted estimates, rather than the erroneous panel letters, govern the record.
- Table 1 and the adjusted model each account for 50 rather than 52 cases, without a clear missing-data explanation.

With the conflicting formulations quarantined and the study restricted to exploratory prognostic association, the bounded six-gate review is `passed` for the supplied main PDF.

## Bounded synthetic section-language frames

These are newly synthesized writing frames derived from the evidence reconstructions above. They are not quotations and do not supply facts for a new manuscript.

### PMID 32068166 frames

- `We integrated [cohort-specific molecular layers] at article level but did not treat incomplete assay overlap as paired multi-omics.`
- `Although most [genotype-defined] tumors showed a [low/intermediate] immune state, a subset retained higher [pathway], checkpoint and immune-infiltration signals.`
- `The comparison was directionally consistent with [pattern], but did not reach statistical significance and therefore remained inconclusive.`
- `The observed molecular-immune association supports biological stratification but does not validate treatment benefit in the absence of patient outcome data.`

### PMID 33096269 frames

- `The platforms provided complementary evidence across partly overlapping assay subsets rather than one completely paired multi-omics cohort.`
- `After adjustment for [covariates], the association with [immune feature] remained detectable.`
- `The unadjusted difference in [feature] did not persist after multivariable adjustment, whereas [covariate] remained associated with the feature.`
- `Gene-set enrichment supported [cell/program] activity at the transcriptomic level but did not directly measure cell abundance or function.`

### PMID 37247843 frames

- `To harmonize [derived metric] across platforms, values were transformed and standardized within platform before pooled analysis.`
- `Although the correlations were statistically detectable, their magnitudes were weak, indicating limited shared variation.`
- `Within [subgroup], [endpoint 1] differed significantly, whereas [endpoint 2] and [endpoint 3] showed only numerical differences.`
- `The marker was associated with outcome during [treatment], but predictive utility was not established without a formal treatment interaction and external validation.`

### PMID 40056978 frames

- `To characterize temporal remodeling, [omics assays] were combined with [orthogonal assays] at prespecified time points after treatment.`
- `After quality control and filtering, [n] cells were retained from [model or cohort].`
- `[Condition] produced a directional change in [measure], but the comparison reached only borderline significance and supports a tentative interpretation.`
- `In an exploratory targeted-panel analysis of [n] samples, features meeting the screening threshold were treated as candidates for validation.`

### PMID 40850615 frames

- `Features meeting both the prespecified FDR threshold and the absolute effect-size threshold were considered differentially expressed.`
- `After adjustment, [marker] was associated with mortality, although the wide confidence interval indicated substantial imprecision.`
- `The association observed in [group A] was not detected in [group B]; without a formal interaction, the contrast remained descriptive.`
- `Because the data source captured only [available variables], residual confounding by [unmeasured social, exposure or treatment factors] could not be addressed.`

## Registration outcome

- Formal JTO main-text corpus: five new included records.
- Main-text reading: complete for all five supplied PDFs.
- Supplement status: `not_supplied` for all five.
- Six-gate live status: `passed` for PMIDs 37247843 and 40850615; `needs_correction` for PMIDs 32068166, 33096269 and 40056978.
- Sentence reuse: every record remains bound to its source paper, supplied version, SHA-256 and physical page. `passed` permits only bounded template reuse; `needs_correction` remains audit/bounded-only and is excluded by `--accepted-only`.
- No sentence template transfers a source gene, cohort, treatment, endpoint, number or conclusion into a user's study. The user must provide the facts being written.
