---
name: artificial-writing-skill
description: "Translate, revise, draft, audit, synthesize, report, and present biomedical evidence with section-aware vocabulary, collocations, sentence frames, and paragraph structures for Abstract, Introduction, Materials and Methods, Results, Discussion, Conclusion, and related research genres. Use for medical or SCI translation, oncology terminology, evidence-calibrated reporting, or communication involving multi-omics, bioinformatics, preclinical experiments, statistics, immunotherapy, or targeted therapy. Resolve journal, disease or tumor type, communication scenario, manuscript section, audience, and modality as independent selections; use a learned profile only when its registered scope supports the task. Do not use for general non-biomedical translation, clinical decision support, or inventing data, methods, citations, or claims."
---

# Artificial biomedical evidence communication

Produce faithful, concise biomedical communication whose claim strength follows the study design. Use US English unless the user supplies another language convention. Follow an explicitly supplied journal format, report template, presentation constraint, word limit, reporting guideline, or output format before any corpus-informed profile.

## Resolve independent selections

Resolve these axes separately before substantive work:

1. **Operation:** translate, polish, rewrite, draft, audit, synthesize, report, or present.
2. **Communication scenario:** journal manuscript, scientific or technical report, standalone results statement, abstract, slide or oral presentation, poster, response letter, literature synthesis, or another user-defined deliverable.
3. **Journal profile:** no journal profile, CCR, another registered journal, or an unsupported journal governed only by supplied instructions and core rules.
4. **Disease profile:** general biomedical, general oncology, lung cancer, another registered disease or tumor type, or source-grounded terminology without a learned disease profile.
5. **Manuscript section or genre unit:** title, Abstract component, Introduction, Methods, Results, Discussion, Conclusion, Translational Relevance, a non-IMRaD unit, or a complete document processed section by section.
6. **Audience and use:** specialist, multidisciplinary, executive, regulatory, patient-facing, internal research, submission, publication, or presentation.
7. **Evidence domain:** clinical, translational, multi-omics, bioinformatics, preclinical, statistical, therapeutic, or mixed.

Read [profile-registry.md](references/profile-registry.md) to determine which profile selections are currently corpus-backed, rules-only, source-grounded, or unsupported. Record the selected route internally as `operation | scenario | journal | disease | section-or-genre | audience | domain`.

Apply this precedence order: explicit user selection, supplied source context, registered profile scope, then conservative core fallback. Do not silently infer a journal or tumor type from vocabulary alone. If no journal is relevant to the deliverable, select `journal=none`. If the tumor type is unspecified or mixed, select `disease=general-oncology` unless the evidence clearly supports a narrower choice.

CCR is currently the only corpus-backed journal selection, and lung cancer is currently the only corpus-backed tumor selection. Treat both as replaceable selections rather than permanent properties of the skill. The current CCR corpus is lung-cancer-focused, not an all-cancer CCR corpus. Separate source-grounded STK11-priority sets contain four JTO papers, two Cancer Discovery papers and one Nature paper; these do not establish corpus-backed journal-wide styles. Use each within its documented article-level scope. For another journal or tumor type, apply core rules and source terminology without claiming a learned profile unless registered and validated.

Keep journal, disease, scenario, and modality corpora, phrase signals, and quantitative summaries separate. Combine selections functionally, but never pool their corpus statistics or imply cross-domain coverage without explicit evidence. Treat current author instructions as external requirements rather than learned style. Verify current official requirements when exact submission compliance is requested and source access is authorized.

## Follow the two-track workflow

Use the literature-intake track when adding or reclassifying source papers. Use the communication track when translating, writing, reporting, or presenting. When a request requires both, complete literature intake and validation before using the new material in communication.

### Track A: literature intake and profile maintenance

