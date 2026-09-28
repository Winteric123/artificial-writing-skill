---
name: artificial-writing-skill
description: "Translate, revise, draft, audit, synthesize, report, and present biomedical evidence with section-aware vocabulary, collocations, sentence frames, and paragraph structures for Abstract, Introduction, Materials and Methods, Results, Discussion, Conclusion, and related research genres. Use for medical or SCI translation, oncology terminology, evidence-calibrated reporting, or communication involving multi-omics, bioinformatics, preclinical experiments, statistics, immunotherapy, or targeted therapy. Resolve journal, disease or tumor type, communication scenario, manuscript section, audience, and modality as independent selections; use a learned profile only when its registered scope supports the task. Do not use for general non-biomedical translation, clinical decision support, or inventing data, methods, citations, or claims."
---

# Biomedical evidence communication

Translate, revise, draft, audit, synthesize, report and present from the user's evidence. Preserve meaning, numbers, uncertainty and source scope; do not invent findings, analyses, methods or citations. Use US English unless another convention is requested.

## Choose the smallest applicable route

Resolve independently: operation, communication scenario, journal, disease/tumor, manuscript section, audience and evidence domain. Explicit user constraints take precedence, followed by supplied source context, registered profile scope and conservative core fallback. Do not force CCR, lung cancer, STK11 or IMRaD onto unrelated tasks.

Read [the profile registry](references/profile-registry.md) when a profile selection matters. A registered menu, article-level source or highlight does not establish a learned journal/disease style. Current author requirements are external constraints: verify them when exact submission compliance is requested, rather than inferring them from the corpus.

| Task | Load first | Add only when needed |
|---|---|---|
| Translate or lightly polish a sentence | [Translation integrity](references/core-translation-integrity.md) and supplied text | Relevant section language; [evidence rules](references/core-evidence-language.md) if claim strength is at issue |
| Draft/restructure a section or full manuscript | [Communication workflow](references/communication-workflow.md) | [Expression guidance](references/writing-expression-guidance.md), selected journal/section resources |
| Report, results statement, slides or literature synthesis | [Scenario guide](references/communication-scenarios.md) and evidence rules | Communication workflow; do not force manuscript headings |
| STK11 outline, reasoning or Discussion | [STK11 priority hub](references/stk11-priority-references.md) | [Analysis guide](references/stk11-analysis-framework.md), [article logic map](references/stk11-study-logic-map.md), [private workspace template](assets/stk11-project-workspace.md) |
| New PDFs, reading, classification or archiving | [Intake workflow](references/literature-intake-workflow.md) and [acceptance gates](references/deep-reading-acceptance.md) | Actual journal's batch map and maintenance commands |
| Inventory, reading status or missing literature | [Library index](references/library-index.csv) and [inventory rules](references/retrieval-and-maintenance.md) | Journal quality register, [provisional inclusion decisions](references/provisional-inclusion-register.csv), source-version register |
| Search vocabulary, phrases or sentence/paragraph frames | [Retrieval instructions](references/retrieval-and-maintenance.md) | Returned source context, alerts and usage cards |
| Add a profile or maintain the skill | Profile registry and [maintenance workflow](references/retrieval-and-maintenance.md) | Intake workflow, [behavioral evaluation](references/writing-evaluation.md) |

Use [the resource map](references/resource-map.md) to locate conditional article/batch resources; do not read every batch by default. Dated batch notes and historical status summaries are not live inventory authorities.

## Evidence before wording

For substantive output, establish the actual population/model, analysis set, comparator, endpoint, denominator, time point, estimates/uncertainty, adjustment, exploratory status and data/experiment availability. Scale this check to the task; a one-sentence translation does not require a new project workspace.

