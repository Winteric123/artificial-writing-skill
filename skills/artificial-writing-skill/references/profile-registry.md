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
| `cancer-discovery` | Cancer Discovery, CD | Source-grounded | Two original studies (2015/2018), not a journal-wide style corpus. Use the [article language](cancer-discovery-2026-09-19-stk11-language.md), [section catalog](cancer-discovery-section-language-catalog.csv), [bibliography](cancer-discovery-stk11-priority-bibliography.csv), [ledger](cancer-discovery-stk11-deep-reading-ledger.md), and [quality register](cancer-discovery-reading-quality-register.csv). For current main-text, supplement and acceptance states, consult the linked quality register and its dated review evidence; do not reuse historical pending summaries as live status. |
| `nature` | Nature | Source-grounded | One 2024 STK11/KEAP1 original study in its supplied corrected version, not a Nature-wide style corpus. Use the [article language](nature-2026-09-19-stk11-language.md), [section catalog](nature-section-language-catalog.csv), [bibliography](nature-stk11-priority-bibliography.csv), [ledger](nature-stk11-deep-reading-ledger.md), and [quality register](nature-reading-quality-register.csv). Use the linked quality register and dated review record for current states. The supplied corrected main PDF and embedded Extended Data have their own recorded scope; external supplements are not certified by a main-text completion or acceptance entry. |
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
