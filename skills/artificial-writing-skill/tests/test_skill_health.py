import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'scripts'))

from check_skill_health import (
    check,
    check_ccr_results_logic,
    check_inventory,
    check_links,
    check_project_membership,
    check_sentence_templates,
)


class SkillHealth(unittest.TestCase):
    def test_live_health_keeps_scientific_and_behavioral_acceptance_separate(self):
        result = check(ROOT)
        self.assertEqual(result['status'], 'mechanical_checks_passed')
        self.assertFalse(result['scientific_acceptance_certified'])
        self.assertFalse(result['behavioral_evaluation_performed'])
        self.assertEqual(result['project']['unique_articles'], result['project']['highlights'])
        self.assertEqual(result['project']['highlights'], 64)
        self.assertEqual((result['project']['legacy_core'], result['project']['legacy_support']), (13, 51))
        self.assertEqual(result['sentence_templates']['papers'], 15)
        self.assertTrue(result['sentence_templates']['fulltext_coverage'])
        self.assertEqual(result['ccr_results_logic']['papers'], 123)
        self.assertEqual(
            (result['ccr_results_logic']['year_2025'], result['ccr_results_logic']['year_2026']),
            (48, 75),
        )

    def test_sentence_source_identity_corruption_is_reported_by_health(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            shutil.copytree(ROOT / 'references', root / 'references')
            path = root / 'references/stk11-ccr-sentence-templates.json'
            catalog = json.loads(path.read_text(encoding='utf-8'))
            catalog['records'][0]['source']['pdf_sha256'] = '0' * 64
            path.write_text(json.dumps(catalog), encoding='utf-8')
            errors = check_sentence_templates(root)['errors']
            self.assertTrue(any('pdf_sha256 disagrees' in error for error in errors))

    def test_ccr_results_logic_source_identity_corruption_is_reported_by_health(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            shutil.copytree(ROOT / 'references', root / 'references')
            path = root / 'references/ccr-2025-2026-results-logic.json'
            catalog = json.loads(path.read_text(encoding='utf-8'))
            pmid = catalog['papers'][0]['pmid']
            catalog['papers'][0]['pdf_sha256'] = '0' * 64
            for record in catalog['records']:
                if record['pmid'] == pmid:
                    record['source']['pdf_sha256'] = '0' * 64
            path.write_text(json.dumps(catalog), encoding='utf-8')
            errors = check_ccr_results_logic(root)['errors']
            self.assertTrue(any('PDF hash disagrees' in error for error in errors))

    def test_missing_and_escaping_links_are_detected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            (root / 'references').mkdir()
            (root / 'assets').mkdir()
            (root / 'references/good.md').write_text('# Good', encoding='utf-8')
            (root / 'SKILL.md').write_text('[good](references/good.md#section) [missing](references/missing.md) [outside](../outside.md) [web](https://example.org) [anchor](#local)', encoding='utf-8')
            result = check_links(root)
            self.assertEqual(result['checked'], 3)
            self.assertEqual(len(result['broken']), 2)

    def test_stale_inventory_and_summary_are_detected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            shutil.copytree(ROOT / 'references', root / 'references')
            path = root / 'references/library-summary.json'
            summary = json.loads(path.read_text(encoding='utf-8-sig'))
            summary['included'] += 1
            path.write_text(json.dumps(summary), encoding='utf-8')
            self.assertIn('Stale summary: included', check_inventory(root)['errors'])

    def test_legacy_tier_mutation_and_missing_evidence_are_detected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            shutil.copytree(ROOT / 'references', root / 'references')
            path = root / 'references/stk11-writing-reference-map.json'
            mapping = json.loads(path.read_text(encoding='utf-8'))
            support = next(record for record in mapping['records'] if record['tier'] == 'topic_support')
            support['tier'] = 'core_highlight'
            support['source_refs'] = ['../not-a-source.md']
            path.write_text(json.dumps(mapping), encoding='utf-8')
            errors = check_project_membership(root)['errors']
            self.assertIn('Historical STK11 highlight tier counts changed', errors)
            self.assertTrue(any('invalid evidence path' in error for error in errors))


if __name__ == '__main__':
    unittest.main()
