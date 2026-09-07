---
name: artificial-writing-skill
description: "Translate, revise, draft, audit, synthesize, report, and present biomedical evidence across manuscripts, scientific reports, results narratives, abstracts, slide or poster text, briefings, response letters, and other research communications. Use for medical or SCI translation, oncology terminology, evidence-calibrated reporting, or communication involving multi-omics, bioinformatics, preclinical experiments, statistics, immunotherapy, or targeted therapy. Resolve journal, disease or tumor type, communication scenario, audience, and modality as independent selections; use a learned profile only when its registered scope supports the task. Do not use for general non-biomedical translation, clinical decision support, or inventing data, methods, citations, or claims."
---

# Artificial biomedical evidence communication

Produce faithful, concise biomedical communication whose claim strength follows the study design. Use US English unless the user supplies another language convention. Follow an explicitly supplied journal format, report template, presentation constraint, word limit, reporting guideline, or output format before any corpus-informed profile.

## Resolve independent selections

Resolve these axes separately before substantive work:

1. **Operation:** translate, polish, rewrite, draft, audit, synthesize, report, or present.
2. **Communication scenario:** journal manuscript, scientific or technical report, standalone results statement, abstract, slide or oral presentation, poster, response letter, literature synthesis, or another user-defined deliverable.
3. **Journal profile:** no journal profile, CCR, another registered journal, or an unsupported journal governed only by supplied instructions and core rules.
4. **Disease profile:** general biomedical, general oncology, lung cancer, another registered disease or tumor type, or source-grounded terminology without a learned disease profile.
5. **Audience and use:** specialist, multidisciplinary, executive, regulatory, patient-facing, internal research, submission, publication, or presentation.
6. **Evidence domain:** clinical, translational, multi-omics, bioinformatics, preclinical, statistical, therapeutic, or mixed.

Read [profile-registry.md](references/profile-registry.md) to determine which selections are currently corpus-backed, rules-only, source-grounded, or unsupported. Record the selected route internally as `operation | scenario | journal | disease | audience | domain`.

Apply this precedence order: explicit user selection, supplied source context, registered profile scope, then conservative core fallback. Do not silently infer a journal or tumor type from vocabulary alone. If no journal is relevant to the deliverable, select `journal=none`. If the tumor type is unspecified or mixed, select `disease=general-oncology` unless the evidence clearly supports a narrower choice.

CCR is currently the only corpus-backed journal selection, and lung cancer is currently the only corpus-backed tumor selection. Treat both as replaceable selections rather than permanent properties of the skill. The current CCR corpus is lung-cancer-focused; do not present it as a general all-cancer CCR corpus. For another journal or tumor type, apply core rules and source terminology without claiming a learned profile unless it has been registered and validated.

Keep journal, disease, scenario, and modality corpora, phrase signals, and quantitative summaries separate. Combine selections functionally, but never pool their corpus statistics or imply cross-domain coverage without explicit evidence. Treat current author instructions as external requirements rather than learned style. Verify current official requirements when exact submission compliance is requested and source access is authorized.

## Load only the references needed

