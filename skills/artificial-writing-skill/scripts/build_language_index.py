import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True

from library_common import atomic_json, content_hash, file_hash, journal_registry, read_csv, read_json, reference_path
from validate_reading_quality import validate
from retrieval_metadata import article_scope, expression_metadata
from source_provenance import FACETS, attach_pdf_locator, load_pdf_locators, load_scope_annotations


def normalize(value):
    return re.sub(r'\s+', '-', value.strip().casefold().replace('_', '-'))


def stable_id(journal, row):
    identity = [journal, row['source_asset'], row.get('source_container', ''), row.get('source_heading', ''),
                row['expression'].strip(), sorted(row['source_article_ids'].split(';'))]
    return f'{journal}-lang-{content_hash(identity)[:20]}'


def markdown_entries(path):
    pmid, heading = '', ''
    for number, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
        match = re.match(r'^## PMID (\d{8})', line)
        if match:
            pmid, heading = match[1], ''
        elif line.startswith('## '):
            pmid, heading = '', ''
        elif line.startswith('### '):
            heading = line[4:].strip()
        elif pmid and heading and line.startswith('- `'):
            section_match = re.search(r'abstract (background|methods|results|conclusion)|introduction|methods|results|discussion|conclusion|figure', heading, re.I)
            if not section_match:
                raise ValueError(f'Unmapped language heading: {path.name}:{number}: {heading}')
            section = normalize(section_match[0])
            for expression in re.findall(r'`([^`]+)`', line):
                is_sentence = '[' in expression or expression.endswith('.')
                unit = 'paragraph-model' if 'paragraph' in heading.casefold() else ('sentence-frame' if is_sentence else 'vocabulary')
                yield dict(entry_id=f'JTO-LINE-{number}', expression=expression, source_article_ids=pmid,
                           primary_section=section, secondary_sections='', function='terminology' if unit == 'vocabulary' else normalize(heading),
                           domain='clinical-oncology;genomics;statistics', domain_basis='broad article-set tags; inspect expression before domain-specific reuse',
                           unit_type=unit, evidence_tier='retrospective-observational', source_asset=path.name, source_heading=heading,
                           source_line=str(number), usage_constraint=line.split('`')[-1].strip(' —'),
                           provenance_granularity='single-paper-synthesis', reuse_status='conventional-term-or-collocation' if unit == 'vocabulary' else 'synthetic-model')


def apply_controls(entry, controls):
    ranks = {'usable': 0, 'needs_source_check': 1, 'quarantined': 2}
    entry['retrieval_state'] = 'usable'
    entry['control_reasons'] = []
    entry['source_alerts'] = []
    identifiers = set(entry['source_article_ids'].split(';'))
    for alert in controls.get('article_alerts', []):
        if identifiers.intersection(alert['article_ids']):
            entry['source_alerts'].append(alert)
    for rule in controls.get('entry_rules', []):
        if rule['state'] not in ranks:
            raise ValueError(f'Invalid retrieval state: {rule["id"]}')
        matches_id = entry['stable_id'] in rule.get('stable_ids', [])
        matches_pattern = bool(rule.get('expression_regex')) and bool(identifiers.intersection(rule.get('article_ids', []))) and bool(re.search(rule['expression_regex'], entry['expression'], re.I))
        if matches_id or matches_pattern:
            if ranks[rule['state']] > ranks[entry['retrieval_state']]:
                entry['retrieval_state'] = rule['state']
            entry['control_reasons'].append(rule)
    return entry


