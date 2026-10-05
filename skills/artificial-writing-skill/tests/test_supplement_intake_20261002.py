"""Regression guards for the user-scoped October 2 supplemental intake.

These checks validate recorded identities and retrieval behavior. They do not
certify scientific reading, independent review, or permission to delete PDFs.
"""

import csv
import hashlib
import json
import sys
import unittest
from collections import Counter
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1]
REFS = SKILL / 'references'
sys.path.insert(0, str(SKILL / 'scripts'))
from search_language import load_index, search
from search_stk11_references import load_records, matches


NEW_PMIDS = {'40057483', '42008781', '39694700', '41135949', '36512628',
             '37098232', '37100205', '37068173', '40882030', '41423267',
             '33853830', '34870237', '34045189', '33264619', '34341533'}
PMIDS = NEW_PMIDS | {'36150391'}
PARTIAL_SUPPLEMENTS = {'34870237', '33264619', '34341533'}
GATES = ('coverage_check', 'evidence_check', 'results_check', 'language_check',
         'traceability_check', 'transfer_check')
EXPECTED_REVIEWS = {
    '40057483': ('source-rechecks/2026-10-02-40057483.md', '/root/recheck_mechanisms_6', 'independent_agent_source_recheck', '2026-10-02'),
    '42008781': ('source-rechecks/2026-10-02-42008781.md', '/root/recheck_mechanisms_6', 'independent_agent_source_recheck', '2026-10-02'),
    '39694700': ('source-rechecks/2026-10-05-39694700.md', '/root/recheck_mechanisms_6', 'independent_agent_source_recheck', '2026-10-02'),
    '41135949': ('source-rechecks/2026-10-05-41135949.md', '/root/recheck_mechanisms_6', 'independent_agent_source_recheck', '2026-10-02'),
    '36512628': ('source-rechecks/2026-10-05-36512628.md', '/root/finish_36512628', 'independent_agent_source_recheck', '2026-10-05'),
    '37098232': ('source-rechecks/2026-10-02-37098232.md', '/root/recheck_clinical_5', 'independent_agent_source_recheck', '2026-10-02'),
    '37100205': ('source-rechecks/2026-10-02-37100205.md', '/root/recheck_clinical_5', 'independent_agent_source_recheck', '2026-10-02'),
    '37068173': ('source-rechecks/2026-10-05-37068173.md', '/root/recheck_clinical_5', 'independent_agent_source_recheck', '2026-10-02'),
    '40882030': ('source-rechecks/2026-10-02-40882030.md', '/root/recheck_clinical_5', 'independent_agent_source_recheck', '2026-10-02'),
    '41423267': ('source-rechecks/2026-10-02-41423267.md', '/root/recheck_clinical_5', 'independent_agent_source_recheck', '2026-10-02'),
    '33853830': ('source-rechecks/2026-10-05-33853830.md', '/root/finish_33853830', 'independent_agent_source_recheck', '2026-10-05'),
    '36150391': ('source-rechecks/2026-10-05-36150391.md', '/root', 'same_agent_source_recheck', '2026-10-02'),
    '34870237': ('source-rechecks/2026-10-05-34870237.md', '/root/final_behavior_run/blinded_responses', 'independent_agent_source_recheck', '2026-10-02'),
    '34045189': ('source-rechecks/2026-10-02-34045189.md', '/root/final_behavior_run/blinded_responses', 'independent_agent_source_recheck', '2026-10-02'),
    '33264619': ('source-rechecks/2026-10-02-33264619.md', '/root/final_behavior_run/blinded_responses', 'independent_agent_source_recheck', '2026-10-02'),
    '34341533': ('source-rechecks/2026-10-02-34341533.md', '/root/final_behavior_run/blinded_responses', 'independent_agent_source_recheck', '2026-10-02'),
}


def rows(name):
    with (REFS / name).open(encoding='utf-8-sig', newline='') as source:
        return list(csv.DictReader(source))


