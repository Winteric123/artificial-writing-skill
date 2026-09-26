import csv
import json
import unittest
from pathlib import Path


REFERENCES = Path(__file__).resolve().parents[1] / 'references'
NEW_PMIDS = {
    '36201167',
    '36692420',
    '41563386',
    '41511400',
    '35838647',
    '33558425',
    '33593884',
    '33622705',
    '33685865',
    '33685866',
    '33947695',
    '38630755',
    '33023953',
    '39150541',
}
DUPLICATE_PMIDS = {'33323404', '38980931'}


def records(filename):
    with (REFERENCES / filename).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


class September26Intake(unittest.TestCase):
    def setUp(self):
        self.manifest = records('ccr-2026-09-26-reading-manifest.csv')
        self.library = {row['pmid']: row for row in records('library-index.csv')}
        self.bibliography = {row['pmid']: row for row in records('ccr-corpus-bibliography.csv')}
        self.catalog = records('ccr-section-language-catalog.csv')

    def test_batch_identity_pages_and_duplicate_dates(self):
        self.assertEqual(len(self.manifest), 16)
        self.assertEqual({row['pmid'] for row in self.manifest}, NEW_PMIDS | DUPLICATE_PMIDS)
        self.assertEqual(sum(int(row['physical_pages']) for row in self.manifest), 264)
        for article in self.manifest:
            indexed = self.library[article['pmid']]
            self.assertEqual(indexed['title'], article['title'])
            self.assertEqual(indexed['journal'], 'Clinical Cancer Research')
            self.assertEqual(indexed['reading_stage'], 'main_text_deep_read_complete')
            self.assertEqual(indexed['review_status'], 'not_reviewed')
            self.assertEqual(indexed['supplement_status'], 'not_supplied')
            self.assertEqual(indexed['stk11_highlight'], 'no')
            self.assertEqual(len(article['sha256']), 64)
            self.assertTrue(article['main_visual_physical_pages'])
        for pmid in NEW_PMIDS:
            self.assertEqual(self.library[pmid]['main_read_completed_on'], '2026-09-26')
        for pmid in DUPLICATE_PMIDS:
            self.assertEqual(self.library[pmid]['main_read_completed_on'], '2026-09-24')

    def test_new_sources_reach_all_section_routes_and_alerts(self):
        controls = json.loads((REFERENCES / 'language-controls.json').read_text(encoding='utf-8-sig'))
        sections = {
            'abstract-background',
            'abstract-methods',
            'abstract-results',
            'abstract-conclusion',
            'introduction',
            'methods',
            'results',
            'discussion',
            'conclusion',
            'translational-relevance',
        }
        manifest = {row['pmid']: row for row in self.manifest}
        for pmid in NEW_PMIDS:
            article = manifest[pmid]
            entries = [entry for entry in self.catalog if entry['source_asset'] == article['source_asset']]
            self.assertTrue(sections <= {entry['primary_section'] for entry in entries}, pmid)
            self.assertTrue({'vocabulary', 'sentence-frame', 'paragraph-model'} <= {entry['unit_type'] for entry in entries})
            self.assertTrue(all(entry['source_article_ids'] == pmid for entry in entries))
            self.assertTrue(any(pmid in alert['article_ids'] for alert in controls['article_alerts']))

    def test_cross_tumor_and_modality_boundaries(self):
        self.assertEqual(self.bibliography['41563386']['source_role'], 'cross-tumor-clinical-methods')
        self.assertEqual(self.bibliography['41511400']['source_role'], 'cross-tumor-clinical-methods')
        self.assertIn('no lung-specific efficacy analysis', self.bibliography['41563386']['disease_scope'])
        self.assertIn('no lung-specific efficacy analysis', self.bibliography['41511400']['disease_scope'])
        self.assertEqual(self.bibliography['33622705']['source_role'], 'cross-tumor-transcriptomic-bioinformatics')
        self.assertIn('spatial-transcriptomics', self.bibliography['38630755']['secondary_classifications'])
        self.assertIn('spatial-transcriptomics', self.bibliography['39150541']['secondary_classifications'])
        self.assertNotIn('proteomics', self.bibliography['38630755']['secondary_classifications'])

    def test_intake_membership_survives_later_updates(self):
        ccr_rows = [row for row in self.library.values() if row['journal'] == 'Clinical Cancer Research']
        ccr_ids = {row['pmid'] for row in ccr_rows}
        self.assertTrue((NEW_PMIDS | DUPLICATE_PMIDS) <= ccr_ids)
        included = [row for row in ccr_rows if row['eligibility'] == 'included']
        complete = [row for row in included if row['reading_stage'] == 'main_text_deep_read_complete']
        incomplete = [row for row in included if row['reading_stage'] != 'main_text_deep_read_complete']
        self.assertEqual(len(included), len(complete) + len(incomplete))


if __name__ == '__main__':
    unittest.main()
