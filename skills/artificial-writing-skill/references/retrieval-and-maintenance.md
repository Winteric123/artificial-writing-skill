# Executable retrieval and maintenance

## Retrieval

Run from the skill folder, with a Python 3.10+ interpreter. Retrieval, index builders and tests use the standard library. The optional original-PDF locator builder additionally requires PyMuPDF. Example:

```powershell
python scripts/search_language.py --journal ccr --section results --highlight --single-paper --query "co-mutation" --limit 5
python scripts/search_language.py --journal jto --section methods --query "cohort" --limit 5
python scripts/search_language.py --section discussion --query "外部验证" --limit 5
python scripts/search_language.py --pmid 41619904 --purpose audit --include-held --limit 10
python scripts/search_language.py --disease SCLC --section results --limit 5
python scripts/search_language.py --disease lung-cancer --include-subtypes --query "克隆性造血" --limit 5
python scripts/search_language.py --pmid 37756581 --domain spatial-protein --limit 5
python scripts/search_language.py --tissue plasma --model human-clinical --source-role lung-primary --limit 5
python scripts/search_language.py --pmid 37097610 --pdf-located --limit 5
```

Filters: journal ID/name, publication year, primary/secondary section, rhetorical function, expression domain, broad article domain, unit, evidence tier, PMID, highlight, single-paper provenance, source disease, tissue, experimental model and source role. `--reviewed` requires every contributing source to have acceptance status `passed`; zero results is legitimate. Year/PMID/highlight/disease/tissue/model/source-role filters must match the same contributing article, not different articles in a batch. These are article-level facets, not proof that an assay used every listed tissue or disease. Abstract includes its component tags.

Tags match complete normalized values, never arbitrary substrings: `SCLC` is not `NSCLC`. `--disease` is exact; `--include-subtypes` explicitly traverses the registered disease hierarchy. Unknown facets do not match. `--source-role` uses controlled `use_roles`, not a fuzzy search over the historical free-text source-role field. See [retrieval-vocabulary.json](retrieval-vocabulary.json) for aliases and allowed filters. Curated facets and expression-topic corrections are in [retrieval-annotations.json](retrieval-annotations.json); both files are hash-checked dependencies. Source references are existing read records, not new source-recheck acceptance.

`--query` expands recognized Chinese/English concepts as alternatives, then AND-matches the concept clauses and remaining words across expressions, usage explanations and cards. Longer phrases take precedence. Unregistered text is literal; this is deterministic retrieval, not semantic embedding or unrestricted synonym generation. Closely related concepts are retrieval aids, not scientifically interchangeable measures: knockdown/knockout and target engagement/occupancy retain separate concepts. Equivalent registered Chinese/English queries should return the same IDs. Query punctuation and inflections are not arbitrary natural-language understanding; use the registered collocation when needed.

The cross-journal index is a retrieval view, not a merged corpus or learned multi-journal style. Every hit retains its journal, PMID/DOI/title/year, actual source asset/line, original catalog alias, source quality status, warnings and usage cards. JTO bullets are searchable without being added to CCR counts. `--domain` uses `expression_domains`; `--article-domain` deliberately selects broad historical `article_domains`. Automatically detected expression topics are labelled `lexical-topic-candidate`, not validated methods; manually reviewed examples are `curated-expression-topic`. Unclassified expressions remain searchable by literal query and source filters. Preserve the original article's version boundaries.

The manifest reports source-facet, expression-topic and PDF-locator coverage separately. Original scope annotations plus [source-scope-backfill.json](source-scope-backfill.json) supply structured disease/tissue/model/role filters in both retrieval and `library-index.csv`. Populated facets mean identified-not-exhaustive; empty facets mean not-curated-not-absent. Neither guarantees exhaustive specimen mapping. New vocabulary labels do not establish learned disease/journal profiles. Inspect the article boundary before transferring an assay or outcome across cohorts.

[source-pdf-locators.json](source-pdf-locators.json) binds each literal match to a PMID, registered PDF SHA-256 and one-based physical page (PDF viewer page, not printed journal pagination). `precision=pdf-text-match` and `pdf_text_match_verified=true` mean normalized literal text was found mechanically, not that the full scientific context was validated. `--pdf-located` must match a contributing PMID that also satisfies all other source filters. No match may reflect abstraction, wording variation or extraction artifacts; it does not prove the PDF is missing or the article was unread. Reference-list exclusion is a text-heading heuristic, not visual certification; inspect the actual page before reuse.

`recorded_page_hints` preserve old note numbers with `page_numbering=unverified-reading-note-numbering`; even numbers within PDF bounds are not confirmed physical pages. Out-of-range hints remain flagged, never silently repaired. `section-context` and `asset-only` describe curated-asset precision only. `synthetic-not-a-verbatim-quotation` is an expected state for rewritten sentence/paragraph frames, not a missing quotation that should be filled. Conventional vocabulary and collocations are distinguished from synthetic frames. `original_wording_verified`, `original_pdf_location_verified` and `quotation_verified` remain false: machine text-location checks do not upgrade them. The dated [repair audit](source-provenance-audit.md) records bounded visual spot checks separately, not independent review acceptance.

