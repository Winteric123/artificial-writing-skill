# Artificial Writing Skill

An evidence-calibrated, section-aware Codex skill for biomedical translation, writing, reporting, synthesis, and presentation.

The skill resolves the operation, communication scenario, journal, disease or tumor type, audience, and evidence domain independently. The current release has one corpus-backed journal selection (Clinical Cancer Research, CCR), one corpus-backed tumor selection (lung cancer), and article-level STK11-priority sets from JTO, Cancer Discovery and Nature. These are registered options rather than permanent properties of every task; the smaller sets do not establish journal-wide style profiles.

## What it does

- translates Chinese biomedical text into publication-ready English and English biomedical text into accurate Chinese;
- polishes, rewrites, drafts, and audits manuscripts without silently changing scientific meaning;
- prepares scientific or technical reports, standalone results statements, abstracts, slide text, speaker notes, posters, briefings, response letters, and literature syntheses;
- supports oncology communication involving multi-omics, bioinformatics, preclinical experiments, statistics, immunotherapy, targeted therapy, and drug response or resistance;
- retrieves vocabulary, collocations, sentence frames, and paragraph architectures by Title, Abstract component, Introduction, Methods, Results, Discussion, Conclusion, or Translational Relevance;
- provides a 9,499-entry cross-journal retrieval view across twelve registered journals, with isolated source catalogs, including 7,902 CCR entries covering 263 completed CCR main-text reads, with article-level provenance and source alerts;
- prioritizes thirteen framework papers—six CCR, four JTO, two Cancer Discovery and one Nature—for STK11-focused lung-cancer work without presenting them as a validated STK11 molecular profile;
- connects those thirteen core highlights with six separately labelled topic-support papers, using an analysis guide and article-level reasoning map without promoting support papers to core highlights;
- tracks main-text completion separately from supplementary-material coverage and documented six-gate source-recheck acceptance;
- calibrates causal, predictive, subgroup, validation, superiority, and clinical-utility claims to the underlying evidence;
- checks numbers, terminology, tense, abbreviations, provenance, and unsupported assertions.

Counts are a 2026-09-29 generated snapshot. The [generated inventory](skills/artificial-writing-skill/references/library-index.md) and [summary](skills/artificial-writing-skill/references/library-summary.json) distinguish all-journal year totals from journal-by-year subsets. Topic or intake-batch counts require an additional explicit filter. Of the 9,499 language entries, 9,490 are retrieval-eligible and nine are quarantined; eligibility is not scientific acceptance.

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

The concise [entrypoint](skills/artificial-writing-skill/SKILL.md) routes tasks to the [communication workflow](skills/artificial-writing-skill/references/communication-workflow.md) or [literature intake workflow](skills/artificial-writing-skill/references/literature-intake-workflow.md), loading detailed references only when relevant. Journal, tumor and STK11 selections are optional, not fixed requirements for every task.

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

## Inventory scope and retrieval

The 2026-09-29 formal-journal inventory has 328 registered records: 310 included and 18 excluded or background-only. Main-text reading is marked complete for all 310 included records; no eligible indexed record remains incomplete. The included set comprises 263 CCR, 32 JTO and 15 articles across ten other journals. Preprints and candidate references have separate registers and do not enter these denominators. These are supplied-version main-reading states, not proof of exhaustive journal coverage, complete supplementary-material review or independent acceptance.

| Scope | Included | Main-text complete | Included, incomplete |
|---|---:|---:|---:|
| 2025, all registered formal journals, no topic filter | 53 | 53 | 0 |
| 2025, CCR only, no topic filter | 48 | 48 | 0 |
| All indexed years, CCR only, no topic filter | 263 | 263 | 0 |

The five-paper difference between the two 2025 rows consists of four JTO articles and one Cell Research article marked main-text complete. Neither row is a genomics-only count or evidence that the entire 2025 journal literature has been acquired. In the summary JSON, `years` aggregates journals; `journal_years` preserves journal/year intersections.

