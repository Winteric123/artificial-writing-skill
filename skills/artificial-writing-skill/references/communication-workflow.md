# Biomedical communication workflow

Load this detailed workflow for section/manuscript drafting, restructuring, synthesis, reports and presentations. For a short faithful translation, apply [core translation integrity](core-translation-integrity.md) and the requested constraints without loading every project or batch reference. [Core evidence rules](core-evidence-language.md) and [expression guidance](writing-expression-guidance.md) support evidence-calibrated prose.

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

Identify the deliverable unit, scenario, genre, target section, audience, study design, population or model, comparator, endpoint hierarchy, analysis status, evidence maturity, and intended use. Normalize manuscript headings to `title`, `abstract`, `introduction`, `methods`, `results`, `discussion`, `conclusion`, or `translational-relevance`; preserve a journal-specific displayed heading in the output. Treat `Patients and Methods`, `Materials and Methods`, `Experimental Procedures`, and equivalent headings as `methods`. Do not force a report, results statement, presentation, commentary, review, regulatory summary, response letter, figure legend, or table note into IMRaD structure.

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

## Select section-indexed language

Route learned language in this order:

1. manuscript section or non-IMRaD genre;
2. rhetorical function within that section;
3. evidence domain such as oncology, multi-omics, bioinformatics, preclinical, statistics, immunotherapy, targeted therapy, efficacy, safety, or pharmacology;
4. expression unit: vocabulary, collocation, phrase frame, sentence frame, or paragraph architecture;
5. evidence and claim tier.

For an Abstract, route each clause separately as background, objective, methods, results, or conclusion; do not treat the entire Abstract as one undifferentiated style pool. For a full manuscript, process sections independently and then run a cross-section coherence audit. If a supplied heading is absent, infer the section from function only when the distinction is clear; otherwise ask a focused question when section choice would materially change tense, claim strength, or information order.

Technical terms are often valid across several sections. Treat their section labels as typical-use metadata rather than exclusivity rules. Rhetorical frames and paragraph architectures are section-bound: do not move procedural Methods wording into Results, direct observations into Discussion-only interpretation, or validation recommendations into the Results backbone.

When using the structured catalog, preserve the selected row's `reuse_status` and provenance granularity. A catalog row is a retrieval and traceability record, not a quotation record. Rebuild the final sentence from the user's evidence and never attribute an abstracted or synthetic expression verbatim to a listed article without reopening that article.

Use the stable retrieval ID and content-addressed index version for traceability. Sequential legacy IDs require their original catalog hash. Default retrieval excludes held or quarantined entries; audit-only visibility does not authorize writing reuse. Follow usage cards for Chinese meaning, confusable expressions and safe transfer, without treating a card as source acceptance.

For the 13 user-designated STK11 framework articles, consult [the dated source rechecks](source-rechecks/2026-09-28-summary.md). These bounded same-agent checks do not certify every expression or external supplement. `--context-reviewed` selects individually rechecked expression contexts; `--reviewed` selects article-level acceptance and `--pdf-located` selects mechanical literal matches. These are different filters. Returned `source_context_rechecks` retain PDF hash, physical pages, reviewer, date and support boundaries without certifying quotations. Use the [additional bilingual usage cards](language-usage-cards-rechecks.json) for collocations, safe/unsafe examples and common denominator, endpoint, assay and inference confusions.

Keep article themes, source disease/tissue/model, and expression-level topics separate. `--domain` selects expression topics; `--article-domain` explicitly selects broad legacy article tags. Lexical topic candidates are not verified assay annotations. Scope filters exclude unclassified records rather than guessing from titles; zero hits do not establish literature absence. Disease filters are exact unless `--include-subtypes` is requested, so SCLC never silently matches NSCLC. An article-level match does not link every method to every listed disease: read the returned context, particularly for mixed-cohort multi-omics studies.

Treat `source_line` as a line in a curated asset, not a PDF page. `source_locator` separates hash-linked, one-based physical PDF text matches from unverified reading-note page hints and unlocated expressions. `--pdf-located` selects literal text matches in the same source article as the other source filters; it does not certify semantic context or quotations. Synthetic frames need no verbatim counterpart and must never receive guessed quotation pages. `original_wording_verified=false` prohibits presenting the expression as a checked verbatim quotation. Curated topic labels, main-text completion and source-recheck acceptance remain independent.

Use [source-scope-backfill.json](source-scope-backfill.json) together with the original annotations for legacy disease, tissue, model and source-role facets. Consult `facet_status`: empty means not curated, not absent; populated facets are identified but not exhaustive, and article-level tags do not join separate cohorts or assays. These filter labels are not new learned tumor/journal profiles. See [source-provenance-audit.md](source-provenance-audit.md) for the dated repair scope and remaining limitations; live counts and queues are generated by `scripts/build_provenance_audit.py`.

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
