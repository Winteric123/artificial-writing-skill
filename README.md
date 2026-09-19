# Artificial Writing Skill

An evidence-calibrated, section-aware Codex skill for biomedical translation, writing, reporting, synthesis, and presentation.

The skill resolves the operation, communication scenario, journal, disease or tumor type, audience, and evidence domain independently. The current release has one corpus-backed journal selection (Clinical Cancer Research, CCR), one corpus-backed tumor selection (lung cancer), and a narrow source-grounded JTO selection supported by four STK11-priority articles. These are registered options rather than permanent properties of every task.

## What it does

- translates Chinese biomedical text into publication-ready English and English biomedical text into accurate Chinese;
- polishes, rewrites, drafts, and audits manuscripts without silently changing scientific meaning;
- prepares scientific or technical reports, standalone results statements, abstracts, slide text, speaker notes, posters, briefings, response letters, and literature syntheses;
- supports oncology communication involving multi-omics, bioinformatics, preclinical experiments, statistics, immunotherapy, targeted therapy, and drug response or resistance;
- retrieves vocabulary, collocations, sentence frames, and paragraph architectures by Title, Abstract component, Introduction, Methods, Results, Discussion, Conclusion, or Translational Relevance;
- provides a 2,770-entry article-linked language catalog covering all 83 completed CCR main-text deep reads, with PMID scope and provenance granularity for every entry;
- prioritizes ten deeply read framework papers—six CCR ATM/SMARCA4/KRAS/AmpRatio studies and four JTO ERBB2/KRAS/STK11-copy-deletion/MTAP studies—for future STK11-focused lung-cancer work without presenting them as a dedicated STK11 profile;
- tracks main-text completion separately from supplementary-material coverage and documented six-gate source-recheck acceptance;
- calibrates causal, predictive, subgroup, validation, superiority, and clinical-utility claims to the underlying evidence;
- checks numbers, terminology, tense, abbreviations, provenance, and unsupported assertions.

It does not provide clinical decision support and must not invent data, methods, citations, registrations, ethics approvals, or novelty claims.

## Selection model

The skill selects seven axes for each task:

1. operation;
2. communication scenario;
3. journal profile;
4. disease or tumor profile;
5. manuscript section or genre unit;
6. audience and intended use;
7. evidence domain.

Explicit user instructions take priority, followed by supplied source context, registered profile scope, and conservative core fallback. Non-journal deliverables can use journal=none. Unspecified or mixed tumors can use disease=general-oncology.

Supported options and extension requirements are recorded in [profile-registry.md](skills/artificial-writing-skill/references/profile-registry.md). Report, results-statement, presentation, and synthesis architectures are recorded in [communication-scenarios.md](skills/artificial-writing-skill/references/communication-scenarios.md).

## Workflow

The skill uses two linked tracks:

1. **Literature intake and profile maintenance:** verify bibliographic identity and article type; route the paper by its actual journal before assigning topic labels; keep each journal's bibliography, deep-reading ledger, language assets, provenance, and counts separate; exclude commentaries, editorials, replies, rebuttals, and response-only correspondence from reusable learning assets; deep-read the supplied main PDF; classify it within the journal; curate section-indexed language; register completion or user-designated priority; and validate identifiers, numbers, links, counts, hashes, and skill structure.
2. **Biomedical communication:** resolve the operation, scenario, journal, disease, section or genre, audience, and evidence domain; load only matching references; build an evidence ledger; retrieve section- and evidence-calibrated language; produce the requested manuscript, translation, report, results statement, synthesis, or presentation; and audit numbers, terminology, tense, and claim strength before delivery.

Folder names and download locations never determine journal classification. Cross-journal highlight files are retrieval indexes only and do not merge journal corpora or statistics. When one request both adds literature and uses it for writing, the intake track is completed and validated before the new material is used.

Reading states distinguish indexed, screened, main-text deep-read complete, and source-recheck passed. The final state requires a documented return to the source and acceptance across coverage, scientific interpretation, central numerical results, section-language curation, traceability, and safe transfer. Main-text completion, expression counts, or a successful validation script do not establish acceptance or independent review. See [deep-reading-acceptance.md](skills/artificial-writing-skill/references/deep-reading-acceptance.md) and the journal-specific reading-quality registers.

## Install for Codex

Use $CODEX_HOME/skills when CODEX_HOME is set; otherwise use $HOME/.codex/skills.

PowerShell example:

~~~powershell
git clone https://github.com/Winteric123/artificial-writing-skill.git
$skillsRoot = if ($env:CODEX_HOME) {
    Join-Path $env:CODEX_HOME "skills"
} else {
    Join-Path $HOME ".codex\skills"
}
New-Item -ItemType Directory -Force $skillsRoot | Out-Null
Copy-Item -Recurse -Force ".\artificial-writing-skill\skills\artificial-writing-skill" (Join-Path $skillsRoot "artificial-writing-skill")
~~~

Start a new Codex conversation after installation if the skill does not appear immediately.

## Share with Wisp Science

