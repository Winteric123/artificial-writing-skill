import argparse
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

from build_language_index import normalize
from library_common import file_hash, read_json, reference_path


def load_index(skill):
    manifest = read_json(reference_path(skill, 'language-index-manifest.json'))
    index_path = reference_path(skill, 'language-retrieval-index.json')
    if manifest['schema_version'] != 1 or file_hash(index_path) != manifest['index_file_sha256']:
        raise ValueError('Language index is incompatible or modified; rebuild before retrieval')
    for relative, expected in manifest['dependencies'].items():
        if file_hash(reference_path(skill, relative)) != expected:
            raise ValueError(f'Stale language index dependency: {relative}; run build_language_index.py')
    payload = read_json(index_path)
    for entry in payload['entries']:
        entry['source_articles'] = [payload['articles'][identifier] for identifier in entry['source_article_ids'].split(';')]
        entry['usage_cards'] = [payload['usage_cards'][identifier] for identifier in entry['usage_card_ids']]
        entry['source_alerts'] = [payload['article_alerts'][identifier] for identifier in entry['source_alert_ids']]
    return payload['entries'], manifest


def search(entries, *, query='', journal='', year='', section='', function='', domain='', unit='', evidence_tier='', pmid='', entry_id='', highlight=False, single_paper=False, reviewed=False, include_held=False, limit=10):
    if not 1 <= limit <= 100:
        raise ValueError('limit must be between 1 and 100')
    result = []
    tokens = re.findall(r'[^\s]+', query.casefold())
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
        matching_sources = [article for article in entry['source_articles'] if (not year or article['year'] == str(year)) and (not pmid or article['pmid'] == pmid) and (not highlight or article['highlight'])]
        if not matching_sources:
            continue
        sections = [entry['primary_section'], *entry['secondary_sections'].split(';')]
        if section and not any(normalize(section) == value or (normalize(section) == 'abstract' and value.startswith('abstract-')) for value in sections):
            continue
        if any(wanted and normalize(wanted) not in normalize(entry.get(field, '')) for field, wanted in [('function', function), ('domain', domain), ('unit_type', unit), ('evidence_tier', evidence_tier)]):
            continue
        searchable = json.dumps([entry['expression'], entry.get('usage_constraint', ''), entry['usage_cards']], ensure_ascii=False).casefold()
        if not all(token in searchable for token in tokens):
            continue
        score = sum(token in entry['expression'].casefold() for token in tokens) * 3 + int(entry['provenance_granularity'] == 'single-paper-synthesis')
        result.append((score, {**entry, 'matching_source_pmids': [article['pmid'] for article in matching_sources]}))
    result.sort(key=lambda pair: (-pair[0], pair[1]['stable_id']))
    return {'matched_count': len(result), 'entries': [entry for _, entry in result[:limit]]}


def main():
    parser = argparse.ArgumentParser(description='Retrieve source-linked language; held expressions are excluded unless auditing.')
    parser.add_argument('--skill-path', type=Path, default=Path(__file__).resolve().parents[1])
    for option in ('query', 'journal', 'year', 'section', 'function', 'domain', 'unit', 'evidence-tier', 'pmid', 'entry-id'):
        parser.add_argument('--' + option, default='')
    for option in ('highlight', 'single-paper', 'reviewed', 'include-held'):
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