1. **Verify source identity:** confirm the title, journal, year, PMID, DOI, article type, source file, uniqueness, and current publication status when relevant. Treat the PDF filename, NIHMS identifier, PMCID, DOI and PMID as separate fields; never infer a PMID from a filename or overwrite a verified PMID because of a legacy manifest join. When any identity field conflicts, resolve it against PubMed/DOI metadata and record the old-to-correct mapping in [source-identity-corrections.csv](references/source-identity-corrections.csv) before rebuilding indexes.
2. **Route by journal first:** assign the paper to its actual journal before applying topic labels. Folder names, download locations, keywords, and the user's project name do not determine journal identity.
3. **Keep journal assets separate:** store bibliography rows, deep-reading status, language assets, provenance, and counts under the journal-specific prefix. A cross-journal priority register such as the STK11 highlight list is a retrieval index only and never a pooled corpus.
4. **Apply the genre gate:** keep narrative reviews and non-original narrative infrastructure reports in a separate background register, not original-study Methods/Results learning or original-study completion counts; exclude commentaries, editorials, author replies, rebuttals, reviewer-response documents, and response-only correspondence from reusable literature-learning assets and corpus counts. These genres can still be translated, drafted, or audited when requested.
5. **Deep-read the supplied evidence:** follow [deep-reading-acceptance.md](references/deep-reading-acceptance.md) for complete main-text and main-figure/table coverage, scientific understanding, numerical checks, section-language curation, traceability, and safe transfer. Record supplementary files separately; time spent, PDF parsing, and expression counts do not establish deep reading.
6. **Classify within the journal:** add study design, disease or tumor, molecular topic, clinical/translational domain, omics modality, statistical method, experimental system, and treatment context as secondary classifications. User-supplied original cross-tumor studies may enter as explicitly labelled article-level methods/language references; retain their actual disease and source role, and do not count them as lung-specific validation or silently create a learned disease profile. Verify the publisher's section independently; manuscript-declared labels remain provisional until verified.
7. **Curate section-indexed language:** organize vocabulary, collocations, synthetic sentence frames, paragraph architectures, and figure/table narratives by Abstract component, Introduction, Methods, Results, Discussion, Conclusion, and other applicable genres. Do not store source-specific sentences as reusable templates.
8. **Register status and priority:** update the journal bibliography, authoritative main-text reading ledger, and separate reading-quality register. Preserve reading history; promote review_status to passed only after a documented source recheck passes all six gates. Add a cross-journal highlight only when the user designates the paper as a framework priority; a highlight never establishes review acceptance.
9. **Validate the update:** check identifiers, denominators, numerical transcription, duplicate records, journal isolation, relative links, counts, file hashes, and skill validity before deployment. Run scripts/validate_reading_quality.py for register consistency; report its mechanical checks separately from scientific acceptance or independent review.

For each article, retain the publication year, full title, actual journal, PMID, and DOI in its journal-specific bibliography. Keep publication year separate from download and reading dates; when online and issue years differ, record that distinction. A shortened PDF filename must remain traceable to the full bibliographic record. Use journal/year folders and an author-title-PMID filename when archiving new PDFs, and preserve original-to-archive paths and file hashes in the local intake manifest.

When the user authorizes clearing an intake folder, delete only the exact supplied files whose archived copies have matching hashes and whose actual versions have completed reading records. Preserve unprocessed files and non-PDF contents. An already-read identical copy keeps its original completion date; a preprint copy is checked against its own record, not the formal publication.

Keep formal publication metadata separate from the actual supplied PDF version. A journal pre-proof or author manuscript can support a version-specific main-text read but must not be called the version of record. A preprint with a separate DOI cannot complete its published counterpart. Use [source-version-register.csv](references/source-version-register.csv) for recorded header/identity checks; these checks are not new scientific reads. Preserve unknown dates or categories as unverified rather than filling them from download dates or topic inference.

When reporting completion, distinguish the supplied batch from the entire journal corpus. Check the journal ledger and quality register; report indexed, screened, main-text-complete, and source-recheck-passed states without conflating them. Separate newly completed articles, previously completed duplicates, and pending articles, and state main-text, main-figure/table, supplement, and review scope. Historical completed entries are not automatically rechecked or independently verified. A completed batch does not change the status of other indexed articles. Keep STK11 highlight priority independent of journal classification and reading/review status.

