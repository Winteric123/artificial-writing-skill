import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'scripts'))

from retrieval_metadata import normalize_section
from search_language import load_index, search


class SectionAliases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries, _ = load_index(ROOT)

    def test_heading_and_chinese_aliases_return_identical_hits(self):
        groups = {
            'methods': ['Materials and Methods', 'Patients and Methods', 'Experimental Procedures', 'method', '材料与方法', '方法'],
            'results': ['result', '结果', '研究结果'],
            'discussion': ['disscussion', '讨论'],
            'conclusion': ['Conclusions', '结论'],
            'introduction': ['引言'],
            'title': ['标题'],
            'figure': ['Figure legends', '图注'],
        }
        for canonical, aliases in groups.items():
            expected = search(self.entries, section=canonical, limit=100)
            self.assertGreater(expected['matched_count'], 0)
            for alias in aliases:
                with self.subTest(section=canonical, alias=alias):
                    actual = search(self.entries, section=alias, limit=100)
                    self.assertEqual(actual['matched_count'], expected['matched_count'])
                    self.assertEqual([entry['stable_id'] for entry in actual['entries']], [entry['stable_id'] for entry in expected['entries']])

    def test_abstract_alias_preserves_component_scope(self):
        self.assertEqual(search(self.entries, section='摘要', limit=100), search(self.entries, section='abstract', limit=100))
        results = search(self.entries, section='摘要结果', limit=100)
        self.assertEqual(results, search(self.entries, section='abstract-results', limit=100))
        self.assertGreater(results['matched_count'], 0)
        self.assertLess(results['matched_count'], search(self.entries, section='abstract')['matched_count'])

    def test_alias_keeps_source_review_and_journal_constraints(self):
        options = dict(pmid='37097610', journal='ccr', reviewed=True, context_reviewed=True, limit=100)
        self.assertEqual(search(self.entries, section='结果', **options), search(self.entries, section='results', **options))
        self.assertEqual(search(self.entries, section='结果', pmid='37097610', journal='jto')['matched_count'], 0)

    def test_unknown_heading_does_not_fall_back_to_all_sections(self):
        self.assertEqual(normalize_section('Custom Heading'), 'custom-heading')
        self.assertEqual(search(self.entries, section='not-a-manuscript-section')['matched_count'], 0)
        self.assertEqual(normalize_section(''), '')


if __name__ == '__main__':
    unittest.main()
