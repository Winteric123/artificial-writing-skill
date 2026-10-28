# Five supplied JTO papers: bounded independent source recheck

## Scope

- Review date: 2026-10-25 (Asia/Shanghai).
- Method: `independent_agent_source_recheck`. Three independent subagents reviewed the supplied PDFs. This is not human peer review, raw-data reanalysis or study replication.
- Reviewers: `/root/read_jto_2020_pair` for PMIDs 32068166 and 33096269; `/root/read_jto_2023_2026_pair` for PMIDs 37247843 and 40850615; `/root/read_jto_ccr8` for PMID 40056978.
- Coverage: five PDFs, 111 physical pages. All main scientific text and all main figures, tables and captions in the supplied versions were read and visually checked.
- Supplements: `not_supplied` for all five. External supplementary methods, figures and tables cited by the articles were not inferred or marked reviewed.
- Journal identity: all five are JTO articles despite the supplied folder name. None was added to the CCR bibliography.
- Source-linked language: only whole sentences checked against the supplied PDF and text extraction enter the dated sentence catalog. Disputed source formulations are absent, quarantined, or held for source check.

## Per-paper disposition

| PMID | Supplied version and main-display coverage | Evidence/result/transfer disposition | Overall |
|---|---|---|---|
| 32068166 | NIH author manuscript, 24 pp; Figures 1-5 and Table 1 checked | Multi-cohort RNA/RPPA/genomic and preclinical layers were separated. STING immune association and STK11/TP53 context were preserved, but patient-level treatment prediction was not inferred. Multiple assay-denominator and caption-testing conflicts remain unresolved. | `needs_correction` |
| 33096269 | NIH unedited author manuscript, 20 pp; Figures 1-4 checked | Flow, mIF, bulk expression, TCR, WES and cytokine sets were treated as partly overlapping rather than one paired cohort. Adjusted, unadjusted, negative and GSEA-inferred results were separated. WES/TCR denominators conflict and central supporting details are in the unavailable supplement. | `needs_correction` |
| 37247843 | NIH author manuscript, 23 pp; Figures 1-6 and Table 1 checked | Targeted-genomic ICI outcomes, nonrandomized comparator analyses, independent mIF and TCGA deconvolution were separated. Weak correlations remained weak; internal cross-validation was not called external validation; treatment-context association was not called prediction. The binary-outcome HR/OR wording is quarantined. | `passed` |
| 40056978 | Corrected proof/article in press, 25 pp; Figures 1-7 checked | Mouse pooled single-cell data, targeted assays, functional experiments and small human evidence were separated. Cell count was not substituted for animal count; safety and human efficacy claims were downgraded. Figure 5B and supplement-dependent central checks remain unresolved. | `needs_correction` |
| 40850615 | NIH author manuscript, 19 pp; Figures 1-5 and Table 1 checked | TCGA RNA, methylation, survival and GTEx normal expression were kept distinct. Prognostic association was not promoted to treatment prediction or race specificity. Six source conflicts were localized and the affected formulations quarantined. | `passed` |

## Six-gate verdict

| PMID | coverage_check | evidence_check | results_check | language_check | traceability_check | transfer_check | Review status |
|---|---|---|---|---|---|---|---|
| 32068166 | pass | pass | fail | pass | pass | pass | `needs_correction` |
| 33096269 | pass | pass | fail | pass | pass | pass | `needs_correction` |
| 37247843 | pass | pass | pass | pass | pass | pass | `passed` |
| 40056978 | pass | pass | pending | pass | pass | pass | `needs_correction` |
| 40850615 | pass | pass | pass | pass | pass | pass | `passed` |

Gate basis:

- `coverage_check`: every supplied main-PDF page and main display/caption was reviewed; missing external supplements are explicit.
- `evidence_check`: population or model, assay layer, denominator, comparator and association-versus-function boundaries were reconstructed.
- `results_check`: positive, negative, borderline, adjusted, imprecise and exploratory results were checked against main text and visuals. A fail or pending value marks unresolved source conflict or unavailable central support; it does not erase the completed read.
- `language_check`: disputed source wording was excluded or put under live control; retained templates preserve uncertainty and evidence ceiling.
- `traceability_check`: PMID, DOI, supplied version, SHA-256, physical page, review record and archive filename are registered.
- `transfer_check`: templates require the user's actual facts and do not transfer genes, cohorts, treatments, numbers or conclusions.

The two `passed` outcomes are bounded to the supplied main PDF and the cataloged sentences. They do not imply review of external supplements or independent validation of the studies. The three `needs_correction` articles remain visible for audit and bounded learning but are excluded by `--accepted-only` and cannot be rendered as approved templates.
