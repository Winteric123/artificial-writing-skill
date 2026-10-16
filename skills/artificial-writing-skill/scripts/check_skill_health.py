import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

sys.dont_write_bytecode = True

from library_common import journal_registry, read_csv, read_json
from search_language import load_index
from search_ccr_results_logic import load_catalog as load_ccr_results_logic_catalog
from search_stk11_sentence_templates import load_catalog
from validate_reading_quality import validate


def check_links(skill):
    broken = []
    external_local = []
    checked = 0
    documents = [skill / 'SKILL.md', *sorted((skill / 'references').rglob('*.md')), *sorted((skill / 'assets').rglob('*.md'))]
    for path in documents:
        for raw in re.findall(r'\]\(([^)\n]+)\)', path.read_text(encoding='utf-8-sig')):
            target = unquote(raw.split('#', 1)[0])
            if not target or target.startswith(('https:', 'http:', 'mailto:', 'data:')):
                continue
            source = path.relative_to(skill).as_posix()
            if re.match(r'^[a-zA-Z]:[\\/]', target) or target.startswith(('file:', '/', '\\')):
                external_local.append(dict(source=source, target=target))
                continue
            destination = (path.parent / target).resolve()
            if not destination.is_relative_to(skill) or not destination.exists():
                broken.append(dict(source=source, target=target))
            checked += 1
    return dict(checked=checked, broken=broken, external_local=external_local)


def check_inventory(skill):
    library = {row['pmid']: row for row in read_csv(skill / 'references/library-index.csv')}
    authoritative = {}
    for configuration in journal_registry(skill).values():
        bibliography = {row['pmid']: row for row in read_csv(skill / 'references' / configuration['bibliography'])}
        for record in read_csv(skill / 'references' / configuration['quality']):
            identifier = record['pmid']
            authoritative[identifier] = {**bibliography[identifier], **record}
    errors = []
    if library.keys() != authoritative.keys():
        errors.append('Library membership differs from authoritative journal records')
    for identifier in library.keys() & authoritative.keys():
        for field in ('title', 'year', 'journal', 'eligibility', 'reading_stage', 'review_status', 'supplement_status'):
            if library[identifier][field] != authoritative[identifier][field]:
                errors.append(f'{identifier}: stale {field}')
    included = [row for row in authoritative.values() if row['eligibility'] == 'included']
    complete = sum(row['reading_stage'] == 'main_text_deep_read_complete' for row in included)
    passed = sum(row['review_status'] == 'passed' for row in included)
    expected = dict(registered=len(authoritative), included=len(included), excluded=len(authoritative) - len(included), main_text_complete=complete, eligible_incomplete=len(included) - complete, source_recheck_passed=passed,
                    stk11_highlights=sum(row['stk11_highlight'] == 'yes' for row in library.values()))
    summary = read_json(skill / 'references/library-summary.json')
    for field, value in expected.items():
        if summary[field] != value:
            errors.append(f'Stale summary: {field}')
    return dict(counts=expected, errors=errors)


