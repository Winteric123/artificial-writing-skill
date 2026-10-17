import csv
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / 'references'
EXPECTED = {
    '31548347': ('Clinical Cancer Research', '2020', 'author_manuscript', 19),
    '32102950': ('Clinical Cancer Research', '2020', 'author_manuscript', 15),
    '33323401': ('Clinical Cancer Research', '2021', 'publisher_typeset_pdf', 10),
    '35504291': ('Cell Metabolism', '2022', 'publisher_typeset_main_with_embedded_supplement', 35),
}


def rows(name):
    with (REF / name).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def resource(name):
    return json.loads((REF / name).read_text(encoding='utf-8-sig'))


class DesktopOctober18Intake(unittest.TestCase):
    def test_actual_identity_versions_and_reading_scope(self):
        library = {row['pmid']: row for row in rows('library-index.csv')}
        versions = {row['pmid']: row for row in rows('source-version-register.csv')}
        locators = resource('source-pdf-locators.json')['sources']
        ccr_quality = {row['pmid']: row for row in rows('ccr-reading-quality-register.csv')}
        cmet_quality = {row['pmid']: row for row in rows('cell-metabolism-reading-quality-register.csv')}
        for pmid, (journal, year, version, pages) in EXPECTED.items():
            with self.subTest(pmid=pmid):
                article = library[pmid]
                self.assertEqual(article['journal'], journal)
                self.assertEqual(article['year'], year)
                self.assertEqual(article['supplied_pdf_version'], version)
                self.assertEqual(article['reading_stage'], 'main_text_deep_read_complete')
                self.assertEqual(article['main_read_completed_on'], '2026-10-18')
                self.assertEqual(article['review_status'], 'not_reviewed')
                self.assertEqual(article['stk11_highlight'], 'no')
                self.assertEqual(versions[pmid]['sha256'], locators[pmid]['sha256'])
                self.assertEqual(locators[pmid]['physical_pages'], pages)
                self.assertEqual(versions[pmid]['supplied_pdf_version'], version)
                quality = (cmet_quality if pmid == '35504291' else ccr_quality)[pmid]
                for gate in ('coverage', 'evidence', 'results', 'language', 'traceability', 'transfer'):
                    self.assertEqual(quality[gate + '_check'], 'pending')
                self.assertEqual(article['supplement_status'], 'partially_reviewed' if pmid == '35504291' else 'not_supplied')

    def test_sentence_provenance_and_synthetic_transfer(self):
        catalog = resource('supplement-ccr-2026-10-18-sentence-patterns.json')
        papers = {row['pmid']: row for row in catalog['papers']}
        records = catalog['records']
        self.assertEqual(set(papers), set(EXPECTED))
        self.assertEqual(len(records), 34)
        self.assertEqual(Counter(row['pmid'] for row in records), {'31548347': 10, '32102950': 8, '33323401': 12, '35504291': 4})
        self.assertEqual(len({row['id'] for row in records}), 34)
        for row in records:
            with self.subTest(record=row['id']):
                source = row['source']
                paper = papers[row['pmid']]
                self.assertEqual(source['pdf_sha256'], paper['sha256'])
                self.assertEqual(source['supplied_pdf_version'], paper['version'])
                self.assertTrue(source['source_sentence'])
                self.assertTrue(source['visual_verified'])
                self.assertIn(source['text_extraction_match'], {'normalized_literal', 'punctuation_insensitive', 'cross_page_fragments_normalized_literal'})
                self.assertTrue(all(1 <= page <= paper['physical_pages'] for page in source['physical_pages']))
                self.assertTrue(source['physical_pages'])
                self.assertTrue((REF / source['verification_record']).is_file())
                for field in ('content_type', 'use_scenario', 'rewrite_template', 'evidence_boundary'):
                    self.assertTrue(row[field], field)
                self.assertIn('[', row['rewrite_template'])

    def test_each_article_has_full_section_language_and_visible_alert(self):
        ccr = rows('ccr-section-language-catalog.csv')
        cmet = rows('cell-metabolism-section-language-catalog.csv')
        controls = resource('language-controls.json')
        required = {'introduction', 'methods', 'results', 'discussion', 'conclusion'}
        for pmid in EXPECTED:
            entries = [row for row in (cmet if pmid == '35504291' else ccr) if row['source_article_ids'] == pmid]
            self.assertTrue(required <= {row['primary_section'] for row in entries}, pmid)
            self.assertTrue({'vocabulary', 'sentence-frame', 'paragraph-model'} <= {row['unit_type'] for row in entries}, pmid)
            self.assertTrue(any(pmid in row['article_ids'] for row in controls['article_alerts']), pmid)

    def test_per_article_note_hashes_and_scientific_boundaries(self):
        annotations = resource('coalteration-annotations.json')['articles']
        for pmid in EXPECTED:
            for evidence in annotations[pmid]['evidence']:
                note = REF / evidence['source']
                self.assertEqual(hashlib.sha256(note.read_bytes()).hexdigest(), evidence['source_sha256'])
        guide = (REF / 'supplement-ccr-2026-10-18-intake.md').read_text(encoding='utf-8')
        for marker in ('TTF', 'OR1.09', 'P=.69', 'P=.010', 'unmeasured', 'Data S1', 'not a separate four-article six-gate acceptance pass'):
            self.assertIn(marker, guide)
        cmet = (REF / 'cell-metabolism-2022-35504291-language.md').read_text(encoding='utf-8')
        self.assertNotIn('tracer flux', cmet)
        self.assertNotIn('schedule-dependent combination effect', cmet)
        self.assertIn('isotopic labeling', cmet)


if __name__ == '__main__':
    unittest.main()
