import csv
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / 'references'
sys.path.insert(0, str(ROOT / 'scripts'))
from build_language_index import markdown_entries, stable_id

PMIDS = {'36240971', '36494075', '36775193', '36958689', '37182602', '37543207',
         '37572870', '37806385', '37838086', '38096950', '38154514', '39111731',
         '39694414', '40320171', '40518016', '41161592', '41260457', '41903702', '42749051'}


def records(filename):
    with (REFERENCES / filename).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


class JtoSeptember28Intake(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = records('jto-2026-09-28-reading-manifest.csv')
        cls.library = {row['pmid']: row for row in records('library-index.csv')}
        cls.catalog = records('jto-section-language-catalog.csv')
        cls.queue = records('jto-maintenance-queue.csv')

    def test_batch_identity_completion_and_journal_boundaries(self):
        self.assertEqual({row['pmid'] for row in self.manifest}, PMIDS)
        self.assertEqual(len(self.manifest), 19)
        self.assertEqual(sum(int(row['physical_pages']) for row in self.manifest), 270)
        self.assertEqual(sum(int(row['new_language_entries']) for row in self.manifest), 513)
        ccr = {row['pmid'] for row in records('ccr-corpus-bibliography.csv')}
        self.assertFalse(PMIDS & ccr)
        for source in self.manifest:
            article = self.library[source['pmid']]
            self.assertEqual(article['journal'], 'Journal of Thoracic Oncology')
            self.assertEqual(article['title'], source['title'])
            self.assertEqual(article['reading_stage'], 'main_text_deep_read_complete')
            self.assertEqual(article['main_read_completed_on'], '2026-09-28')
            self.assertEqual(article['review_status'], 'not_reviewed')
            self.assertEqual(article['stk11_highlight'], 'no')
            self.assertEqual(article['official_category_status'], 'not_recorded_for_this_journal')

    def test_version_and_supplement_scope(self):
        versions = {row['pmid']: row for row in records('source-version-register.csv')}
        for source in self.manifest:
            self.assertEqual(source['sha256'], versions[source['pmid']]['sha256'])
            self.assertEqual(source['physical_pages'], versions[source['pmid']]['physical_pages'])
            self.assertEqual(source['supplement_status'], 'reviewed' if source['pmid'] == '41903702' else 'not_supplied')
        self.assertEqual(versions['36775193']['archived_pdf_count'], '2')
        self.assertEqual(versions['36775193']['physical_pages'], '13')
        self.assertIn('comparatively checked', versions['36775193']['scope'])
        self.assertEqual(versions['42749051']['supplied_pdf_version'], 'journal_preproof')

    def test_complete_sections_traceability_and_old_ids(self):
        required = {'abstract-background', 'abstract-methods', 'abstract-results', 'abstract-conclusion',
                    'introduction', 'methods', 'results', 'discussion', 'conclusion'}
        alerts = json.loads((REFERENCES / 'language-controls.json').read_text(encoding='utf-8'))['article_alerts']
        for source in self.manifest:
            entries = [row for row in self.catalog if row['source_article_ids'] == source['pmid']]
            self.assertEqual(len(entries), int(source['new_language_entries']))
            self.assertTrue(required <= {row['primary_section'] for row in entries}, source['pmid'])
            self.assertTrue({'vocabulary', 'sentence-frame', 'paragraph-model'} <= {row['unit_type'] for row in entries})
            self.assertTrue(any(source['pmid'] in alert['article_ids'] for alert in alerts))
            for entry in entries:
                lines = (REFERENCES / entry['source_asset']).read_text(encoding='utf-8').splitlines()
                self.assertIn(entry['expression'], lines[int(entry['source_line']) - 1])
        old_ids = {stable_id('jto', row) for row in markdown_entries(REFERENCES / 'jto-2026-09-14-stk11-priority-language.md')}
        self.assertTrue(old_ids <= {stable_id('jto', row) for row in self.catalog})

    def test_queue_is_not_a_completed_corpus(self):
        self.assertEqual(len(self.queue), len({row['pmid'] for row in self.queue}))
        self.assertEqual(len(self.queue), 137)
        self.assertEqual(sum(bool(row['local_pdf_sha256']) for row in self.queue), 24)
        self.assertEqual(sum(bool(row['main_read_completed_on']) for row in self.queue), 23)
        self.assertEqual(sum(row['group'] == 'R' for row in self.queue), 20)
        pending = {row['pmid'] for row in self.queue if row['local_pdf_sha256'] and not row['main_read_completed_on']}
        self.assertEqual(pending, {'37495171'})
        for row in self.queue:
            self.assertNotIn('\\', row['local_pdf_filename'])
            self.assertNotIn('/', row['local_pdf_filename'])
            if row['group'] == 'R':
                self.assertEqual(row['maintenance_scope'], 'background_only_not_original_language_learning')
                self.assertNotIn(row['pmid'], self.library)
            if row['pmid'] in self.library:
                self.assertEqual(row['reading_stage'], self.library[row['pmid']]['reading_stage'])
                self.assertEqual(row['review_status'], self.library[row['pmid']]['review_status'])
                self.assertEqual(row['stk11_highlight'], self.library[row['pmid']]['stk11_highlight'])


if __name__ == '__main__':
    unittest.main()
