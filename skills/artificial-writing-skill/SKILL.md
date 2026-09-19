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

CCR is currently the only corpus-backed journal selection, and lung cancer is currently the only corpus-backed tumor selection. Treat both as replaceable selections rather than permanent properties of the skill. The current CCR corpus is lung-cancer-focused; do not present it as a general all-cancer CCR corpus. JTO has a registered four-paper, source-grounded STK11-priority set but no corpus-backed journal profile; use those papers only within their documented article-level scope. For another journal or tumor type, apply core rules and source terminology without claiming a learned profile unless it has been registered and validated.

Keep journal, disease, scenario, and modality corpora, phrase signals, and quantitative summaries separate. Combine selections functionally, but never pool their corpus statistics or imply cross-domain coverage without explicit evidence. Treat current author instructions as external requirements rather than learned style. Verify current official requirements when exact submission compliance is requested and source access is authorized.

## Follow the two-track workflow

Use the literature-intake track when adding or reclassifying source papers. Use the communication track when translating, writing, reporting, or presenting. When a request requires both, complete literature intake and validation before using the new material in communication.

### Track A: literature intake and profile maintenance

1. **Verify source identity:** confirm the title, journal, year, PMID, DOI, article type, source file, uniqueness, and current publication status when relevant.
2. **Route by journal first:** assign the paper to its actual journal before applying topic labels. Folder names, download locations, keywords, and the user's project name do not determine journal identity.
3. **Keep journal assets separate:** store bibliography rows, deep-reading status, language assets, provenance, and counts under the journal-specific prefix. A cross-journal priority register such as the STK11 highlight list is a retrieval index only and never a pooled corpus.
4. **Apply the genre gate:** exclude commentaries, editorials, author replies, rebuttals, reviewer-response documents, and response-only correspondence from reusable literature-learning assets and corpus counts. These genres can still be translated, drafted, or audited when requested.
5. **Deep-read the supplied evidence:** follow [deep-reading-acceptance.md](references/deep-reading-acceptance.md) for complete main-text and main-figure/table coverage, scientific understanding, numerical checks, section-language curation, traceability, and safe transfer. Record supplementary files separately; time spent, PDF parsing, and expression counts do not establish deep reading.
6. **Classify within the journal:** add study design, disease or tumor, molecular topic, clinical/translational domain, omics modality, statistical method, experimental system, and treatment context as secondary classifications.
7. **Curate section-indexed language:** organize vocabulary, collocations, synthetic sentence frames, paragraph architectures, and figure/table narratives by Abstract component, Introduction, Methods, Results, Discussion, Conclusion, and other applicable genres. Do not store source-specific sentences as reusable templates.
8. **Register status and priority:** update the journal bibliography, authoritative main-text reading ledger, and separate reading-quality register. Preserve reading history; promote review_status to passed only after a documented source recheck passes all six gates. Add a cross-journal highlight only when the user designates the paper as a framework priority; a highlight never establishes review acceptance.
9. **Validate the update:** check identifiers, denominators, numerical transcription, duplicate records, journal isolation, relative links, counts, file hashes, and skill validity before deployment. Run scripts/validate_reading_quality.py for register consistency; report its mechanical checks separately from scientific acceptance or independent review.

For each article, retain the publication year, full title, actual journal, PMID, and DOI in its journal-specific bibliography. Keep publication year separate from download and reading dates; when online and issue years differ, record that distinction. A shortened PDF filename must remain traceable to the full bibliographic record. Use journal/year folders and an author-title-PMID filename when archiving new PDFs, and preserve original-to-archive paths and file hashes in the local intake manifest.

When reporting completion, distinguish the supplied batch from the entire journal corpus. Check the journal ledger and quality register; report indexed, screened, main-text-complete, and source-recheck-passed states without conflating them. Separate newly completed articles, previously completed duplicates, and pending articles, and state main-text, main-figure/table, supplement, and review scope. Historical completed entries are not automatically rechecked or independently verified. A completed batch does not change the status of other indexed articles. Keep STK11 highlight priority independent of journal classification and reading/review status.

### Track B: biomedical communication

1. Resolve the seven independent selections: operation, scenario, journal, disease, section or genre, audience, and evidence domain.
2. Load only the references authorized by those selections, with the user's source text, data, and explicit constraints taking precedence over learned language.
3. Build an evidence ledger that preserves study design, analysis sets, comparators, endpoints, denominators, estimates, uncertainty, multiplicity, and limitations.
4. Retrieve language by section, rhetorical function, evidence domain, expression unit, and evidence tier.
5. Translate, revise, draft, audit, synthesize, report, or present without adding unsupported facts or analyses.
6. Run the mandatory number, terminology, tense, and claim-strength audits.
7. Deliver the requested format and report only unresolved scientific queries or material changes to evidence interpretation.

## Load only the references needed

