import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from library_common import read_csv, read_json
from retrieval_metadata import detected_terms
from search_language import load_index, search


class DomainAndUnitRepairs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries, _ = load_index(ROOT)
        cls.vocabulary = read_json(ROOT / 'references/retrieval-vocabulary.json')

    def test_genomics_domain_does_not_hide_exome_sequencing(self):
        unfiltered = search(self.entries, query='whole-exome sequencing', limit=100)
        filtered = search(self.entries, query='whole-exome sequencing', domain='genomics', limit=100)
        self.assertGreater(filtered['matched_count'], 0)
        explicit = {entry['stable_id'] for entry in unfiltered['entries'] if 'whole-exome' in entry['expression']}
        self.assertTrue(explicit <= {entry['stable_id'] for entry in filtered['entries']})

    def test_preclinical_domain_retains_immunoblotting(self):
        hits = search(self.entries, query='immunoblotting', domain='preclinical', pmid='36240971')
        self.assertTrue(any(entry['expression'] == 'phosphorylation-specific immunoblotting' for entry in hits['entries']))

    def test_exome_and_germline_glosses_are_terms_not_sentences(self):
        rows = read_csv(ROOT / 'references/ccr-section-language-catalog.csv')
        for expression in ['whole-exome sequencing', 'matched germline control']:
            row = next(row for row in rows if row['source_article_ids'] == '35247929' and row['expression'] == expression)
            self.assertEqual(row['unit_type'], 'vocabulary')
            self.assertEqual(row['function'], 'terminology')
            self.assertEqual(row['reuse_status'], 'conventional-term-or-collocation')
            entry = next(entry for entry in self.entries if entry['source_article_ids'] == '35247929' and entry['expression'] == expression)
            self.assertEqual(entry['expression_origin'], 'conventional-term-or-collocation')
            self.assertNotEqual(entry['source_locator']['state'], 'synthetic-not-a-verbatim-quotation')

    def test_domains_are_topics_not_assay_or_quotation_acceptance(self):
        for entry in search(self.entries, query='whole-exome sequencing', domain='genomics')['entries']:
            self.assertFalse(entry['original_wording_verified'])
            self.assertIn(entry['expression_annotation_status'], {'lexical-topic-candidate', 'curated-expression-topic'})
        self.assertNotIn('proteomics', detected_terms('LC-MS/MS metabolite profiling', self.vocabulary['domains']))
        self.assertEqual(detected_terms('reverse-phase protein array', self.vocabulary['domains']), ['targeted-protein-assay'])

    def test_glossed_clauses_are_not_downgraded_to_vocabulary(self):
        rows = read_csv(ROOT / 'references/ccr-section-language-catalog.csv')
        for expression in ['resistance poses substantial clinical challenges',
                           'objective responses were rarely observed',
                           'patient accrual was discontinued']:
            row = next(row for row in rows if row['expression'] == expression)
            self.assertEqual(row['unit_type'], 'sentence-frame')


if __name__ == '__main__':
    unittest.main()
