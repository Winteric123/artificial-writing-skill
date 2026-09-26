import csv
import json
import unittest
from pathlib import Path


REFERENCES = Path(__file__).resolve().parents[1] / 'references'


def records(filename):
    with (REFERENCES / filename).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


class Reading2024IntakeBoundaries(unittest.TestCase):
    def setUp(self):
        self.manifest = records('ccr-2024-and-intake-2026-09-23-reading-manifest.csv')
        self.quality = {row['pmid']: row for row in records('ccr-reading-quality-register.csv')}
        self.catalog = records('ccr-section-language-catalog.csv')

    def test_batch_scope_and_all_applicable_sections(self):
        self.assertEqual(len(self.manifest), 37)
        originals = [row for row in self.manifest if row['reading_stage'] == 'main_text_deep_read_complete']
        self.assertEqual(len(originals), 33)
        for article in originals:
            entries = [entry for entry in self.catalog if entry['source_asset'] == article['source_asset']]
            sections = {entry['primary_section'] for entry in entries}
            self.assertTrue({'introduction', 'methods', 'results', 'discussion', 'conclusion', 'translational-relevance'} <= sections, article['pmid'])
            self.assertTrue(any(section.startswith('abstract') for section in sections), article['pmid'])
            self.assertTrue({'vocabulary', 'sentence-frame', 'paragraph-model'} <= {entry['unit_type'] for entry in entries})
            self.assertEqual({entry['source_article_ids'] for entry in entries}, {article['pmid']})

    def test_background_reading_is_not_original_completion(self):
        expected = {'37903180', '37831007', '37955563', '39177967'}
        background = {row['pmid']: row for row in records('ccr-background-reading-register.csv')}
        for pmid in expected:
            self.assertEqual(background[pmid]['main_read_completed_on'], '2026-09-23')
            self.assertEqual(self.quality[pmid]['eligibility'], 'excluded')
            self.assertNotEqual(self.quality[pmid]['reading_stage'], 'main_text_deep_read_complete')
            self.assertFalse(any(pmid in entry['source_article_ids'].split(';') for entry in self.catalog))

    def test_no_automatic_acceptance_or_supplement_upgrade(self):
        for article in self.manifest:
            self.assertEqual(article['review_status'], 'not_reviewed')
            self.assertEqual(article['supplement_status'], 'not_supplied')
            self.assertEqual(len(article['sha256']), 64)
            self.assertTrue((REFERENCES / article['source_asset']).is_file())
            self.assertEqual(self.quality[article['pmid']]['review_status'], 'not_reviewed')

    def test_current_candidate_overlay_preserves_history(self):
        history = records('ccr-omics-supplement-candidates-2026-09-23.csv')
        current = records('ccr-omics-candidates-current-status.csv')
        self.assertEqual({row['pmid'] for row in history}, {row['pmid'] for row in current})
        self.assertTrue(all(row['reading_status'] == 'metadata_and_abstract_screened_not_fulltext_read' for row in history))
        acquired = {row['pmid'] for row in current if row['acquired_this_batch'] == 'yes' and row['status_as_of'] == '2026-09-23'}
        self.assertEqual(acquired, {'40833744', '41403154', '42148883', '42484497'})
        self.assertTrue(all(row['stk11_highlight'] == 'no' for row in current))
        for candidate in current:
            if candidate['current_indexed'] == 'yes':
                self.assertEqual(candidate['current_reading_stage'], self.quality[candidate['pmid']]['reading_stage'])
                self.assertTrue((REFERENCES / candidate['source_asset']).is_file())
            else:
                self.assertNotIn(candidate['pmid'], self.quality)
                self.assertEqual(candidate['current_reading_stage'], 'abstract_screened_not_fulltext_read')

    def test_classification_reaches_inventory_and_retrieval(self):
        library = {row['pmid']: row for row in records('library-index.csv')}
        alerts = json.loads((REFERENCES / 'language-controls.json').read_text(encoding='utf-8-sig'))['article_alerts']
        for article in self.manifest:
            self.assertEqual(library[article['pmid']]['disease_scope'], article['disease_scope'])
            self.assertEqual(library[article['pmid']]['source_role'], article['source_role'])
            self.assertEqual(library[article['pmid']]['stk11_highlight'], 'no')
            if article['reading_stage'] == 'main_text_deep_read_complete':
                self.assertTrue(any(article['pmid'] in alert['article_ids'] for alert in alerts))
        self.assertEqual(library['38875108']['source_role'], 'regulatory-analysis')
        self.assertEqual(library['39400264']['source_role'], 'registry-and-recommendations')
        self.assertIn('not-NSCLC', library['39078310']['disease_scope'])


if __name__ == '__main__':
    unittest.main()
