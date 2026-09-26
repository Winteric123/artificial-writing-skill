import csv
import unittest
from pathlib import Path


REFERENCES = Path(__file__).resolve().parents[1] / 'references'


def rows(filename):
    with (REFERENCES / filename).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


class SourceIdentityCorrections(unittest.TestCase):
    def test_legacy_pmids_are_not_active_bibliography_keys(self):
        corrections = rows('source-identity-corrections.csv')
        bibliography = {row['pmid']: row for row in rows('ccr-corpus-bibliography.csv')}
        versions = {row['pmid']: row for row in rows('source-version-register.csv')}
        self.assertEqual({row['legacy_pmid'] for row in corrections}, {'37219515', '37154821'})
        self.assertEqual({row['correct_pmid'] for row in corrections}, {'37265412', '37227187'})
        for row in corrections:
            self.assertNotIn(row['legacy_pmid'], bibliography)
            self.assertIn(row['correct_pmid'], bibliography)
            self.assertIn(row['correct_pmid'], versions)
            self.assertEqual(bibliography[row['correct_pmid']]['doi'].casefold(), row['doi'].casefold())

    def test_types_and_roles_are_separate(self):
        bibliography = {row['pmid']: row for row in rows('ccr-corpus-bibliography.csv')}
        regulatory = bibliography['37265412']
        trial = bibliography['37227187']
        self.assertEqual(regulatory['ccr_official_category'], 'CCR Drug Updates')
        self.assertEqual(regulatory['primary_classification'], 'FDA approval summary / regulatory analysis')
        self.assertEqual(regulatory['source_role'], 'regulatory-analysis')
        self.assertEqual(trial['ccr_official_category'], 'Clinical Trials: Targeted Therapy')
        self.assertEqual(trial['primary_classification'], 'phase I clinical trial')
        self.assertEqual(trial['source_role'], 'primary-clinical')


if __name__ == '__main__':
    unittest.main()
