import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

from build_language_index import normalize
from library_common import file_hash, read_json, reference_path
from retrieval_metadata import canonical, exact_tag_match, query_clauses, query_matches


def load_index(skill):
    manifest = read_json(reference_path(skill, 'language-index-manifest.json'))
    index_path = reference_path(skill, 'language-retrieval-index.json')
    if manifest['schema_version'] != 2 or file_hash(index_path) != manifest['index_file_sha256']:
        raise ValueError('Language index is incompatible or modified; rebuild before retrieval')
    for relative, expected in manifest['dependencies'].items():
        if file_hash(reference_path(skill, relative)) != expected:
            raise ValueError(f'Stale language index dependency: {relative}; run build_language_index.py')
    payload = read_json(index_path)
    if payload['schema_version'] != 2:
        raise ValueError('Unsupported language payload schema; rebuild before retrieval')
    for entry in payload['entries']:
        entry['_vocabulary'] = payload['vocabulary']
        entry['source_articles'] = [payload['articles'][identifier] for identifier in entry['source_article_ids'].split(';')]
        entry['usage_cards'] = [payload['usage_cards'][identifier] for identifier in entry['usage_card_ids']]
        entry['source_alerts'] = [payload['article_alerts'][identifier] for identifier in entry['source_alert_ids']]
    return payload['entries'], manifest


def source_matches(article, vocabulary, *, year, pmid, highlight, disease, include_subtypes, tissue, model, source_role):
    if (year and article['year'] != str(year)) or (pmid and article['pmid'] != pmid) or (highlight and not article['highlight']):
        return False
    scope = article.get('source_scope', {})
    if disease:
        wanted = {canonical(disease, vocabulary.get('diseases', {}))}
        if include_subtypes:
            pending = list(wanted)
            while pending:
                parent = pending.pop()
                for child in vocabulary.get('disease_children', {}).get(parent, []):
                    if child not in wanted:
                        wanted.add(child)
                        pending.append(child)
        if not wanted.intersection(scope.get('disease_ids', [])):
            return False
    for value, field, group in [(tissue, 'tissue_ids', 'tissues'), (model, 'model_ids', 'models'), (source_role, 'use_roles', 'roles')]:
        if value and not exact_tag_match(value, scope.get(field, []), vocabulary.get(group, {})):
            return False
    return True


def search(entries, *, query='', journal='', year='', section='', function='', domain='', article_domain='', disease='', include_subtypes=False, tissue='', model='', source_role='', unit='', evidence_tier='', pmid='', entry_id='', highlight=False, single_paper=False, reviewed=False, include_held=False, pdf_located=False, limit=10):
    if not 1 <= limit <= 100:
        raise ValueError('limit must be between 1 and 100')
    result = []
    vocabulary = entries[0].get('_vocabulary', {}) if entries else {}
    clauses = query_clauses(query, vocabulary.get('concepts', []))
    for entry in entries:
        if entry_id and entry['stable_id'] != entry_id:
            continue
        if not include_held and entry['retrieval_state'] != 'usable':
            continue
        if journal and journal.casefold() not in {entry['journal_id'].casefold(), entry['journal'].casefold()}:
            continue
        if single_paper and entry['provenance_granularity'] != 'single-paper-synthesis':
            continue
        if reviewed and not all(article['review_status'] == 'passed' for article in entry['source_articles']):
            continue
        matching_sources = [article for article in entry['source_articles'] if source_matches(article, vocabulary, year=year, pmid=pmid, highlight=highlight, disease=disease, include_subtypes=include_subtypes, tissue=tissue, model=model, source_role=source_role)]
        if not matching_sources:
            continue
        if pdf_located:
            located = {match['pmid'] for match in entry.get('source_locator', {}).get('literal_matches', [])}
            matching_sources = [article for article in matching_sources if article['pmid'] in located]
            if not matching_sources:
                continue
        sections = [entry['primary_section'], *entry['secondary_sections'].split(';')]
        if section and not any(normalize(section) == value or (normalize(section) == 'abstract' and value.startswith('abstract-')) for value in sections):
            continue
        if any(wanted and not exact_tag_match(wanted, entry.get(field, ''), {}) for field, wanted in [('function', function), ('unit_type', unit), ('evidence_tier', evidence_tier)]):
            continue
        if domain and not exact_tag_match(domain, entry.get('expression_domains', entry.get('domain', '')), vocabulary.get('domains', {})):
            continue
        if article_domain and not exact_tag_match(article_domain, entry.get('article_domains', entry.get('domain', '')), vocabulary.get('domains', {})):
            continue
        searchable = json.dumps([entry['expression'], entry.get('usage_constraint', ''), entry['usage_cards']], ensure_ascii=False).casefold()
        if not query_matches(searchable, clauses):
            continue
        score = sum(query_matches(entry['expression'], [clause]) for clause in clauses) * 3 + int(entry['provenance_granularity'] == 'single-paper-synthesis')
        visible = {key: value for key, value in entry.items() if not key.startswith('_')}
        result.append((score, {**visible, 'matching_source_pmids': [article['pmid'] for article in matching_sources]}))
    result.sort(key=lambda pair: (-pair[0], pair[1]['stable_id']))
    return {'matched_count': len(result), 'entries': [entry for _, entry in result[:limit]]}


def main():
    parser = argparse.ArgumentParser(description='Retrieve source-linked language; held expressions are excluded unless auditing.')
    parser.add_argument('--skill-path', type=Path, default=Path(__file__).resolve().parents[1])
    for option in ('query', 'journal', 'year', 'section', 'function', 'domain', 'article-domain', 'disease', 'tissue', 'model', 'source-role', 'unit', 'evidence-tier', 'pmid', 'entry-id'):
        parser.add_argument('--' + option, default='')
    for option in ('highlight', 'single-paper', 'reviewed', 'include-held', 'include-subtypes', 'pdf-located'):
        parser.add_argument('--' + option, action='store_true')
    parser.add_argument('--purpose', choices=('writing', 'audit'), default='writing')
    parser.add_argument('--limit', type=int, default=10)
    arguments = parser.parse_args()
    if arguments.include_held and arguments.purpose != 'audit':
        parser.error('--include-held requires --purpose audit; held entries are not writing recommendations')
    entries, manifest = load_index(arguments.skill_path)
    options = vars(arguments).copy()
    options.pop('skill_path')
    options.pop('purpose')
    result = search(entries, **options)
    migrations = read_json(reference_path(arguments.skill_path, 'language-id-migrations.json'))['migrations']
    result['retired_entry'] = next((migration for migration in migrations if migration['retired_id'] == arguments.entry_id), None)
    result.update(index_version=manifest['index_version'], purpose=arguments.purpose,
                  boundary='Synthetic language, not quotations or verified study findings. Review source_alerts and usage constraints; source acceptance is reported separately.')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
