import argparse
import csv
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path


GATES = (
    'coverage_check', 'evidence_check', 'results_check',
    'language_check', 'traceability_check', 'transfer_check',
)
FIELDS = (
    'pmid', 'year', 'title', 'eligibility', 'reading_stage',
    'main_read_completed_on', 'review_status', *GATES,
    'supplement_status', 'reading_evidence', 'review_record',
    'reviewer_id', 'review_method', 'reviewed_on', 'note',
)
JOURNALS = {
    'ccr': ('ccr-corpus-bibliography.csv', 'ccr-deep-reading-ledger.md'),
    'jto': ('jto-stk11-priority-bibliography.csv', 'jto-stk11-deep-reading-ledger.md'),
}
METHODS = {'same_agent_source_recheck', 'independent_agent_source_recheck', 'human_source_recheck'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_rows(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def check_path(references, value, label):
    relative = Path(value.split('#', 1)[0])
    require(bool(value) and not relative.is_absolute(), f'{label}: expected relative file path')
    resolved = (references / relative).resolve()
    require(resolved.is_relative_to(references.resolve()), f'{label}: path escapes references')
    require(resolved.is_file() and resolved.stat().st_size > 0, f'{label}: missing or empty file {value}')


def validate(skill_path):
    references = skill_path / 'references'
    summary = {}
    for journal, (bibliography_name, ledger_name) in JOURNALS.items():
        bibliography_rows = read_rows(references / bibliography_name)
        bibliography = {row['pmid']: row for row in bibliography_rows}
        require(len(bibliography) == len(bibliography_rows), f'{journal}: duplicate bibliography PMID')
        ledger_text = (references / ledger_name).read_text(encoding='utf-8-sig')
        matches = re.findall(r'^\| (\d{8}) \| (\d{4}-\d{2}-\d{2}) \|', ledger_text, re.M)
        completed = dict(matches)
        require(len(matches) == len(completed), f'{journal}: duplicate completed PMID')
        require(set(completed) <= set(bibliography), f'{journal}: unindexed completed PMID')
        rows = read_rows(references / f'{journal}-reading-quality-register.csv')
        require(len(rows) == len(bibliography), f'{journal}: register/bibliography count mismatch')
        require({row.get('pmid') for row in rows} == set(bibliography), f'{journal}: register PMID mismatch')
        for row in rows:
            label = f"{journal}/{row['pmid']}"
            require(set(row) == set(FIELDS) and all(value is not None for value in row.values()), f'{label}: malformed fields')
            source = bibliography[row['pmid']]
            require(row['year'] == source['year'] and row['title'] == source['title'], f'{label}: identity mismatch')
            require(row['eligibility'] in {'included', 'excluded'}, f'{label}: invalid eligibility')
            if journal == 'ccr':
                excluded = source['corpus_genre_status'].startswith('excluded_')
                require((row['eligibility'] == 'excluded') == excluded, f'{label}: genre boundary mismatch')
            require(row['reading_stage'] in {'indexed', 'screened', 'main_text_deep_read_complete'}, f'{label}: invalid stage')
            is_complete = row['reading_stage'] == 'main_text_deep_read_complete'
            require(is_complete == (row['pmid'] in completed), f'{label}: reading ledger mismatch')
            require(row['main_read_completed_on'] == completed.get(row['pmid'], ''), f'{label}: completion date mismatch')
            if row['main_read_completed_on']:
                date.fromisoformat(row['main_read_completed_on'])
            require(row['review_status'] in {'not_reviewed', 'in_progress', 'needs_correction', 'passed'}, f'{label}: invalid review status')
            require(all(row[gate] in {'pending', 'not_reaudited', 'pass', 'fail'} for gate in GATES), f'{label}: invalid gate')
            require(is_complete or all(row[gate] != 'not_reaudited' for gate in GATES), f'{label}: inherited gate without completed reading')
            require(row['supplement_status'] in {'not_recorded', 'not_supplied', 'supplied_unread', 'partially_reviewed', 'reviewed'}, f'{label}: invalid supplement status')
            require(bool(row['reading_evidence']), f'{label}: no reading-evidence reference')
            for evidence in row['reading_evidence'].split(';'):
                check_path(references, evidence, label)
            if row['review_record']:
                check_path(references, row['review_record'], label)
            if row['review_method']:
                require(row['review_method'] in METHODS, f'{label}: invalid review method')
            if row['reviewed_on']:
                date.fromisoformat(row['reviewed_on'])
                require(row['review_status'] != 'not_reviewed', f'{label}: review date without review')
            if row['eligibility'] == 'excluded':
                require(not is_complete and row['review_status'] != 'passed', f'{label}: excluded record promoted')
            if row['review_status'] == 'passed':
                require(is_complete, f'{label}: review passed before reading completion')
                require(all(row[gate] == 'pass' for gate in GATES), f'{label}: review passed with unpassed gate')
                require(all(row[field].strip() for field in ('review_record', 'reviewer_id', 'review_method', 'reviewed_on')), f'{label}: missing review evidence')
                require(date.fromisoformat(row['reviewed_on']) >= date.fromisoformat(row['main_read_completed_on']), f'{label}: review predates main read')
        summary[journal] = {
            'registered': len(rows),
            'main_text_complete': len(completed),
            'reading_stages': dict(Counter(row['reading_stage'] for row in rows)),
            'review_statuses': dict(Counter(row['review_status'] for row in rows)),
            'excluded_legacy_records': sum(row['eligibility'] == 'excluded' for row in rows),
        }
    return {'validation': 'mechanical_checks_passed', 'scientific_acceptance_certified_by_script': False, 'journals': summary}


def main():
    parser = argparse.ArgumentParser(description='Validate reading-quality register consistency; not scientific correctness.')
    parser.add_argument('--skill-path', type=Path, default=Path(__file__).resolve().parents[1])
    arguments = parser.parse_args()
    try:
        result = validate(arguments.skill_path)
    except (ValueError, KeyError, OSError) as error:
        parser.exit(1, f'Validation failed: {error}\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
