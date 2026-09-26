import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True

from library_common import atomic_json, file_hash, journal_registry, read_csv, read_json, reference_path
from build_language_index import markdown_entries, stable_id
from retrieval_metadata import expression_metadata
from validate_reading_quality import validate


def normalized_text(text):
    text = unicodedata.normalize('NFKC', text).casefold().replace('\u00ad', '')
    text = re.sub(r'(?<=\w)-\s*\n\s*(?=\w)', '', text)
    text = text.translate(str.maketrans({'–': '-', '—': '-', '−': '-', '‑': '-'}))
    return re.sub(r'\s+', ' ', text).strip()


def literal_occurrence(expression, text):
    pattern = literal_pattern(expression)
    return bool(pattern and pattern.search(normalized_text(text)))


def literal_pattern(expression):
    needle = normalized_text(expression)
    if not needle or '[' in needle or ']' in needle:
        return None
    return re.compile(r'(?<!\w)' + re.escape(needle) + r'(?!\w)')


def page_hints(text):
    pages = set()
    for match in re.finditer(r'(?i)(?<![a-z])(?:pp?\.?|physical\s+pages?)\s*(\d+(?:\s*[-–—]\s*\d+)?(?:\s*,\s*\d+(?:\s*[-–—]\s*\d+)?)*)', text):
        for part in match[1].split(','):
            numbers = [int(number) for number in re.findall(r'\d+', part)]
            if len(numbers) == 1:
                pages.add(numbers[0])
            elif numbers[0] <= numbers[1] and numbers[1] - numbers[0] < 100:
                pages.update(range(numbers[0], numbers[1] + 1))
    return sorted(pages)


def main_text_pages(pages):
    references_started = False
    result = []
    for text in pages:
        reference = re.search(r'(?im)^\s*(?:references|bibliography|literature cited)\s*$', text)
        figure = re.search(r'(?im)^\s*(?:figure|table)\s*\d+[.:\s]', text)
        if reference and not references_started:
            result.append(text[:reference.start()])
            references_started = True
        elif references_started:
            result.append(text[figure.start():] if figure else '')
        else:
            result.append(text)
    return result


def locate_entry(entry, sources, texts, lines, texts_normalized=False):
    hints = []
    if len(entry['source_article_ids'].split(';')) == 1:
        hints = page_hints(lines[int(entry['source_line']) - 1])
        if not hints:
            hints = page_hints(entry.get('source_locator', {}).get('context', ''))
    unit = entry['unit_type'].replace('_', '-')
    conventional = unit in {'vocabulary', 'collocation'}
    pattern = literal_pattern(entry['expression']) if conventional else None
    matches = []
    recorded = []
    unmatched = []
    for pmid in entry['source_article_ids'].split(';'):
        source = sources[pmid]
        if any(page < 1 or page > source['physical_pages'] for page in hints):
            recorded.append({'pmid': pmid, 'state': 'out-of-range-recorded-hint', 'recorded_pages': hints, 'page_numbering': 'unverified-reading-note-numbering'})
        elif hints:
            recorded.append({'pmid': pmid, 'state': 'reading-note-page-hint-not-rechecked', 'recorded_pages': hints, 'page_numbering': 'unverified-reading-note-numbering'})
        found = [number + 1 for number, text in enumerate(texts[pmid]) if pattern and pattern.search(text if texts_normalized else normalized_text(text))]
        if found:
            matches.append({'pmid': pmid, 'sha256': source['sha256'], 'physical_pages': found, 'method': 'normalized-literal-text-search', 'visual_check': False})
        else:
            unmatched.append(pmid)
    state = 'pdf-text-located' if matches else ('synthetic-not-a-verbatim-quotation' if not conventional else 'no-literal-match-needs-context-review')
    return {'expression': entry['expression'], 'source_article_ids': entry['source_article_ids'], 'state': state,
            'literal_matches': matches, 'recorded_page_hints': recorded, 'unmatched_source_pmids': unmatched,
            'quotation_verified': False,
            'boundary': 'Literal matches use one-based physical PDF pages, not printed journal pages. They are mechanically located wording, not semantic verification or quotation authorization. Reading-note page numbering is unverified and is not a PDF anchor. Synthetic frames have no required verbatim counterpart.'}


def build(skill, inventory_path):
    import pymupdf

    validate(skill)
    references = skill / 'references'
    vocabulary = read_json(references / 'retrieval-vocabulary.json')
    raw_entries, assets = [], {}
    for journal, configuration in journal_registry(skill).items():
        name = configuration.get('language_catalog') or configuration.get('language_markdown')
        if not name:
            continue
        path = reference_path(skill, name)
        rows = read_csv(path) if configuration.get('language_catalog') else list(markdown_entries(path))
        for row in rows:
            asset = row['source_asset']
            if asset not in assets:
                assets[asset] = reference_path(skill, asset).read_text(encoding='utf-8-sig').splitlines()
            number = int(row['source_line'])
            if not 1 <= number <= len(assets[asset]) or row['expression'] not in assets[asset][number - 1]:
                raise ValueError(f'Stale source expression line: {asset}/{number}')
            raw_entries.append({**row, **expression_metadata(row, assets[asset], vocabulary), 'stable_id': stable_id(journal, row)})
    inventory = {row['pmid']: row for row in read_json(inventory_path)}
    versions = {row['pmid']: row for row in read_csv(references / 'source-version-register.csv')}
    sources, texts = {}, {}
    for pmid in sorted({identifier for entry in raw_entries for identifier in entry['source_article_ids'].split(';')}):
        row = inventory[pmid]
        path = Path(row['selected']['path'])
        digest = file_hash(path)
        allowed = {value.strip().casefold() for value in re.split(r'[;|]', versions[pmid]['sha256'])}
        if digest not in allowed or digest != row['selected']['sha256']:
            raise ValueError(f'PDF version/hash mismatch: PMID {pmid}')
        with pymupdf.open(path) as document:
            pages = [page.get_text(sort=True) for page in document]
        sources[pmid] = {'filename': path.name, 'sha256': digest, 'physical_pages': len(pages), 'supplied_pdf_version': versions[pmid]['supplied_pdf_version'], 'identity_check': 'registered-sha256-match'}
        texts[pmid] = [normalized_text(text) for text in main_text_pages(pages)]
    entries = {}
    for entry in raw_entries:
        name = entry['source_asset']
        if entry['stable_id'] in entries:
            raise ValueError('Duplicate language identity during PDF location')
        entries[entry['stable_id']] = locate_entry(entry, sources, texts, assets[name], texts_normalized=True)
    output = {'schema_version': 1, 'page_numbering': 'one-based physical PDF page', 'scope': 'All current language entries; automatic normalized literal matching for conventional terms/collocations only. No new reading/acceptance or semantic quotation checks.',
              'sources': sources, 'entries': entries, 'states': dict(Counter(entry['state'] for entry in entries.values())),
              'source_asset_hashes': {name: file_hash(references / name) for name in sorted(assets)}}
    atomic_json(references / 'source-pdf-locators.json', output)
    return {'source_pdfs': len(sources), 'entries': len(entries), 'states': output['states'], 'entries_with_recorded_page_hints': sum(bool(entry['recorded_page_hints']) for entry in entries.values())}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reopen hash-registered local PDFs and locate conventional language; never assign synthetic frames a guessed quotation page.')
    parser.add_argument('--skill-path', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--local-inventory', type=Path, required=True)
    arguments = parser.parse_args()
    print(json.dumps(build(arguments.skill_path, arguments.local_inventory), ensure_ascii=False, indent=2))
