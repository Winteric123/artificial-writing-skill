"""Regression invariants for the bounded local-PDF STK11 intake, not scientific certification."""
import csv
import json
import sys
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
REFS = SKILL / 'references'
sys.path.insert(0, str(SKILL / 'scripts'))
from search_stk11_references import load_records, matches


def rows(name):
    with (REFS / name).open(encoding='utf-8-sig', newline='') as source:
        return list(csv.DictReader(source))


class LocalStk11Intake(unittest.TestCase):
    def test_new_main_read_does_not_promote_review_or_priority(self):
        record = next(r for r in rows('library-index.csv') if r['pmid'] == '37495171')
        self.assertEqual(record['main_read_completed_on'], '2026-10-02')
        self.assertEqual(record['reading_stage'], 'main_text_deep_read_complete')
        self.assertEqual(record['review_status'], 'in_progress')
        self.assertEqual(record['supplement_status'], 'not_supplied')
        self.assertNotEqual(record['stk11_highlight'], 'yes')
        quality = next(r for r in rows('jto-reading-quality-register.csv') if r['pmid'] == record['pmid'])
        self.assertEqual(quality['review_method'], 'independent_agent_source_recheck')
        self.assertEqual(quality['results_check'], 'pending')
        self.assertEqual(quality['traceability_check'], 'pending')
        self.assertTrue((REFS / quality['review_record']).is_file())

    def test_historical_read_dates_are_preserved(self):
        expected = {'38300729':'2026-09-23','38980931':'2026-09-24',
                    '42456046':'2026-09-08','42485106':'2026-09-08',
                    '33077574':'2026-09-12','33323404':'2026-09-24',
                    '36958689':'2026-09-28','41690367':'2026-09-29',
                    '34450259':'2026-09-29','41161592':'2026-09-28','42749050':'2026-09-29'}
        library = {r['pmid']:r for r in rows('library-index.csv')}
        for pmid, completed in expected.items():
            with self.subTest(pmid=pmid):
                self.assertEqual(library[pmid]['main_read_completed_on'], completed)
                self.assertEqual(library[pmid]['review_status'], 'not_reviewed')

    def test_language_units_have_single_paper_source_lines(self):
        jto = [r for r in rows('jto-section-language-catalog.csv') if r['source_article_ids'] == '37495171']
        self.assertEqual(len(jto), 62)
        self.assertTrue({'vocabulary','sentence-frame','paragraph-model'} <= {r['unit_type'] for r in jto})
        self.assertTrue({'introduction','methods','results','discussion'} <= {r['primary_section'] for r in jto})
        ccr = rows('ccr-section-language-catalog.csv')
        for pmid in ('42456046', '42485106'):
            addendum = [r for r in ccr if r['source_article_ids'] == pmid and 'language-addendum' in r['source_asset']]
            self.assertGreaterEqual(len(addendum), 10)
            self.assertTrue({'vocabulary','sentence-frame','paragraph-model'} <= {r['unit_type'] for r in addendum})
            jto.extend(addendum)
        for r in jto:
            lines = (REFS / r['source_asset']).read_text(encoding='utf-8-sig').splitlines()
            self.assertIn(r['expression'], lines[int(r['source_line'])-1])

    def test_assay_and_structural_analogue_boundaries(self):
        new = next(r for r in load_records(SKILL, True) if r['pmid'] == '37495171')
        self.assertTrue(matches(new, assays=['bulk_rna'], origin='original'))
        self.assertTrue(matches(new, assays=['bulk_rna'], origin='reanalysis'))
        self.assertFalse(matches(new, assays=['single_cell_rna']))
        self.assertFalse(matches(new, assays=['targeted_dna']))
        self.assertTrue(matches(new, treatments=['chemoimmunotherapy']))
        mapping = json.loads((REFS / 'stk11-writing-reference-map.json').read_text(encoding='utf-8'))
        for r in mapping['records']:
            if r['pmid'] in ('41161592','42749050'):
                self.assertEqual(r['tier'], 'topic_support')
                self.assertEqual(r['stk11_relation'], 'structural_analogue')
                self.assertFalse(r['in_cross_gene_16'])


if __name__ == '__main__':
    unittest.main()