- Read [profile-registry.md](references/profile-registry.md) when selecting, explaining, combining, or extending journal, disease, scenario, audience, or modality profiles.
- Read [core-translation-integrity.md](references/core-translation-integrity.md) for translation, polishing, rewriting, or bilingual alignment under every journal profile.
- Read [core-evidence-language.md](references/core-evidence-language.md) for Results, Discussion, Conclusions, abstract conclusions, biomarker claims, subgroup analyses, diagnostic or AI models, and translational claims under every journal profile.
- Read [communication-scenarios.md](references/communication-scenarios.md) for scientific reports, standalone results statements, slide or oral presentations, posters, technical briefings, executive summaries, or literature syntheses. Use its scenario architecture independently of the journal and tumor selections.
- Read [ccr-section-patterns.md](references/ccr-section-patterns.md) when drafting or restructuring a manuscript section with the selected CCR profile.
- Read [ccr-non-imrad-genres.md](references/ccr-non-imrad-genres.md) for CCR-informed commentaries, narrative reviews, regulatory summaries, response letters, figure legends, or other non-IMRaD writing.
- Read [ccr-phrase-patterns.md](references/ccr-phrase-patterns.md) only after selecting the CCR profile and identifying the section and evidence tier. Use its patterns functionally; never copy source sentences or treat phrases as quotas.
- Read [ccr-2026-translational-mechanisms-fulltext-language.md](references/ccr-2026-translational-mechanisms-fulltext-language.md) when the task needs full-manuscript CCR language for tumor biology, transcriptomics, TCR profiling, bioinformatics, basic experiments, statistical results, immunotherapy, targeted therapy, drug activity, resistance, or translational interpretation. Observe its modality-coverage boundary: the five-paper set does not support primary single-cell, spatial-transcriptomic, or proteomic wording.
- Read [ccr-corpus-provenance.md](references/ccr-corpus-provenance.md) when explaining the CCR profile's evidence base, coverage, quantitative signals, or limitations.
- Read [ccr-category-index.md](references/ccr-category-index.md) whenever the user asks how corpus articles are classified by CCR, how many articles fall in each CCR category, or which category-level genre exclusions apply. Treat `ccr_official_category` in the bibliography as the article-level authority and do not infer a detailed section for an Online First record labeled only `Research Article`.
- Read [ccr-deep-reading-ledger.md](references/ccr-deep-reading-ledger.md) whenever the user asks which articles have been deeply read, fully read for language, or remain pending. Treat this ledger as the sole authority for deep-reading completion; never infer completion from corpus processing, PDF parsing, source-coverage, section-corpus, or phrase-bank flags.
- Search [ccr-corpus-bibliography.csv](references/ccr-corpus-bibliography.csv) only when the user asks about a paper title, PMID, DOI, publication year, corpus membership, CCR official category, category-verification source, genre status, article type, corpus-processing history, or the complete source list. Filter to relevant rows before loading content; load or format all 204 rows only when explicitly requested.

## Route the operation and deliverable

Classify each input segment independently:

- **Translate:** Preserve meaning, scope, logic, numbers, citations, and uncertainty. Treat the source as authoritative unless it conflicts with another supplied source.
- **Polish:** Improve grammar, precision, cohesion, and idiomatic expression without changing scientific content.
- **Rewrite:** Reorganize supplied content while preserving every supported assertion and explicitly flagging any material change.
- **Draft:** Write only from facts and evidence supplied by the user or retrieved from authorized sources.
- **Audit:** Identify factual, numerical, terminology, logic, structure, or claim-strength problems without rewriting unless requested.
- **Synthesize:** Combine multiple supplied or authorized sources while preserving source boundaries, disagreement, evidence hierarchy, and traceability.
- **Report:** Organize evidence into the selected report architecture, distinguish observations from interpretation, and preserve limitations and provenance.
- **Present:** Convert evidence into audience-appropriate slide, poster, oral, or briefing language without simplifying away uncertainty or inflating conclusions.
- **Hybrid:** Apply the appropriate mode separately to each part.

Identify the deliverable unit, scenario, genre, target section, audience, study design, population or model, comparator, endpoint hierarchy, analysis status, evidence maturity, and intended use. Do not force a report, results statement, presentation, commentary, review, regulatory summary, response letter, figure legend, or table note into IMRaD structure.

## Build an evidence ledger

Before drafting substantive claims, record internally:

- design, setting, population or model, and analysis set;
- intervention or exposure and comparator;
- primary, secondary, safety, mechanistic, and exploratory endpoints;
- denominators, follow-up, and experimental time points;
- effect estimates, uncertainty intervals, P or q values, and adjustment method;
- prespecified, post hoc, or exploratory status;
- multiplicity or FDR handling and subgroup interaction evidence;
- training, tuning, internal validation, and independent external validation;
- central limitations and the inference each limitation weakens;
- proposed clinical or experimental use.

Use a lightweight ledger for a single sentence and a complete ledger for a section or manuscript. Mark missing, ambiguous, or contradictory elements. Never fill a gap from plausibility.

## Draft by evidence tier

Choose verbs from the evidence, not from the desired rhetorical strength. Never upgrade:

- association to causation;
- prognosis to treatment prediction;
- analytical performance to clinical utility;
- internal validation to external validation;
- a single-arm signal to comparative benefit;
- a secondary endpoint to overall trial success;
- a null result to equivalence;
- an exploratory subgroup to confirmatory evidence;
- preclinical efficacy to patient benefit;
- a review or commentary interpretation to newly generated primary evidence.

Keep a negative primary endpoint prominent in the Abstract, opening Discussion, Conclusion, and Translational Relevance. Do not let a favorable secondary or subgroup result obscure it.

## Execute the requested mode

