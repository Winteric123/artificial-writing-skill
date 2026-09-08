# Artificial Writing Skill

An evidence-calibrated, section-aware Codex skill for biomedical translation, writing, reporting, synthesis, and presentation.

The skill resolves the operation, communication scenario, journal, disease or tumor type, audience, and evidence domain independently. The current release has one corpus-backed journal selection (Clinical Cancer Research, CCR) and one corpus-backed tumor selection (lung cancer). They are registered options rather than permanent properties of every task.

## What it does

- translates Chinese biomedical text into publication-ready English and English biomedical text into accurate Chinese;
- polishes, rewrites, drafts, and audits manuscripts without silently changing scientific meaning;
- prepares scientific or technical reports, standalone results statements, abstracts, slide text, speaker notes, posters, briefings, response letters, and literature syntheses;
- supports oncology communication involving multi-omics, bioinformatics, preclinical experiments, statistics, immunotherapy, targeted therapy, and drug response or resistance;
- retrieves vocabulary, collocations, sentence frames, and paragraph architectures by Title, Abstract component, Introduction, Methods, Results, Discussion, Conclusion, or Translational Relevance;
- provides a 1,012-entry article-linked language catalog covering all 39 completed deep reads, with PMID scope and provenance granularity for every entry;
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

- Article-level bibliography: 204 records with verified source-text coverage, totaling 3,329 PDF pages.
- Language-focused deep reading: 39 articles completed across three full-text batches; the other 165 records must not be described as completed deep reads.
- Structured section-language catalog: 1,012 entries covering all 39 completed PMIDs, including vocabulary, collocations, phrase and sentence frames, sentence models, paragraph architectures, and paragraph models.
- Legacy standardized section corpus: 1,095,664 words and 46,895 sentences from the original 189-article base.
- Legacy reusable phrase-example bank: 9,411 rows from 181 distinct articles.
- September 2026 research-only supplement: 15 articles and 371 pages, screened for corpus inclusion and qualitative profile calibration but not thereby deeply read.
- Eight historical CCR Translations commentaries remain traceability-only and are excluded from future language-learning and quantitative-corpus updates.

The complete article index is [ccr-corpus-bibliography.csv](skills/artificial-writing-skill/references/ccr-corpus-bibliography.csv). CCR category definitions and counts are in [ccr-category-index.md](skills/artificial-writing-skill/references/ccr-category-index.md). Deep-reading completion is governed only by [ccr-deep-reading-ledger.md](skills/artificial-writing-skill/references/ccr-deep-reading-ledger.md). Article-linked expression retrieval uses [ccr-section-language-catalog.csv](skills/artificial-writing-skill/references/ccr-section-language-catalog.csv); PMID lists in that catalog identify a single-paper, subsection, batch, or cross-corpus synthesis scope and are not verbatim-quotation claims.

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
|   \-- build_ccr_section_language_catalog.ps1
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
