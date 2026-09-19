import copy
import csv
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / 'scripts'))

from build_language_index import apply_controls, stable_id
from build_library_index import build, related_formal_state
from library_common import atomic_json, journal_registry, read_csv, read_json, reference_path
from search_language import load_index, search
from validate_reading_quality import validate


def synthetic_entry():
    return dict(stable_id='test-lang-one', journal_id='test', journal='Synthetic journal', expression='co-mutation pattern',
                source_article_ids='99990001;99990002', source_asset='synthetic.md', source_line='2',
                source_heading='Results', source_container='', primary_section='results', secondary_sections='abstract-results',
                provenance_granularity='batch-synthesis', domain='genomics', function='comparison', unit_type='vocabulary',
                evidence_tier='observational', retrieval_state='usable', usage_cards=[],
                source_articles=[dict(pmid='99990001', year='2025', highlight=False, review_status='not_reviewed'),
                                 dict(pmid='99990002', year='2026', highlight=True, review_status='not_reviewed')])


class RetrievalInvariants(unittest.TestCase):
    def test_stable_identity_ignores_row_position(self):
        first = synthetic_entry()
        second = {**first, 'entry_id': 'legacy-999', 'source_line': '600', 'catalog_version': 'new'}
        self.assertEqual(stable_id('test', first), stable_id('test', second))

    def test_identity_changes_with_expression_or_source(self):
        first = synthetic_entry()
        for field, value in [('expression', 'another expression'), ('source_article_ids', '99990003')]:
            self.assertNotEqual(stable_id('test', first), stable_id('test', {**first, field: value}))

    def test_holds_excluded_by_default(self):
        entry = synthetic_entry()
        for state in ('needs_source_check', 'quarantined'):
            entry['retrieval_state'] = state
            self.assertEqual(search([entry])['matched_count'], 0)
            self.assertEqual(search([entry], include_held=True)['matched_count'], 1)

    def test_control_precedence_and_alert_propagation(self):
        entry = synthetic_entry()
        controls = dict(article_alerts=[dict(article_ids=['99990001'], restriction='Synthetic restriction')], entry_rules=[
            dict(id='block', state='quarantined', article_ids=['99990001'], expression_regex='co-mutation'),
            dict(id='hold', state='needs_source_check', article_ids=['99990002'], expression_regex='pattern')])
        result = apply_controls(entry, controls)
        self.assertEqual(result['retrieval_state'], 'quarantined')
        self.assertEqual(len(result['source_alerts']), 1)

    def test_year_highlight_and_pmid_match_same_article(self):
        entry = synthetic_entry()
        self.assertEqual(search([entry], year='2025', highlight=True)['matched_count'], 0)
        self.assertEqual(search([entry], year='2026', pmid='99990001')['matched_count'], 0)
        self.assertEqual(search([entry], year='2026', highlight=True)['matched_count'], 1)

    def test_batch_not_single_paper(self):
        self.assertEqual(search([synthetic_entry()], single_paper=True)['matched_count'], 0)

    def test_review_not_inferred_from_language_presence(self):
        entry = synthetic_entry()
        self.assertEqual(search([entry], reviewed=True)['matched_count'], 0)
        entry['source_articles'][0]['review_status'] = 'passed'
        self.assertEqual(search([entry], reviewed=True)['matched_count'], 0)

    def test_abstract_routes_components(self):
        self.assertEqual(search([synthetic_entry()], section='Abstract')['matched_count'], 1)

    def test_journal_and_domain_filters(self):
        entry = synthetic_entry()
        self.assertEqual(search([entry], journal='ccr')['matched_count'], 0)
        self.assertEqual(search([entry], domain='proteomics')['matched_count'], 0)
        self.assertEqual(search([entry], journal='test', domain='genomics')['matched_count'], 1)

    def test_chinese_usage_card_retrieval(self):
        entry = synthetic_entry()
        entry['usage_cards'] = [dict(zh='共突变', use_when='条件人群')]
        self.assertEqual(search([entry], query='共突变 条件人群')['matched_count'], 1)

    def test_limit_validation(self):
        with self.assertRaises(ValueError):
            search([], limit=0)

    def test_stable_id_lookup(self):
        self.assertEqual(search([synthetic_entry()], entry_id='test-lang-one')['matched_count'], 1)
        self.assertEqual(search([synthetic_entry()], entry_id='test-lang-absent')['matched_count'], 0)

    def test_safe_terms_not_held_for_source_numeric_conflict(self):
        entry = synthetic_entry()
        entry.update(source_article_ids='41619904', expression='multivariable hazard ratio')
        controls = read_json(SKILL / 'references/language-controls.json')
        self.assertEqual(apply_controls(entry, controls)['retrieval_state'], 'usable')
        self.assertTrue(entry['source_alerts'])

    def test_actual_invalid_atm_trio_rule(self):
        entry = synthetic_entry()
        entry.update(source_article_ids='37733794', expression='HR 0.731 (95% CI 0.899–1.038)')
        controls = read_json(SKILL / 'references/language-controls.json')
        self.assertEqual(apply_controls(entry, controls)['retrieval_state'], 'quarantined')

    def test_preprint_and_formal_version_independent(self):
        preprint = dict(related_pmid='99990001', related_doi='10.synthetic/formal', reading_stage='main_text_deep_read_complete', formal_version_read='no')
        original = copy.deepcopy(preprint)
        self.assertEqual(related_formal_state(preprint, {}), 'not_indexed')
        formal = dict(doi='10.synthetic/formal', reading_stage='indexed')
        self.assertEqual(related_formal_state(preprint, {'99990001': formal}), 'indexed')
        formal['reading_stage'] = 'main_text_deep_read_complete'
        self.assertEqual(related_formal_state(preprint, {'99990001': formal}), 'main_text_deep_read_complete')
        self.assertEqual(preprint, original)

    def test_preprint_doi_mismatch_rejected(self):
        with self.assertRaises(ValueError):
            related_formal_state(dict(related_pmid='99990001', related_doi='10.synthetic/formal'), {'99990001': dict(doi='10.synthetic/other', reading_stage='indexed')})

    def test_real_index_integrity_and_journal_isolation(self):
        entries, manifest = load_index(SKILL)
        self.assertEqual(len(entries), manifest['entry_count'])
        self.assertEqual(len(entries), len({entry['stable_id'] for entry in entries}))
        results = search(entries, journal='jto', highlight=True, section='methods', limit=5)['entries']
        self.assertTrue(results)
        self.assertTrue(all(entry['journal_id'] == 'jto' for entry in results))
        self.assertTrue(all(entry['source_alerts'] for entry in results))


