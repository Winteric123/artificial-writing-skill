import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from library_common import journal_registry, read_csv, read_json
from retrieval_metadata import contains_phrase
from search_language import load_index, search
from source_context_rechecks import attach_context_recheck, load_context_rechecks
from test_retrieval import synthetic_entry


class SourceContextRechecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries, cls.manifest = load_index(ROOT)
        cls.sources = read_json(ROOT / 'references/source-pdf-locators.json')['sources']
        cls.records = load_context_rechecks(ROOT, cls.sources)

    def test_selected_contexts_have_current_sources_and_no_quotation_promotion(self):
        historical = [record for record in self.records.values() if record['reviewed_on'] == '2026-09-28']
        self.assertEqual(len(historical), 139)
        self.assertEqual(len({record['pmid'] for record in historical}), 13)
        added = [record for record in self.records.values() if record['pmid'] == '34740862']
        self.assertEqual(len(added), 10)
        self.assertEqual(len(self.records), 149)
        by_id = {entry['stable_id']: entry for entry in self.entries}
        for identifier, record in self.records.items():
            with self.subTest(identifier=identifier):
                entry = by_id[identifier]
                self.assertEqual(entry['source_context_rechecks'], [record])
                self.assertFalse(record['quotation_verified'])
                self.assertFalse(entry['original_wording_verified'])
                self.assertEqual(record['review_method'], 'independent_agent_source_recheck'
                                 if record['pmid'] == '34740862' else 'same_agent_source_recheck')
                self.assertEqual(record['sha256'], self.sources[record['pmid']]['sha256'])

    def test_article_acceptance_does_not_imply_each_entry_was_context_checked(self):
        reviewed = search(self.entries, reviewed=True, include_held=True)['matched_count']
        contextual = search(self.entries, context_reviewed=True, include_held=True)['matched_count']
        self.assertEqual(contextual, len(self.records))
        self.assertGreater(reviewed, contextual)

    def test_context_filter_requires_same_contributing_article(self):
        entry = synthetic_entry()
        entry['source_context_rechecks'] = [{'pmid': '99990001'}]
        entry['source_locator'] = {'literal_matches': [{'pmid': '99990002'}]}
        self.assertEqual(search([entry], year='2025', context_reviewed=True)['matched_count'], 1)
        self.assertEqual(search([entry], year='2026', context_reviewed=True)['matched_count'], 0)
        self.assertEqual(search([entry], context_reviewed=True, pdf_located=True)['matched_count'], 0)
        entry['source_locator']['literal_matches'].append({'pmid': '99990001'})
        self.assertEqual(search([entry], context_reviewed=True, pdf_located=True)['matched_count'], 1)

    def test_tampered_context_rejected(self):
        data = read_json(ROOT / 'references/source-context-rechecks.json')
        changes = [('sha256', 'incorrect'), ('physical_pages', [99999]),
                   ('physical_pages', [0]), ('quotation_verified', True),
                   ('review_method', 'script_pass'), ('reviewed_on', 'yesterday')]
        for field, value in changes:
            with self.subTest(field=field, value=value):
                changed = copy.deepcopy(data)
                changed['entries'][0][field] = value
                with patch('source_context_rechecks.read_json', return_value=changed):
                    with self.assertRaises(ValueError):
                        load_context_rechecks(ROOT, self.sources)

    def test_changed_expression_requires_new_context_check(self):
        entry = copy.deepcopy(next(entry for entry in self.entries if entry['stable_id'] in self.records))
        entry['expression'] += ' changed'
        with self.assertRaisesRegex(ValueError, 'expression/source mismatch'):
            attach_context_recheck(entry, self.records)

    def test_only_highlights_are_accepted_by_this_recheck(self):
        expected = {record['pmid'] for record in self.records.values()
                    if record['reviewed_on'] == '2026-09-28'}
        quality = [row for configuration in journal_registry(ROOT).values()
                   for row in read_csv(ROOT / 'references' / configuration['quality'])]
        this_recheck = {row['pmid'] for row in quality if row['review_status'] == 'passed'
                        and row['reviewed_on'] == '2026-09-28'
                        and row['reviewer_id'] == 'codex-main-agent-2026-09-28'}
        self.assertEqual(this_recheck, expected)
        for row in quality:
            if row['pmid'] in expected:
                self.assertEqual(row['review_method'], 'same_agent_source_recheck')
                self.assertEqual(row['reviewed_on'], '2026-09-28')
        self.assertGreaterEqual(sum(row['eligibility'] == 'included' for row in quality), 289)

    def test_unsafe_rechecked_expressions_remain_held(self):
        examples = [('37097610', 'TP53/EGFR mutual depletion'),
                    ('41417462', 'multiplex immunofluorescence'),
                    ('41619904', 'median PFS was not reached')]
        for pmid, expression in examples:
            with self.subTest(pmid=pmid):
                entry = next(entry for entry in self.entries
                             if entry['source_article_ids'] == pmid and entry['expression'] == expression)
                self.assertNotEqual(entry['retrieval_state'], 'usable')
                self.assertEqual(search(self.entries, entry_id=entry['stable_id'])['matched_count'], 0)
                self.assertEqual(search(self.entries, entry_id=entry['stable_id'], include_held=True)['matched_count'], 1)

    def test_priority_standalone_paragraphs_are_indexed(self):
        expected = {'39864548', '41932614', '41619904', '42409117'}
        paragraphs = [entry for entry in self.entries if entry['journal_id'] == 'jto'
                      and entry['source_article_ids'] in expected and entry['unit_type'] == 'paragraph-model']
        self.assertEqual(len(paragraphs), 8)
        self.assertEqual({entry['source_article_ids'] for entry in paragraphs}, expected)

    def test_bilingual_cards_are_practical_and_phrase_scoped(self):
        cards = read_json(ROOT / 'references/language-usage-cards-rechecks.json')['cards']
        self.assertEqual(len(cards), 24)
        self.assertGreaterEqual(self.manifest['usage_card_count'], 77)
        for card in cards:
            for field in ('collocations', 'safe_example', 'unsafe_example', 'confusable', 'boundary'):
                self.assertTrue(card[field])
            self.assertTrue(any('\u4e00' <= character <= '\u9fff' for character in card['zh']))
        self.assertFalse(contains_phrase('the lowest response', 'WES'))
        self.assertTrue(contains_phrase('WES with a matched control', 'WES'))
        self.assertGreater(search(self.entries, query='条件比例')['matched_count'], 0)


if __name__ == '__main__':
    unittest.main()
