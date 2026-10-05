# Profile registry

Use this registry to select independent communication profiles and to avoid claiming unsupported learned styles. A selection can be combined with selections on other axes, but its evidence scope does not expand through combination.

## Support levels

- **Corpus-backed:** Derived from an identified corpus with documented provenance, boundaries, and validation.
- **Rules-only:** Supported by general scientific communication rules but not by a dedicated learned corpus.
- **Source-grounded:** Use terminology and structure supplied by the user or authorized sources without claiming a reusable learned profile.
- **Unsupported:** No adequate rules, source material, or validated corpus is available; ask for material only when the gap is consequential.

## Status authority

This registry describes reusable support and fallback, not live completion counts. Read current bibliographies/quality registers through [the journal registry](journal-registry.json) and [library index](library-index.csv). Dated batch prose is historical when it conflicts with those records. Core priority, topic support, main-text reading, bounded same-agent source review and independent review are separate fields; none should be inferred from this menu.

## Current selections

### Journal

| Selection | Aliases | Support | Scope and fallback |
|---|---|---|---|
| `none` | non-journal, internal | Rules-only | Use core integrity, evidence, and selected scenario rules. |
| `ccr` | CCR, Clinical Cancer Research | Corpus-backed | Current corpus is lung-cancer-focused with explicitly labelled user-supplied cross-tumor methods/language references. Those sources retain their actual disease and article-level source role; they do not establish a disease-wide learned profile. Use CCR section, genre, phrase, provenance, category, and bibliography references only within their documented coverage. |
| `jto` | JTO, Journal of Thoracic Oncology | Source-grounded | Article-level original-research sources are registered in [jto-corpus-bibliography.csv](jto-corpus-bibliography.csv), with [section language](jto-section-language-catalog.csv) and [reading evidence](jto-deep-reading-ledger.md). The four historical STK11 highlights remain a subset, not the whole JTO set. The separate [maintenance queue](jto-maintenance-queue.md) includes candidates and background-only reviews; it is not a read corpus or complete JTO inventory. Do not claim a learned journal-wide JTO style. |
| `cancer-discovery` | Cancer Discovery, CD | Source-grounded | Article-specific molecular subtype, immune resistance and mechanism sources, not a journal-wide style corpus. Use the [section catalog](cancer-discovery-section-language-catalog.csv), [bibliography](cancer-discovery-stk11-priority-bibliography.csv), [ledger](cancer-discovery-stk11-deep-reading-ledger.md), and [quality register](cancer-discovery-reading-quality-register.csv). Human clinical and mouse-model evidence retain separate scopes. |
| `nature` | Nature | Source-grounded | Article-specific dual-checkpoint and perioperative biomarker sources, not a Nature-wide style corpus. Use the [section catalog](nature-section-language-catalog.csv), [bibliography](nature-stk11-priority-bibliography.csv), [ledger](nature-stk11-deep-reading-ledger.md), and [quality register](nature-reading-quality-register.csv). Supplied corrected/early typeset versions and embedded Extended Data retain their own boundaries; external supplements are not certified by main-text completion. |
| `annals-of-oncology` | Annals of Oncology | Source-grounded | Selected metastatic genomics, clonality and trial biomarkers; [journal registry](journal-registry.json) names the separate bibliography, ledger, quality and section catalog. No journal-wide learned style. |
| `nature-medicine` | Nature Medicine | Source-grounded | HUDSON article-level trial and biomarker language; not a general learned journal profile. Separate nonrandomized regimen comparisons and experimental hypotheses. See journal registry. |
| `nature-genetics` | Nature Genetics | Source-grounded | SelectSim computational co-mutation analysis; not experimental synergy or a journal-wide style. See journal registry and [classification guide](stk11-assay-treatment-guide.md). |
| `cell-research` | Cell Research | Source-grounded | Selected surgical progression/omics article; preserve original versus external data and model context. See journal registry. |
| `cancer-cell` | Cancer Cell | Source-grounded | Selected KRAS resistance/plasticity article; clinical and mouse multiomics remain distinct. See journal registry. |
| `sttt` | Signal Transduction and Targeted Therapy | Source-grounded | JOSD2/LKB1 article-level mechanism language; functional suppression is not a patient co-mutation result. See journal registry. |
| `jitc` | Journal for ImmunoTherapy of Cancer, JITC | Source-grounded | Selected clinical biomarker, smoking-context and preclinical immune-mechanism studies; protein expression, sequence mutation and treatment-associated outcomes remain distinct. No universal ICI response rule or journal-wide style. See journal registry and [intake boundaries](supplement-ccr-2026-10-02-intake.md). |
| `jco` | Journal of Clinical Oncology, JCO | Source-grounded | Selected acquired-ICI-resistance and CodeBreaK100 follow-up articles; retain paired-assay, efficacy-evaluable and extreme-outcome biomarker denominators. No journal-wide learned style. See journal registry. |
| `cancer-research` | Cancer Research | Source-grounded | Article-specific STK11/LKB1 immune, epigenetic, metabolic and therapeutic-vulnerability sources; early clinical pharmacodynamics are not established clinical benefit. Not a journal-wide learned style. See journal registry and [intake boundaries](supplement-ccr-2026-10-02-intake.md). |
| `nature-communications` | Nature Communications | Source-grounded | Article-specific metabolic, IAP-JAK immune-mechanism and LCNEC molecular-characterization sources; preserve tumor type, original/reanalyzed assays and model boundaries. No journal-wide learned style. |
| `nature-cancer` | Nature Cancer | Source-grounded | PMID34870237 NSCLC proteogenomic subtypes and classifier evaluation, with embedded Extended Data; not a journal-wide learned style or treatment-predictive validation. Source: [bibliography](nature-cancer-corpus-bibliography.csv), [reading ledger](nature-cancer-deep-reading-ledger.md), [language](nature-cancer-section-language-catalog.csv), [quality](nature-cancer-reading-quality-register.csv), 2026-10-02. Use core rules outside this article's scope; first-pass source reading is not independent acceptance. |
| `cell-reports` | Cell Reports | Source-grounded | PMID33264619 STK11/KEAP1 co-loss, ferroptosis and SCD1 dependence; clinical prognosis and immunodeficient-model vulnerability remain separate. Source: [bibliography](cell-reports-corpus-bibliography.csv), [ledger](cell-reports-deep-reading-ledger.md), [language](cell-reports-section-language-catalog.csv), [quality](cell-reports-reading-quality-register.csv), 2026-10-02. No journal-wide style, immune-competent efficacy or patient drug-benefit validation; use core fallback elsewhere. |
| `nature-cell-biology` | Nature Cell Biology | Source-grounded | PMID34341533 stage-dependent chromatin accessibility and metastasis; original mouse and reanalyzed human assays are separate, not same-cell multiome. Source: [bibliography](nature-cell-biology-corpus-bibliography.csv), [ledger](nature-cell-biology-deep-reading-ledger.md), [language](nature-cell-biology-section-language-catalog.csv), [quality](nature-cell-biology-reading-quality-register.csv), 2026-10-02. No journal-wide learned style or therapeutic-efficacy validation; use core fallback outside article scope. |
| `esmo-open` | ESMO Open | Source-grounded | One real-world STK11/KEAP1 prognostic study; observational prognosis is not treatment prediction. |
| `nature-metabolism` | Nature Metabolism | Source-grounded | One LKB1/KEAP1 metabolic-mechanism study; model vulnerability is not clinical efficacy. |
| `cell` | Cell | Source-grounded | One lung-adenocarcinoma proteogenomic study; retain assay, cohort and validation layers. |
| `jco-precision-oncology` | JCO Precision Oncology | Source-grounded | One STK11/TP53 immunotherapy cohort; retrospective subgroup association is not a prospective selection rule. |
| `jto-crr` | JTO Clinical and Research Reports | Source-grounded | One randomized-trial exploratory biomarker analysis; this journal is separate from JTO and is not assigned JTO's profile or impact factor. |
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

