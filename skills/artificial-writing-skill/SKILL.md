---
name: artificial-writing-skill
description: "Translate Chinese biomedical text into publication-ready English, translate English biomedical or oncology text into accurate Chinese, polish or rewrite English, and draft or audit biomedical manuscripts with evidence-calibrated journal profiles. Use for medical or SCI translation, manuscript polishing, section drafting, logic revision, response letters, abstracts, Methods, Results, Discussion, Translational Relevance, reviews, commentaries, and related oncology writing. Use the Clinical Cancer Research (CCR) lung-cancer profile by default until another supported journal profile is explicitly selected. Do not use for general non-biomedical translation, clinical decision support, or inventing data, methods, citations, or claims."
---

# Artificial biomedical translation and writing

Produce faithful, concise biomedical prose whose claim strength follows the study design. Use US English unless the user supplies another language convention. Follow an explicitly supplied journal format, word limit, reporting guideline, or output format before any corpus-informed profile.

## Select the journal profile

- Use the **CCR lung-cancer profile** for `CCR`, `Clinical Cancer Research`, lung-cancer CCR style, or any request that does not name another journal. It is the only bundled journal profile in this version and is therefore the default.
- If the user names an unsupported journal, apply the core integrity and evidence rules, follow any supplied author instructions, and do not claim to use a learned profile for that journal. Ask for clarification only when profile-specific imitation would materially change the result.
- Keep journal corpora, phrase signals, and quantitative summaries separate. Do not blend profiles unless the user explicitly requests a hybrid.
- Treat current author instructions as external requirements rather than learned style. Verify the journal's current official requirements when exact submission compliance is requested and source access is authorized.

## Load only the references needed

- Read [core-translation-integrity.md](references/core-translation-integrity.md) for translation, polishing, rewriting, or bilingual alignment under every journal profile.
- Read [core-evidence-language.md](references/core-evidence-language.md) for Results, Discussion, Conclusions, abstract conclusions, biomarker claims, subgroup analyses, diagnostic or AI models, and translational claims under every journal profile.
- Read [ccr-section-patterns.md](references/ccr-section-patterns.md) when drafting or restructuring a manuscript section with the default CCR profile.
- Read [ccr-non-imrad-genres.md](references/ccr-non-imrad-genres.md) for CCR-informed commentaries, narrative reviews, regulatory summaries, response letters, figure legends, or other non-IMRaD writing.
- Read [ccr-phrase-patterns.md](references/ccr-phrase-patterns.md) only after selecting the CCR profile and identifying the section and evidence tier. Use its patterns functionally; never copy source sentences or treat phrases as quotas.
- Read [ccr-corpus-provenance.md](references/ccr-corpus-provenance.md) when explaining the CCR profile's evidence base, coverage, quantitative signals, or limitations.
- Search [ccr-corpus-bibliography.csv](references/ccr-corpus-bibliography.csv) only when the user asks about a paper title, PMID, DOI, publication year, corpus membership, article type, reading status, or the complete source list. Filter to relevant rows before loading content; load or format all 189 rows only when explicitly requested.

## Route the request

Classify each input segment independently:

- **Translate:** Preserve meaning, scope, logic, numbers, citations, and uncertainty. Treat the source as authoritative unless it conflicts with another supplied source.
- **Polish:** Improve grammar, precision, cohesion, and idiomatic expression without changing scientific content.
- **Rewrite:** Reorganize supplied content while preserving every supported assertion and explicitly flagging any material change.
- **Draft:** Write only from facts and evidence supplied by the user or retrieved from authorized sources.
- **Audit:** Identify factual, numerical, terminology, logic, structure, or claim-strength problems without rewriting unless requested.
- **Hybrid:** Apply the appropriate mode separately to each part.

Identify the manuscript unit, genre, target section, study design, population or model, comparator, endpoint hierarchy, analysis status, evidence maturity, and intended use. Do not force a commentary, review, regulatory summary, response letter, figure legend, or table note into IMRaD structure.

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

For translation, preserve scientific equivalence first and then make the target language natural. For polishing, retain the original fact structure unless restructuring is requested. For rewriting or drafting, use the relevant section architecture and connect each conclusion to the evidence ledger. For auditing, distinguish errors from optional stylistic preferences.

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

Do not list routine grammar edits. Honor requests for clean-only, bilingual, sentence-aligned, tracked-change, table, or reviewer-response output.

## Extend with another journal profile

- Keep translation integrity, evidence calibration, numerical fidelity, and anti-fabrication rules in the `core-*` references.
- Add journal-specific section, genre, phrase, provenance, and bibliography files directly under `references/` with a stable journal prefix.
- Add the new journal and its aliases to the profile-selection rules, while keeping CCR as the default unless the user changes that preference.
- Preserve separate corpus counts and limitations for every journal. Never pool coverage or phrase-bank statistics without an explicit cross-journal analysis.
- Revalidate the complete skill and forward-test explicit-profile, default-profile, unsupported-journal, and cross-profile-conflict requests after each profile addition.
