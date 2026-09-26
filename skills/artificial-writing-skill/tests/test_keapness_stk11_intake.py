import csv
import json
import unittest
from pathlib import Path


REFERENCES = Path(__file__).resolve().parents[1] / 'references'


def rows(filename):
    with (REFERENCES / filename).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


class KeapnessStk11Intake(unittest.TestCase):
    def setUp(self):
        self.manifest = rows('ccr-keapness-stk11-2026-09-24-reading-manifest.csv')
        self.library = {row['pmid']: row for row in rows('library-index.csv')}
        self.bibliography = {row['pmid']: row for row in rows('ccr-corpus-bibliography.csv')}

    def test_identity_versions_and_completion_scope(self):
        self.assertEqual({row['pmid'] for row in self.manifest}, {'38980931', '33323404'})
        self.assertEqual(sum(int(row['physical_pages']) for row in self.manifest), 42)
        expected = {'38980931': ('2024', 'publisher_typeset_pdf'), '33323404': ('2021', 'author_manuscript')}
        for article in self.manifest:
            indexed = self.library[article['pmid']]
            self.assertEqual((article['year'], article['pdf_version']), expected[article['pmid']])
            self.assertEqual(indexed['title'], article['title'])
            self.assertEqual(indexed['doi'], article['doi'])
            self.assertEqual(indexed['journal'], 'Clinical Cancer Research')
            self.assertEqual(indexed['reading_stage'], 'main_text_deep_read_complete')
            self.assertEqual(indexed['main_read_completed_on'], '2026-09-24')
            self.assertEqual(indexed['review_status'], 'not_reviewed')
            self.assertEqual(indexed['supplement_status'], 'not_supplied')
            self.assertEqual(indexed['stk11_highlight'], 'no')
            self.assertEqual(indexed['supplied_pdf_version'], article['pdf_version'])
            self.assertEqual(len(article['sha256']), 64)

    def test_full_section_language_and_provenance(self):
        catalog = rows('ccr-section-language-catalog.csv')
        required = {'abstract-background', 'abstract-methods', 'abstract-results', 'abstract-conclusion',
                    'introduction', 'methods', 'results', 'discussion', 'conclusion', 'translational-relevance'}
        controls = json.loads((REFERENCES / 'language-controls.json').read_text(encoding='utf-8-sig'))
        for article in self.manifest:
            entries = [row for row in catalog if row['source_asset'] == article['source_asset']]
            self.assertTrue(required <= {row['primary_section'] for row in entries})
            self.assertTrue({'vocabulary', 'sentence-frame', 'paragraph-model'} <= {row['unit_type'] for row in entries})
            self.assertTrue(all(row['source_article_ids'] == article['pmid'] for row in entries))
            self.assertTrue(any(article['pmid'] in alert['article_ids'] for alert in controls['article_alerts']))

    def test_official_category_and_modality(self):
        self.assertEqual(self.bibliography['38980931']['ccr_official_category'], 'Precision Medicine and Imaging')
        self.assertEqual(self.bibliography['33323404']['ccr_official_category'], 'Translational Cancer Mechanisms and Therapy')
        self.assertEqual(self.bibliography['33323404']['pmcid'], 'PMC8138942')
        for pmid in ('38980931', '33323404'):
            self.assertEqual(self.bibliography[pmid]['ccr_category_status'], 'official_section')
            self.assertNotIn('single-cell', self.bibliography[pmid]['secondary_classifications'])
            self.assertNotIn('spatial-transcriptomics', self.bibliography[pmid]['secondary_classifications'])

    def test_candidate_is_no_longer_unread_or_unregistered(self):
        candidates = {row['pmid']: row for row in rows('stk11-expanded-reference-directory.csv')}
        candidate = candidates['33323404']
        self.assertEqual(candidate['local_registration'], 'registered')
        self.assertEqual(candidate['local_reading_stage'], 'main_text_deep_read_complete')
        self.assertEqual(candidate['local_review_status'], 'not_reviewed')
        self.assertEqual(candidate['stk11_highlight'], 'no')
        self.assertEqual(candidate['snapshot_date'], '2026-09-19')
        self.assertEqual(candidate['checked_on'], '2026-09-24')

    def test_negative_results_and_source_alerts_are_retained(self):
        keapness = (REFERENCES / 'ccr-2024-38980931-language.md').read_text(encoding='utf-8')
        radiation = (REFERENCES / 'ccr-2021-33323404-language.md').read_text(encoding='utf-8')
        for marker in ('314', '312', 'docetaxel', 'not establish an immunotherapy-specific predictive effect'):
            self.assertIn(marker, keapness)
        for marker in ('P=.1129', 'P=.119', '2.123', 'MitoSOX', 'not include KEAP1', 'time to tumor-volume doubling'):
            self.assertIn(marker, radiation)


if __name__ == '__main__':
    unittest.main()