def build(skill):
    validate(skill)
    references = skill / 'references'
    dependencies = {'journal-registry.json', 'language-controls.json', 'language-usage-cards.json', 'language-id-migrations.json', 'stk11-priority-references.md', 'source-version-register.csv', 'library-index.csv', 'retrieval-vocabulary.json', 'retrieval-annotations.json'}
    vocabulary = read_json(references / 'retrieval-vocabulary.json')
    annotations = read_json(references / 'retrieval-annotations.json')
    annotations['articles'] = load_scope_annotations(skill, vocabulary)
    pdf_locators = load_pdf_locators(skill)
    dependencies.update({'source-scope-backfill.json', 'source-pdf-locators.json'})
    dependencies.update(pdf_locators['source_asset_hashes'])
    library = {row['pmid']: row for row in read_csv(references / 'library-index.csv')}
    expression_annotations = {}
    for annotation in annotations['expressions']:
        selector = (annotation['pmid'], annotation['expression'])
        if selector in expression_annotations:
            raise ValueError(f'Duplicate expression annotation: {selector}')
        expression_annotations[selector] = annotation
    annotation_hits = Counter()
    for annotation in [*annotations['articles'].values(), *annotations['expressions']]:
        relative = annotation['source_reference']
        reference_path(skill, relative)
        dependencies.add(relative)
        for field, group in [('disease_ids', 'diseases'), ('tissue_ids', 'tissues'), ('model_ids', 'models'), ('use_roles', 'roles'), ('expression_domains', 'domains')]:
            if not set(annotation.get(field, [])).issubset(vocabulary[group]):
                raise ValueError(f'Unknown annotation tag: {relative}/{field}')
    asset_lines = {}
    controls = read_json(reference_path(skill, 'language-controls.json'))
    cards = read_json(reference_path(skill, 'language-usage-cards.json'))['cards']
    if len({card['id'] for card in cards}) != len(cards):
        raise ValueError('Duplicate usage-card ID')
    for card in cards:
        for field in ('id', 'match_terms', 'zh', 'sections', 'use_when', 'confusable', 'safe_example', 'unsafe_example', 'boundary', 'basis'):
            if not card.get(field):
                raise ValueError(f'Incomplete usage card: {card.get("id")}/{field}')
        dependencies.add(card['basis'])
        reference_path(skill, card['basis'])
    for rule in controls['entry_rules']:
        if not rule.get('stable_ids') and not (rule.get('article_ids') and rule.get('expression_regex')):
            raise ValueError(f'Unscoped entry control: {rule["id"]}')
        if rule.get('expression_regex'):
            re.compile(rule['expression_regex'])
    for rule in [*controls['article_alerts'], *controls['entry_rules']]:
        relative = rule['source_reference'].split('#', 1)[0]
        reference_path(skill, relative)
        dependencies.add(relative)
    versions = {row['pmid']: row for row in read_csv(references / 'source-version-register.csv')}
    highlights = set(re.findall(r'^\| 1 \| [^|]+ \| \d{4} \| (\d{8}) \|', (references / 'stk11-priority-references.md').read_text(encoding='utf-8-sig'), re.M))
    entries = []
    articles = {}
    seen_pmids = set()
    for journal_id, configuration in journal_registry(skill).items():
        dependencies.update(configuration[field] for field in ('bibliography', 'ledger', 'quality'))
        bibliography = {row['pmid']: row for row in read_csv(references / configuration['bibliography'])}
        if seen_pmids.intersection(bibliography):
            raise ValueError('Duplicate PMID across journal registries')
        seen_pmids.update(bibliography)
        quality = {row['pmid']: row for row in read_csv(references / configuration['quality'])}
        source_name = configuration.get('language_catalog') or configuration.get('language_markdown')
        if not source_name:
            continue
        source_path = reference_path(skill, source_name)
        dependencies.add(source_name)
        catalog_hash = file_hash(source_path)
        raw_rows = read_csv(source_path) if configuration.get('language_catalog') else list(markdown_entries(source_path))
        for row in raw_rows:
            source_ids = row['source_article_ids'].split(';')
            if not source_ids or any(identifier not in bibliography for identifier in source_ids):
                raise ValueError(f'Unknown or cross-journal language source: {source_name}/{row["entry_id"]}')
            if any(quality[identifier]['eligibility'] != 'included' or quality[identifier]['reading_stage'] != 'main_text_deep_read_complete' for identifier in source_ids):
                raise ValueError(f'Language source is excluded or incomplete: {source_name}/{row["entry_id"]}')
            asset = reference_path(skill, row['source_asset'])
            dependencies.add(row['source_asset'])
            if row['source_asset'] not in asset_lines:
                asset_lines[row['source_asset']] = asset.read_text(encoding='utf-8-sig').splitlines()
            lines = asset_lines[row['source_asset']]
            line_number = int(row['source_line'])
            if not 1 <= line_number <= len(lines) or row['expression'] not in lines[line_number - 1]:
                raise ValueError(f'Stale language locator: {source_name}/{row["entry_id"]}')
            entry = dict(row)
            entry.update(stable_id=stable_id(journal_id, row), journal_id=journal_id, journal=configuration['name'],
                         source_catalog=source_name, source_catalog_sha256=catalog_hash,
                         primary_section=normalize(row['primary_section']),
                         secondary_sections=';'.join(normalize(section) for section in row.get('secondary_sections', '').split(';') if section),
                         domain=row.get('domain', '').replace('_', '-'),
                         source_articles=[dict(pmid=identifier, year=bibliography[identifier]['year'], title=bibliography[identifier]['title'], doi=bibliography[identifier]['doi'],
                                               reading_stage=quality[identifier]['reading_stage'], review_status=quality[identifier]['review_status'],
                                               main_read_completed_on=quality[identifier]['main_read_completed_on'], supplement_status=quality[identifier]['supplement_status'],
                                               supplied_pdf_version=versions.get(identifier, {}).get('supplied_pdf_version', 'not_recorded'),
                                               source_sha256=versions.get(identifier, {}).get('sha256', ''),
                                               highlight=identifier in highlights) for identifier in source_ids],
                         usage_cards=[card for card in cards if any(term.casefold() in row['expression'].casefold() for term in card['match_terms'])])
            selected = [(identifier, row['expression']) for identifier in source_ids if (identifier, row['expression']) in expression_annotations]
            if len(selected) > 1:
                raise ValueError(f'Ambiguous multi-source expression annotation: {selected}')
            annotation = expression_annotations[selected[0]] if selected else None
            metadata = expression_metadata(row, lines, vocabulary)
            metadata['usage_constraint'] = ' '.join(filter(None, [row.get('usage_constraint', ''), metadata['usage_constraint']]))
            if annotation:
                annotation_hits[selected[0]] += 1
                metadata.update({key: value for key, value in annotation.items() if key not in {'pmid', 'expression'}})
                metadata['expression_annotation_status'] = 'curated-expression-topic'
            entry.update(metadata)
            attach_pdf_locator(entry, pdf_locators)
            apply_controls(entry, controls)
            if any(quality[identifier]['review_status'] == 'needs_correction' for identifier in source_ids) and entry['retrieval_state'] != 'quarantined':
                entry['retrieval_state'] = 'needs_source_check'
                entry['control_reasons'].append({'id': 'article-needs-correction', 'reason': 'At least one source article requires correction; reopen the source.'})
            for article in entry.pop('source_articles'):
                article['review_record'] = quality[article['pmid']]['review_record']
                scope_row = {**library.get(article['pmid'], {}), 'scope_reference': 'library-index.csv'}
                article['source_scope'] = article_scope(scope_row, vocabulary, annotations['articles'].get(article['pmid']))
                article['source_pdf'] = pdf_locators['sources'].get(article['pmid'], {'identity_check': 'not-yet-located'})
                articles[article['pmid']] = article
            entry['usage_card_ids'] = [card['id'] for card in entry.pop('usage_cards')]
            entry['source_alert_ids'] = [alert['id'] for alert in entry.pop('source_alerts')]
            entries.append(entry)
    if set(annotations['articles']) - set(articles):
        raise ValueError('Article scope annotation has no eligible language source')
    if any(annotation_hits[selector] != 1 for selector in expression_annotations):
        raise ValueError(f'Stale or ambiguous expression annotation: {[selector for selector in expression_annotations if annotation_hits[selector] != 1]}')
    identifiers = [entry['stable_id'] for entry in entries]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError('Duplicate stable language ID; reconcile identical source records')
    if set(pdf_locators['entries']) - set(identifiers):
        raise ValueError('PDF locators reference retired entries; regenerate PDF locators')
    for rule in controls['entry_rules']:
        if not set(rule.get('stable_ids', [])).issubset(identifiers):
            raise ValueError(f'Entry control references an absent stable ID: {rule["id"]}')
    migrations = read_json(references / 'language-id-migrations.json')['migrations']
    for migration in migrations:
        if migration['retired_id'] in identifiers or migration['replacement_id'] not in identifiers:
            raise ValueError('Inconsistent language-ID migration')
    entries.sort(key=lambda entry: entry['stable_id'])
    dependency_hashes = {name: file_hash(reference_path(skill, name)) for name in sorted(dependencies)}
    payload = dict(schema_version=2, entries=entries, articles=articles, vocabulary=vocabulary,
                   usage_cards={card['id']: card for card in cards},
                   article_alerts={alert['id']: alert for alert in controls['article_alerts']})
    manifest = dict(schema_version=2, index_version=content_hash(payload), entry_count=len(entries),
                    journals=dict(Counter(entry['journal_id'] for entry in entries)),
                    retrieval_states=dict(Counter(entry['retrieval_state'] for entry in entries)),
                    usage_card_count=len(cards), dependencies=dependency_hashes,
                    source_scope_status=dict(Counter(article['source_scope']['annotation_status'] for article in articles.values())),
                    source_facet_coverage={field: dict(Counter(article['source_scope']['facet_status'][field] for article in articles.values())) for field in FACETS},
                    pdf_locator_states=dict(Counter(entry['source_locator']['state'] for entry in entries)),
                    source_pdf_count=sum(article['source_pdf']['identity_check'] == 'registered-sha256-match' for article in articles.values()),
                    entries_with_recorded_page_hints=sum(bool(entry['source_locator']['recorded_page_hints']) for entry in entries),
                    expression_annotation_status=dict(Counter(entry['expression_annotation_status'] for entry in entries)),
                    scope='Cross-journal retrieval view only; source corpora, counts and reading statuses remain separate.')
    atomic_json(references / 'language-retrieval-index.json', payload)
    manifest['index_file_sha256'] = file_hash(references / 'language-retrieval-index.json')
    atomic_json(references / 'language-index-manifest.json', manifest)
    return {key: value for key, value in manifest.items() if key != 'dependencies'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build stable, source-linked language retrieval without changing reading status.')
    parser.add_argument('--skill-path', type=Path, default=Path(__file__).resolve().parents[1])
    arguments = parser.parse_args()
    import json
    print(json.dumps(build(arguments.skill_path), ensure_ascii=False, indent=2))
