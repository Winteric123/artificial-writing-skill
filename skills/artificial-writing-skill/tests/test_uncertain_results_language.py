import json
import sys
import unittest
from pathlib import Path


sys.dont_write_bytecode = True
SKILL = Path(__file__).resolve().parents[1]
REFERENCES = SKILL / 'references'
sys.path.insert(0, str(SKILL / 'scripts'))

from search_language import load_index, search


def read_json(name):
    return json.loads((REFERENCES / name).read_text(encoding='utf-8'))


class WritingEvaluationStructure(unittest.TestCase):
    def setUp(self):
        self.payload = read_json('writing-evaluation-cases.json')
        self.cases = self.payload['cases']
        self.by_id = {case['id']: case for case in self.cases}

    def test_schema_and_unique_ids(self):
        self.assertEqual(
            set(self.payload),
            {'schema_version', 'case_set', 'scope', 'cases'},
        )
        self.assertIsInstance(self.payload['schema_version'], int)
        self.assertTrue(self.payload['case_set'])
        self.assertTrue(self.payload['scope'])
        self.assertEqual(len(self.by_id), len(self.cases))
        for case in self.cases:
            self.assertEqual(set(case), {'id', 'prompt', 'must_preserve', 'must_not'})
            self.assertRegex(case['id'], r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
            self.assertTrue(case['prompt'].strip())
            for field in ('must_preserve', 'must_not'):
                self.assertIsInstance(case[field], list)
                self.assertTrue(case[field])
                self.assertEqual(len(case[field]), len(set(case[field])))
                self.assertTrue(all(isinstance(item, str) and item.strip() for item in case[field]))

    def test_no_replacement_characters_in_behavioral_cases(self):
        serialized = json.dumps(self.payload, ensure_ascii=False)
        self.assertNotIn('\ufffd', serialized)

    def test_nonsignificant_and_unknown_status_are_separate_cases(self):
        required = {
            'nonsignificant-wide-ci-threshold',
            'nonsignificant-precise-near-null',
            'pilot-mechanism-does-not-rescue-clinical-endpoint',
            'negative-primary-exploratory-subgroup-signal',
            'statistical-significance-unreported',
        }
        self.assertTrue(required.issubset(self.by_id))
        unknown = ' '.join(self.by_id['statistical-significance-unreported']['must_preserve']).casefold()
        forbidden = ' '.join(self.by_id['statistical-significance-unreported']['must_not']).casefold()
        self.assertIn('cannot be determined', unknown)
        self.assertIn('nonsignificant', forbidden)
        self.assertIn('significant', forbidden)


class UncertainResultsResources(unittest.TestCase):
    def test_focused_guide_is_routed_and_exists(self):
        guide = REFERENCES / 'nonsignificant-results-language.md'
        self.assertTrue(guide.is_file())
        skill_text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('references/nonsignificant-results-language.md', skill_text)
        self.assertNotIn('\ufffd', guide.read_text(encoding='utf-8'))

    def test_retrieval_taxonomy_keeps_unknown_status_distinct(self):
        concepts = {item['id']: item['terms'] for item in read_json('retrieval-vocabulary.json')['concepts']}
        self.assertIn('nonsignificance', concepts)
        self.assertIn('statistical-significance-undetermined', concepts)
        self.assertIn('informative-inconclusive-result', concepts)
        self.assertNotEqual(
            set(concepts['nonsignificance']),
            set(concepts['statistical-significance-undetermined']),
        )

    def test_usage_cards_define_value_and_boundaries(self):
        cards = {item['id']: item for item in read_json('language-usage-cards.json')['cards']}
        informative = cards['informative-inconclusive-result']
        unknown = cards['statistical-significance-undetermined']
        for card in (informative, unknown):
            self.assertEqual(
                set(card),
                {
                    'id', 'match_terms', 'zh', 'sections', 'use_when',
                    'confusable', 'safe_example', 'unsafe_example', 'boundary', 'basis',
                },
            )
            self.assertTrue(all(card[field] for field in card))
            self.assertTrue((REFERENCES / card['basis']).is_file())
        self.assertRegex(informative['boundary'].casefold(), r'阈值|threshold|区间|interval')
        self.assertRegex(unknown['unsafe_example'].casefold(), r'nonsignificant')


class UncertainResultsRetrieval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries, cls.manifest = load_index(SKILL)

    def test_unknown_significance_bilingual_queries_return_same_editorial_card(self):
        chinese = search(self.entries, query='统计学意义无法判断', limit=5)
        english = search(self.entries, query='statistical significance could not be determined', limit=5)
        chinese_ids = {card['id'] for card in chinese['editorial_cards']}
        english_ids = {card['id'] for card in english['editorial_cards']}
        self.assertEqual(chinese_ids, english_ids)
        self.assertIn('statistical-significance-undetermined', chinese_ids)
        self.assertGreater(chinese['editorial_card_count'], 0)

    def test_informative_card_has_real_statistical_hits_without_fusion_false_positive(self):
        attached = [
            entry for entry in self.entries
            if 'informative-inconclusive-result' in entry['usage_card_ids']
        ]
        self.assertTrue(attached)
        self.assertTrue(any(
            phrase in entry['expression'].casefold()
            for entry in attached
            for phrase in ('statistically inconclusive', 'wide confidence interval', 'interval did not exclude')
        ))
        fusion = next(
            entry for entry in self.entries
            if entry['stable_id'] == 'ccr-lang-5c60b8e93633ab4f09a0'
        )
        self.assertNotIn('informative-inconclusive-result', fusion['usage_card_ids'])

    def test_nonsignificance_and_undetermined_editorial_concepts_do_not_merge(self):
        nonsignificant = {
            card['id'] for card in search(self.entries, query='未达到统计学显著性', limit=5)['editorial_cards']
        }
        undetermined = {
            card['id'] for card in search(self.entries, query='统计学意义无法判断', limit=5)['editorial_cards']
        }
        self.assertIn('null-result', nonsignificant)
        self.assertIn('statistical-significance-undetermined', undetermined)
        self.assertNotIn('statistical-significance-undetermined', nonsignificant)
        self.assertNotIn('null-result', undetermined)


if __name__ == '__main__':
    unittest.main()
