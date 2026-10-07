# Artificial Writing Skill

**Source-grounded biomedical writing and evidence communication**

Artificial Writing Skill is a Codex resource for biomedical translation, manuscript development, and literature synthesis, with a focus on clinical and translational oncology. It integrates structured article-level reading records with section-specific language retrieval. The governing principle is fidelity to the underlying evidence: clearer expression should not alter numerical results, uncertainty, study context, or the strength of a scientific claim.

## Research scope

The resource supports Chinese–English translation, manuscript drafting and revision, evidence summaries, research reports, and presentation text. Its principal domains include cancer biomarkers, immunotherapy, targeted therapy, multi-omics, computational analysis, and preclinical models.

The corpus-backed communication profiles focus on *Clinical Cancer Research* and lung cancer within documented source coverage. Selected articles from other journals, including the *Journal of Thoracic Oncology*, contribute study-specific evidence and language resources; they do not establish journal-wide writing profiles. Task, journal, disease, manuscript section, audience, and evidence domain are selected independently. See the [profile registry](skills/artificial-writing-skill/references/profile-registry.md) for supported combinations and fallback rules.

An optional **STK11/LKB1 module** organizes core references and separately designated supporting studies. It distinguishes direct molecular evidence from contextual analyses and methodological analogues, and separates sequence variation, copy-number alterations, functional state, immune mechanisms, metabolism, and clinical outcomes.

## Evidence and language workflow

1. **Source registration.** Record article identity, eligibility, PMID/DOI, source version, and available reading evidence.
2. **Structured appraisal.** Retain the research question, design, population or model, assays, endpoints, analysis sets, central findings, negative results, and limitations.
3. **Language curation.** Organize terminology, collocations, and explicitly labelled synthetic sentence and paragraph frames by manuscript section and rhetorical function.
4. **Contextual retrieval.** Select resources by source and scientific scope while retaining provenance, usage restrictions, and review status. Held or quarantined entries are excluded from default writing retrieval.

Source registration, main-text reading, supplementary-material coverage, source rechecking, and independent review are separate states. Completion of one does not establish the others. Corpus inclusion is not evidence of exhaustive journal coverage or a systematic review.

