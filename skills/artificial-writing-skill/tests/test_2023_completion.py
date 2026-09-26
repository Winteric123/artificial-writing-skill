import csv
import json
import unittest
from pathlib import Path


REFERENCES = Path(__file__).resolve().parents[1] / 'references'


def read_rows(name):
    with (REFERENCES / name).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


class Completion2023Tests(unittest.TestCase):
    def test_batch_and_year_scope(self):
        manifest = read_rows('ccr-2023-completion-2026-09-26-manifest.csv')
        self.assertEqual(len(manifest), 34)
        self.assertEqual(len({row['pmid'] for row in manifest}), 34)
        library = {row['pmid']: row for row in read_rows('library-index.csv') if row['journal'] == 'Clinical Cancer Research'}
        for article in manifest:
            indexed = library[article['pmid']]
            self.assertEqual(indexed['year'], '2023')
            self.assertEqual(indexed['reading_stage'], 'main_text_deep_read_complete')
            self.assertEqual(indexed['main_read_completed_on'], '2026-09-26')
            self.assertEqual(indexed['review_status'], 'not_reviewed')
            self.assertEqual(indexed['supplement_status'], 'not_supplied')
            self.assertEqual(len(article['sha256']), 64)
            self.assertTrue((REFERENCES / article['source_asset']).exists())
        for pmid in ('35616593', '37581538'):
            self.assertEqual(library[pmid]['eligibility'], 'excluded')
            self.assertNotEqual(library[pmid]['reading_stage'], 'main_text_deep_read_complete')
        year_rows = [row for row in library.values() if row['year'] == '2023' and row['eligibility'] == 'included']
        self.assertTrue(all(row['reading_stage'] == 'main_text_deep_read_complete' for row in year_rows))

    def test_section_routes_and_background_exclusion(self):
        catalog = read_rows('ccr-section-language-catalog.csv')
        manifest = read_rows('ccr-2023-completion-2026-09-26-manifest.csv')
        required = {'abstract-background','abstract-methods','abstract-results','abstract-conclusion','introduction','methods','results','discussion','conclusion','translational-relevance'}
        controls = json.loads((REFERENCES / 'language-controls.json').read_text(encoding='utf-8-sig'))
        for article in manifest:
            entries = [row for row in catalog if row['source_asset'] == article['source_asset']]
            self.assertTrue(required <= {row['primary_section'] for row in entries}, article['pmid'])
            self.assertTrue({'vocabulary','sentence-frame','paragraph-model'} <= {row['unit_type'] for row in entries})
            self.assertTrue(all(row['source_article_ids'] == article['pmid'] for row in entries))
            self.assertTrue(all(row['source_set'].startswith('ccr-2023-completion-') for row in entries))
            self.assertTrue(any(article['pmid'] in alert['article_ids'] for alert in controls['article_alerts']))
        self.assertFalse(any(set(row['source_article_ids'].split(';')) & {'35616593','37581538'} for row in catalog))

    def test_actual_modality_and_version_boundaries(self):
        bibliography = {row['pmid']:row for row in read_rows('ccr-corpus-bibliography.csv')}
        self.assertIn('sarcoma',bibliography['37756581']['disease_scope'])
        self.assertIn('tonsillar',bibliography['37756581']['disease_scope'])
        self.assertIn('not SCLC',bibliography['36255391']['disease_scope'])
        self.assertIn('MST1R',bibliography['36537918']['secondary_classifications'])
        companion = json.loads((REFERENCES / 'ccr-2023-main-figure-companion.json').read_text())
        self.assertEqual(companion['physical_pages'],3)
        self.assertEqual(len(companion['sha256']),64)
        self.assertIn('conflict',companion['scope'])


if __name__ == '__main__':
    unittest.main()