Run from `skills/artificial-writing-skill` with Python 3.10 or later:

~~~powershell
python scripts/search_language.py --journal ccr --year 2025 --section results --query "co-mutation" --limit 5
python scripts/search_language.py --pmid 39804166 --section discussion --single-paper --limit 5
python scripts/search_language.py --section "Materials and Methods" --query "co-mutation" --limit 5
python scripts/check_skill_health.py
python scripts/validate_reading_quality.py
python -m unittest discover -s tests -v
~~~

Retrieval preserves stable IDs, section/function/domain tags, usage cards, source warnings and reading/review states. Follow [retrieval-and-maintenance.md](skills/artificial-writing-skill/references/retrieval-and-maintenance.md) for rebuilds and scope rules. The package is stored without Git newline conversion because dependency manifests verify exact file hashes. Preserve these bytes when deploying, or rebuild the indexes after intentional source edits. The regression suite and skill-format validator must pass for each release; mechanical checks do not certify scientific acceptance.

The health check is read-only: it verifies reading-register consistency, retrieval dependency hashes, inventory summaries, project membership and relative documentation links. Registered Chinese and common English section aliases are normalized without broadening other filters. The [25 behavioral fixtures](skills/artificial-writing-skill/references/writing-evaluation-cases.json) require actual responses and semantic assessment; fixture coverage, same-agent assessment and independent evaluation remain distinct.

For STK11 work, use the [analysis guide](skills/artificial-writing-skill/references/stk11-analysis-framework.md), [article logic map](skills/artificial-writing-skill/references/stk11-study-logic-map.md) and [project membership map](skills/artificial-writing-skill/references/stk11-writing-reference-map.json). Sequence co-mutation, copy-number/neighboring-locus context, clinical association and functional mechanism retain separate inference limits. `--highlight` remains core-only; topic-support papers are retrievable by PMID.

## CCR corpus provenance

- Article-level bibliography: 281 registered CCR records, of which 263 are included and 18 are excluded or retained as background-only. Indexing and coverage checks do not establish journal-wide completeness. The 2020 SMARCA4 paper is an explicit user-priority historical qualitative exception to the 2021–2026 base.
- Language-focused deep reading: all 263 included CCR articles are marked main-text complete; no eligible indexed CCR record remains incomplete. Main-article completion does not imply review of unsupplied supplementary files or a passed source recheck.
- Indexed 2026 coverage: 75/75 included CCR main articles are complete, including EVOKE-02 (PMID 41961582) from the supplied publisher-manuscript version. This is the local indexed subset, not proof of exhaustive coverage of every 2026 CCR publication.
- Structured section-language catalog: 7,902 entries covering the 263 completed CCR records, including vocabulary, collocations, phrase and sentence frames, sentence models, paragraph architectures, and paragraph models.
- Acceptance status: six CCR core highlights are marked source-recheck-passed, within a cross-journal set of thirteen. These are documented same-agent source rechecks, not independent reviews or exhaustive certification of every expression. Consult the [recheck summary](skills/artificial-writing-skill/references/source-rechecks/2026-09-28-summary.md) and each journal's quality register for actual gates and boundaries.
- Remaining-queue completion: the indexed 2021–2022 queue resolved 49 original-research reads plus three background-only reviews; the indexed 2023 queue resolved 34 research, regulatory, or methods reads plus two background sources. The dated completion maps preserve paper-level scope and caveats.
- STK11 priorities: thirteen framework papers remain highlighted across CCR, JTO, Cancer Discovery, and Nature. They are contextual writing frameworks, not a validated STK11 molecular profile.
- Legacy standardized section corpus: 1,095,664 words and 46,895 sentences from the original 189-article base.
- Legacy reusable phrase-example bank: 9,411 rows from 181 distinct articles.
- September 2026 research-only supplement: 15 articles and 371 pages, screened for corpus inclusion and qualitative profile calibration but not thereby deeply read.
- Eight historical CCR Translations commentaries remain traceability-only and are excluded from future language-learning and quantitative-corpus updates.