class IsolatedMaintenance(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='writing-skill-test-')
        self.skill = Path(self.temporary.name).resolve() / 'skill'
        shutil.copytree(SKILL / 'references', self.skill / 'references')

    def tearDown(self):
        self.temporary.cleanup()

    def test_stale_controls_fail_closed(self):
        path = self.skill / 'references' / 'language-controls.json'
        controls = read_json(path)
        controls['test_change'] = True
        atomic_json(path, controls)
        with self.assertRaisesRegex(ValueError, 'Stale language index'):
            load_index(self.skill)

    def test_missing_dependency_fail_closed(self):
        with self.assertRaises(ValueError):
            reference_path(self.skill, '../outside.md')

    def test_new_journal_is_configuration_driven(self):
        references = self.skill / 'references'
        config_path = references / 'journal-registry.json'
        registry = read_json(config_path)
        bibliography = read_csv(references / 'jto-stk11-priority-bibliography.csv')[0]
        quality = read_csv(references / 'jto-reading-quality-register.csv')[0]
        quality = {**quality, 'pmid': bibliography['pmid'], 'year': bibliography['year'], 'title': bibliography['title']}
        for name, row in [('synthetic-bibliography.csv', bibliography), ('synthetic-quality.csv', quality)]:
            with (references / name).open('w', encoding='utf-8', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=list(row))
                writer.writeheader()
                writer.writerow(row)
        (references / 'synthetic-ledger.md').write_text(f'| {quality["pmid"]} | {quality["main_read_completed_on"]} | synthetic test |\n', encoding='utf-8')
        registry['journals']['synthetic'] = dict(name='Synthetic', bibliography='synthetic-bibliography.csv', ledger='synthetic-ledger.md', quality='synthetic-quality.csv')
        atomic_json(config_path, registry)
        self.assertIn('synthetic', journal_registry(self.skill))
        self.assertEqual(validate(self.skill)['journals']['synthetic']['registered'], 1)

    def test_bad_preprint_does_not_partially_rewrite_inventory(self):
        references = self.skill / 'references'
        output_names = ('library-index.csv', 'library-index.md', 'library-summary.json', 'ccr-category-index.md')
        originals = {name: (references / name).read_bytes() for name in output_names}
        preprints = read_csv(references / 'preprint-source-register.csv')
        preprints[0]['related_pmid'] = '32709715'
        with (references / 'preprint-source-register.csv').open('w', encoding='utf-8', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(preprints[0]))
            writer.writeheader()
            writer.writerows(preprints)
        with self.assertRaisesRegex(ValueError, 'DOI mismatch'):
            build(self.skill)
        self.assertEqual(originals, {name: (references / name).read_bytes() for name in output_names})


if __name__ == '__main__':
    unittest.main()