def data(name):
    return json.loads((REFS / name).read_text(encoding='utf-8-sig'))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SupplementalIntakeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = data('supplement-ccr-2026-10-02-intake.json')
        cls.intake = {row['pmid']: row for row in cls.manifest['records']}
        cls.library = {row['pmid']: row for row in rows('library-index.csv')}
        cls.versions = {row['pmid']: row for row in rows('source-version-register.csv')}
        cls.locators = data('source-pdf-locators.json')
        cls.registry = data('journal-registry.json')['journals']
        cls.tags = {row['pmid']: row for row in load_records(SKILL, True)}
        cls.entries, cls.index_manifest = load_index(SKILL)
        cls.quality = {}
        cls.catalog_rows = []
        note_assets = {row['note'] for row in cls.intake.values()}
        for journal in cls.registry.values():
            cls.quality.update({row['pmid']: row for row in rows(journal['quality'])
                                if row['pmid'] in PMIDS})
            cls.catalog_rows.extend(row for row in rows(journal['language_catalog'])
                                    if row['source_asset'] in note_assets)

    def test_exact_batch_and_user_deferred_source(self):
        self.assertEqual(set(self.intake), PMIDS)
        self.assertEqual({pmid for pmid, row in self.intake.items()
                          if row['new_to_library']}, NEW_PMIDS)
        self.assertEqual(sum(len(row['files']) for row in self.intake.values()), 17)
        self.assertEqual(len({row['journal_id'] for row in self.intake.values()}), 10)
        self.assertNotIn('ccr', {row['journal_id'] for row in self.intake.values()})
        self.assertEqual(self.intake['37068173']['files'],
                         ['nihms-1889724.pdf', 'nihms-1889724 (1).pdf'])
        self.assertEqual(len(self.manifest['skipped']), 1)
        skipped = self.manifest['skipped'][0]
        self.assertEqual((skipped['pmid'], skipped['file']), ('35504291', 'mmc3.pdf'))
        self.assertEqual(skipped['status'], 'skipped_by_user_incomplete')
        self.assertIs(skipped['source_preserved'], True)
        self.assertNotIn('35504291', self.library)
        self.assertNotIn('35504291', self.locators['sources'])
        self.assertEqual(search(self.entries, pmid='35504291', include_held=True)['matched_count'], 0)

    def test_intake_reading_and_later_live_acceptance_are_separate(self):
        overlay = self.manifest['review_overlay']
        self.assertIn('Intake-time snapshot', self.manifest['scope'])
        self.assertEqual(set(overlay['passed_pmids']), PMIDS)
        self.assertEqual(set(overlay['independent_agent_source_recheck_pmids']),
                         PMIDS - {'36150391'})
        self.assertEqual(set(overlay['same_agent_source_recheck_pmids']), {'36150391'})
        self.assertEqual(set(overlay['supplement_status']['not_supplied_pmids']),
                         PMIDS - PARTIAL_SUPPLEMENTS)
        self.assertEqual(set(overlay['supplement_status']['partially_reviewed_pmids']),
                         PARTIAL_SUPPLEMENTS)
        for pmid in PMIDS:
            with self.subTest(pmid=pmid):
                self.assertNotIn('review_status', self.intake[pmid])
                self.assertEqual(self.library[pmid]['reading_stage'],
                                 'main_text_deep_read_complete')
                self.assertEqual(self.library[pmid]['review_status'], 'passed')
                self.assertEqual(self.library[pmid]['stk11_highlight'], 'no')
                quality = self.quality[pmid]
                self.assertEqual(quality['review_status'], 'passed')
                for gate in GATES:
                    self.assertEqual(quality[gate], 'pass')
                review_record, reviewer, method, reviewed_on = EXPECTED_REVIEWS[pmid]
                self.assertEqual((quality['review_record'], quality['reviewer_id'],
                                  quality['review_method'], quality['reviewed_on']),
                                 (review_record, reviewer, method, reviewed_on))
                self.assertEqual(overlay['review_records'][pmid], review_record)
                self.assertTrue((REFS / review_record).is_file())
                self.assertGreater(search(self.entries, pmid=pmid, reviewed=True)['matched_count'], 0)
                self.assertEqual(search(self.entries, pmid=pmid, highlight=True)['matched_count'], 0)

    def test_supplement_and_pdf_version_boundaries(self):
        for pmid, record in self.intake.items():
            with self.subTest(pmid=pmid):
                expected = 'partially_reviewed' if pmid in PARTIAL_SUPPLEMENTS else 'not_supplied'
                self.assertEqual(record['supplement_status_for_supplied_version'], expected)
                self.assertEqual(self.library[pmid]['supplement_status'], expected)
                self.assertEqual(self.quality[pmid]['supplement_status'], expected)
                self.assertEqual(record['note_sha256'], digest(REFS / record['note']))
                if pmid in NEW_PMIDS:
                    self.assertEqual(self.versions[pmid]['sha256'], record['sha256'])
                    self.assertEqual(self.locators['sources'][pmid]['sha256'], record['sha256'])
                    self.assertEqual(self.locators['sources'][pmid]['physical_pages'], record['pages'])
        selected = self.versions['36150391']
        additional = self.intake['36150391']
        self.assertEqual((selected['supplied_pdf_version'], int(selected['physical_pages'])),
                         ('publisher_typeset_pdf', 26))
        self.assertEqual((additional['version'], additional['pages']), ('author_manuscript', 44))
        self.assertNotEqual(selected['sha256'], additional['sha256'])
        self.assertEqual(selected['archived_pdf_count'], '2')
        self.assertIn(additional['sha256'], selected['scope'])
        self.assertEqual(self.locators['sources']['36150391']['sha256'], selected['sha256'])
        self.assertEqual(self.locators['sources']['36150391']['physical_pages'], 26)
        self.assertEqual(self.tags['36150391']['pdf_sha256'], selected['sha256'])
        self.assertIn('no rechallenge evidence', self.tags['36150391']['boundary'])
        self.assertEqual(self.library['36150391']['supplement_status'], 'not_supplied')

    def test_exact_language_retention_and_source_lines(self):
        self.assertEqual(len(self.catalog_rows), 220)
        self.assertEqual({row['source_article_ids'] for row in self.catalog_rows}, PMIDS)
        self.assertEqual(Counter(row['unit_type'] for row in self.catalog_rows),
                         Counter({'sentence-frame': 126, 'collocation': 44,
                                  'vocabulary': 27, 'paragraph-frame': 23}))
        # Only this intake's note assets count: prior 36150391 language is not new.
        self.assertEqual(sum(row['source_article_ids'] == '36150391'
                             for row in self.catalog_rows), 12)
        for row in self.catalog_rows:
            with self.subTest(entry=row['entry_id']):
                record = self.intake[row['source_article_ids']]
                self.assertEqual(row['source_asset'], record['note'])
                lines = (REFS / row['source_asset']).read_text(encoding='utf-8-sig').splitlines()
                line = int(row['source_line'])
                self.assertTrue(1 <= line <= len(lines))
                self.assertIn(row['expression'], lines[line - 1])
                self.assertTrue(row['source_locator'])

    def test_section_retrieval_and_warnings_remain_attached(self):
        for pmid in PMIDS:
            with self.subTest(pmid=pmid):
                for section in ('methods', 'results'):
                    result = search(self.entries, pmid=pmid, section=section, limit=100)
                    self.assertGreater(result['matched_count'], 0, (pmid, section))
                    for entry in result['entries']:
                        self.assertIn(pmid, entry['matching_source_pmids'])
                        self.assertTrue(entry['source_alerts'], entry['stable_id'])
        for pmid in ('34341533', '37098232', '37100205', '37068173', '36150391',
                     '40882030', '41423267', '33853830'):
            self.assertGreater(search(self.entries, pmid=pmid, section='figure')['matched_count'], 0)

    def test_assay_filters_do_not_cross_origin_or_modality(self):
        self.assertTrue(matches(self.tags['41135949'], assays=['single_cell_rna'], origin='reanalysis'))
        self.assertFalse(matches(self.tags['41135949'], assays=['single_cell_rna'], origin='original'))
        self.assertTrue(matches(self.tags['40882030'], assays=['chip_seq'], origin='original'))
        self.assertFalse(matches(self.tags['40882030'], assays=['atac_seq']))
        self.assertTrue(matches(self.tags['41423267'], assays=['targeted_protein'], origin='original'))
        self.assertFalse(matches(self.tags['41423267'], assays=['global_proteomics']))
        self.assertTrue(matches(self.tags['37100205'], assays=['targeted_rna'], origin='original'))
        self.assertTrue(matches(self.tags['37100205'], assays=['spatial_protein'], origin='original'))
        self.assertFalse(matches(self.tags['37100205'], assays=['single_cell_rna']))
        self.assertFalse(matches(self.tags['37100205'], assays=['spatial_rna']))
        self.assertTrue(matches(self.tags['34341533'], assays=['atac_seq'], origin='original'))
        self.assertTrue(matches(self.tags['34341533'], assays=['atac_seq'], origin='reanalysis'))
        self.assertTrue(matches(self.tags['34341533'], assays=['single_cell_atac'], origin='original'))
        self.assertFalse(matches(self.tags['34341533'], assays=['single_cell_atac'], origin='reanalysis'))


if __name__ == '__main__':
    unittest.main()