The complete article index is [ccr-corpus-bibliography.csv](skills/artificial-writing-skill/references/ccr-corpus-bibliography.csv). CCR category definitions and counts are in [ccr-category-index.md](skills/artificial-writing-skill/references/ccr-category-index.md). Deep-reading completion is governed only by [ccr-deep-reading-ledger.md](skills/artificial-writing-skill/references/ccr-deep-reading-ledger.md). Article-linked expression retrieval uses [ccr-section-language-catalog.csv](skills/artificial-writing-skill/references/ccr-section-language-catalog.csv); PMID lists in that catalog identify a single-paper, subsection, batch, or cross-corpus synthesis scope and are not verbatim-quotation claims.

Per-article acceptance and supplement status are recorded in [ccr-reading-quality-register.csv](skills/artificial-writing-skill/references/ccr-reading-quality-register.csv) and [jto-reading-quality-register.csv](skills/artificial-writing-skill/references/jto-reading-quality-register.csv). The [quality-register validator](skills/artificial-writing-skill/scripts/validate_reading_quality.py) checks identities, status consistency, paths, and upgrade guards; it does not certify scientific correctness.

## JTO STK11 priority provenance

The local registered JTO corpus now has 32 included articles marked main-text complete. Its [bibliography](skills/artificial-writing-skill/references/jto-corpus-bibliography.csv), [reading ledger](skills/artificial-writing-skill/references/jto-deep-reading-ledger.md) and [maintenance queue](skills/artificial-writing-skill/references/jto-maintenance-queue.md) distinguish completed records from screened candidates. The following four-paper provenance describes the original core highlights, not the full JTO inventory.

The latest two-paper intake adds 80 section-indexed language units from [EGFR DNA/RNA allele fractions](skills/artificial-writing-skill/references/jto-2026-42674257-language.md) and [lorlatinib biomarker analyses](skills/artificial-writing-skill/references/jto-2026-42749050-language.md). Both supplied main texts and main figures/tables are read. The EGFR supplement was not supplied; the lorlatinib embedded scientific tables/figures were read, but administrative TableS1 was only inventoried. Both remain initial reads with acceptance gates pending, and neither is automatically added to the thirteen core highlights.

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
|   |-- build_library_index.py
|   |-- build_language_index.py
|   |-- search_language.py
|   |-- check_skill_health.py
|   \-- validate_reading_quality.py
|-- tests/
|-- assets/stk11-project-workspace.md
\-- references/
    |-- profile-registry.md
    |-- communication-scenarios.md
    |-- communication-workflow.md
    |-- literature-intake-workflow.md
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
    |-- ccr-2025-2026-09-19-intake-language.md
    |-- ccr-2025-genomics-2026-09-20-language.md
    |-- ccr-2025-genomics-2026-09-20-manifest.csv
    |-- cancer-discovery-2026-09-19-stk11-language.md
    |-- nature-2026-09-19-stk11-language.md
    |-- library-index.csv
    |-- library-index.md
    |-- library-summary.json
    |-- language-retrieval-index.json
    |-- language-index-manifest.json
    |-- language-controls.json
    |-- retrieval-and-maintenance.md
    |-- deep-reading-acceptance.md
    |-- ccr-reading-quality-register.csv
    |-- jto-reading-quality-register.csv
    |-- jto-2026-09-14-stk11-priority-language.md
    |-- jto-stk11-priority-bibliography.csv
    |-- jto-stk11-deep-reading-ledger.md
    |-- stk11-priority-references.md
    |-- stk11-analysis-framework.md
    |-- stk11-study-logic-map.md
    |-- stk11-writing-reference-map.json
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
