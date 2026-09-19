# Deep-reading acceptance and source recheck

## Purpose and authority

For this writing skill, deep reading means understanding the evidence, curating usable language, retaining source traceability, and transferring expressions without transferring unsupported claims. Elapsed time, PDF pages parsed, raw tokens, number of extracted expressions, and successful script execution are not acceptance criteria. These are operational standards for this skill, not a universal journal standard.

The journal-specific deep-reading ledger remains authoritative for recorded main-text reading completion. The journal-specific quality register is authoritative for the separate source-recheck status. Keep the two synchronized without treating either a historical completion label or a highlight designation as proof of a new review.

- CCR: [reading ledger](ccr-deep-reading-ledger.md) and [quality register](ccr-reading-quality-register.csv).
- JTO priority set: [reading ledger](jto-stk11-deep-reading-ledger.md) and [quality register](jto-reading-quality-register.csv).
- New journals need their own bibliography, ledger, and register; never pool completion rates across journals.

## Reading stage and review status

Store two axes rather than overwriting reading history with a review verdict:

| Field/value | Meaning and evidence required |
|---|---|
| reading_stage=indexed | Identity and membership registered; do not infer screening or reading from processing labels. |
| reading_stage=screened | Relevance/design screening recorded; full main-text reading not yet completed. |
| reading_stage=main_text_deep_read_complete | Complete main text and main figures/tables reviewed, evidence and section-language assets recorded, and the journal ledger updated. |
| review_status=not_reviewed | No documented acceptance recheck under this protocol. |
| review_status=in_progress | Source recheck started; acceptance is not yet established. |
| review_status=needs_correction | A substantive omission, error, or unresolved acceptance issue remains. |
| review_status=passed | All six gates pass with a dated review record, identified reviewer/method, and no unresolved blocking issue. |

Display these as 已入库, 已初筛, 主文精读完成, and 精读复核通过. The fourth display state requires both main-text completion and review_status=passed. Supplement coverage, genre eligibility, and STK11 priority are separate fields, not reading stages. Excluded commentaries remain traceable but are never promoted or queued for language learning.

A repeat check by the same assistant may be recorded as same_agent_source_recheck, not independent review. Use independent_agent_source_recheck only for an actual separate agent pass and human_source_recheck only for a documented human pass. No program can certify scientific understanding merely by validating fields.

## Six acceptance gates

| Register field | Pass requires auditable evidence |
|---|---|
| coverage_check | An applicable-section map covering Abstract components, Introduction, Methods, Results, Discussion, Conclusion/closing synthesis, Translational Relevance, and every main figure/table/caption. Record absent headings, unreadable pages, PDF version, and supplementary scope explicitly. Do not invent a separate Conclusion section. |
| evidence_check | A source-grounded explanation of the question, design, population/model, comparator, analysis sets, central findings, limitations, and strongest defensible claim. Separate samples from patients, association from causality, and prognostic from treatment-predictive evidence. |
| results_check | Return to original text and main figures/tables for every central numerical result, including primary, key negative, safety, and conclusion-driving findings. Retain denominators, units, timing, effect estimates, uncertainty, significance/adjustment, and exploratory status where applicable. Record unavailable statistics rather than inventing them. |
| language_check | Useful vocabulary, collocations, sentence frames, and paragraph logic organized by applicable writing section and rhetorical function, with usage explanation or constraints. Cover only domains actually studied. Distinguish conventional terms from synthetic models; no quota or verbatim paragraph collection. |
| traceability_check | Facts and curated expressions point to article identity and source locations. Review records identify PDF version/hash, section/page/figure or table, language asset heading/line, and catalog version plus entry ID where available. Batch-level provenance is not exact single-paper attribution. |
| transfer_check | Demonstrate how selected expressions can describe supplied evidence or explicitly bracketed placeholders while preserving design, uncertainty, tumor type, and inference limits. Include unsafe reuse boundaries; do not invent STK11 data or treat another tumor's efficacy as STK11 validation. |

Each gate is pass, fail, pending, or not_reaudited. Use not_reaudited only for inherited completed records that have not been checked under this protocol; it is neither a failed read nor a pass. Use pending when the task has not yet established that gate. Document inapplicable subitems inside a gate instead of claiming the whole gate is unnecessary.

No weighted score can compensate for a failed gate. Missing central evidence, an untraceable material claim, or an unresolved reading/transcription error prevents review_status=passed. A faithfully documented source inconsistency may pass only when uncertainty is explicit, the affected claim is withheld or qualified, and the reviewer explains the disposition; do not silently repair the article.

## Source-recheck procedure