Label every inventory count with its publication-year range, journal scope and any topic/batch filter. Compute included, main-text-complete and eligible-incomplete counts from the same filtered PMID set; report registered and excluded counts separately. In `library-summary.json`, `years` combines all registered formal journals, whereas `journal_years` gives a named journal's year-specific subset. Neither is a topic count without an explicit topic filter. Do not label a year-specific CCR subset as all-year CCR totals, or a cross-journal year total as CCR alone; preprints remain outside formal-journal denominators.

### Track B: biomedical communication

1. Resolve the seven independent selections: operation, scenario, journal, disease, section or genre, audience, and evidence domain.
2. Load only the references authorized by those selections, with the user's source text, data, and explicit constraints taking precedence over learned language.
3. Build an evidence ledger that preserves study design, analysis sets, comparators, endpoints, denominators, estimates, uncertainty, multiplicity, and limitations.
4. Retrieve language by section, rhetorical function, evidence domain, expression unit, and evidence tier.
5. Translate, revise, draft, audit, synthesize, report, or present without adding unsupported facts or analyses.
6. Run the mandatory number, terminology, tense, and claim-strength audits.
7. Deliver the requested format and report only unresolved scientific queries or material changes to evidence interpretation.

## Load only the references needed

- For the2023 remaining-queue completion, use [the36-source map](references/ccr-2023-completion-2026-09-26.md):34 research/regulatory/methods reads with full-section language and2 separately read background sources. This closes the indexed2023 queue only. Keep source numerical/version caveats, actual disease/omics modality, supplementary scope and acceptance status explicit.
- For the 2021–2022 remaining queue, consult [the live batch map](references/ccr-2021-2022-completion-2026-09-26.md). Only individually completed sources contribute section-indexed language; pending sources remain unread, and reviews remain background-only. Preserve numerical/source-version alerts and actual tumor scope.
- For inventories and completion questions, filter [library-index.csv](references/library-index.csv) or read the journal/year overview in [library-index.md](references/library-index.md). Rebuild derived indexes with `python scripts/build_library_index.py`; never infer reading from file presence.
- Select the route in [profile-registry.md](references/profile-registry.md), then load only matching entries from [resource-map.md](references/resource-map.md). Keep core integrity and evidence-calibration rules active under every profile.
- Retrieve language with `python scripts/search_language.py` by section, function, domain, evidence tier and source filters. Follow [retrieval-and-maintenance.md](references/retrieval-and-maintenance.md) for commands, stable IDs, controls and rebuilds. The cross-journal view preserves journal isolation; open the linked asset and inspect returned source alerts before factual reuse.
- For constructive paragraph organization and bilingual collocations, use [writing-expression-guidance.md](references/writing-expression-guidance.md) and returned usage cards. These are rules-only synthetic patterns, not new literature reads or quotations.
- For STK11 writing, prioritize the user-designated [highlight register](references/stk11-priority-references.md). Priority is independent of journal, year, topic classification, reading completion and acceptance review.
- For KEAPness or STK11/radiotherapy wording, use [the two-paper source map](references/ccr-keapness-stk11-2026-09-24.md). Distinguish expression phenocopies from mutation status, treatment associations from predictive effects, and model radiosensitization from patient benefit; retain the source-specific numerical/protocol alerts.
- For the 2026-09-26 intake, use [the 16-PDF batch map](references/ccr-2026-09-26-intake.md) and [version manifest](references/ccr-2026-09-26-reading-manifest.csv). Fourteen newly registered studies contribute article-level section language spanning plasma/tissue NGS, KRAS and EGFR clinicogenomics, ROS1 resistance, CAF bioinformatics, spatial transcriptomics, cellular therapy, lineage plasticity and basket-trial methods; two exact duplicates retain their prior records. Preserve cross-tumor and preclinical transfer limits, and do not infer STK11 priority.
- For the seven-paper 2026-09-24 intake, use [the batch map](references/ccr-2026-09-24-intake.md): FGFR functional profiling, VIOLETTE, ADC/ATR dose escalation, BTC clinicogenomics, ctDNA assay comparison, spatial pathology and MYC amplification. Preserve each source's denominator, version, statistical and cross-tumor transfer restrictions.
- For the2024completion and latest four2026intake sources, use [the37-source batch map](references/ccr-2024-and-intake-2026-09-23.md). It routes article-specific language, source caveats and read-background records; regulatory analyses and secondary data reanalyses retain their distinct roles.
- For the completed 2026-09-23 batch, use [the reading manifest](references/ccr-2026-09-23-reading-manifest.csv) and its section-language assets. Preserve source-specific statistical alerts; cross-tumor methodology references do not establish lung-cancer efficacy. The [SEZ6 review](references/ccr-2025-sez6-review-background.md) is read background only, outside original-study counts.
- For further genomics, multi-omics and bioinformatics acquisition, consult [the 2026-09-23 candidate directory](references/ccr-omics-supplement-candidates-2026-09-23.md). The19-row candidate list is a historical abstract-screening snapshot; consult its current-status overlay before describing acquisition or reading. Only acquired, read and separately indexed sources contribute language; keep cross-tumor methodology, official-category verification and STK11 priority separate.
- For 2025 genomics and clinicogenomic wording, retrieve the [genomics-adjacent batch](references/ccr-2025-genomics-2026-09-20-language.md) through the section catalog. Keep molecular profiles, functional assays, analytical performance, prognosis and treatment prediction distinct; inclusion in this batch does not confer STK11 highlight status.
- Preprints remain version-specific, source-grounded references in [preprint-source-register.csv](references/preprint-source-register.csv), outside formal-journal counts and style catalogs. Never mark a published version read from a preprint alone.
- On corpus updates, regenerate the CCR language catalog when its sources changed, validate reading registers, rebuild the library and language indexes, run regression tests, and validate the skill. The journal registry configures supported inventories. Mechanical consistency is not scientific acceptance.
- For sustained STK11 drafting, use the private [project workspace template](assets/stk11-project-workspace.md) for locked study facts, terminology, figure/result links, citations and resume checkpoints. Never store private study data in the shared skill or publish it with skill updates.
- After a material model/workflow change, use [writing-evaluation.md](references/writing-evaluation.md). Record actual test scope; do not claim model improvement, independent review or higher reading acceptance merely because the model changed.

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