For translation, preserve scientific equivalence first and then make the target language natural. For polishing, retain the original fact structure unless restructuring is requested. For rewriting or drafting, use the relevant section architecture and connect each conclusion to the evidence ledger. For auditing, distinguish errors from optional stylistic preferences. For synthesis, retain article-level provenance and distinguish consensus from disagreement. For reports, separate purpose, data scope, findings, interpretation, limitations, and recommended next steps as appropriate. For results statements, state the comparison, direction, magnitude, uncertainty, time point, and inference boundary when available. For presentations, use evidence-based headlines, visible denominators and uncertainty, and audience-appropriate explanations while retaining material caveats.

Do not import PDF extraction artifacts, broken line-end hyphenation, headers, watermarks, disclosure boilerplate, or reference-list fragments into the output.

## Run four mandatory audits

1. **Numbers:** Compare every N, n/N, percentage, sign, decimal, range, date, dose, unit, phase, stage, grade, estimate, CI, P/q/FDR value, AUC, sensitivity, specificity, and follow-up value against the source.
2. **Terminology:** Keep one mapping for abbreviations and for genes, proteins, drugs, assays, endpoints, cohorts, and analysis sets. Do not guess an expansion that changes meaning.
3. **Tense:** Use tense by scientific function. Do not imply that an analysis was prespecified, completed, validated, or ongoing unless the source says so.
4. **Claims:** Inspect every causal, predictive, novelty, superiority, validation, and clinical-utility statement against the evidence ledger.

Do not calculate an unstated value unless requested. Label a requested calculation as derived. Never invent a missing CI, P value, denominator, cutoff, unit, registration, ethics approval, method, cohort, citation, or novelty claim.

## Handle uncertainty

Ask no more than three focused questions before proceeding when uncertainty about the design, comparator, endpoint hierarchy, numerical value, unit, abbreviation, analysis status, target section, or journal format would materially change the result.

For non-blocking omissions, use the most conservative supported wording and state the assumption. For isolated issues in a long document, continue with `[QUERY: ...]` rather than withholding the entire revision. If the user requests an unsupported claim, decline only that claim and offer an evidence-bounded formulation, a clearly marked fill-in field, or an explicitly illustrative example.

## Deliver

Default to:

1. clean requested text;
2. scientific queries only when unresolved issues remain;
3. material edit notes only when claim strength, logic, or structure changed.

Do not list routine grammar edits. Honor requests for clean-only, bilingual, sentence-aligned, tracked-change, table, reviewer-response, report, slide outline, speaker notes, poster text, briefing, or structured results output.

## Maintain CCR corpus boundaries

Apply these rules whenever adding source literature to the CCR profile:

- Include a full research article only when it reports original analyzable data relevant to lung cancer. For a basket or pan-tumor study, require an explicitly reported lung-cancer cohort or lung-specific analysis.
- Exclude commentaries and editorials. Exclude author replies, replies to letters or reviewers, rebuttals, and response-only correspondence. Do not add excluded genres to the bibliography, corpus counts, section statistics, or phrase bank.
- Preserve the eight legacy `CCR Translations` commentary rows only for traceability and honor their `excluded_commentary_legacy_index_only` status; never use them in future language-learning or quantitative-corpus updates.
- Do not mistake scientific phrases such as `response to treatment` or `predictors of response` for reply-type correspondence; verify the journal article category, title, and full text.
- Verify the main-article PDF, title, PMID, DOI, article type, uniqueness, and review status before changing corpus records or counts.

These boundaries govern source-corpus maintenance only. Continue to translate, draft, polish, or audit a commentary or response letter when the user requests that writing task.

## Extend the selection registry

- Keep translation integrity, evidence calibration, numerical fidelity, and anti-fabrication rules in the `core-*` references.
- Register every new journal, disease or tumor type, communication scenario, audience, or modality in [profile-registry.md](references/profile-registry.md) before calling it supported.
- Add journal-specific section, genre, phrase, provenance, and bibliography files under `references/` with a stable journal prefix.
- Add disease-specific terminology, endpoint, staging, treatment, assay, and limitation references with a stable disease prefix. Keep molecular alterations such as `STK11` as topic or biomarker selections unless the user explicitly defines a reusable molecular profile.
- Add or revise scenario guidance in [communication-scenarios.md](references/communication-scenarios.md) when supporting a new report or presentation type.
- Record aliases, scope, evidence source, support level, exclusions, fallback, and validation status for every selection. A menu entry alone does not make a profile corpus-backed.
- Preserve separate corpus counts and limitations for every journal and disease. Never pool coverage or phrase-bank statistics without an explicit cross-profile analysis.
- Revalidate the complete skill and forward-test explicit, unspecified, unsupported, and conflicting combinations after each selection addition.