For newly supplied PDFs, the [intake safeguards](skills/artificial-writing-skill/SKILL.md#inventory-and-intake-safeguards) require physical-page coverage of text, figures, tables, captions, and reference or administrative pages. Text extraction is not a reading check; source-internal numerical conflicts remain explicit alerts rather than silently reconciled estimates.

## Resource directory

| Resource | Purpose |
|---|---|
| [Literature index](skills/artificial-writing-skill/references/library-index.md) · [Inventory summary](skills/artificial-writing-skill/references/library-summary.json) | Current article coverage, inclusion decisions, and recorded reading states |
| [Language manifest](skills/artificial-writing-skill/references/language-index-manifest.json) · [Retrieval guide](skills/artificial-writing-skill/references/retrieval-and-maintenance.md) | Section-specific language resources, filters, and source-context interpretation |
| [STK11/LKB1 analysis guide](skills/artificial-writing-skill/references/stk11-analysis-framework.md) · [Study logic map](skills/artificial-writing-skill/references/stk11-study-logic-map.md) | Question-specific selection of molecular, clinical, and mechanistic evidence |
| [STK11 assay and treatment guide](skills/artificial-writing-skill/references/stk11-assay-treatment-guide.md) | Article retrieval by assay, data origin, treatment, research method, and relation to STK11 |
| [Co-alteration classification](skills/artificial-writing-skill/references/coalteration-topics.md) | Structured retrieval distinguishing sequence co-mutation, copy-number alterations, fusions, and other genomic contexts |
| [Reading acceptance criteria](skills/artificial-writing-skill/references/deep-reading-acceptance.md) · [Writing evaluation](skills/artificial-writing-skill/references/writing-evaluation.md) | Distinct requirements for source review, software checks, and writing-case assessment |
| [Skill entrypoint](skills/artificial-writing-skill/SKILL.md) | Task routing, evidence rules, and operational safeguards |

The linked registers and generated indexes are the authorities for current coverage; this overview does not duplicate changing article counts. See the [changelog](CHANGELOG.md) for selected dated updates, [maintenance and reproducibility](MAINTENANCE.md) for automated checks and snapshots, and [citation guidance](CITATION.md) for recording the version used in research.

## Installation and use

Install `skills/artificial-writing-skill` under the canonical Codex skills root: `$CODEX_HOME/skills` when configured, otherwise `$HOME/.codex/skills`. The following PowerShell example is for a **new installation** and stops if the target already exists:

```powershell
git clone https://github.com/Winteric123/artificial-writing-skill.git
$skillsRoot = if ($env:CODEX_HOME) {
    Join-Path $env:CODEX_HOME "skills"
} else {
    Join-Path $HOME ".codex\skills"
}
$skillTarget = Join-Path $skillsRoot "artificial-writing-skill"
if (Test-Path -LiteralPath $skillTarget) {
    throw "An installation already exists. Review and reconcile it before updating."
}
New-Item -ItemType Directory -Force $skillsRoot | Out-Null
Copy-Item -Recurse ".\artificial-writing-skill\skills\artificial-writing-skill" $skillTarget
```

Provide the source text or study results and specify the intended output:

```text
Use $artificial-writing-skill to revise this Discussion.
Journal: Clinical Cancer Research. Disease: lung cancer.
Preserve numerical results and uncertainty. Distinguish exploratory
subgroup associations from evidence of treatment prediction.
```

For direct retrieval, run from `skills/artificial-writing-skill` with Python 3.10 or later:

```powershell
python scripts/search_language.py --journal ccr --section results --query "co-mutation" --limit 5
python scripts/search_language.py --pmid 39804166 --section discussion --single-paper --limit 5
```

Read the returned source context before reuse. Synthetic frames are not quotations, and a literal PDF match does not establish contextual appropriateness. Unsupported journal or disease selections rely on supplied source material and core evidence rules.

### STK11 article retrieval

Use the dedicated article directory to select evidence by assay, data origin, treatment, or research method:

```powershell
python scripts/search_stk11_references.py --assay single_cell_rna --origin original
python scripts/search_stk11_references.py --treatment perioperative_ici
python scripts/search_stk11_references.py --relation direct_mutation --method computational-methods
```

Assay and origin must match the same assay record; original and reanalyzed data are not interchangeable. Missing tags indicate incomplete curation, not absence of an assay. Directory membership does not establish completed reading or direct STK11 evidence.

### Structured co-alteration retrieval

For section-specific language from articles with curated genomic classifications, use structured filters rather than relying only on keyword matches:

```powershell
python scripts/search_language.py --co-alteration analyzed --co-gene MTAP --section results --limit 5
python scripts/search_language.py --co-mutation analyzed --co-gene STK11 --section results --single-paper --limit 5
python scripts/search_language.py --journal jto --co-alteration analyzed --co-type copy_number_loss --section discussion --limit 5
```

`--co-alteration` covers broader genomic contexts; `--co-mutation` selects sequence-level co-mutations, with same-gene compound variants separately qualified. Add `--co-gene`, `--co-type`, or `--co-use` to refine the selection. The label `analyzed` includes descriptive or negative findings; it does not establish positive co-occurrence, mechanistic cooperation, or treatment prediction. These are article-level filters, so inspect each returned expression and its source boundary before reuse.

### Wisp Science

Wisp Science may use the same canonical skills root through a verified shared configuration. Avoid maintaining an independent duplicate; after skill changes, reload through **Settings → Skills** and start a new conversation when necessary.

## Scientific integrity and evaluation

Writing must preserve the population or model, comparator, endpoint, denominator, analysis status, and uncertainty. Association is not causation; prognosis is not treatment prediction; subgroup significance is not interaction evidence; preclinical activity is not patient benefit. Missing data, methods, citations, or approvals must not be invented.

Software checks assess register consistency, dependency hashes, retrieval behavior, and links. Writing-case evaluation examines factual fidelity and claim calibration. Article-level acceptance requires the documented source review. None of these checks substitutes for the others, and generated text requires researcher review. The resource is not a clinical decision-support system.

[GitHub Actions](https://github.com/Winteric123/artificial-writing-skill/actions/workflows/repository-checks.yml) runs repository checks and the skill regression suite on Ubuntu and Windows. Consult the run attached to the relevant commit; a green check is software-integrity evidence, not scientific acceptance.

## Independence and rights

This is an independent, unofficial project, unaffiliated with and not endorsed by the American Association for Cancer Research or *Clinical Cancer Research*.

Source PDFs, complete full-text extracts, and private research data are not distributed in this repository. Underlying articles retain their respective copyright and licensing terms. No open-source license has been selected for the repository.