def check_project_membership(skill):
    references = skill / 'references'
    mapping = read_json(references / 'stk11-writing-reference-map.json')
    records = mapping.get('records', [])
    identifiers = [record['pmid'] for record in records]
    library = {row['pmid']: row for row in read_csv(references / 'library-index.csv')}
    highlights = {identifier for identifier, row in library.items() if row['stk11_highlight'] == 'yes'}
    core = {record['pmid'] for record in records if record['tier'] == 'core_highlight'}
    support = {record['pmid'] for record in records if record['tier'] == 'topic_support'}
    errors = []
    if mapping.get('schema_version') != 2 or mapping.get('collection_id') != 'stk11_highlight':
        errors.append('Unsupported STK11 highlight membership schema')
    if mapping.get('membership_rule') != 'all_records' or not mapping.get('membership_semantics') or not mapping.get('tier_semantics'):
        errors.append('Incomplete STK11 highlight membership semantics')
    if len(identifiers) != len(set(identifiers)):
        errors.append('Duplicate project PMID')
    if set(identifiers) != highlights:
        errors.append('Unified project membership differs from authoritative highlight membership')
    actual_tier_counts = {'core_highlight': len(core), 'topic_support': len(support)}
    if mapping.get('legacy_tier_counts') != actual_tier_counts:
        errors.append('Historical STK11 highlight tier counts changed')
    for record in records:
        identifier = record['pmid']
        if identifier not in library or library[identifier]['eligibility'] != 'included':
            errors.append(f'{identifier}: project source is absent or excluded')
        if record['tier'] not in ('core_highlight', 'topic_support'):
            errors.append(f'{identifier}: unknown project tier')
        for relative in record['source_refs']:
            path = (references / relative).resolve()
            if not path.is_relative_to(references.resolve()) or not path.is_file():
                errors.append(f'{identifier}: invalid evidence path {relative}')
            elif identifier not in path.read_text(encoding='utf-8-sig'):
                errors.append(f'{identifier}: evidence does not identify PMID')
    return dict(unique_articles=len(set(identifiers)), highlights=len(highlights), legacy_core=len(core), legacy_support=len(support), core=len(core), support=len(support), errors=errors)


def check_sentence_templates(skill):
    try:
        catalog = load_catalog(skill)
    except (ValueError, KeyError, OSError) as error:
        return dict(errors=[str(error)])
    records = catalog['records']
    return dict(
        records=len(records), papers=len({record['pmid'] for record in records}),
        body_methods=sum(record['source']['section'] == 'methods' for record in records),
        body_results=sum(record['source']['section'] == 'results' for record in records),
        fulltext_coverage=catalog['project_scope'].get('fulltext_coverage', {}).get('coverage_complete', False),
        errors=[],
    )


def check_ccr_results_logic(skill):
    try:
        catalog = load_ccr_results_logic_catalog(skill)
    except (ValueError, KeyError, OSError) as error:
        return dict(errors=[str(error)])
    records = catalog['records']
    papers = catalog['papers']
    return dict(
        records=len(records), papers=len(papers),
        year_2025=sum(paper['year'] == '2025' for paper in papers),
        year_2026=sum(paper['year'] == '2026' for paper in papers),
        positive=sum(record['result_polarity'] == 'positive' for record in records),
        negative=sum(record['result_polarity'] == 'negative' for record in records),
        mixed=sum(record['result_polarity'] == 'mixed' for record in records),
        inconclusive=sum(record['result_polarity'] == 'inconclusive' for record in records),
        descriptive=sum(record['result_polarity'] == 'descriptive' for record in records),
        errors=[],
    )


def check(skill):
    skill = skill.resolve()
    reading = validate(skill)
    entries, manifest = load_index(skill)
    links = check_links(skill)
    inventory = check_inventory(skill)
    project = check_project_membership(skill)
    sentences = check_sentence_templates(skill)
    ccr_results_logic = check_ccr_results_logic(skill)
    failures = (links['broken'] or inventory['errors'] or project['errors']
                or sentences['errors'] or ccr_results_logic['errors'])
    return dict(status='failed' if failures else 'mechanical_checks_passed', scientific_acceptance_certified=False, behavioral_evaluation_performed=False, reading_validation=reading['validation'], inventory=inventory, project=project, sentence_templates=sentences, ccr_results_logic=ccr_results_logic, links=links, language_entries=len(entries), index_version=manifest['index_version'], boundary='Read-only structural/integrity checks. No PDF rereading, scientific acceptance, language-generation evaluation or Wisp live verification is performed.')


def main():
    parser = argparse.ArgumentParser(description='Read-only skill integrity audit; does not certify scientific or writing quality.')
    parser.add_argument('--skill-path', type=Path, default=Path(__file__).resolve().parents[1])
    arguments = parser.parse_args()
    try:
        result = check(arguments.skill_path)
    except (ValueError, KeyError, OSError) as error:
        result = dict(status='failed', error=str(error), scientific_acceptance_certified=False, behavioral_evaluation_performed=False)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['status'] == 'mechanical_checks_passed' else 1


if __name__ == '__main__':
    raise SystemExit(main())