For STK11 project-level planning, [the analysis-method guide](stk11-analysis-framework.md) and [article logic map](stk11-study-logic-map.md) extend the core-highlight route with separately labelled topic support. [Membership](stk11-writing-reference-map.json) is an article-selection layer only: it does not change journal/disease support, core-highlight membership, reading quality, or establish a validated STK11 molecular profile. Distinguish direct STK11 analyses, contextual evidence and structural analogues before combining modules.

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

Current modality support is article-specific, not an assurance that every source supplies every assay. Use the source disease/tissue/model facets, expression-level domains and actual evidence records returned by retrieval. Distinguish bulk inference from direct cellular measurements, patient from mouse data, and targeted protein/imaging panels from global proteomics. Historical capability descriptions have moved to [the conditional resource map](resource-map.md); they are not current article totals or live reading states.

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

## Source-grounded cross-tumor methods — 2026-09-23

The [five-paper methods set](ccr-2025-omics-methods-2026-09-23-language.md) adds article-specific methodology, not new disease-wide profiles. PMID39540841 isosteosarcoma lungmetastasis; PMID39879384 isprostate bone/lungmetastasis; PMID39841860 ismainlypancreaticimaging withaCalu6lungnegativecontrol. Retain actualdisease labels anddo notpool theirclinicalclaims withprimaryNSCLC. CCR remainslung-focused with explicitadjacent-method exceptions. The SEZ6review isbackground-only anddoesnotestablish anoriginalresearch corpus.

## 2024 completion and later2026intake

See [ccr-2024-and-intake-2026-09-23.md](ccr-2024-and-intake-2026-09-23.md) for37article-specific reading records.33eligible sources enter the section catalog;4background sources are excluded from original-study language. New domains include variant-origin prediction, spatial pathology, LCNEC single-cell profiling, proteomics, cfDNA epigenomics and inherited-risk surveillance. These expand article-level terminology, not disease-wide or journal-wide style claims.
