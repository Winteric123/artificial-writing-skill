import csv
import json
import unittest
from collections import Counter
from pathlib import Path


REFERENCES = Path(__file__).resolve().parents[1] / 'references'
PMIDS = {'34759042', '35140122', '38330145', '34016641', '33020056', '34446541', '38261467', '34667030', '38630555'}


def records(filename):
    with (REFERENCES / filename).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


class September28Intake(unittest.TestCase):
    def setUp(self):
        self.manifest = records('ccr-2026-09-28-reading-manifest.csv')
        self.library = {row['pmid']: row for row in records('library-index.csv')}
        self.catalog = records('ccr-section-language-catalog.csv')

    def test_identity_and_completion_scope(self):
        self.assertEqual({row['pmid'] for row in self.manifest}, PMIDS)
        self.assertEqual(len(self.manifest), 9)
        self.assertEqual(sum(int(row['physical_pages']) for row in self.manifest), 131)
        self.assertEqual(Counter(row['year'] for row in self.manifest), {'2021': 3, '2022': 3, '2024': 3})
        for article in self.manifest:
            indexed = self.library[article['pmid']]
            self.assertEqual(indexed['journal'], 'Clinical Cancer Research')
            self.assertEqual(indexed['title'], article['title'])
            self.assertEqual(indexed['reading_stage'], 'main_text_deep_read_complete')
            self.assertEqual(indexed['main_read_completed_on'], '2026-09-28')
            self.assertEqual(indexed['review_status'], 'not_reviewed')
            self.assertEqual(indexed['supplement_status'], 'not_supplied')
            self.assertEqual(indexed['stk11_highlight'], 'no')

    def test_official_categories_and_multi_topic_routes(self):
        self.assertEqual(Counter(row['official_category'] for row in self.manifest), {
            'Precision Medicine and Imaging': 4,
            'Translational Cancer Mechanisms and Therapy': 5,
        })
        annotations = json.loads((REFERENCES / 'retrieval-annotations.json').read_text(encoding='utf-8'))['articles']
        self.assertIn('cross-tumor-methods', annotations['34759042']['use_roles'])
        self.assertIn('computational-methods', annotations['35140122']['use_roles'])
        self.assertIn('preclinical-mechanism', annotations['34667030']['use_roles'])
        for article in self.manifest:
            tags = article['secondary_domain_tags'].split(';')
            self.assertNotIn('single-cell', tags)
            self.assertNotIn('spatial-transcriptomics', tags)
        by_pmid = {row['pmid']: row for row in self.manifest}
        self.assertIn('proteomics', by_pmid['38261467']['secondary_domain_tags'].split(';'))
        self.assertIn('targeted-protein-assay', by_pmid['34667030']['secondary_domain_tags'].split(';'))
        self.assertNotIn('proteomics', by_pmid['34667030']['secondary_domain_tags'].split(';'))

    def test_all_section_language_and_alerts_are_retrievable(self):
        sections = {'abstract-background', 'abstract-methods', 'abstract-results', 'abstract-conclusion',
                    'introduction', 'methods', 'results', 'discussion', 'conclusion', 'translational-relevance'}
        controls = json.loads((REFERENCES / 'language-controls.json').read_text(encoding='utf-8'))
        for article in self.manifest:
            entries = [row for row in self.catalog if row['source_asset'] == article['source_asset']]
            self.assertTrue(sections <= {row['primary_section'] for row in entries}, article['pmid'])
            self.assertTrue({'vocabulary', 'sentence-frame', 'paragraph-model'} <= {row['unit_type'] for row in entries})
            self.assertTrue(all(row['source_article_ids'] == article['pmid'] for row in entries))
            self.assertTrue(any(article['pmid'] in alert['article_ids'] for alert in controls['article_alerts']))

    def test_author_manuscript_and_visual_companion_remain_distinct(self):
        article = next(row for row in self.manifest if row['pmid'] == '34016641')
        self.assertEqual(article['pdf_version'], 'author_manuscript')
        self.assertEqual(article['physical_pages'], '32')
        versions = [row for row in records('source-version-register.csv') if row['pmid'] == '34016641']
        self.assertEqual(len(versions), 1)
        self.assertEqual(versions[0]['archived_pdf_count'], '2')
        self.assertEqual(versions[0]['sha256'], article['sha256'])
        self.assertIn('visual companion', versions[0]['scope'])
        self.assertIn('only physical5/8 inspected', versions[0]['scope'])


if __name__ == '__main__':
    unittest.main()
