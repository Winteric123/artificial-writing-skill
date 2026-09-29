import csv
import json
import unittest
from collections import Counter
from pathlib import Path


REFERENCES = Path(__file__).resolve().parents[1] / 'references'


def records(filename):
    with (REFERENCES / filename).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


class JtoScopeExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((REFERENCES / 'jto-maintenance-expansion-2026-09-29.json').read_text(encoding='utf-8'))
        cls.queue = records('jto-maintenance-queue.csv')
        cls.by_id = {row['pmid']: row for row in cls.queue}
        cls.library = {row['pmid']: row for row in records('library-index.csv')}
        cls.existing = set(cls.manifest['existing_pmids'])
        cls.added = set(cls.manifest['new_pmids'])

    def test_expansion_retains_historical_directory(self):
        self.assertEqual(len(self.queue), len(self.by_id))
        self.assertFalse(self.existing & self.added)
        self.assertEqual(len(self.existing), 137)
        self.assertEqual(len(self.added), 163)
        self.assertEqual(len(self.existing | self.added), self.manifest['count'])
        self.assertTrue(self.existing | self.added <= self.by_id.keys())
        baseline = [self.by_id[pmid] for pmid in self.existing | self.added]
        self.assertEqual(Counter(row['selection_role'] for row in baseline), self.manifest['roles'])

    def test_new_screening_does_not_promote_reading_or_highlights(self):
        self.assertEqual(self.manifest['new_fulltext_reads'], 0)
        self.assertEqual(self.manifest['new_highlights'], 0)
        self.assertEqual(self.manifest['new_acceptances'], 0)
        for pmid in self.added:
            row = self.by_id[pmid]
            self.assertEqual(row['maintenance_added_on'], self.manifest['checked_on'])
            self.assertIn(row['screening_level_current'], {
                'metadata_title_screened_not_fulltext_read', 'metadata_and_abstract_scope_screened'
            })
            if row['main_read_completed_on']:
                self.assertIn(pmid, self.library)
                self.assertEqual(row['main_read_completed_on'], self.library[pmid]['main_read_completed_on'])
                self.assertGreaterEqual(row['main_read_completed_on'], self.manifest['checked_on'])
            else:
                self.assertEqual(row['reading_stage'], 'not_registered_as_deep_read')
                self.assertNotEqual(row['review_status'], 'passed')

    def test_source_identity_and_public_links(self):
        for pmid in self.existing | self.added:
            row = self.by_id[pmid]
            self.assertEqual(row['journal'], 'Journal of Thoracic Oncology')
            self.assertIn(row['year'], {'2023', '2024', '2025', '2026'})
            self.assertTrue(row['chinese_title'])
            self.assertTrue(row['title'])
            self.assertEqual(row['pubmed_url'], f'https://pubmed.ncbi.nlm.nih.gov/{pmid}/')
            self.assertEqual(row['doi_url'], f"https://doi.org/{row['doi']}")
            self.assertTrue(row['doi'].startswith('10.1016/j.jtho.'))
            self.assertNotIn('\\', row['local_pdf_filename'])
            self.assertNotIn('/', row['local_pdf_filename'])
            if row['local_pdf_sha256']:
                self.assertRegex(row['local_pdf_sha256'], r'^[a-f0-9]{64}$')

    def test_genre_and_pending_eligibility_boundaries(self):
        for pmid in {'40464729', '41833817', '42508690'}:
            self.assertNotIn(pmid, self.by_id)
        expected = {
            'background': ('R', 'background_only_not_original_language_learning'),
            'case_reference': ('S', 'case_reference_not_original_cohort_learning'),
            'eligibility_pending': ('Q', 'eligibility_pending_not_original_language_learning'),
        }
        for row in self.queue:
            if row['selection_role'] in expected:
                group, scope = expected[row['selection_role']]
                self.assertEqual((row['group'], row['maintenance_scope']), (group, scope))
        for pmid in {'41563233', '42336204'}:
            self.assertEqual(self.by_id[pmid]['selection_role'], 'eligibility_pending')
            self.assertTrue(self.by_id[pmid]['selection_note'])

    def test_observations_and_diagnostic_methods_keep_cautions(self):
        for pmid in {'41747891', '38762120', '36503175', '42229634', '42697511', '41791703'}:
            self.assertTrue(self.by_id[pmid]['selection_note'], pmid)

    def test_published_directory_covers_every_expansion_record(self):
        content = (REFERENCES / 'jto-maintenance-queue.md').read_text(encoding='utf-8')
        for pmid in self.existing | self.added:
            row = self.by_id[pmid]
            self.assertIn(f"[{pmid}]({row['pubmed_url']})", content)
            self.assertIn(row['doi_url'], content)
        self.assertNotIn('file:///', content)
        self.assertNotIn('C:\\Users\\', content)
        self.assertNotIn('D:\\', content)


if __name__ == '__main__':
    unittest.main()
