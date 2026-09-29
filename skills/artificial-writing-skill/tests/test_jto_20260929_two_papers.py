import csv
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / 'references'
sys.path.insert(0, str(ROOT / 'scripts'))
from search_language import load_index, search


def records(filename):
    with (REFERENCES / filename).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


class JtoSeptember29TwoPapers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries, cls.manifest = load_index(ROOT)
        cls.identifiers = {'42674257', '42749050'}
        cls.library = {row['pmid']: row for row in records('library-index.csv')}

    def test_unique_journal_identity_and_queue_consistency(self):
        bibliography = records('jto-corpus-bibliography.csv')
        queue = records('jto-maintenance-queue.csv')
        ccr = {row['pmid'] for row in records('ccr-corpus-bibliography.csv')}
        self.assertFalse(self.identifiers & ccr)
        for identifier in self.identifiers:
            self.assertEqual(sum(row['pmid'] == identifier for row in bibliography), 1)
            queued = [row for row in queue if row['pmid'] == identifier]
            self.assertEqual(len(queued), 1)
            self.assertEqual(queued[0]['reading_stage'], 'main_text_deep_read_complete')
            self.assertEqual(queued[0]['local_pdf_status'], 'hash_verified_local_pdf')
            source = self.library[identifier]
            self.assertEqual(source['journal'], 'Journal of Thoracic Oncology')
            self.assertEqual(source['year'], '2026')
            self.assertEqual(source['reading_stage'], queued[0]['reading_stage'])
            self.assertEqual(source['stk11_highlight'], 'no')

    def test_complete_main_reading_does_not_promote_acceptance(self):
        quality = {row['pmid']: row for row in records('jto-reading-quality-register.csv')}
        for identifier in self.identifiers:
            record = quality[identifier]
            self.assertEqual(record['review_status'], 'not_reviewed')
            self.assertEqual(record['main_read_completed_on'], '2026-09-29')
            for field in ('coverage_check', 'evidence_check', 'results_check', 'language_check', 'traceability_check', 'transfer_check'):
                self.assertEqual(record[field], 'pending')
            self.assertEqual(search(self.entries, pmid=identifier, reviewed=True)['matched_count'], 0)
            self.assertEqual(search(self.entries, pmid=identifier, highlight=True)['matched_count'], 0)
        self.assertEqual(quality['42674257']['supplement_status'], 'not_supplied')
        self.assertEqual(quality['42749050']['supplement_status'], 'partially_reviewed')

    def test_section_retrieval_and_source_alerts(self):
        counts = {'42674257': 39, '42749050': 41}
        for identifier, expected in counts.items():
            matches = search(self.entries, pmid=identifier, journal='jto', limit=100)['entries']
            self.assertEqual(len(matches), expected)
            for section in ('abstract', 'introduction', 'methods', 'results', 'discussion', 'conclusion', 'figure'):
                self.assertGreater(search(self.entries, pmid=identifier, section=section)['matched_count'], 0, (identifier, section))
            self.assertGreater(search(self.entries, pmid=identifier, unit='paragraph-model')['matched_count'], 0)
            for entry in matches:
                self.assertTrue(entry['source_alerts'])
                self.assertEqual(entry['source_articles'][0]['review_status'], 'not_reviewed')
                self.assertFalse(entry['source_context_rechecks'])
                lines = (REFERENCES / entry['source_asset']).read_text(encoding='utf-8').splitlines()
                self.assertIn(entry['expression'], lines[int(entry['source_line']) - 1])

    def test_omics_and_coalteration_boundaries(self):
        self.assertGreater(search(self.entries, pmid='42674257', article_domain='transcriptomics')['matched_count'], 0)
        self.assertEqual(search(self.entries, pmid='42749050', article_domain='transcriptomics')['matched_count'], 0)
        self.assertGreater(search(self.entries, pmid='42749050', article_domain='liquid-biopsy', tissue='plasma')['matched_count'], 0)
        for identifier in self.identifiers:
            self.assertEqual(search(self.entries, pmid=identifier, article_domain='proteomics')['matched_count'], 0)
            self.assertEqual(search(self.entries, pmid=identifier, article_domain='single-cell')['matched_count'], 0)
        topics = json.loads((REFERENCES / 'coalteration-annotations.json').read_text(encoding='utf-8'))['articles']
        self.assertIn('same_gene_compound', topics['42749050']['alteration_types'])
        self.assertIn('fusion_rearrangement', topics['42749050']['alteration_types'])
        self.assertIn('not an efficacy subgroup', topics['42749050']['boundary'])
        self.assertNotIn('same_gene_compound', topics['42674257']['alteration_types'])


if __name__ == '__main__':
    unittest.main()
