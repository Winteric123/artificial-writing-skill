"""Cross-entry-point regressions for live sentence reuse restrictions.

The private fixture copies only catalog authorities and their audit anchors.
No actual quality register, source PDF, or language-control file is modified.
"""

import copy
import csv
import hashlib
import importlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


sys.dont_write_bytecode = True
SKILL = Path(__file__).resolve().parents[1]
REFERENCES = SKILL / 'references'
SCRIPTS = SKILL / 'scripts'
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

CCR_CATALOG = 'ccr-2025-2026-results-logic.json'
STK_CATALOG = 'stk11-ccr-sentence-templates.json'
ROUTES = {
    'ccr': 'search_ccr_results_logic.py',
    'stk11': 'search_stk11_sentence_templates.py',
    'generic': 'search_source_sentence_templates.py',
}
LIVE_FIELDS = (
    'review_status', 'article_reuse_state', 'effective_reuse_state',
    'article_alerts', 'entry_rules', 'control_compatibility',
)


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def write_json(path, payload):
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')


def write_csv(path, rows):
    with path.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def cli(route, skill, *arguments, as_json=True):
    command = [sys.executable, '-X', 'utf8', '-B', str(SCRIPTS / ROUTES[route]),
               '--skill-path', str(skill)]
    if route == 'generic':
        command.extend(['--catalog', STK_CATALOG])
    command.extend(arguments)
    if as_json:
        command.append('--json')
    return subprocess.run(
        command, cwd=SKILL, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1',
                                 'PYTHONIOENCODING': 'utf-8'},
        capture_output=True, text=True, encoding='utf-8', check=False,
    )


class CurrentCorpusRegression(unittest.TestCase):
    def test_all_current_correction_sentences_and_papers_carry_current_alerts(self):
        catalog = read_json(REFERENCES / CCR_CATALOG)
        with (REFERENCES / 'ccr-reading-quality-register.csv').open(
            encoding='utf-8-sig', newline=''
        ) as stream:
            quality = {row['pmid']: row for row in csv.DictReader(stream)}
        affected = {
            item['pmid'] for item in catalog['records']
            if quality[item['pmid']]['review_status'] == 'needs_correction'
        }
        # Reproduce the concrete gap identified in the 2026-10-22 behavioral audit.
        self.assertEqual(len(affected), 10)
        self.assertEqual(sum(item['pmid'] in affected for item in catalog['records']), 20)
        for pmid in sorted(affected):
            for paper_mode in (False, True):
                with self.subTest(pmid=pmid, paper_mode=paper_mode):
                    arguments = ['--pmid', pmid]
                    if paper_mode:
                        arguments.append('--paper-logic')
                    result = cli('ccr', SKILL, *arguments)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    output = json.loads(result.stdout)
                    records = output['papers' if paper_mode else 'records']
                    self.assertTrue(records)
                    for record in records:
                        self.assertEqual(record['review_status'], 'needs_correction')
                        self.assertEqual(record['effective_reuse_state'], 'bounded_only')
                        self.assertTrue(any(
                            alert['source_reference'] == quality[pmid]['review_record']
                            for alert in record['article_alerts']
                        ))

    def test_current_accepted_partitions_exclude_corrections(self):
        for paper_mode, expected_count in ((False, 250), (True, 114)):
            with self.subTest(paper_mode=paper_mode):
                arguments = ['--accepted-only', '--limit', '500']
                if paper_mode:
                    arguments.append('--paper-logic')
                result = cli('ccr', SKILL, *arguments)
                self.assertEqual(result.returncode, 0, result.stderr)
                output = json.loads(result.stdout)
                self.assertEqual(output['matched_count'], expected_count)
                for item in output['papers' if paper_mode else 'records']:
                    self.assertEqual(item['review_status'], 'passed')
                    self.assertEqual(item['effective_reuse_state'], 'usable_with_boundary')


class LiveAuthorityCLIRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory(prefix='sentence-live-controls-')
        cls.skill = Path(cls.temporary.name) / 'skill'
        cls.references = cls.skill / 'references'
        cls.references.mkdir(parents=True)
        cls.ccr = read_json(REFERENCES / CCR_CATALOG)
        cls.stk = read_json(REFERENCES / STK_CATALOG)
        with (REFERENCES / 'ccr-reading-quality-register.csv').open(
            encoding='utf-8-sig', newline=''
        ) as stream:
            cls.quality = list(csv.DictReader(stream))
        status = {row['pmid']: row['review_status'] for row in cls.quality}
        overlap = ({record['pmid'] for record in cls.ccr['records']}
                   & {record['pmid'] for record in cls.stk['records']})
        cls.pmid = next(pmid for pmid in sorted(overlap) if status[pmid] == 'passed')
        cls.ccr_records = [record for record in cls.ccr['records'] if record['pmid'] == cls.pmid]
        cls.stk_records = [record for record in cls.stk['records'] if record['pmid'] == cls.pmid]
        cls.paper = next(paper for paper in cls.ccr['papers'] if paper['pmid'] == cls.pmid)
        filenames = {
            CCR_CATALOG, STK_CATALOG, 'library-index.csv', 'source-version-register.csv',
            'stk11-writing-reference-map.json', 'language-usage-cards.json',
            'language-usage-cards-rechecks.json',
        }
        for catalog in (cls.ccr, cls.stk):
            for record in catalog['records']:
                source = record['source']['verification_record'].partition('#')[0]
                if source.endswith('.md'):
                    filenames.add(source)
        for filename in filenames:
            target = cls.references / filename
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REFERENCES / filename, target)
        (cls.references / 'fixture-recheck.md').write_text(
            '# Fixture review\n\nTemporary restrictions for regression tests only.\n',
            encoding='utf-8',
        )
        cls.catalog_hashes = {
            name: hashlib.sha256((cls.references / name).read_bytes()).hexdigest()
            for name in (CCR_CATALOG, STK_CATALOG)
        }

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def setUp(self):
        write_csv(self.references / 'ccr-reading-quality-register.csv', self.quality)
        self.controls = {'schema_version': 1, 'article_alerts': [], 'entry_rules': []}
        self.save_controls()

    def tearDown(self):
        for name, expected in self.catalog_hashes.items():
            self.assertEqual(hashlib.sha256((self.references / name).read_bytes()).hexdigest(),
                             expected, 'Live checks must not rewrite catalog snapshots.')

    def save_controls(self):
        write_json(self.references / 'language-controls.json', self.controls)

    def update_quality(self, status, eligibility='included'):
        rows = copy.deepcopy(self.quality)
        row = next(row for row in rows if row['pmid'] == self.pmid)
        row.update(review_status=status, eligibility=eligibility,
                   review_record='fixture-recheck.md')
        write_csv(self.references / 'ccr-reading-quality-register.csv', rows)

    def add_alert(self):
        self.controls['article_alerts'] = [{
            'id': 'fixture-live-warning', 'article_ids': [self.pmid],
            'restriction': 'Do not transfer the disputed estimate; use the current recheck.',
            'source_reference': 'fixture-recheck.md',
        }]
        self.save_controls()

    def output(self, route, *arguments):
        result = cli(route, self.skill, *arguments)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def records(self, route, *arguments):
        output = self.output(route, '--pmid', self.pmid, *arguments)
        return output if route == 'generic' else output['records']

    @staticmethod
    def render_arguments(record):
        arguments = ['--template-id', record['id'], '--render']
        for slot in record['slots']:
            arguments.extend(['--slot', f'{slot["name"]}=USER_VALUE_{slot["name"]}'])
        return arguments

    def unique_source_phrase(self, record, other_records):
        other_text = json.dumps([self.paper, other_records], ensure_ascii=False).casefold()
        candidates = re.findall(r'[A-Za-z]+(?: [A-Za-z]+){3,8}',
                                record['source']['source_sentence'])
        phrase = next((value for value in candidates if value.casefold() not in other_text), None)
        self.assertIsNotNone(phrase, 'Choose a source-only phrase to test sentence-level scope.')
        return phrase

    def add_rule(self, expression, state='quarantined', identifier='fixture-expression-rule'):
        self.controls['entry_rules'].append({
            'id': identifier, 'article_ids': [self.pmid],
            'expression_regex': re.escape(expression), 'state': state,
            'reason': 'This specific expression requires source correction.',
            'source_reference': 'fixture-recheck.md',
        })
        self.save_controls()

    def test_status_and_alert_changes_reach_all_sentence_and_paper_routes(self):
        self.update_quality('needs_correction')
        self.add_alert()
        for route in ROUTES:
            with self.subTest(route=route):
                records = self.records(route)
                self.assertTrue(records)
                for record in records:
                    self.assertEqual(record['review_status'], 'needs_correction')
                    self.assertEqual(record['effective_reuse_state'], 'bounded_only')
                    self.assertEqual(record['article_alerts'][0]['id'], 'fixture-live-warning')
                self.assertEqual(self.records(route, '--accepted-only'), [])
                markdown = cli(route, self.skill, '--pmid', self.pmid, as_json=False)
                self.assertEqual(markdown.returncode, 0, markdown.stderr)
                for text in ('needs_correction', 'bounded_only', 'fixture-live-warning',
                             'Do not transfer the disputed estimate'):
                    self.assertIn(text, markdown.stdout)
        papers = self.output('ccr', '--pmid', self.pmid, '--paper-logic')['papers']
        self.assertEqual(papers[0]['effective_reuse_state'], 'bounded_only')
        self.assertEqual(papers[0]['article_alerts'][0]['id'], 'fixture-live-warning')
        self.assertEqual(self.output('ccr', '--pmid', self.pmid, '--paper-logic',
                                     '--accepted-only')['papers'], [])
        markdown = cli('ccr', self.skill, '--pmid', self.pmid, '--paper-logic', as_json=False)
        self.assertEqual(markdown.returncode, 0, markdown.stderr)
        self.assertIn('fixture-live-warning', markdown.stdout)

    def test_correction_and_unknown_eligibility_block_rendering(self):
        for status, eligibility, state in (
            ('needs_correction', 'included', 'bounded_only'),
            ('not_reviewed', 'included', 'audit_only'),
            ('passed', 'excluded', 'audit_only'),
        ):
            self.update_quality(status, eligibility)
            for route, record in (('ccr', self.ccr_records[0]), ('stk11', self.stk_records[0])):
                with self.subTest(status=status, eligibility=eligibility, route=route):
                    result = cli(route, self.skill, *self.render_arguments(record))
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(state, result.stderr)
                    self.assertNotIn('rendered_text', result.stdout)

    def test_passed_render_preserves_live_warning_in_json_and_markdown(self):
        self.add_alert()
        for route, record in (('ccr', self.ccr_records[0]), ('stk11', self.stk_records[0])):
            with self.subTest(route=route):
                output = self.output(route, *self.render_arguments(record))
                for field in LIVE_FIELDS:
                    self.assertIn(field, output)
                self.assertEqual(output['review_status'], 'passed')
                self.assertEqual(output['effective_reuse_state'], 'usable_with_boundary')
                self.assertEqual(output['article_alerts'][0]['id'], 'fixture-live-warning')
                for slot in record['slots']:
                    self.assertIn(f'USER_VALUE_{slot["name"]}', output['rendered_text'])
                markdown = cli(route, self.skill, *self.render_arguments(record), as_json=False)
                self.assertEqual(markdown.returncode, 0, markdown.stderr)
                self.assertIn('fixture-live-warning', markdown.stdout)
                self.assertIn('usable_with_boundary', markdown.stdout)

    def test_expression_rules_block_only_matching_sentences_in_all_routes(self):
        for state in ('quarantined', 'needs_source_check'):
            self.controls['entry_rules'] = []
            for records in (self.ccr_records, self.stk_records):
                phrase = self.unique_source_phrase(records[0], records[1:])
                self.add_rule(phrase, state=state, identifier=f'fixture-{records[0]["id"]}')
            for route, target in (('ccr', self.ccr_records[0]),
                                  ('stk11', self.stk_records[0]),
                                  ('generic', self.stk_records[0])):
                with self.subTest(route=route, state=state):
                    records = {item['id']: item for item in self.records(route)}
                    self.assertEqual(records[target['id']]['review_status'], 'passed')
                    self.assertEqual(records[target['id']]['effective_reuse_state'], state)
                    accepted = self.records(route, '--accepted-only')
                    self.assertNotIn(target['id'], {item['id'] for item in accepted})
                    self.assertTrue(accepted, 'A rule on one expression must not hold its entire article.')
                    if route != 'generic':
                        rendered = cli(route, self.skill, *self.render_arguments(target))
                        self.assertNotEqual(rendered.returncode, 0)
                        self.assertIn(state, rendered.stderr)

    def test_sentence_restriction_is_disclosed_without_holding_safe_paper_narrative(self):
        target, sibling = self.ccr_records[:2]
        self.add_rule(self.unique_source_phrase(target, self.ccr_records[1:]))
        output = self.output('ccr', '--paper-logic', '--pmid', self.pmid, '--accepted-only')
        self.assertEqual(output['matched_count'], 1)
        paper = output['papers'][0]
        self.assertEqual(paper['effective_reuse_state'], 'usable_with_boundary')
        linked = {item['id']: item for item in paper['linked_record_controls']}
        self.assertEqual(linked[target['id']]['effective_reuse_state'], 'quarantined')
        self.assertEqual(linked[sibling['id']]['effective_reuse_state'], 'usable_with_boundary')
        for record in linked.values():
            self.assertNotIn('source_sentence', record)
            self.assertNotIn('rewrite_template', record)
        accepted = self.records('ccr', '--accepted-only')
        self.assertEqual({item['id'] for item in accepted},
                         {item['id'] for item in self.ccr_records[1:]})

    def test_paper_narrative_rule_is_checked_against_paper_text(self):
        self.add_rule(self.paper['central_results'][0])
        output = self.output('ccr', '--paper-logic', '--pmid', self.pmid)
        self.assertEqual(output['papers'][0]['effective_reuse_state'], 'quarantined')
        accepted = self.output('ccr', '--paper-logic', '--pmid', self.pmid, '--accepted-only')
        self.assertEqual(accepted['papers'], [])

    def test_language_index_stable_ids_are_disclosed_without_guessing_sentence_identity(self):
        self.controls['entry_rules'] = [{
            'id': 'fixture-language-index-only',
            'stable_ids': [self.ccr_records[0]['id'], self.stk_records[0]['id']],
            'state': 'quarantined', 'reason': 'Different identifier namespace.',
            'source_reference': 'fixture-recheck.md',
        }]
        self.save_controls()
        for route in ROUTES:
            with self.subTest(route=route):
                accepted = self.records(route, '--accepted-only')
                self.assertTrue(accepted)
                for item in accepted:
                    self.assertEqual(item['entry_rules'], [])
                    self.assertIn('fixture-language-index-only',
                                  item['control_compatibility']['unmapped_stable_id_rule_ids'])
                markdown = cli(route, self.skill, '--pmid', self.pmid, as_json=False)
                self.assertEqual(markdown.returncode, 0, markdown.stderr)
                self.assertIn('fixture-language-index-only', markdown.stdout)

    def test_direct_renderer_reloads_live_status_instead_of_trusting_cached_pass(self):
        for route, raw in (('ccr', self.ccr_records[0]), ('stk11', self.stk_records[0])):
            module = importlib.import_module(ROUTES[route].removesuffix('.py'))
            self.update_quality('passed')
            record = self.records(route)[0]
            values = {slot['name']: f'user value {slot["name"]}' for slot in record['slots']}
            self.assertEqual(record['effective_reuse_state'], 'usable_with_boundary')
            self.update_quality('needs_correction')
            with self.subTest(route=route), self.assertRaisesRegex(module.CatalogError, 'bounded_only'):
                module.render_template(record, values, skill_path=self.skill)

    def test_missing_live_authority_blocks_accepted_search_and_render(self):
        for filename in ('ccr-reading-quality-register.csv', 'language-controls.json'):
            authority = self.references / filename
            hidden = authority.with_name(filename + '.temporarily-hidden')
            authority.rename(hidden)
            try:
                for route in ROUTES:
                    with self.subTest(authority=filename, route=route, operation='accepted'):
                        result = cli(route, self.skill, '--pmid', self.pmid, '--accepted-only')
                        self.assertNotEqual(result.returncode, 0)
                        self.assertIn('authority is missing', result.stderr)
                        self.assertIn(filename, result.stderr)
                        self.assertEqual(result.stdout, '')
                paper = cli('ccr', self.skill, '--pmid', self.pmid,
                            '--paper-logic', '--accepted-only')
                self.assertNotEqual(paper.returncode, 0)
                self.assertIn('authority is missing', paper.stderr)
                for route, record in (('ccr', self.ccr_records[0]),
                                      ('stk11', self.stk_records[0])):
                    with self.subTest(authority=filename, route=route, operation='render'):
                        result = cli(route, self.skill, *self.render_arguments(record))
                        self.assertNotEqual(result.returncode, 0)
                        self.assertIn('authority is missing', result.stderr)
                        self.assertIn(filename, result.stderr)
                        self.assertEqual(result.stdout, '')
            finally:
                hidden.rename(authority)

    def test_same_stk_sentence_has_identical_rule_scope_in_search_and_render(self):
        record = self.stk_records[0]
        only_in_dedicated_metadata = record['do_not_use_when_zh']
        shared_content = json.dumps({
            key: record[key] for key in (
                'result_type', 'use_when_zh', 'rewrite_template',
                'evidence_boundary', 'source', 'title',
            )
        }, ensure_ascii=False)
        self.assertNotIn(only_in_dedicated_metadata, shared_content)
        self.add_rule(only_in_dedicated_metadata)
        dedicated = self.output('stk11', '--template-id', record['id'], '--accepted-only')['records']
        generic = [item for item in self.records('generic', '--accepted-only')
                   if item['id'] == record['id']]
        rendered = self.output('stk11', *self.render_arguments(record))
        for operation, item in (('dedicated', dedicated[0]), ('generic', generic[0]),
                                ('render', rendered)):
            with self.subTest(operation=operation, rule_location='dedicated_metadata_only'):
                self.assertEqual(item['effective_reuse_state'], 'usable_with_boundary')
                self.assertEqual(item['entry_rules'], [])
        # The dedicated metadata remains a valid user-query target even though
        # it is not part of the common source-expression restriction domain.
        queried = self.output('stk11', '--template-id', record['id'],
                              '--query', only_in_dedicated_metadata)
        self.assertEqual(queried['matched_count'], 1)

        self.controls['entry_rules'] = []
        source_phrase = self.unique_source_phrase(record, self.stk_records[1:])
        self.add_rule(source_phrase)
        dedicated = self.output('stk11', '--template-id', record['id'])['records'][0]
        generic = next(item for item in self.records('generic') if item['id'] == record['id'])
        for operation, item in (('dedicated', dedicated), ('generic', generic)):
            with self.subTest(operation=operation, rule_location='source_sentence'):
                self.assertEqual(item['effective_reuse_state'], 'quarantined')
                self.assertEqual(item['entry_rules'][0]['id'], 'fixture-expression-rule')
        rendered = cli('stk11', self.skill, *self.render_arguments(record))
        self.assertNotEqual(rendered.returncode, 0)
        self.assertIn('quarantined', rendered.stderr)


if __name__ == '__main__':
    unittest.main()
