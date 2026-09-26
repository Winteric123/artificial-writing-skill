import copy
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / 'scripts'))

from build_pdf_locators import literal_occurrence, locate_entry, main_text_pages, page_hints
from library_common import read_csv, read_json
from search_language import load_index, search
from source_provenance import attach_pdf_locator, load_pdf_locators
import test_retrieval


class PdfProvenance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries, cls.manifest = load_index(SKILL)
        cls.locators = load_pdf_locators(SKILL)

    def test_literal_matching_is_not_paraphrase_matching(self):
        self.assertTrue(literal_occurrence('loss of heterozygosity', 'A loss of\nheterozygosity (LOH).'))
        self.assertFalse(literal_occurrence('adjusted hazard ratio', 'an adjusted survival association'))
        self.assertFalse(literal_occurrence('SCLC', 'NSCLC'))
        self.assertFalse(literal_occurrence('[group] had [outcome]', '[group] had [outcome]'))

    def test_reference_only_matches_are_excluded(self):
        pages = main_text_pages(['Main study\nReferences\nwrong phrase', 'more references', 'Figure 1. figure wording'])
        self.assertEqual(pages, ['Main study\n', '', 'Figure 1. figure wording'])

    def test_page_hints_are_not_pdf_anchors(self):
        self.assertEqual(page_hints('Source: pp2-4, 7.'), [2, 3, 4, 7])
        entry = {'expression': '[marker] was associated with [outcome].', 'unit_type': 'sentence-frame',
                 'source_article_ids': '99990001', 'source_line': '1'}
        record = locate_entry(entry, {'99990001': {'physical_pages': 3, 'sha256': 'test'}},
                              {'99990001': [entry['expression'], '', '']}, ['Source: p2.'])
        self.assertEqual(record['state'], 'synthetic-not-a-verbatim-quotation')
        self.assertFalse(record['literal_matches'])
        self.assertEqual(record['recorded_page_hints'][0]['recorded_pages'], [2])
        self.assertEqual(record['recorded_page_hints'][0]['page_numbering'], 'unverified-reading-note-numbering')
        self.assertFalse(record['quotation_verified'])

    def test_out_of_range_hints_are_retained_not_repaired(self):
        entry = {'expression': 'test phrase', 'unit_type': 'vocabulary', 'source_article_ids': '99990001', 'source_line': '1'}
        record = locate_entry(entry, {'99990001': {'physical_pages': 1, 'sha256': 'test'}}, {'99990001': ['test phrase']}, ['Source: p9.'])
        self.assertEqual(record['recorded_page_hints'][0]['state'], 'out-of-range-recorded-hint')
        self.assertEqual(record['literal_matches'][0]['physical_pages'], [1])

    def test_all_current_entries_validate_against_registered_versions(self):
        self.assertEqual(set(self.locators['entries']), {entry['stable_id'] for entry in self.entries})
        for entry in self.entries:
            attach_pdf_locator(copy.deepcopy(entry), self.locators)
            for source in entry['source_articles']:
                self.assertEqual(source['source_pdf']['identity_check'], 'registered-sha256-match')

    def test_unknown_tissue_is_not_negative_evidence(self):
        sources = {source['pmid']: source for entry in self.entries for source in entry['source_articles']}
        for source in sources.values():
            scope = source['source_scope']
            for field in ['disease_ids', 'model_ids', 'use_roles']:
                self.assertTrue(scope[field])
            if not scope['tissue_ids']:
                self.assertEqual(scope['facet_status']['tissue_ids'], 'not-curated-not-absent')

    def test_scope_facets_reach_library(self):
        rows = {row['pmid']: row for row in read_csv(SKILL / 'references/library-index.csv')}
        for entry in self.entries:
            for source in entry['source_articles']:
                self.assertEqual(rows[source['pmid']]['source_disease_ids'], ';'.join(source['source_scope']['disease_ids']))

    def test_no_lung_primary_from_metastasis_or_infection(self):
        for pmid in ['37992307', '38723277', '39841860']:
            self.assertEqual(search(self.entries, pmid=pmid, disease='lung-cancer', include_subtypes=True)['matched_count'], 0)
        self.assertGreater(search(self.entries, pmid='38723277', disease='thyroid-cancer')['matched_count'], 0)
        self.assertEqual(search(self.entries, pmid='38180245', disease='SCLC')['matched_count'], 0)
        self.assertGreater(search(self.entries, pmid='38180245', disease='smarca4-deficient-thoracic')['matched_count'], 0)

    def test_pdf_filter_requires_same_contributing_article(self):
        entry = test_retrieval.synthetic_entry()
        entry['source_locator'] = {'literal_matches': [{'pmid': '99990001'}]}
        self.assertEqual(search([entry], year='2026', pdf_located=True)['matched_count'], 0)
        self.assertEqual(search([entry], year='2025', pdf_located=True)['matched_count'], 1)

    def test_collocations_are_conventional_not_synthetic(self):
        entries = [entry for entry in self.entries if entry['unit_type'] == 'collocation']
        self.assertTrue(entries)
        self.assertTrue(all(entry['expression_origin'] == 'conventional-term-or-collocation' for entry in entries))

    def test_new_entry_explicitly_lacks_pdf_locator(self):
        entry = test_retrieval.synthetic_entry()
        entry['source_locator'] = {}
        attach_pdf_locator(entry, self.locators)
        self.assertEqual(entry['source_locator']['state'], 'not-yet-located')
        self.assertFalse(entry['source_locator']['pdf_text_match_verified'])

    def test_tampered_match_rejected_without_certifying_quotation(self):
        entry = next(entry for entry in self.entries if entry['source_locator']['literal_matches'])
        for field, value in [('pmid', '99999999'), ('sha256', 'wrong'), ('physical_pages', [99999]), ('visual_check', True)]:
            with self.subTest(field=field):
                data = copy.deepcopy(self.locators)
                data['entries'][entry['stable_id']]['literal_matches'][0][field] = value
                with self.assertRaises(ValueError):
                    attach_pdf_locator(copy.deepcopy(entry), data)

    def test_stale_expression_rejected(self):
        entry = copy.deepcopy(self.entries[0])
        entry['expression'] += ' changed'
        with self.assertRaisesRegex(ValueError, 'identity'):
            attach_pdf_locator(entry, self.locators)


class ProvenanceIntegrity(unittest.TestCase):
    setUp = test_retrieval.IsolatedMaintenance.setUp
    tearDown = test_retrieval.IsolatedMaintenance.tearDown

    def test_new_dependency_changes_invalidate_retrieval(self):
        for name in ['source-scope-backfill.json', 'source-pdf-locators.json']:
            path = self.skill / 'references' / name
            original = path.read_bytes()
            path.write_bytes(original + b'\n')
            with self.assertRaisesRegex(ValueError, 'Stale language index'):
                load_index(self.skill)
            path.write_bytes(original)

    def test_stale_source_asset_rejected_by_locator_loader(self):
        data = read_json(self.skill / 'references/source-pdf-locators.json')
        name = next(iter(data['source_asset_hashes']))
        path = self.skill / 'references' / name
        path.write_bytes(path.read_bytes() + b'\n')
        with self.assertRaisesRegex(ValueError, 'Stale PDF locator asset'):
            load_pdf_locators(self.skill)


if __name__ == '__main__':
    unittest.main()
