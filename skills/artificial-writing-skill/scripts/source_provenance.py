import re

from library_common import file_hash, read_csv, read_json, reference_path


FACETS = {'disease_ids': 'diseases', 'tissue_ids': 'tissues', 'model_ids': 'models', 'use_roles': 'roles'}


def registered_hashes(value):
    return {part.strip().casefold() for part in re.split(r'[;|]', value) if part.strip()}


def load_scope_annotations(skill, vocabulary):
    references = skill / 'references'
    original = read_json(references / 'retrieval-annotations.json')['articles']
    backfill = read_json(references / 'source-scope-backfill.json')['articles']
    if set(original).intersection(backfill):
        raise ValueError('Duplicate source-scope annotation across registers')
    annotations = {**original, **backfill}
    versions = {row['pmid']: row for row in read_csv(references / 'source-version-register.csv')}
    for pmid, annotation in annotations.items():
        path = reference_path(skill, annotation['source_reference'])
        if annotation.get('source_reference_line') is not None:
            number = annotation['source_reference_line']
            if type(number) is not int or not 1 <= number <= len(path.read_text(encoding='utf-8-sig').splitlines()):
                raise ValueError(f'Invalid source-scope reference line: {pmid}')
        for field, group in FACETS.items():
            if not set(annotation.get(field, [])).issubset(vocabulary[group]):
                raise ValueError(f'Unknown source-scope tag: {pmid}/{field}')
        digest = annotation.get('source_sha256')
        if digest and digest not in registered_hashes(versions.get(pmid, {}).get('sha256', '')):
            raise ValueError(f'Source-scope PDF hash mismatch: {pmid}')
    return annotations


def load_pdf_locators(skill):
    data = read_json(reference_path(skill, 'source-pdf-locators.json'))
    if data['schema_version'] != 1 or data['page_numbering'] != 'one-based physical PDF page':
        raise ValueError('Unsupported PDF locator schema or page numbering')
    versions = {row['pmid']: row for row in read_csv(skill / 'references/source-version-register.csv')}
    for pmid, source in data['sources'].items():
        if source['sha256'] not in registered_hashes(versions.get(pmid, {}).get('sha256', '')):
            raise ValueError(f'PDF locator registered hash mismatch: {pmid}')
        if source['supplied_pdf_version'] != versions[pmid]['supplied_pdf_version']:
            raise ValueError(f'PDF locator version mismatch: {pmid}')
        if type(source['physical_pages']) is not int or source['physical_pages'] < 1:
            raise ValueError(f'Invalid PDF page count: {pmid}')
        if '/' in source['filename'] or '\\' in source['filename']:
            raise ValueError(f'PDF locator must not export local archive paths: {pmid}')
    for name, expected in data['source_asset_hashes'].items():
        if file_hash(reference_path(skill, name)) != expected:
            raise ValueError(f'Stale PDF locator asset: {name}; regenerate PDF locators')
    return data


def attach_pdf_locator(entry, data):
    record = data['entries'].get(entry['stable_id'])
    if record is None:
        entry['source_locator'].update(state='not-yet-located', pdf_text_match_verified=False,
                                       literal_matches=[], recorded_page_hints=[], quotation_verified=False)
        return
    if record['expression'] != entry['expression'] or record['source_article_ids'] != entry['source_article_ids']:
        raise ValueError(f'Stale PDF locator identity: {entry["stable_id"]}')
    identifiers = set(entry['source_article_ids'].split(';'))
    if not identifiers.issubset(data['sources']):
        raise ValueError('PDF locator source metadata missing')
    conventional = entry['unit_type'].replace('_', '-') in {'vocabulary', 'collocation'}
    if record['quotation_verified'] is not False or (not conventional and record['literal_matches']):
        raise ValueError('PDF locator must not certify quotations or locate synthetic frames verbatim')
    matched = set()
    for match in record['literal_matches']:
        pmid = match['pmid']
        if pmid not in identifiers or pmid in matched:
            raise ValueError('PDF locator has a wrong or duplicate source PMID')
        matched.add(pmid)
        source = data['sources'][pmid]
        if match['sha256'] != source['sha256']:
            raise ValueError('PDF locator match hash mismatch')
        if match['method'] != 'normalized-literal-text-search' or match['visual_check'] is not False:
            raise ValueError('Unsupported PDF locator verification method')
        pages = match['physical_pages']
        if not pages or any(type(page) is not int or not 1 <= page <= source['physical_pages'] for page in pages):
            raise ValueError('PDF locator match page out of bounds')
    if set(record['unmatched_source_pmids']) != identifiers - matched:
        raise ValueError('Inconsistent unmatched PDF source set')
    expected_state = 'pdf-text-located' if matched else ('no-literal-match-needs-context-review' if conventional else 'synthetic-not-a-verbatim-quotation')
    if record['state'] != expected_state:
        raise ValueError('Inconsistent PDF locator state')
    for hint in record['recorded_page_hints']:
        if hint['pmid'] not in identifiers or len(identifiers) != 1:
            raise ValueError('Ambiguous recorded PDF page hint')
        pages = hint['recorded_pages']
        if hint['page_numbering'] != 'unverified-reading-note-numbering':
            raise ValueError('Recorded PDF page hint numbering wrongly certified')
        if not pages or any(type(page) is not int for page in pages):
            raise ValueError('Invalid recorded PDF page hint')
        in_range = all(1 <= page <= data['sources'][hint['pmid']]['physical_pages'] for page in pages)
        expected = 'reading-note-page-hint-not-rechecked' if in_range else 'out-of-range-recorded-hint'
        if hint['state'] != expected:
            raise ValueError('Recorded PDF page hint wrongly upgraded')
    locator = entry['source_locator']
    locator.update({key: value for key, value in record.items() if key not in {'expression', 'source_article_ids'}})
    locator.update(pdf_text_match_verified=bool(matched), original_pdf_location_verified=False,
                   page_numbering=data['page_numbering'])
    if matched:
        locator['precision'] = 'pdf-text-match'