Default retrieval excludes `needs_source_check` and `quarantined`. Held entries are visible only with `--purpose audit --include-held`; they remain unusable as writing recommendations until the issue is actually resolved and the control updated. `usable` means language-retrieval eligible, not acceptance-passed. Article alerts travel with every affected hit, including multi-paper hits. Never treat a multi-paper source list as proof that each article contains the expression.

Load the returned source context before material scientific reuse. Numerical/clinical claims still require the original article or user data. `usage_cards` explain meaning, alternatives, synthetic examples and unsafe transfers; they are not quotations. Missing cards are explicitly uncurated, not automatically filled by a model. Use [language-usage-cards.json](language-usage-cards.json) to curate further high-value items and [language-controls.json](language-controls.json) to manage restrictions.

## Stable identity and compatibility

The authoritative retrieval ID is `<journal>-lang-<content hash>`, derived from journal, source asset, heading/container, expression and source PMID set. Row order and line shifts do not change it; changed expressions or provenance intentionally produce new IDs. Old journal catalog `entry_id` values remain aliases only and are meaningful together with `source_catalog_sha256`. Do not cite an old sequential ID alone.

Use `--entry-id <stable-id>` for exact lookup. [language-id-migrations.json](language-id-migrations.json) records deliberate retirements and replacements. A retired ID returns its migration notice, not a silently substituted expression. Conventional terms are not held merely because an article has a numerical conflict; source alerts still accompany them, while precise disputed claims are held or quarantined.

The index manifest records a content-addressed index version plus hashes of source catalogs, language assets, registry, bibliography, ledger, quality, controls and cards. Retrieval fails closed if a dependency changes or the index is edited. Rebuild rather than bypassing this check. Historical source catalogs can retain historical date labels; the manifest hash identifies the actual retrieval revision, including multiple same-day updates.

Retrieval schema 2 adds vocabulary, source facets, expression topics and locator precision. Rebuild with the matching builder before using the schema-2 reader; historical source catalogs and stable IDs are unchanged. Changing vocabulary, scope backfill, PDF locators, annotations, their supporting references, or the library index invalidates retrieval. The builder rejects absent/ambiguous expression annotations, unknown controlled tags, mismatched PDF hashes/versions, invalid literal page bounds and retired locator IDs. Newly added entries without anchors are explicitly `not-yet-located`, never assumed verified.

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
3. Run `python scripts/validate_reading_quality.py`, then `python scripts/build_library_index.py`. If language assets or registered PDFs changed, regenerate PDF locators before `python scripts/build_language_index.py`; then run `python scripts/build_provenance_audit.py` to refresh the coverage and pending queues.
4. Run `python -m unittest discover -s tests -v` and the skill creator validator. Record actual behavioral evaluation separately using [writing-evaluation.md](writing-evaluation.md).
5. Verify Wisp discovery after the final changes. Updating shared files alone does not refresh an existing conversation.

Preprints and formal versions retain separate IDs, files, hashes and reading stages. The related formal DOI/PMID is a link, not a completion shortcut. The former `formal_version_read` column is now explicitly named `formal_version_read_at_intake`; it records intake-era information only. Runtime status is derived from the current formal bibliography/quality join, never from that cached flag. A formal record can be absent, indexed or independently read without invalidating the preprint. DOI disagreement is an error before outputs are written. Do not copy preprint language into a formal catalog without reading the corresponding version.

Totals come from `library-summary.json` and the generated inventory. Keep historical dated snapshots labeled historical; do not copy live counts into routing instructions. Builders do not certify scientific correctness. Keep local archive paths and private manuscript workspaces outside the distributed skill.

PDF locator rebuild: `python scripts/build_pdf_locators.py --local-inventory <private-inventory.json>`. This reads source catalogs directly (not the possibly stale retrieval index) and reopens every supplied PDF. The private inventory is a list of objects with `pmid` and `selected: {path, sha256}`; paths must point to the exact registered version in `source-version-register.csv`. Regeneration aborts on a missing/hash-mismatched PDF and writes only after successful processing. Never publish the private inventory. Shared locators contain basenames/hashes/pages, not absolute archive paths. Replacing a PDF or moving a language entry requires regeneration rather than copying the old page numbers.

## Project writing

For sustained STK11 writing, copy [the project template](../assets/stk11-project-workspace.md) into the user's project when it will be useful. Do not create a project for a one-sentence translation. Populate the template from actual supplied data, maintain terminology and figure/claim links, and resume from its explicit checkpoint. Do not write private findings into shared reference assets or push them to GitHub.