1. Open the actual main PDF, not only extracted text or earlier notes. Use visual inspection for tables, figures, layout, and ambiguous extraction. Identify separately supplied supplements before making coverage claims.
2. Reconstruct the research question, design, analysis sets, evidence sequence, and claim boundaries from the source. Check the section/figure/table inventory against the reading asset.
3. Recheck all central result rows and compare Abstract, Results, tables, captions, and conclusions. Document numerator/denominator or source inconsistencies and their disposition.
4. Sample language across every applicable section and the expression-unit types actually present. Include high-risk causal/predictive wording, negation, modality names, statistical language, and article-specific frames. Record actual selections and rationale, not only a sampling percentage. Full sampling of language is not required to claim a bounded review pass.
5. If a sample is wrong or untraceable, correct it and extend the check to related entries, sections, or source mappings. Quarantine unresolved expressions from retrieval. Report the actual review scope; never call a sample review exhaustive or error-free.
6. Complete the six gates, reviewer identity, method, date, and source-recheck record. Only then set passed. Main-text completion does not establish supplement review, independent replication, clinical validation, or independent peer review.

Pending review does not erase an existing reading asset or prohibit all source-grounded use. Reopen the source for material article-specific claims; do not describe an unreviewed record as acceptance-verified. If review exposes incomplete original reading, preserve its historical completion date and record the unresolved coverage problem with needs_correction rather than concealing it.

## Per-article review record

Create a real record only when work occurs; do not generate completed-looking placeholder reports. A register row can link to one Markdown record or the precise review subsection of an existing article asset. Paths are relative to references/. Keep the PDF hash/version in that record without publishing private local paths or long copyrighted excerpts.

Use the following structure, adapting rows to the article:

### Identity and scope

- Journal, full title, issue year and online date if different, PMID, DOI.
- Main PDF version, SHA-256, physical page count; separately identified supplement files and review status.
- Reading asset; catalog version; reviewer identifier, method, date, and exact reviewed scope.

### Coverage and interpretation

| Section / main figure / table | Physical locator | What was checked | Outstanding issue |
|---|---|---|---|

Record the research question, design, population/model, analysis sets, major findings, negative findings, limitations, and claim ceiling. Distinguish direct evidence from inference.

### Central-result recheck

| Claim / endpoint | Analysis set and denominator | Estimate, uncertainty, timing and adjustment | Source locator | Recheck and disposition |
|---|---|---|---|---|

### Language and transfer recheck

| Asset/heading and catalog version/ID | Writing section and function | Unit type and source locator | Usage explanation / safe transfer | Unsafe use / correction |
|---|---|---|---|---|

Record the sampled entries, selection rationale, expanded checks after any failure, and unsampled scope. Use supplied data or explicit placeholders for transfer demonstrations, never invented study findings.

### Verdict

| Gate | Status | Evidence location / justification |
|---|---|---|

Complete all six gates. List unresolved issues and quarantined entries, distinguish source inconsistencies from reading errors, and state main-text versus supplement coverage. A pass is bounded by the documented scope and sampling; it does not mean zero residual error.

## Register contract and migration

One row per journal bibliography PMID, including excluded legacy rows for traceability. Match year and full title to that bibliography. Fields:

- pmid, year, title, eligibility: included or excluded, with the existing genre boundary preserved.
- reading_stage, main_read_completed_on: must agree with the journal ledger. The conservative stage for an uncompleted legacy record is indexed, not an invented screening result.
- review_status and the six gate columns above.
- supplement_status: not_recorded, not_supplied, supplied_unread, partially_reviewed, or reviewed. Record which files were checked; main-text references to supplementary results are not supplement review.
- reading_evidence: semicolon-separated relative ledger/language-asset paths; these locate inherited work but do not prove a new gate pass.
- review_record, reviewer_id, review_method, reviewed_on: required for a passed review. The date must not precede main-read completion. Review methods are same_agent_source_recheck, independent_agent_source_recheck, and human_source_recheck.
- note: migration provenance, remaining issues, or explanatory scope; not a substitute for a source-recheck record.

The 2026-09-19 migration preserves 68 CCR and four JTO main-text completion records. Every inherited completed record starts with review_status=not_reviewed and six not_reaudited gates; other indexed CCR records start with pending gates. No article receives a new pass, reviewer, review date, or synthetic review record during this migration. Preserve known supplement boundaries; unknown historical coverage stays not_recorded.

For future additions, record evidence for the six dimensions during reading; a later documented source recheck is still required before promoting the review status. Update the relevant ledger and quality register together. Add new registers to the validator when a new journal is registered.

Run scripts/validate_reading_quality.py after editing a register, ledger, or review record. It checks identity joins, status consistency, required paths and fields, and upgrade guards. It does not verify scientific accuracy, reviewer independence, the truth of a filled-in gate, or completeness of PDF reading. Report mechanical validation separately from article acceptance.
