# Profile registry

Use this registry to select independent communication profiles and to avoid claiming unsupported learned styles. A selection can be combined with selections on other axes, but its evidence scope does not expand through combination.

## Support levels

- **Corpus-backed:** Derived from an identified corpus with documented provenance, boundaries, and validation.
- **Rules-only:** Supported by general scientific communication rules but not by a dedicated learned corpus.
- **Source-grounded:** Use terminology and structure supplied by the user or authorized sources without claiming a reusable learned profile.
- **Unsupported:** No adequate rules, source material, or validated corpus is available; ask for material only when the gap is consequential.

## Current selections

### Journal

| Selection | Aliases | Support | Scope and fallback |
|---|---|---|---|
| `none` | non-journal, internal | Rules-only | Use core integrity, evidence, and selected scenario rules. |
| `ccr` | CCR, Clinical Cancer Research | Corpus-backed | Current corpus is lung-cancer-focused. Use CCR section, genre, phrase, provenance, category, and bibliography references only within their documented coverage. |
| `jto` | JTO, Journal of Thoracic Oncology | Source-grounded | Four deeply read original-research papers (one 2025 and three 2026) are registered only as STK11-priority article-level references. Use [jto-2026-09-14-stk11-priority-language.md](jto-2026-09-14-stk11-priority-language.md) within that scope; do not claim a corpus-backed or journal-wide JTO style profile. |
| `cancer-discovery` | Cancer Discovery, CD | Source-grounded | Two original studies (2015/2018), not a journal-wide style corpus. Use the [article language](cancer-discovery-2026-09-19-stk11-language.md), [section catalog](cancer-discovery-section-language-catalog.csv), [bibliography](cancer-discovery-stk11-priority-bibliography.csv), [ledger](cancer-discovery-stk11-deep-reading-ledger.md), and [quality register](cancer-discovery-reading-quality-register.csv). Main-text complete; separate acceptance recheck pending. |
| `nature` | Nature | Source-grounded | One 2024 STK11/KEAP1 original study in its supplied corrected version, not a Nature-wide style corpus. Use the [article language](nature-2026-09-19-stk11-language.md), [section catalog](nature-section-language-catalog.csv), [bibliography](nature-stk11-priority-bibliography.csv), [ledger](nature-stk11-deep-reading-ledger.md), and [quality register](nature-reading-quality-register.csv). Main text and embedded Extended Data read; external supplements and acceptance recheck not complete. |
| `medrxiv-preprint` | medRxiv, supplied preprint version | Source-grounded | One version-specific PRO trajectory paper in [preprint-source-register.csv](preprint-source-register.csv). Use [its language and restrictions](medrxiv-2025-pro-trajectories-language.md) only as preprint evidence, not a journal style corpus or proof that the corresponding CCR version has been read. |
| `other-journal` | user-specified title | Source-grounded | Follow supplied or verified author instructions plus core rules. Do not claim a learned journal style. |

### Disease or tumor type

| Selection | Aliases | Support | Scope and fallback |
|---|---|---|---|
| `general-biomedical` | biomedical, medical | Rules-only | Use source terminology and core evidence rules. |
| `general-oncology` | cancer, pan-cancer, mixed tumors | Rules-only | Use general oncology terminology; preserve tumor-specific distinctions from the source. |
| `lung-cancer` | lung cancer, NSCLC, SCLC when applicable | Corpus-backed | Use the CCR lung-cancer corpus only for covered language functions and retain subtype, stage, biomarker, and treatment distinctions. |
| `other-disease` | user-specified disease or tumor | Source-grounded | Use supplied or authorized disease terminology without claiming a learned profile. |

Do not treat a gene, protein, pathway, assay, drug, or biomarker as a tumor type. Record `STK11`, for example, as a molecular topic within the selected disease profile unless a separate validated molecular profile is later registered.

### Molecular topic