- Read [deep-reading-acceptance.md](references/deep-reading-acceptance.md) when performing literature intake, judging reading depth, or reviewing completion claims. Use [ccr-reading-quality-register.csv](references/ccr-reading-quality-register.csv) or [jto-reading-quality-register.csv](references/jto-reading-quality-register.csv) for per-article acceptance status; load only relevant rows. A pending review does not erase prior reading, and a script pass does not prove scientific understanding.
- Read [profile-registry.md](references/profile-registry.md) when selecting, explaining, combining, or extending journal, disease, scenario, audience, or modality profiles.
- Read [core-translation-integrity.md](references/core-translation-integrity.md) for translation, polishing, rewriting, or bilingual alignment under every journal profile.
- Read [core-evidence-language.md](references/core-evidence-language.md) for Results, Discussion, Conclusions, abstract conclusions, biomarker claims, subgroup analyses, diagnostic or AI models, and translational claims under every journal profile.
- Read [communication-scenarios.md](references/communication-scenarios.md) for scientific reports, standalone results statements, slide or oral presentations, posters, technical briefings, executive summaries, or literature syntheses. Use its scenario architecture independently of the journal and tumor selections.
- Read [ccr-section-patterns.md](references/ccr-section-patterns.md) when drafting, translating, polishing, or restructuring a manuscript section with the selected CCR profile. Normalize the target to its functional section before selecting language.
- Read [ccr-non-imrad-genres.md](references/ccr-non-imrad-genres.md) for CCR-informed commentaries, narrative reviews, regulatory summaries, response letters, figure legends, or other non-IMRaD writing.
- Read [ccr-phrase-patterns.md](references/ccr-phrase-patterns.md) only after selecting the CCR profile and identifying the manuscript section, rhetorical function, evidence domain, expression unit, and evidence tier. Treat it as the runtime authority for section-indexed vocabulary, collocations, phrase frames, sentence frames, and paragraph architectures. Never copy source sentences or treat phrases as quotas.
- Search [ccr-section-language-catalog.csv](references/ccr-section-language-catalog.csv) when the task benefits from an article-traceable expression learned from the 83-paper deep-read set. Filter first by `primary_section` or `secondary_sections`, then by `function`, `domain`, `unit_type`, and `evidence_tier`; load only the matching rows rather than the complete catalog. Use `source_article_ids` together with `provenance_granularity`: `single-paper-synthesis` is the narrowest assignment, whereas `subsection-synthesis` and `batch-synthesis` identify a contributing source scope and must not be presented as proof that every listed paper contains the expression.
- Read [stk11-priority-references.md](references/stk11-priority-references.md) whenever the task centers on STK11-focused lung-cancer writing, translation, reporting, synthesis, or presentation. The ten highlighted papers—six CCR ATM/SMARCA4/KRAS/AmpRatio studies and four JTO ERBB2/KRAS/STK11-copy-deletion/MTAP studies—are user-designated core writing-framework references. Prioritize them when planning the manuscript outline, section logic, Results sequence, and figure/table narrative, as well as when retrieving language. Adapt their structural patterns to the user's available evidence; their priority does not establish an STK11 mechanism or treatment effect. PMID 42409117 is a structural analogue without an STK11/LKB1 analysis in the supplied main text.
- Read [ccr-2026-09-14-atm-smarca4-stk11-priority-language.md](references/ccr-2026-09-14-atm-smarca4-stk11-priority-language.md) for the three priority papers' article-specific section maps, vocabulary, collocations, synthetic sentence and paragraph models, numerical checks, source inconsistencies, and STK11-specific reuse boundaries.
- Read [ccr-2026-09-19-supplement-language.md](references/ccr-2026-09-19-supplement-language.md) for the 14-paper addition covering KRAS G12V/Q61 clinicogenomics, STK11/KEAP1 co-mutation context, MET biomarkers and targeted therapy, ctDNA and machine learning, spatial and single-cell immune profiling, cellular therapy, phase I/II efficacy and safety, RET retreatment, mitotic cell-death experiments, and ADC pharmacology. PMID 41417462 and PMID 42268349 are STK11 framework highlights; use their allele-conditioned structures without converting retrospective treatment associations into predictive claims.
- Read [ccr-2026-09-19-batch2-language.md](references/ccr-2026-09-19-batch2-language.md) for the eight-paper second addition: AmpRatio copy-number genomics and STK11 co-alteration context, clonal-hematopoiesis classification and fragmentomics, longitudinal ultrasensitive ctDNA, rare-cancer brain metastases, phase I immunotherapy pharmacology, single-nucleus RNA and patient-level pseudobulk analysis, and CD24 macrophage experiments. PMID 41870274 is an STK11 framework highlight, not STK11-specific treatment validation. Coverage includes the supplied main articles and their figures/tables, not separate supplements or a new global-proteomics corpus.
- Read [ccr-2026-09-19-pending15-language.md](references/ccr-2026-09-19-pending15-language.md) for the 15-paper completion of the existing 2026 CCR queue: methylation diagnostics, PFAS exposure epidemiology, SMARCA4 allele-specific genomics, EGFR/RET resistance, targeted and ADC basket trials, patient-reported outcomes, response-adaptive radiotherapy, RRAS functional experiments, PEF single-cell/AbSeq immune profiling, and AI pathology with an ICI cohort. Keep main-text completion separate from pending acceptance rechecks and unsupplied supplements. Use its article-specific source-conflict restrictions before reusing numerical or mechanistic claims; these papers do not create additional STK11 highlights.
- Read [jto-2026-09-14-stk11-priority-language.md](references/jto-2026-09-14-stk11-priority-language.md) for the four JTO priority papers' article-specific classifications, section maps, vocabulary, collocations, synthetic sentence and paragraph models, figure/table narratives, numerical checks, source inconsistencies, and STK11-specific reuse boundaries. Treat PMID 39864548 as a direct copy-deletion/expression/treatment-outcome framework; PMID 41619904 as a direct but partly STK11/CDKN2A-combined clinical-outcome framework; PMID 41932614 as an indirect genomic-context framework; and PMID 42409117 as an indirect structural analogue with no STK11/LKB1 analysis in the supplied main text.
- Read [ccr-2026-09-12-supplement-language.md](references/ccr-2026-09-12-supplement-language.md) for the four-paper addition covering NRF2/STK11/KEAP1 models and signatures, LAURA post-progression endpoints, ceralasertib/durvalumab and Bayesian reporting, and YL201 targeted plasma proteomics. Use its article-specific section maps, PDF-page locators, denominator checks, and quarantined source inconsistencies. Main-PDF completion does not imply independent review of unsupplied supplements.
- Read [ccr-2025-immunotherapy-fulltext-language.md](references/ccr-2025-immunotherapy-fulltext-language.md) for the 17-paper full-text set covering checkpoint-inhibitor resistance and discontinuation, CAR T and CAR NK cells, engineered TCR therapy, gene therapy, bispecific ADCs, PD-L1 PET, ctDNA monitoring, transcriptomics, limited direct proteomics and immunopeptidomics, bioinformatics, exposure-response modeling, efficacy, and safety. Preserve its paper-specific denominator and inference checks.
- Read [ccr-2026-translational-mechanisms-fulltext-language.md](references/ccr-2026-translational-mechanisms-fulltext-language.md) when the task needs full-manuscript CCR language for tumor biology, bulk transcriptomics, TCR profiling, bioinformatics, basic experiments, statistical results, immunotherapy, targeted therapy, drug activity, resistance, or translational interpretation.
- Read [ccr-2026-immunotherapy-fulltext-language.md](references/ccr-2026-immunotherapy-fulltext-language.md) for the additional 17-paper full-text set covering clinical immunotherapy, radiation, single-cell and spatial transcriptomics, BCR/TCR repertoires, ctDNA and MRD, metagenomics, metabolomics, machine learning, digital pathology, CAR T-cell experiments, pharmacokinetics, safety, and regulatory language. Keep its FDA Approval Summary patterns separate from original-research prose; that 2026 subset itself contains no primary mass-spectrometry proteomics workflow.
- Read [ccr-corpus-provenance.md](references/ccr-corpus-provenance.md) when explaining the CCR profile's evidence base, coverage, quantitative signals, or limitations.
- Read [ccr-category-index.md](references/ccr-category-index.md) whenever the user asks how corpus articles are classified by CCR, how many articles fall in each CCR category, or which category-level genre exclusions apply. Treat `ccr_official_category` in the bibliography as the article-level authority and do not infer a detailed section for an Online First record labeled only `Research Article`.
- Read [ccr-deep-reading-ledger.md](references/ccr-deep-reading-ledger.md) whenever the user asks which articles have been deeply read, fully read for language, or remain pending. Treat this ledger as the sole authority for deep-reading completion; never infer completion from corpus processing, PDF parsing, source-coverage, section-corpus, or phrase-bank flags.
- Read [jto-stk11-deep-reading-ledger.md](references/jto-stk11-deep-reading-ledger.md) when the user asks whether a highlighted JTO article has been deeply read. Its scope is only the registered four-paper JTO STK11-priority set; it is not a journal-wide JTO inventory.
- Search [ccr-corpus-bibliography.csv](references/ccr-corpus-bibliography.csv) only when the user asks about a paper title, PMID, DOI, publication year, corpus membership, CCR official category, category-verification source, genre status, article type, corpus-processing history, or the complete source list. Filter to relevant rows before loading content; load or format all 231 rows only when explicitly requested. A blank official category with `pending_official_verification` means unverified, not a new CCR category; manuscript-declared labels and content tags are not substitutes for verified publisher classification.
- Search [jto-stk11-priority-bibliography.csv](references/jto-stk11-priority-bibliography.csv) for the four highlighted JTO papers' title, PMID, DOI, publication details, article-level classifications, STK11 role, source PDF, and supplement status. Never merge these rows into CCR counts or imply that they represent the complete JTO literature.

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

- Include a full research article only when it reports original analyzable data relevant to lung cancer. For a basket or pan-tumor study, require an explicitly reported lung-cancer cohort or lung-specific analysis.
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
