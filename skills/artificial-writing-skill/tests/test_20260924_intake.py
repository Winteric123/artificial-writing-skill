import csv
import json
import unittest
from pathlib import Path


REFERENCES = Path(__file__).resolve().parents[1] / 'references'


def records(filename):
    with (REFERENCES / filename).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


class September24Intake(unittest.TestCase):
    def setUp(self):
        self.manifest = records('ccr-2026-09-24-reading-manifest.csv')
        self.library = {row['pmid']: row for row in records('library-index.csv')}
        self.bibliography = {row['pmid']: row for row in records('ccr-corpus-bibliography.csv')}
        self.catalog = records('ccr-section-language-catalog.csv')

    def test_identity_versions_and_main_read_scope(self):
        self.assertEqual(len(self.manifest), 7)
        self.assertEqual(sum(row['year'] == '2026' for row in self.manifest), 6)
        self.assertEqual(sum(int(row['physical_pages']) for row in self.manifest), 193)
        self.assertEqual({row['pmid'] for row in self.manifest if row['year'] == '2023'}, {'37227187'})
        for article in self.manifest:
            indexed = self.library[article['pmid']]
            self.assertEqual(indexed['title'], article['title'])
            self.assertEqual(indexed['journal'], 'Clinical Cancer Research')
            self.assertEqual(indexed['reading_stage'], 'main_text_deep_read_complete')
            self.assertEqual(indexed['main_read_completed_on'], '2026-09-24')
            self.assertEqual(indexed['supplied_pdf_version'], article['pdf_version'])
            self.assertEqual(indexed['review_status'], 'not_reviewed')
            self.assertEqual(indexed['supplement_status'], 'not_supplied')
            self.assertEqual(indexed['stk11_highlight'], 'no')
            self.assertEqual(len(article['sha256']), 64)
            self.assertTrue(article['main_visual_physical_pages'])

    def test_every_source_reaches_sections_and_alerts(self):
        controls = json.loads((REFERENCES / 'language-controls.json').read_text(encoding='utf-8-sig'))
        sections = {'abstract-background', 'abstract-methods', 'abstract-results', 'abstract-conclusion', 'introduction', 'methods', 'results', 'discussion', 'conclusion', 'translational-relevance'}
        for article in self.manifest:
            entries = [entry for entry in self.catalog if entry['source_asset'] == article['source_asset']]
            self.assertTrue(sections <= {entry['primary_section'] for entry in entries}, article['pmid'])
            self.assertTrue({'vocabulary', 'sentence-frame', 'paragraph-model'} <= {entry['unit_type'] for entry in entries})
            self.assertTrue(all(entry['source_article_ids'] == article['pmid'] for entry in entries))
            self.assertTrue(any(article['pmid'] in alert['article_ids'] for alert in controls['article_alerts']))
            self.assertEqual(self.library[article['pmid']]['disease_scope'], article['disease_scope'])
            self.assertEqual(self.library[article['pmid']]['source_role'], article['source_role'])

    def test_category_and_modality_boundaries(self):
        provisional = self.bibliography['42765908']
        self.assertEqual(provisional['ccr_official_category'], '')
        self.assertEqual(provisional['ccr_category_status'], 'pending_official_verification')
        self.assertIn('manuscript', provisional['ccr_category_source'])
        expected = {'42360806': 'Translational Mechanisms and Therapy', '42377115': 'Research Briefs: Precision Medicine and Therapeutics', '42456051': 'Artificial Intelligence and Computational Oncology', '42340371': 'Novel Biomarkers and Precision Medicine'}
        for pmid, category in expected.items():
            self.assertEqual(self.bibliography[pmid]['ccr_official_category'], category)
            self.assertEqual(self.bibliography[pmid]['ccr_category_status'], 'official_section')
        self.assertIn('spatial-histology', self.bibliography['42456051']['secondary_classifications'])
        self.assertNotIn('spatial-transcriptomics', self.bibliography['42456051']['secondary_classifications'])
        self.assertIn('bulk-RNA', self.bibliography['42340371']['secondary_classifications'])

    def test_candidate_overlay_has_updated_newly_read_sources(self):
        overlay = {row['pmid']: row for row in records('ccr-omics-candidates-current-status.csv')}
        for pmid in ('42340371', '42440358'):
            self.assertEqual(overlay[pmid]['status_as_of'], '2026-09-24')
            self.assertEqual(overlay[pmid]['current_indexed'], 'yes')
            self.assertEqual(overlay[pmid]['current_reading_stage'], 'main_text_deep_read_complete')
            self.assertEqual(overlay[pmid]['stk11_highlight'], 'no')


if __name__ == '__main__':
    unittest.main()