| Selection | Aliases | Support | Scope and fallback |
|---|---|---|---|
| `stk11` | LKB1, STK11/LKB1 | Source-grounded with thirteen user-designated, main-text-read framework references | Use the user's study evidence first. For lung-cancer tasks, prioritize the six CCR ATM/SMARCA4/KRAS/AmpRatio papers and four JTO ERBB2/KRAS/STK11-copy-deletion/MTAP papers, two Cancer Discovery molecular-subtype/PD-1-resistance papers and one Nature dual-checkpoint paper in [stk11-priority-references.md](stk11-priority-references.md), then use the NRF2/STK11/KEAP1 paper in [ccr-2026-09-12-supplement-language.md](ccr-2026-09-12-supplement-language.md) when relevant. PMID 41417462 and PMID 42268349 add direct KRAS-allele-conditioned STK11 co-mutation frameworks. PMID 42409117 remains a structural analogue with no STK11/LKB1 analysis in the supplied main text. PMID 41870274 adds NSCLC STK11/EGFR amplification-ratio co-alteration context, not STK11 copy-loss thresholds or treatment validation. This is not a dedicated, validated STK11 molecular profile and does not establish STK11-specific causality or treatment prediction. |

### Communication scenario

| Selection | Support | Primary use |
|---|---|---|
| `journal-manuscript` | Rules plus selected journal profile | Abstracts and manuscript sections. |
| `scientific-report` | Rules-only | Research, project, experiment, analysis, or technical reports. |
| `results-statement` | Rules-only | Concise narrative statements of statistical, experimental, clinical, or omics findings. |
| `presentation` | Rules-only | Slides, oral reports, posters, speaker notes, and briefings. |
| `response-letter` | Rules plus selected journal profile | Reviewer, editor, regulatory, or stakeholder responses. |
| `literature-synthesis` | Rules-only | Evidence summaries that retain article-level provenance and disagreement. |
| `user-defined` | Source-grounded | Follow the user's template, audience, and constraints. |

Read [communication-scenarios.md](communication-scenarios.md) for scenario-specific execution.

### Evidence domain

Select one or more without treating them as corpus-backed unless a registered reference supports that claim:

- `clinical-oncology`
- `translational-research`
- `transcriptomics`
- `single-cell`
- `spatial-omics`
- `proteomics`
- `multi-omics`
- `bioinformatics`
- `preclinical-experiments`
- `statistics`
- `immunotherapy`
- `targeted-therapy`
- `drug-response-resistance`

In the pre-intake snapshot, the 83-paper CCR full-text deep-read set supported tumor biology, clinical and translational immunotherapy, targeted therapy, bulk and single-cell transcriptomics, spatial transcriptomics, BCR/TCR repertoire profiling, liquid biopsy and MRD, metagenomics, metabolomics, bioinformatics, machine learning, digital pathology, basic experiments, pharmacokinetics, exposure-response modeling, safety, statistics, and regulatory communication. Limited direct proteomics coverage includes the 2025 DKK3 study using global-proteome and secretome LC-MS/MS, MHC-I immunopeptidomics, and plasma proximity-extension profiling, plus the 2026 YL201 study using a targeted 92-protein inflammation panel (75 proteins retained after QC). The latter is antibody-based proximity extension with a PCR/qPCR readout, not proteome sequencing or untargeted mass spectrometry. Treat this as narrow article-level support rather than a mature proteomics profile; protein imaging, flow cytometry, cytokine assays, receptor-occupancy measurements, or reverse-phase protein arrays must not be relabeled as global proteomics. The September 12 CCR addition supports NRF2/STK11/KEAP1 models, post-progression endpoints, and Bayesian clinical estimates. The September 14 CCR priority set adds SMARCA4/ATM/STK11 co-mutation analysis, mutation-class and protein-expression distinctions, bulk-RNA immune deconvolution, reverse-phase-protein-array terminology, retrospective immunotherapy outcomes, and ATM-knockout chemotherapy-response experiments. The September 19 CCR addition adds direct KRAS G12V/Q61–STK11 frameworks, MET IHC/FISH cutoff analysis, serial ctDNA with external validation, spatial and single-cell immune profiling, CSF cellular-therapy pharmacodynamics, rare-histology phase II reporting, RET inhibitor retreatment, Rb-deficient mitotic cell-death experiments, and FRalpha-ADC component-level pharmacology. The eight-paper second September 19 addition adds ploidy-normalized amplification ratios, tissue/liquid concordance, fragmentomic clonal-hematopoiesis classification, longitudinal molecular response, brain-metastasis safety, phase I bispecific-antibody pharmacology, paired single-nucleus RNA with patient-level pseudobulk, and macrophage-dependent phagocytosis. See [ccr-2026-09-19-batch2-language.md](ccr-2026-09-19-batch2-language.md); these are article-level capabilities, not an expanded global-proteomics profile. The later 15-paper existing-index completion adds methylation diagnostic classifiers, epigenetic-instability metrics, PFAS exposure epidemiology, allele-specific SMARCA4 and EGFR analysis, paired resistance genomics, null basket-trial findings, longitudinal patient-reported outcomes, competing-risk adaptive-radiotherapy analysis, RRAS transformation and xenograft experiments, PEF single-cell RNA/AbSeq immune profiling, and externally evaluated AI pathology. See [ccr-2026-09-19-pending15-language.md](ccr-2026-09-19-pending15-language.md); targeted surface-protein assays and multiplex pathology are not an expanded global-proteomics profile. The separate four-paper JTO source set adds ERBB2 domain-stratified genomics, TMB/FGA, STK11/KEAP1/SMARCA4 and STK11/CDKN2A co-alteration language, direct STK11 copy-deletion and 19p locus analysis, targeted gene-level TCGA RNA and reverse-phase-protein-array correlations, multiplex immunofluorescence, stage III cCRT plus durvalumab outcomes, competing-risk recurrence and brain-metastasis reporting, MTAP/CDKN2A/B locus disambiguation, NGS-IHC concordance, EGFR/ALK TKI outcomes, and selected paired-progression sampling. It adds no primary single-cell or spatial-omics dataset, no global proteomics workflow, and no new laboratory intervention experiment. See [ccr-2026-09-12-supplement-language.md](ccr-2026-09-12-supplement-language.md), [ccr-2026-09-14-atm-smarca4-stk11-priority-language.md](ccr-2026-09-14-atm-smarca4-stk11-priority-language.md), [ccr-2026-09-19-supplement-language.md](ccr-2026-09-19-supplement-language.md), and [jto-2026-09-14-stk11-priority-language.md](jto-2026-09-14-stk11-priority-language.md).

