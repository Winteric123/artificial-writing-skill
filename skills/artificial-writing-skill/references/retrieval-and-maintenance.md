# Executable retrieval and maintenance

## Retrieval

Run from the skill folder, with a Python 3.10+ interpreter. The scripts use only the standard library. Example:

```powershell
python scripts/search_language.py --journal ccr --section results --highlight --single-paper --query "co-mutation" --limit 5
python scripts/search_language.py --journal jto --section methods --query "cohort" --limit 5
python scripts/search_language.py --section discussion --query "外部验证" --limit 5
python scripts/search_language.py --pmid 41619904 --purpose audit --include-held --limit 10
```

Filters: journal ID/name, publication year, primary/secondary section, rhetorical function, domain, unit, evidence tier, PMID, highlight and single-paper provenance. `--reviewed` requires every contributing source to have acceptance status `passed`; zero results is legitimate. Year/PMID/highlight filters must match the same contributing article. Abstract includes its component tags. Query tokens are AND-matched in expressions, usage explanations and usage cards; this is deterministic text retrieval, not semantic embedding search.

The cross-journal index is a retrieval view, not a merged corpus or learned multi-journal style. Every hit retains its journal, PMID/DOI/title/year, actual source asset/line, original catalog alias, source quality status, warnings and usage cards. JTO bullets are now searchable without being added to CCR counts. JTO domain tags are broad article-set routing hints, not term-level scientific annotations. Preserve the original article's version boundaries.

Default retrieval excludes `needs_source_check` and `quarantined`. Held entries are visible only with `--purpose audit --include-held`; they remain unusable as writing recommendations until the issue is actually resolved and the control updated. `usable` means language-retrieval eligible, not acceptance-passed. Article alerts travel with every affected hit, including multi-paper hits. Never treat a multi-paper source list as proof that each article contains the expression.

Load the returned source context before material scientific reuse. Numerical/clinical claims still require the original article or user data. `usage_cards` explain meaning, alternatives, synthetic examples and unsafe transfers; they are not quotations. Missing cards are explicitly uncurated, not automatically filled by a model. Use [language-usage-cards.json](language-usage-cards.json) to curate further high-value items and [language-controls.json](language-controls.json) to manage restrictions.

## Stable identity and compatibility

The authoritative retrieval ID is `<journal>-lang-<content hash>`, derived from journal, source asset, heading/container, expression and source PMID set. Row order and line shifts do not change it; changed expressions or provenance intentionally produce new IDs. Old journal catalog `entry_id` values remain aliases only and are meaningful together with `source_catalog_sha256`. Do not cite an old sequential ID alone.

Use `--entry-id <stable-id>` for exact lookup. [language-id-migrations.json](language-id-migrations.json) records deliberate retirements and replacements. A retired ID returns its migration notice, not a silently substituted expression. Conventional terms are not held merely because an article has a numerical conflict; source alerts still accompany them, while precise disputed claims are held or quarantined.

The index manifest records a content-addressed index version plus hashes of source catalogs, language assets, registry, bibliography, ledger, quality, controls and cards. Retrieval fails closed if a dependency changes or the index is edited. Rebuild rather than bypassing this check. Historical source catalogs can retain historical date labels; the manifest hash identifies the actual retrieval revision, including multiple same-day updates.

## Updates

### Inventory reporting scope

Before reporting counts, state the issue-year range, journal selection and any topic/batch selection. Use `library-summary.json` as follows:

- Top-level totals: all registered formal journals and all indexed issue years, with no topic filter.
- `years[year]`: that issue year across all registered formal journals, not CCR alone.
- `journal_years[journal][year]`: the named journal and issue year, without a topic filter.
- For a topic or intake batch, filter `library-index.csv` using a documented PMID set or explicit content criteria before counting. Do not rename an entire journal/year subset as a topic-specific set.

Within each selection, `included = complete + incomplete` and `registered = included + excluded`. Completion means `reading_stage=main_text_deep_read_complete` among included records, not review acceptance. Excluded records are not pending research readings. Count preprint versions separately and do not add their related formal PMID as a completed formal record. Report missing formal versions outside the registered subset separately rather than adding them to its pending denominator.

Use a scope-bearing label such as “2025年／全部已登记正式期刊／不限定专题” or “2025年／CCR／不限定专题”; include the actual topic or batch when one is selected. Rebuild rather than relying on a historical numerical example.

### Maintenance sequence

1. Modify authoritative sources and only genuinely completed reading/review records. Register new journals in [journal-registry.json](journal-registry.json) and document their support in the profile registry. A configured journal without a language source can be inventoried but is not a learned style.
2. Regenerate CCR's source catalog if a contributing CCR language asset changed.
3. Run `python scripts/validate_reading_quality.py`, then `python scripts/build_library_index.py`, then `python scripts/build_language_index.py`.
4. Run `python -m unittest discover -s tests -v` and the skill creator validator. Record actual behavioral evaluation separately using [writing-evaluation.md](writing-evaluation.md).
5. Verify Wisp discovery after the final changes. Updating shared files alone does not refresh an existing conversation.

Preprints and formal versions retain separate IDs, files, hashes and reading stages. The related formal DOI/PMID is a link, not a completion shortcut. The former `formal_version_read` column is now explicitly named `formal_version_read_at_intake`; it records intake-era information only. Runtime status is derived from the current formal bibliography/quality join, never from that cached flag. A formal record can be absent, indexed or independently read without invalidating the preprint. DOI disagreement is an error before outputs are written. Do not copy preprint language into a formal catalog without reading the corresponding version.

Totals come from `library-summary.json` and the generated inventory. Keep historical dated snapshots labeled historical; do not copy live counts into routing instructions. Builders do not certify scientific correctness. Keep local archive paths and private manuscript workspaces outside the distributed skill.

## Project writing

For sustained STK11 writing, copy [the project template](../assets/stk11-project-workspace.md) into the user's project when it will be useful. Do not create a project for a one-sentence translation. Populate the template from actual supplied data, maintain terminology and figure/claim links, and resume from its explicit checkpoint. Do not write private findings into shared reference assets or push them to GitHub.