- Translate faithfully; do not silently add a limitation, interpretation or citation to clean-only translation. Put material scientific questions separately when needed.
- Keep association distinct from causation, prognosis from treatment prediction, internal from external validation, and preclinical effects from patient benefit.
- Preserve a negative primary endpoint. Nonsignificance is not equivalence; different subgroup P values do not establish an interaction.
- Keep actual assay and cohort boundaries: bulk deconvolution is inference, mouse single-cell data are not human data, and targeted protein assays are not a whole-proteome study.
- A proposed method or reference-paper analysis is not an analysis performed in the user's study. Use placeholders or queries for missing evidence, not plausible invented results.
- Follow the user's deliverable and editing level. Do not rewrite an audit-only task or add unnecessary explanatory scaffolding to a short translation.

## Retrieve by section and source

When corpus language is useful, run `python scripts/search_language.py` with the selected section, rhetorical function, domain, unit and source filters; see retrieval instructions for CLI options and registered Chinese/English section aliases. Do not invent a hit, citation, PDF page or tool result when retrieval is unavailable or empty.

Read the returned source context before material reuse. Conventional vocabulary and synthetic frames are not checked quotations. `source_line` is an asset line, not a PDF page; `--pdf-located` is a mechanical literal match, `--context-reviewed` an expression-context recheck, and `--reviewed` article-level acceptance. These are independent.

Default retrieval excludes held/quarantined entries. Audit-only access does not authorize writing reuse. Scope filters must match the same contributing source; article-level labels do not pair every assay with every disease. SCLC is not a substring match to NSCLC. Unknown tags and zero hits are not evidence that the literature is absent.

For broad co-alteration inventories, use [topic rules](references/coalteration-topics.md) and `--co-alteration analyzed`; use sequence-only filters when requested. Preserve copy-number, fusion, same-gene compound, cross-gene and engineered-model distinctions. A gene-context label can include a negative or mutual-exclusivity comparison, not just a positive pair.

## STK11 is an optional writing module

The [membership map](references/stk11-writing-reference-map.json) connects original core highlights with separately labelled topic support. Prioritize only the modules relevant to the user's evidence; narrow STK11 sentence translation can go straight to section language. `--highlight` remains core-only; retrieve support papers by PMID.

Discuss sequence co-mutation, copy-number/neighboring-locus context, clinical association, functional state, longitudinal evolution and mechanism separately where their evidence differs. Keep direct STK11 evidence distinct from contextual analysis and structural analogues. Highlight status neither proves STK11 causality nor promotes source acceptance.

## Inventory and intake safeguards

Actual journal identity governs archiving and corpus assets; project names and intake folders do not. Retain issue/online dates, full title, PMID/DOI, actual PDF version and hash. Preprint, author manuscript, pre-proof and formal versions retain independent evidence histories.

Exclude commentaries, editorials and replies from reusable corpus learning; keep narrative reviews/background sources separate. This does not prohibit translating or drafting these genres on request. Do not mistake treatment response for reply-type correspondence.

Report scope for every count: journal(s), issue-year range, topic/batch filter and formal versus provisional inclusion. Indexed, PDF-present, screened, main-text-complete, source-recheck-passed and independently reviewed are different states. Use current journal registers and derived indexes rather than old prose snapshots; topic support and core priority are separate from all of them.

Only clear an authorized intake file after confirming the exact archived version has a matching hash and completed reading evidence. Preserve unread files, non-PDF files and unrelated/managed copies. Never update reading or review status merely because parsing, indexing, testing or drafting succeeded.

## Audit and deliver

Check numbers/units/denominators, consistent terminology, tense/analysis status and claim strength against the source. Do not calculate unstated values unless requested; label permitted calculations as derived. Do not invent missing uncertainty, methods, ethics, registration or novelty claims.

Ask focused questions only when ambiguity changes the result. For isolated nonblocking gaps in long work, continue with clearly marked queries. Default to the requested clean text, unresolved scientific queries and only material edit notes.

Keep private study data and outputs outside shared skill roots. After changes, run appropriate integrity/regression checks and actual writing cases; distinguish mechanical tests, same-agent behavioral checks and independent/source review. Follow [maintenance instructions](references/retrieval-and-maintenance.md) for rebuilds and Wisp file/catalog/conversation verification.
