from datetime import date

from library_common import read_json, reference_path


METHODS = {'same_agent_source_recheck', 'independent_agent_source_recheck', 'human_source_recheck'}


def load_context_rechecks(skill, pdf_sources):
    data = read_json(reference_path(skill, 'source-context-rechecks.json'))
    if data['schema_version'] != 1:
        raise ValueError('Unsupported source-context recheck schema')
    records = {}
    for record in data['entries']:
        identifier = record['stable_id']
        if identifier in records:
            raise ValueError('Duplicate context-rechecked entry')
        source = pdf_sources.get(record['pmid'])
        if not source or record['sha256'] != source['sha256']:
            raise ValueError('Context recheck PDF hash mismatch')
        if record['review_method'] not in METHODS or not record['reviewer_id'] or not record['reviewed_on']:
            raise ValueError('Context recheck lacks reviewer provenance')
        date.fromisoformat(record['reviewed_on'])
        if record['page_numbering'] != 'one-based physical PDF page':
            raise ValueError('Context recheck page numbering is ambiguous')
        pages = record['physical_pages']
        if not pages or any(type(page) is not int or not 1 <= page <= source['physical_pages'] for page in pages):
            raise ValueError('Context recheck page out of bounds')
        if record['quotation_verified'] is not False or not record['support']:
            raise ValueError('Context support is not a quotation verification')
        reference_path(skill, record['review_record'])
        records[identifier] = record
    return records


def attach_context_recheck(entry, records):
    record = records.get(entry['stable_id'])
    entry['source_context_rechecks'] = []
    if record is None:
        return
    if record['pmid'] not in entry['source_article_ids'].split(';') or record['expression'] != entry['expression']:
        raise ValueError('Context recheck expression/source mismatch')
    entry['source_context_rechecks'] = [record]
