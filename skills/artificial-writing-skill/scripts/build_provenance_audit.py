import argparse
import csv
import io
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

from library_common import atomic_json, atomic_text
from search_language import load_index


def write_queue(path, rows, fields):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
    atomic_text(path, '\ufeff' + stream.getvalue())


def build(skill):
    entries, manifest = load_index(skill)
    articles = {source['pmid']: source for entry in entries for source in entry['source_articles']}
    pending_scope = []
    for pmid, article in sorted(articles.items()):
        scope = article['source_scope']
        missing = [field for field, status in scope['facet_status'].items() if status == 'not-curated-not-absent']
        if missing:
            pending_scope.append(dict(pmid=pmid, year=article['year'], title=article['title'], missing_facets=';'.join(missing),
                                      source_reference=scope['source_reference'], state='not-curated-not-absent'))
    pending_language = []
    for entry in entries:
        locator = entry['source_locator']
        if locator['state'] not in {'no-literal-match-needs-context-review', 'not-yet-located'}:
            continue
        pending_language.append(dict(stable_id=entry['stable_id'], expression=entry['expression'],
                                     source_article_ids=entry['source_article_ids'], source_asset=entry['source_asset'],
                                     source_line=entry['source_line'], state=locator['state']))
    summary = {key: manifest[key] for key in ['index_version', 'entry_count', 'source_scope_status', 'source_facet_coverage',
                                            'pdf_locator_states', 'source_pdf_count', 'entries_with_recorded_page_hints']}
    summary.update(scope='Current language-source articles only; all registered journals and indexed years; no new reading or acceptance.',
                   source_articles=len(articles), articles_with_unknown_facets=len(pending_scope),
                   entries_needing_literal_context_review=len(pending_language),
                   boundary='Synthetic frames are excluded from the missing-literal queue; unknown tissue is not absent tissue.')
    references = skill / 'references'
    write_queue(references / 'source-scope-pending.csv', pending_scope,
                ['pmid', 'year', 'title', 'missing_facets', 'source_reference', 'state'])
    write_queue(references / 'source-locator-pending.csv', pending_language,
                ['stable_id', 'expression', 'source_article_ids', 'source_asset', 'source_line', 'state'])
    atomic_json(references / 'source-provenance-summary.json', summary)
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Report provenance coverage without upgrading any reading or quotation status.')
    parser.add_argument('--skill-path', type=Path, default=Path(__file__).resolve().parents[1])
    arguments = parser.parse_args()
    print(json.dumps(build(arguments.skill_path), ensure_ascii=False, indent=2))
