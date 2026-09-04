# Artificial Writing Skill

An evidence-calibrated Codex skill for biomedical translation, manuscript writing, polishing, restructuring, and claim auditing.

The current release contains one journal profile: a lung-cancer and oncology writing profile informed by articles published in *Clinical Cancer Research* (CCR). CCR is the default profile when no journal is specified. The repository is structured so additional journal profiles can be added without mixing their corpora or quantitative signals.

## What it does

- translates Chinese biomedical text into publication-ready English;
- translates English oncology text into accurate Chinese;
- polishes or rewrites manuscripts without silently changing scientific meaning;
- drafts and audits Abstracts, Methods, Results, Discussions, Translational Relevance statements, reviews, commentaries, and response letters;
- calibrates causal, predictive, subgroup, model-validation, and clinical-utility claims to the underlying evidence;
- checks numbers, terminology, tense, abbreviations, and unsupported assertions.

It does not provide clinical decision support and must not invent data, methods, citations, registrations, ethics approvals, or novelty claims.

## Install for Codex

Codex discovers personal skills from `$HOME/.agents/skills`. Clone this repository, then copy the bundled skill directory into that location. See OpenAI's [Build skills documentation](https://learn.chatgpt.com/docs/build-skills.md).

PowerShell example:

```powershell
git clone https://github.com/Winteric123/artificial-writing-skill.git
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\artificial-writing-skill\skills\artificial-writing-skill" "$HOME\.agents\skills\artificial-writing-skill"
```

Start a new Codex conversation after installation if the skill does not appear immediately.

## Use

Default CCR profile:

```text
Use $artificial-writing-skill to translate the following Chinese Results paragraph into publication-ready English.
```

Explicit profile:

```text
Use $artificial-writing-skill.
Target journal profile: Clinical Cancer Research.
Task: Revise this Discussion and audit causal and subgroup claims.
```

Only the CCR profile is bundled in this release. If another journal is named, the skill applies its universal integrity and evidence rules but must not claim to have learned that journal's style.

## CCR corpus provenance

- Fully reviewed PDFs: 189/189, covering 2,958 pages.
- Standardized section corpus: 1,095,664 words and 46,895 sentences.
- Reusable phrase-example bank: 9,411 rows from 181 distinct articles.
- Eight commentary articles without standard section headings were reviewed through page-level full-text fallback. They inform qualitative genre rules but are absent from the standardized section statistics and phrase-example bank.

The complete article-level index is [`ccr-corpus-bibliography.csv`](skills/artificial-writing-skill/references/ccr-corpus-bibliography.csv). It records titles, publication years, PMIDs, DOIs, available PMCIDs, corpus article types, reading-history status, and separate coverage flags.

The repository does not distribute source PDFs, abstracts, full-text extracts, or the raw phrase-example bank. Article titles and public bibliographic identifiers are included for traceability. Underlying articles remain subject to their respective copyright and licensing terms.

## Repository layout

```text
skills/artificial-writing-skill/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── core-translation-integrity.md
    ├── core-evidence-language.md
    ├── ccr-section-patterns.md
    ├── ccr-non-imrad-genres.md
    ├── ccr-phrase-patterns.md
    ├── ccr-corpus-provenance.md
    └── ccr-corpus-bibliography.csv
```

## Independence and license status

This is an independent, unofficial project. It is not affiliated with, endorsed by, or sponsored by the American Association for Cancer Research or *Clinical Cancer Research*.

No open-source license has been selected for this repository yet. A license can be added later if redistribution and modification rights are to be granted.
