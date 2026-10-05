"""Regression boundaries for the 18-paper local-PDF STK11 reconciliation."""

import csv
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1]
REFS = SKILL / 'references'
PMIDS = {'26833127', '28538732', '30297358', '31040157', '32312757', '32649874',
         '34740862', '36150391', '36793385', '38330261', '38877143', '38997257',
         '39207369', '39637943', '40198901', '40645185', '40749670', '40830141'}
STRICT = PMIDS - {'38330261', '36793385'}
LIVE_PASSED = {'34740862', '36150391'}
REVIEW_METADATA = {
    '34740862': ('independent_agent_source_recheck', '2026-10-02'),
    '36150391': ('same_agent_source_recheck', '2026-10-02'),
}


def rows(name):
    with (REFS / name).open(encoding='utf-8-sig', newline='') as source:
        return list(csv.DictReader(source))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class LocalUnreadReconciliation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = rows('stk11-2026-10-02-local-unread-intake.csv')
        cls.intake = {row['pmid']: row for row in cls.manifest}
        cls.library = {row['pmid']: row for row in rows('library-index.csv')}
        cls.registry = json.loads((REFS / 'journal-registry.json').read_text(encoding='utf-8'))['journals']
        cls.locators = json.loads((REFS / 'source-pdf-locators.json').read_text(encoding='utf-8'))
        cls.scopes = json.loads((REFS / 'source-scope-backfill.json').read_text(encoding='utf-8'))['articles']
        cls.vocabulary = json.loads((REFS / 'retrieval-vocabulary.json').read_text(encoding='utf-8'))
        cls.coalteration = json.loads((REFS / 'coalteration-annotations.json').read_text(encoding='utf-8'))['articles']
        cls.membership = {row['pmid']: row for row in json.loads((REFS / 'stk11-writing-reference-map.json').read_text(encoding='utf-8'))['records']}
        cls.tags = {row['pmid']: row for row in json.loads((REFS / 'stk11-assay-treatment-tags.json').read_text(encoding='utf-8'))['records']}
        cls.catalog_rows = []
        cls.quality = {}
        for configuration in cls.registry.values():
            # Preserve the historical intake's exact language assets; later version addenda are tested separately.
            cls.catalog_rows.extend(row for row in rows(configuration['language_catalog']) if row['source_article_ids'] in PMIDS and row['source_asset'] == cls.intake[row['source_article_ids']]['language_note'])
            cls.quality.update({row['pmid']: row for row in rows(configuration['quality']) if row['pmid'] in PMIDS})

    def test_exact_batch_and_false_positive_boundary(self):
        self.assertEqual({row['pmid'] for row in self.manifest}, PMIDS)
        for pmid in PMIDS:
            with self.subTest(pmid=pmid):
                self.assertEqual(self.intake[pmid]['jif_over_10_in_2025_snapshot'], 'yes' if pmid in STRICT else 'no')
        self.assertNotIn('17676035', {row['pmid'] for row in self.manifest})

    def test_intake_snapshot_is_separate_from_live_review_status(self):
        for pmid in PMIDS:
            with self.subTest(pmid=pmid):
                row = self.library[pmid]
                self.assertEqual(row['reading_stage'], 'main_text_deep_read_complete')
                self.assertEqual(row['main_read_completed_on'], '2026-10-02')
                expected_review = 'passed' if pmid in LIVE_PASSED else 'not_reviewed'
                self.assertEqual(row['review_status'], expected_review)
                self.assertEqual(row['stk11_highlight'], 'no')
                manifest = self.intake[pmid]
                # This manifest records intake, not a later independent source recheck.
                self.assertEqual(manifest['review_status'], 'not_reviewed')
                self.assertGreaterEqual(int(manifest['language_units']), 6)
                self.assertTrue((REFS / manifest['reading_note']).is_file())
                self.assertTrue((REFS / manifest['language_note']).is_file())
                quality = self.quality[pmid]
                self.assertEqual(quality['review_status'], expected_review)
                for gate in ('coverage_check', 'evidence_check', 'results_check', 'language_check', 'traceability_check', 'transfer_check'):
                    self.assertEqual(quality[gate], 'pass' if pmid in LIVE_PASSED else 'pending')
                if pmid in LIVE_PASSED:
                    self.assertEqual((quality['review_method'], quality['reviewed_on']),
                                     REVIEW_METADATA[pmid])
                    self.assertTrue((REFS / quality['review_record']).is_file())

    def test_new_journals_have_isolated_assets(self):
        expected = {'cancer-research', 'nature-communications', 'esmo-open', 'nature-metabolism',
                    'cell', 'jco-precision-oncology', 'jto-crr'}
        self.assertTrue(expected <= set(self.registry))
        for journal in expected:
            with self.subTest(journal=journal):
                for field in ('bibliography', 'ledger', 'quality', 'language_catalog'):
                    self.assertTrue((REFS / self.registry[journal][field]).is_file())

    def test_candidate_snapshot_now_has_expected_completion_counts(self):
        candidates = json.loads((REFS / 'stk11-reference-candidates.json').read_text(encoding='utf-8'))['records']
        strict = [row for row in candidates if row['jif_over_10']]
        appendix = [row for row in candidates if not row['jif_over_10']]
        self.assertEqual((len(strict), len(appendix)), (80, 4))
        later = json.loads((REFS / 'supplement-ccr-2026-10-02-intake.json').read_text(encoding='utf-8'))
        new = {row['pmid'] for row in later['records'] if row['new_to_library']}
        self.assertEqual(sum(self.library.get(row['pmid'], {}).get('reading_stage') == 'main_text_deep_read_complete' for row in strict), 48 + len(new & {r['pmid'] for r in strict}))
        self.assertEqual(sum(self.library.get(row['pmid'], {}).get('reading_stage') == 'main_text_deep_read_complete' for row in appendix), 2 + len(new & {r['pmid'] for r in appendix}))

    def test_language_locators_resolve_to_exact_lines(self):
        counts = Counter(row['source_article_ids'] for row in self.catalog_rows)
        self.assertEqual(counts, Counter({pmid: int(self.intake[pmid]['language_units']) for pmid in PMIDS}))
        self.assertEqual(Counter(row['unit_type'] for row in self.catalog_rows),
                         Counter({'collocation': 108, 'sentence-frame': 69, 'paragraph-model': 18, 'vocabulary': 17}))
        locator_rows = {}
        for record in self.locators['entries'].values():
            locator_rows.setdefault((record['source_article_ids'], record['expression']), []).append(record)
        explicit_locator_count = 0
        for row in self.catalog_rows:
            lines = (REFS / row['source_asset']).read_text(encoding='utf-8-sig').splitlines()
            self.assertIn(row['expression'], lines[int(row['source_line']) - 1])
            self.assertIn('source_locator', row)
            self.assertTrue(row['source_locator'])
            pages = {int(value) for value in __import__('re').findall(r'(?i)(?:physical\s+)?p(?:p)?\.?\s*(\d+)', row['source_locator'])}
            if pages:
                explicit_locator_count += 1
                matches = locator_rows[(row['source_article_ids'], row['expression'])]
                recorded = {page for match in matches for hint in match['recorded_page_hints'] for page in hint['recorded_pages']}
                self.assertTrue(pages <= recorded, (row['entry_id'], pages, recorded))
        self.assertGreater(explicit_locator_count, 0)

    def test_pdf_identity_scope_and_membership_are_complete(self):
        facet_groups = {'disease_ids': 'diseases', 'tissue_ids': 'tissues', 'model_ids': 'models', 'use_roles': 'roles'}
        for pmid in PMIDS:
            with self.subTest(pmid=pmid):
                manifest = self.intake[pmid]
                source = self.locators['sources'][pmid]
                self.assertEqual(source['sha256'], manifest['sha256'])
                self.assertEqual(source['physical_pages'], int(manifest['physical_pages']))
                self.assertEqual(source['identity_check'], 'registered-sha256-match')
                scope = self.scopes[pmid]
                self.assertEqual(scope['source_sha256'], manifest['sha256'])
                for field, group in facet_groups.items():
                    self.assertTrue(scope[field])
                    self.assertTrue(set(scope[field]) <= set(self.vocabulary[group]))
                    self.assertEqual(scope['facet_status'][field], 'identified-not-exhaustive')
                    self.assertEqual(self.library[pmid]['source_' + field], ';'.join(scope[field]))
                membership = self.membership[pmid]
                self.assertEqual(membership['tier'], 'topic_support')
                self.assertFalse(membership['in_cross_gene_16'])
                self.assertTrue(membership['source_refs'])
                tag = self.tags[pmid]
                self.assertEqual(tag['pdf_sha256'], manifest['sha256'])
                self.assertEqual(tag['evidence_sha256'], digest(REFS / tag['evidence']))
                self.assertEqual(set(tag['alteration_types']), set(self.coalteration[pmid]['alteration_types']))
                self.assertEqual(set(tag['gene_contexts']), {'+'.join(value) for value in self.coalteration[pmid]['gene_contexts']})

    def test_coalteration_boundaries_and_evidence_are_auditable(self):
        expected = {
            '36150391': ('context_only', 'analyzed'),
            '36793385': ('context_only', 'context_only'),
            '40830141': ('context_only', 'context_only'),
            '40198901': ('analyzed', 'analyzed'),
        }
        for pmid in PMIDS:
            with self.subTest(pmid=pmid):
                record = self.coalteration[pmid]
                if pmid in expected:
                    self.assertEqual((record['co_mutation_status'], record['co_alteration_status']), expected[pmid])
                else:
                    self.assertEqual((record['co_mutation_status'], record['co_alteration_status']), ('analyzed', 'analyzed'))
                self.assertEqual(record['pdf']['checked_context_pages'],
                                 [3, 4, 5, 6, 7, 8, 9, 10] if pmid == '34740862' else [])
                self.assertEqual(record['pdf']['sha256'], self.intake[pmid]['sha256'])
                self.assertTrue(record['evidence'])
                for evidence in record['evidence']:
                    path = REFS / evidence['source']
                    lines = path.read_text(encoding='utf-8-sig').splitlines()
                    self.assertEqual(evidence['source_sha256'], digest(path))
                    self.assertTrue(1 <= evidence['first_line'] <= evidence['last_line'] <= len(lines))
                    self.assertNotEqual((evidence['first_line'], evidence['last_line']), (1, len(lines)))

    def test_mixed_source_and_assay_tags_keep_their_boundaries(self):
        assays_407 = {item['assay'] for item in self.tags['40749670']['assays']}
        self.assertIn('global_proteomics', assays_407)
        self.assertIn('phosphoproteomics', assays_407)
        self.assertNotIn('targeted_protein', assays_407)
        self.assertTrue(all(item['origin'] == 'mixed_new_and_previous' for item in self.tags['40749670']['assays']))
        self.assertIn('spatial_protein', {item['assay'] for item in self.tags['39637943']['assays']})
        self.assertIn('clinical_outcomes', {item['assay'] for item in self.tags['40645185']['assays']})
        self.assertTrue({'gemcitabine', 'anti-PD-1', 'durvalumab'} <= set(self.tags['40645185']['drugs']))
        self.assertIn('mixed_new_and_previous', {item['origin'] for item in self.tags['38330261']['assays']})


if __name__ == '__main__':
    unittest.main()