Configure WISP_SKILLS_PATH to include the canonical Codex skills root. Wisp then reads the same skill folder instead of maintaining a second copy. Reload skills from **Settings -> Skills -> Reload Skills** and start a new conversation when the updated instructions must be guaranteed.

## Usage examples

Journal manuscript:

~~~text
Use $artificial-writing-skill.
Operation: rewrite and audit.
Scenario: journal manuscript.
Journal: Clinical Cancer Research.
Disease: lung cancer.
Revise this Discussion without overstating subgroup evidence.
~~~

Scientific report:

~~~text
Use $artificial-writing-skill to prepare a technical report from these experimental and statistical results.
Audience: multidisciplinary research team.
~~~

Standalone results statement:

~~~text
Use $artificial-writing-skill to convert this table into concise Results statements with denominators, effect sizes, confidence intervals, and inference boundaries.
~~~

Presentation:

~~~text
Use $artificial-writing-skill to prepare evidence-based slide headlines and speaker notes for these multi-omics findings.
~~~

For an unsupported journal or tumor type, provide the relevant instructions or source material. The skill applies core integrity and evidence rules but does not claim a learned profile until that selection is registered and validated.

## CCR corpus provenance

- Article-level bibliography: 231 records with recorded main-text coverage checks, totaling 3,957 physical PDF pages. Indexing and coverage checks do not establish deep reading. The 2020 SMARCA4 paper is an explicit user-priority historical qualitative exception to the 2021–2026 base.
- Language-focused deep reading: 83 articles completed across eight full-text batches; 148 records remain incomplete, including 140 eligible research records and eight excluded legacy commentaries that must not enter a research-reading queue. Main-article completion does not imply review of unsupplied supplementary files or a passed source recheck.
- Indexed 2026 coverage: 62/62 main articles completed. This is the local indexed subset, not exhaustive coverage of every 2026 CCR publication. EVOKE-02 (PMID 41961582) remains unsupplied, unread, and outside the bibliography denominator.
- Structured section-language catalog: 2,770 entries covering all 83 completed CCR PMIDs, including vocabulary, collocations, phrase and sentence frames, sentence models, paragraph architectures, and paragraph models.
- Acceptance status: no article is marked source-recheck-passed. The earlier 68 CCR completion records retain not_reaudited gates; the latest 15 have pending recheck gates. JTO review status is recorded separately.
- September 12 addition: three 2026 Online First papers and one formally published in 2021; 177 new single-paper, section-indexed expressions with main-PDF locators. Three new official CCR classifications remain unverified; topic tags and the LAURA manuscript-declared category are recorded separately from official classification.
- September 14 priority addition: one 2020 SMARCA4 and two 2023 ATM studies; 228 new single-paper, section-indexed expressions with main-PDF locators and explicit STK11 reuse boundaries. All three are marked as priority contextual references, not a validated STK11 molecular profile.
- September 19 first addition: 14 main articles and 511 language entries, including user-highlighted KRAS G12V/Q61 frameworks; clinical, omics, experimental, statistical, and therapeutic expressions remain article-traceable.
- September 19 second addition: eight main articles and 330 language entries, including the user-highlighted AmpRatio framework, fragmentomics, longitudinal ctDNA, phase I immunotherapy, single-nucleus RNA, and macrophage experiments.
- September 19 existing-index completion: 15 previously indexed 2026 main articles and 512 language entries (249 vocabulary/collocations, 233 sentence frames, 16 paragraph models, and 14 paragraph architectures). All main figures/tables were included; separate supplements were not supplied. This batch adds no bibliography records or STK11 highlights.
- Legacy standardized section corpus: 1,095,664 words and 46,895 sentences from the original 189-article base.
- Legacy reusable phrase-example bank: 9,411 rows from 181 distinct articles.
- September 2026 research-only supplement: 15 articles and 371 pages, screened for corpus inclusion and qualitative profile calibration but not thereby deeply read.
- Eight historical CCR Translations commentaries remain traceability-only and are excluded from future language-learning and quantitative-corpus updates.

The complete article index is [ccr-corpus-bibliography.csv](skills/artificial-writing-skill/references/ccr-corpus-bibliography.csv). CCR category definitions and counts are in [ccr-category-index.md](skills/artificial-writing-skill/references/ccr-category-index.md). Deep-reading completion is governed only by [ccr-deep-reading-ledger.md](skills/artificial-writing-skill/references/ccr-deep-reading-ledger.md). Article-linked expression retrieval uses [ccr-section-language-catalog.csv](skills/artificial-writing-skill/references/ccr-section-language-catalog.csv); PMID lists in that catalog identify a single-paper, subsection, batch, or cross-corpus synthesis scope and are not verbatim-quotation claims.

Per-article acceptance and supplement status are recorded in [ccr-reading-quality-register.csv](skills/artificial-writing-skill/references/ccr-reading-quality-register.csv) and [jto-reading-quality-register.csv](skills/artificial-writing-skill/references/jto-reading-quality-register.csv). The [quality-register validator](skills/artificial-writing-skill/scripts/validate_reading_quality.py) checks identities, status consistency, paths, and upgrade guards; it does not certify scientific correctness.

