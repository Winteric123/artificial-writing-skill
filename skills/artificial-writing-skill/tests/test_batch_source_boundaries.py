import csv
import unittest
from pathlib import Path


REFERENCES = Path(__file__).resolve().parents[1] / 'references'


def records(filename):
    with (REFERENCES / filename).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


class BatchSourceBoundaries(unittest.TestCase):
    def test_each_new_original_source_has_section_language(self):
        catalog = records('ccr-section-language-catalog.csv')
        manifest = records('ccr-2026-09-23-reading-manifest.csv')
        expected = {'abstract-background', 'abstract-methods', 'abstract-results', 'abstract-conclusion', 'introduction', 'methods', 'results', 'discussion', 'conclusion', 'translational-relevance'}
        originals = [entry for entry in manifest if entry['source_role'] != 'background-review-only']
        self.assertEqual(len(originals), 11)
        for article in originals:
            matching = [entry for entry in catalog if entry['source_article_ids'] == article['pmid'] and entry['source_asset'] == article['source_asset']]
            self.assertTrue(expected <= {entry['primary_section'] for entry in matching}, article['pmid'])
            self.assertTrue({'vocabulary', 'sentence-frame', 'paragraph-model'} <= {entry['unit_type'] for entry in matching}, article['pmid'])

    def test_review_is_read_background_not_original_corpus(self):
        quality = {entry['pmid']: entry for entry in records('ccr-reading-quality-register.csv')}
        review = quality['40911432']
        self.assertEqual(review['eligibility'], 'excluded')
        self.assertNotEqual(review['reading_stage'], 'main_text_deep_read_complete')
        self.assertFalse(any('40911432' in entry['source_article_ids'].split(';') for entry in records('ccr-section-language-catalog.csv')))
        background = records('ccr-background-reading-register.csv')
        self.assertEqual(background[0]['pmid'], '40911432')
        self.assertEqual(background[0]['reading_stage'], 'background_review_read')
        self.assertEqual(background[0]['main_read_completed_on'], '2026-09-23')

    def test_supplied_versions_and_disease_boundaries_survive(self):
        manifest = {entry['pmid']: entry for entry in records('ccr-2026-09-23-reading-manifest.csv')}
        self.assertEqual(manifest['40378060']['year'], '2025')
        self.assertEqual(manifest['41961582']['pdf_version'], 'publisher_line_numbered_manuscript')
        self.assertEqual(manifest['39540841']['source_role'], 'cross-tumor-methodology')
        self.assertIn('not-NSCLC', manifest['39879384']['disease_scope'])
        for entry in manifest.values():
            self.assertEqual(entry['review_status'], 'not_reviewed')
            self.assertEqual(entry['supplement_status'], 'not_supplied')
            self.assertEqual(len(entry['sha256']), 64)

    def test_candidate_directory_does_not_claim_reading_or_priority(self):
        candidates = records('ccr-omics-supplement-candidates-2026-09-23.csv')
        self.assertEqual(len(candidates), 19)
        self.assertEqual(len({entry['pmid'] for entry in candidates}), 19)
        for entry in candidates:
            self.assertEqual(entry['included_in_corpus'], 'false')
            self.assertEqual(entry['stk11_highlight'], 'false')
            self.assertEqual(entry['reading_status'], 'metadata_and_abstract_screened_not_fulltext_read')
            self.assertEqual(bool(entry['official_category']), bool(entry['category_source']))


if __name__ == '__main__':
    unittest.main()
