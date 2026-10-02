import sys
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / 'scripts'))
from search_stk11_references import load_records, matches


class AssayTagTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_records(SKILL, True)
        cls.by_id = {row['pmid']: row for row in cls.rows}

    def test_main_read_is_not_review_or_highlight(self):
        row = self.by_id['42432246']
        self.assertEqual(row['reading_stage'], 'main_text_deep_read_complete')
        self.assertEqual(row['review_status'], 'not_reviewed')
        self.assertFalse(row['core_highlight'])
        self.assertEqual(sum(row['core_highlight'] for row in self.rows), 13)

    def test_same_assay_origin_must_match(self):
        row = dict(pmid='fixture', core_highlight=False, stk11_relation='fixture', assays=[dict(assay='single_cell_rna', origin='reanalysis'), dict(assay='targeted_protein', origin='original')], treatment_types=[], methods=[])
        self.assertFalse(matches(row, assays=['single_cell_rna'], origin='original'))
        self.assertTrue(matches(row, assays=['single_cell_rna'], origin='reanalysis'))

    def test_specific_omics_and_models(self):
        self.assertFalse(matches(self.by_id['36948245'], assays=['single_cell_rna']))
        self.assertTrue(matches(self.by_id['36535627'], assays=['microarray', 'single_cell_rna'], origin='original'))
        self.assertFalse(matches(self.by_id['38207230'], assays=['spatial_rna']))
        self.assertTrue(matches(self.by_id['38207230'], assays=['spatial_protein']))
        self.assertTrue(matches(self.by_id['42432246'], assays=['wes'], origin='reanalysis'))
        self.assertFalse(matches(self.by_id['42432246'], assays=['wes'], origin='original'))

    def test_scope_and_stable_identity(self):
        detailed = [row for row in self.rows if row['classification_level'] == 'supplied_main_text_curated']
        self.assertEqual(len(detailed), 38)
        self.assertEqual(len({row['stable_id'] for row in self.rows}), len(self.rows))
        self.assertTrue(all(row['stable_id'] == 'STK11-PMID-' + row['pmid'] for row in self.rows))
        self.assertEqual(self.by_id['42749049']['stk11_relation'], 'structural_analogue')

    def test_treatment_is_not_causal_efficacy(self):
        self.assertTrue(matches(self.by_id['42587156'], treatments=['perioperative_ici']))
        self.assertTrue(matches(self.by_id['42432246'], treatments=['treatment_covariates_not_efficacy']))
        self.assertFalse(matches(self.by_id['42432246'], treatments=['ici_mono']))


if __name__ == '__main__':
    unittest.main()