## JTO STK11 priority provenance

- Four JTO original-research papers (one 2025 and three 2026) were deeply read from supplied PDFs: PMID 41932614, PMID 41619904, PMID 39864548, and PMID 42409117.
- The 90 reviewed physical pages cover all four complete main articles, main tables, figures, captions, and contributor material. Cited supplementary files were not supplied or independently reviewed.
- PMID 41932614 supplies an ERBB2 domain-stratified clinicogenomic and co-mutation framework in which STK11 is an indirect genomic-context variable.
- PMID 41619904 supplies a direct KRAS/STK11-CDKN2A stage III outcome framework covering cCRT, consolidative durvalumab, PFS/OS, competing risks, distant failure, and brain metastasis.
- PMID 39864548 supplies the most direct JTO STK11 copy-deletion framework, covering mono-/bi-allelic state, 19p co-deletion, STK11 RNA/LKB1 protein expression, chemoimmunotherapy and ICI outcomes, and multiplex immunofluorescence.
- PMID 42409117 supplies an indirect MTAP/CDKN2A/B locus-disambiguation, NGS-IHC concordance, targeted-therapy prognosis, and paired-progression framework; its supplied main text contains no STK11/LKB1 analysis and it is not direct STK11 evidence.
- The JTO set is source-grounded and article-specific, not a corpus-backed JTO journal profile. It is excluded from every CCR bibliography, deep-reading, language-catalog, and phrase-statistics count.

JTO metadata and classifications are in [jto-stk11-priority-bibliography.csv](skills/artificial-writing-skill/references/jto-stk11-priority-bibliography.csv). Completion status is in [jto-stk11-deep-reading-ledger.md](skills/artificial-writing-skill/references/jto-stk11-deep-reading-ledger.md). Section-indexed vocabulary, collocations, synthetic sentence and paragraph frames, numerical checks, figure/table narratives, and source inconsistencies are in [jto-2026-09-14-stk11-priority-language.md](skills/artificial-writing-skill/references/jto-2026-09-14-stk11-priority-language.md).

The repository does not distribute source PDFs, abstracts, complete full-text extracts, or the raw phrase-example bank. Article titles and public bibliographic identifiers are included for traceability. Underlying articles remain subject to their respective copyright and licensing terms.

## Corpus update policy

Future CCR corpus updates include only full research articles with original analyzable data relevant to lung cancer. Basket or pan-tumor studies require an explicitly reported lung-cancer cohort or lung-specific analysis. Commentaries, editorials, author replies, reviewer-response letters, rebuttals, and response-only correspondence are excluded from corpus learning and counts.

These source restrictions do not prevent the skill from drafting, translating, polishing, or auditing those genres when requested.

## Repository layout

~~~text
skills/artificial-writing-skill/
|-- SKILL.md
|-- agents/openai.yaml
|-- scripts/
|   |-- build_ccr_section_language_catalog.ps1
|   \-- validate_reading_quality.py
\-- references/
    |-- profile-registry.md
    |-- communication-scenarios.md
    |-- core-translation-integrity.md
    |-- core-evidence-language.md
    |-- ccr-section-patterns.md
    |-- ccr-non-imrad-genres.md
    |-- ccr-phrase-patterns.md
    |-- ccr-2025-immunotherapy-fulltext-language.md
    |-- ccr-2026-immunotherapy-fulltext-language.md
    |-- ccr-2026-translational-mechanisms-fulltext-language.md
    |-- ccr-2026-09-12-supplement-language.md
    |-- ccr-2026-09-14-atm-smarca4-stk11-priority-language.md
    |-- ccr-2026-09-19-supplement-language.md
    |-- ccr-2026-09-19-batch2-language.md
    |-- ccr-2026-09-19-pending15-language.md
    |-- ccr-2026-09-19-pending15-manifest.csv
    |-- deep-reading-acceptance.md
    |-- ccr-reading-quality-register.csv
    |-- jto-reading-quality-register.csv
    |-- jto-2026-09-14-stk11-priority-language.md
    |-- jto-stk11-priority-bibliography.csv
    |-- jto-stk11-deep-reading-ledger.md
    |-- stk11-priority-references.md
    |-- ccr-section-language-catalog.csv
    |-- ccr-corpus-provenance.md
    |-- ccr-category-index.md
    |-- ccr-deep-reading-ledger.md
    \-- ccr-corpus-bibliography.csv
~~~

## Adding selections

Register a new journal, disease or tumor type, communication scenario, audience, modality, or molecular topic before describing it as supported. Record aliases, scope, support level, source provenance, exclusions, fallback behavior, and validation status. Keep corpus counts and phrase signals separate across profiles.

## Independence and license status

This is an independent, unofficial project. It is not affiliated with, endorsed by, or sponsored by the American Association for Cancer Research or *Clinical Cancer Research*.

No open-source license has been selected for this repository yet. A license can be added later if redistribution and modification rights are to be granted.
