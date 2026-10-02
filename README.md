# Artificial Writing Skill

A source-grounded Codex skill for biomedical translation, scientific writing, and evidence synthesis. It combines structured literature reading with retrieval of section-specific terminology, collocations, sentence frames, and paragraph models. Its purpose is to improve scientific expression while preserving the meaning, numerical results, uncertainty, and scope of the underlying evidence.

## Scope and capabilities

The skill supports Chinese–English biomedical translation, manuscript revision and drafting, evidence audits, literature summaries, research reports, and presentation text. Clinical and translational oncology are the principal application areas, including biomarker studies, immunotherapy, targeted therapy, multi-omics, computational analyses, and experimental models.

Operation, communication scenario, journal, disease, manuscript section, audience, and evidence domain are selected independently. The corpus-backed profiles cover *Clinical Cancer Research* and lung-cancer communication within their documented source coverage. Other journals contribute article-specific evidence and language resources; inclusion does not establish a learned journal-wide style. The [profile registry](skills/artificial-writing-skill/references/profile-registry.md) defines these support levels and their limits.

The optional STK11/LKB1 module links core framework references with separately labelled topic-support studies. It distinguishes sequence variants, copy-number alterations, functional state, immune mechanisms, metabolism, and clinical outcomes. The [analysis guide](skills/artificial-writing-skill/references/stk11-analysis-framework.md), [study logic map](skills/artificial-writing-skill/references/stk11-study-logic-map.md), and [membership register](skills/artificial-writing-skill/references/stk11-writing-reference-map.json) support study-specific selection without treating contextual evidence as direct STK11 evidence.

## Literature, provenance, and retrieval

Each journal retains its own bibliography, reading ledger, quality register, and language catalog. Records preserve bibliographic identifiers, supplied source versions, article-level scope, and links to reading evidence. The [library index](skills/artificial-writing-skill/references/library-index.md) and [inventory summary](skills/artificial-writing-skill/references/library-summary.json) provide current coverage and reading states; the [language manifest](skills/artificial-writing-skill/references/language-index-manifest.json) reports retrieval coverage. These generated records are the inventory authorities.

Literature intake verifies article identity and eligibility, reads the supplied main text and available supporting material, records central findings and limitations, and curates language by section and rhetorical function. Main-text completion, supplementary coverage, source rechecking, and independent review remain distinct. The [acceptance criteria](skills/artificial-writing-skill/references/deep-reading-acceptance.md) define the evidence required for status changes. Indexed coverage is not exhaustive journal coverage.

Retrieval can be filtered by journal, year, PMID, section, evidence domain, and language-unit type. Results retain source context, usage restrictions, and review status. Synthetic frames are labelled separately from source expressions; a literal PDF match does not establish contextual suitability. Held or quarantined entries are excluded from default writing retrieval.

Run these examples from `skills/artificial-writing-skill` with Python 3.10 or later:

```powershell
python scripts/search_language.py --journal ccr --section results --query "co-mutation" --limit 5
python scripts/search_language.py --pmid 39804166 --section discussion --single-paper --limit 5
```

Consult [retrieval and maintenance](skills/artificial-writing-skill/references/retrieval-and-maintenance.md) for additional filters, source-scope interpretation, index rebuilding, and validation.

## Installation and use

Install the `skills/artificial-writing-skill` directory under the canonical Codex skills root: `$CODEX_HOME/skills` when configured, otherwise `$HOME/.codex/skills`. For a new PowerShell installation:

```powershell
git clone https://github.com/Winteric123/artificial-writing-skill.git
$skillsRoot = if ($env:CODEX_HOME) {
    Join-Path $env:CODEX_HOME "skills"
} else {
    Join-Path $HOME ".codex\skills"
}
New-Item -ItemType Directory -Force $skillsRoot | Out-Null
Copy-Item -Recurse ".\artificial-writing-skill\skills\artificial-writing-skill" $skillsRoot
```

Invoke the skill with source text or study results and specify the required output:

```text
Use $artificial-writing-skill to revise this Discussion.
Journal: Clinical Cancer Research. Disease: lung cancer.
Preserve all numerical results and distinguish exploratory subgroup
associations from evidence of treatment prediction.
```

The [skill entrypoint](skills/artificial-writing-skill/SKILL.md) routes the task to the relevant workflow and references. Unsupported journal or disease selections use supplied source material and core evidence rules.

Wisp Science can share the canonical skills root through `WISP_SKILLS_PATH` or an existing skills-root directory junction. Use the configured shared route without creating a duplicate installation. After changes, reload skills in **Settings → Skills** and start a new conversation when updated instructions are required.

## Scientific boundaries and validation

Outputs must preserve population, model, comparator, endpoint, denominator, analysis status, and uncertainty. The workflow distinguishes association from causation, prognosis from treatment prediction, subgroup findings from interaction evidence, and preclinical effects from patient benefit. It does not provide clinical decision support or invent data, methods, citations, or study approvals.

Source eligibility follows the registered corpus policy. Commentaries, editorials, and replies are excluded from reusable corpus learning; background sources and preprints retain separate status. These restrictions do not prevent requested writing or translation in those genres.

Maintenance checks cover record consistency, provenance, dependency hashes, retrieval behavior, and documentation links. Scientific acceptance requires the documented source review; passing software checks alone does not establish it. The [evaluation guide](skills/artificial-writing-skill/references/writing-evaluation.md) separates mechanical checks, writing-case assessment, and independent review.

## Independence and rights

This is an independent, unofficial project, unaffiliated with and not endorsed or sponsored by the American Association for Cancer Research or *Clinical Cancer Research*.

The repository does not distribute source PDFs, complete full-text extracts, or private research data. Bibliographic identifiers and curated resources support traceability; underlying articles retain their respective copyright and licensing terms. No open-source license has been selected for this repository.