The separate Cancer Discovery set adds bulk/microRNA/copy-number/RPPA subtyping, independent classifier evaluation, cell-line drug response and rescue/knockdown, multi-cohort immunotherapy outcomes, and CRISPR syngeneic models. The Nature article adds direct mouse single-cell RNA profiling, pooled in-vivo CRISPR/Tuba-seq, exploratory POSEIDON biomarker contrasts, human bulk immune deconvolution, multiplex imaging, and model-specific immune/iNOS perturbation. These do not create a global-proteomics or human single-cell corpus. The [expanded reference directory](stk11-expanded-reference-directory.md) adds discovery options only, not learned language or completed reading. New routes were registered 2026-09-19; retain journal isolation and use core fallback for unsupported formats.

## Latest intake extension

The [eight-paper 2025 intake](ccr-2025-2026-09-19-intake-language.md) brings the CCR main-text set to91 articles. It adds CNS response-confirmation language, MAPK pathway/ICI biomarker interpretation, empirical shared-variant diagnostics, longitudinal immune/radiomic resistance profiling, oncolytic-virus spatial protein analysis, YAP/HER3/RET perturbation and xenografts, ecMYC genomic/spatial immune context, and LPA resistance multiomics. Actual global protein-abundance profiling in PMID40853904 must retain the unresolved label-free-versus-TMT Methods discrepancy; it does not establish a mature general proteomics profile. MIBI/IMC are spatial protein assays, not spatial RNA sequencing. c4 LPA secretion and CellChat signaling are inferred, not directly measured. None of these additions automatically becomes an STK11 highlight. The earlier83-paper description is the pre-intake snapshot; use [library-index.md](library-index.md) for current totals.

## Selection procedure

1. Extract explicit choices and constraints from the request.
2. Infer a narrower choice from supplied content only when unambiguous.
3. Check the support level and scope in this registry.
4. Apply the relevant references independently for each axis.
5. Use conservative core fallback for unspecified or unsupported axes.
6. State assumptions only when they materially affect the output.

## Registration template

Before adding a reusable selection, record:

- stable ID and aliases;
- profile type: journal, disease, scenario, audience, modality, or molecular topic;
- support level;
- inclusion and exclusion boundaries;
- corpus or rule provenance;
- reference files and version or evidence date;
- fallback behavior;
- validation cases and current validation status.

Do not label a selection corpus-backed until its sources, boundaries, and validation are documented.
