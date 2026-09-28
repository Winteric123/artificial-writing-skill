import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'scripts'))

from check_skill_health import check, check_inventory, check_links, check_project_membership


class SkillHealth(unittest.TestCase):
    def test_live_health_keeps_scientific_and_behavioral_acceptance_separate(self):
        result = check(ROOT)
        self.assertEqual(result['status'], 'mechanical_checks_passed')
        self.assertFalse(result['scientific_acceptance_certified'])
        self.assertFalse(result['behavioral_evaluation_performed'])
        self.assertEqual(result['project']['unique_articles'], result['project']['core'] + result['project']['support'])

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

    def test_support_promotion_and_missing_evidence_are_detected(self):
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
            self.assertIn('Project core tier differs from authoritative highlight membership', errors)
            self.assertTrue(any('invalid evidence path' in error for error in errors))


if __name__ == '__main__':
    unittest.main()