Keep article themes, source disease/tissue/model, and expression-level topics separate. `--domain` selects expression topics; `--article-domain` explicitly selects broad legacy article tags. Lexical topic candidates are not verified assay annotations. Scope filters exclude unclassified records rather than guessing from titles; zero hits do not establish literature absence. Disease filters are exact unless `--include-subtypes` is requested, so SCLC never silently matches NSCLC. An article-level match does not link every method to every listed disease: read the returned context, particularly for mixed-cohort multi-omics studies.

Treat `source_line` as a line in a curated asset, not a PDF page. `source_locator` separates hash-linked, one-based physical PDF text matches from unverified reading-note page hints and unlocated expressions. `--pdf-located` selects literal text matches in the same source article as the other source filters; it does not certify semantic context or quotations. Synthetic frames need no verbatim counterpart and must never receive guessed quotation pages. `original_wording_verified=false` prohibits presenting the expression as a checked verbatim quotation. Curated topic labels, main-text completion and source-recheck acceptance remain independent.

Use [source-scope-backfill.json](references/source-scope-backfill.json) together with the original annotations for legacy disease, tissue, model and source-role facets. Consult `facet_status`: empty means not curated, not absent; populated facets are identified but not exhaustive, and article-level tags do not join separate cohorts or assays. These filter labels are not new learned tumor/journal profiles. See [source-provenance-audit.md](references/source-provenance-audit.md) for the dated repair scope and remaining limitations; live counts and queues are generated by `scripts/build_provenance_audit.py`.

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

## Maintain JTO STK11-priority boundaries

- Treat the four highlighted JTO papers as article-level source-grounded references, not as a corpus-backed JTO style profile or a complete JTO literature inventory.
- For PMID 41932614, do not describe the adjusted ECD-versus-TKD PFS comparison as statistically significant; its reported CI includes 1 and P=0.06.
- For PMID 41619904, use Figure 4 when assigning exact univariable and multivariable STK11/CDKN2A HRs and disclose the mismatch with the Results prose when exact values matter.
- Do not convert the KRAS/STK11 association under cCRT followed by durvalumab into proof of STK11-mediated durvalumab resistance; the study has no non-durvalumab comparator or treatment interaction.
- For PMID 39864548, distinguish mono-allelic deletion from bi-allelic inactivation, keep TCGA expression analyses separate from treatment cohorts, and disclose extensive 19p13.2-13.3 co-deletion and cohort-dependent ICI-alone results.
- Do not call the PMID 39864548 deletion association a validated predictive immunotherapy biomarker; its retrospective non-immunotherapy control does not replace a randomized treatment interaction.
- For PMID 42409117, preserve the article's operational definition of MTAP loss as homozygous deletion with estimated gene copy number below 0.6; do not transfer that definition to STK11 or to PMID 39864548.
- PMID 42409117 contains no STK11/LKB1 analysis in the supplied main text. Use it only as a structural analogue and never as direct STK11 evidence.
- Keep all four JTO papers out of CCR bibliography, ledger, language-catalog, and corpus counts.
- Do not imply that unprovided supplementary files were reviewed.

## Maintain CCR corpus boundaries

Apply these rules whenever adding source literature to the CCR profile:

- For the default lung-focused corpus, include original analyzable lung-cancer research; a basket or pan-tumor study needs an explicitly reported lung cohort or lung-specific analysis to count as lung evidence. Separately allow user-designated original cross-tumor studies as article-level methods/language references, with actual disease and source role recorded. Regulatory approval analyses retain their regulatory role rather than being relabeled primary trials. These exceptions do not validate lung efficacy or establish a new learned tumor profile. Background-only and excluded genres remain outside original-study language learning.
- Add a historical paper outside the current 2021–2026 base only as an explicit, relevant user-priority qualitative exception. Mark the scope exception in the bibliography and provenance, and do not merge it into legacy standardized-section or phrase-bank statistics without rerunning those complete pipelines.
- Exclude commentaries and editorials. Exclude author replies, replies to letters or reviewers, rebuttals, and response-only correspondence. Do not add excluded genres to the bibliography, corpus counts, section statistics, or phrase bank.
- Preserve the eight legacy `CCR Translations` commentary rows only for traceability and honor their `excluded_commentary_legacy_index_only` status; never use them in future language-learning or quantitative-corpus updates.
- Do not mistake scientific phrases such as `response to treatment` or `predictors of response` for reply-type correspondence; verify the journal article category, title, and full text.
- Verify the main-article PDF, title, PMID, DOI, article type, uniqueness, and review status before changing corpus records or counts.
- Curate each reusable language item with a manuscript section, rhetorical function, evidence domain, expression-unit type, evidence tier, source set, source article identifiers, provenance granularity, source asset, and source line. Assign one primary section and optional secondary sections; use `cross-section-terminology` only for genuinely reusable technical terms.
- Preserve conventional terms and short collocations, but abstract source wording into synthetic phrase, sentence, or paragraph frames. Never store a source-specific sentence as a reusable model merely because it is well written.
- After changing any contributing full-text language asset or the central Abstract/Title bank, run `powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/build_ccr_section_language_catalog.ps1 -SkillPath <skill-folder>`. Accept the update only if every language-bearing subsection is mapped, required fields are nonempty, every PMID is valid, and the completed PMID set read from the authoritative ledger is represented exactly.

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
