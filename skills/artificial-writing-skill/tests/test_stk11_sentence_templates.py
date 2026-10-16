import copy
import csv
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


sys.dont_write_bytecode = True
SKILL = Path(__file__).resolve().parents[1]
REFERENCES = SKILL / 'references'
sys.path.insert(0, str(SKILL / 'scripts'))

from search_stk11_sentence_templates import (
    CatalogError,
    load_catalog,
    render_template,
    search,
    validate_catalog,
)


EXPECTED_CCR_PMIDS = {
    '32709715', '33077574', '33323404', '37097610', '37733794',
    '38300729', '38980931', '39545922', '39804166', '41417462',
    '41870274', '42268349', '42456046', '42485106', '42507545',
}


def slot(name):
    return {
        'name': name,
        'description': f'Synthetic test description for {name}',
        'required': True,
        'evidence_source': 'user_supplied',
    }


def record_one():
    return {
        'id': 'stk11-ccr-sent-99990001-results-fixture-one',
        'pmid': '99990001',
        'doi': '10.0000/synthetic.1',
        'title': 'Synthetic fixture one; not a literature record',
        'journal': 'Clinical Cancer Research',
        'journal_id': 'ccr',
        'year': '2024',
        'legacy_origin_tier': 'core_highlight',
        'stk11_relation': 'direct_analysis',
        'source': {
            'pdf_sha256': 'a' * 64,
            'supplied_pdf_version': 'synthetic_test_fixture',
            'physical_page': 3,
            'section': 'results',
            'source_sentence': (
                'Synthetic marker A was associated with synthetic endpoint B '
                'in a synthetic cohort.'
            ),
            'verification_level': 'visually_verified_exact',
            'quotation_verified': True,
            'verification_record': 'synthetic-test-fixture',
        },
        'result_type': 'adjusted_prognostic_association',
        'significance_status': 'significant',
        'evidence_layer': 'genomic',
        'rhetorical_function': 'report an adjusted association',
        'target_sections': ['abstract-results', 'results'],
        'use_when_zh': '测试：用户提供了完整的关联结果时。',
        'do_not_use_when_zh': '测试：缺少比较或统计量时。',
        'rewrite_template': (
            'In [population], [index_marker] was associated with [endpoint] '
            '([statistic]).'
        ),
        'slots': [
            slot('population'), slot('index_marker'), slot('endpoint'),
            slot('statistic'),
        ],
        'source_specific_tokens': [
            'Synthetic marker A', 'synthetic endpoint B', 'synthetic cohort',
        ],
        'usage_card_ids': ['association'],
        'claim_ceiling': 'association_only',
        'evidence_boundary': 'Synthetic test boundary: association is not causation.',
        'transfer_notes': 'Synthetic test fixture; never use as literature evidence.',
    }


def record_two():
    return {
        'id': 'stk11-ccr-sent-99990002-results-fixture-two',
        'pmid': '99990002',
        'doi': '10.0000/synthetic.2',
        'title': 'Synthetic fixture two; not a literature record',
        'journal': 'Clinical Cancer Research',
        'journal_id': 'ccr',
        'year': '2025',
        'legacy_origin_tier': 'topic_support',
        'stk11_relation': 'contextual_analysis',
        'source': {
            'pdf_sha256': 'b' * 64,
            'supplied_pdf_version': 'synthetic_test_fixture',
            'physical_page': 5,
            'section': 'discussion',
            'source_sentence': (
                'Synthetic groups C and D did not differ in synthetic outcome E.'
            ),
            'verification_level': 'normalized_pdf_text_match',
            'quotation_verified': False,
            'verification_record': 'synthetic-test-fixture',
        },
        'result_type': 'null_or_inconclusive',
        'significance_status': 'nonsignificant',
        'evidence_layer': 'clinical',
        'rhetorical_function': 'report a bounded null comparison',
        'target_sections': ['results', 'discussion'],
        'use_when_zh': '测试：已实施比较且结果未显著时。',
        'do_not_use_when_zh': '测试：没有推断检验或区间时。',
        'rewrite_template': (
            'The difference in [endpoint] between [group_a] and [group_b] '
            'was not statistically significant ([statistic]).'
        ),
        'slots': [
            slot('endpoint'), slot('group_a'), slot('group_b'), slot('statistic'),
        ],
        'source_specific_tokens': [
            'Synthetic groups C and D', 'synthetic outcome E',
        ],
        'usage_card_ids': ['null-result'],
        'claim_ceiling': 'association_only',
        'evidence_boundary': 'Synthetic test boundary: nonsignificance is not equivalence.',
        'transfer_notes': 'Synthetic test fixture; never use as literature evidence.',
    }


def payload():
    return {
        'schema_version': 1,
        'updated': '2026-10-15',
        'scope': 'Synthetic unit-test records only; not literature evidence.',
        'project_scope': {
            'membership_source': 'stk11-writing-reference-map.json',
            'journal_id': 'ccr',
            'legacy_origin_tiers': ['core_highlight', 'topic_support'],
            'expected_pmids': ['99990001', '99990002'],
            'coverage_unit': 'at_least_one_template_per_expected_paper',
            'coverage_complete': True,
            'coverage_statement': 'Synthetic fixture covers both expected IDs.',
        },
        'records': [record_one(), record_two()],
    }


def write_installed_fixture(skill, catalog_payload, authority_payload=None):
    """Write a self-contained relative-path fixture for installed-source checks."""
    authority_payload = authority_payload or catalog_payload
    references = skill / 'references'
    references.mkdir(parents=True, exist_ok=True)
    (references / 'stk11-ccr-sentence-templates.json').write_text(
        json.dumps(catalog_payload, ensure_ascii=False, indent=2), encoding='utf-8'
    )

    authoritative_records = authority_payload['records']
    library_fields = ['pmid', 'doi', 'title', 'journal', 'year']
    with (references / 'library-index.csv').open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=library_fields)
        writer.writeheader()
        for record in authoritative_records:
            writer.writerow({field: record[field] for field in library_fields})

    membership = {
        'schema_version': 1,
        'records': [
            {
                'pmid': record['pmid'],
                'tier': record['legacy_origin_tier'],
                'stk11_relation': record['stk11_relation'],
            }
            for record in authoritative_records
        ],
    }
    (references / 'stk11-writing-reference-map.json').write_text(
        json.dumps(membership, ensure_ascii=False, indent=2), encoding='utf-8'
    )

    version_fields = ['pmid', 'supplied_pdf_version', 'sha256', 'physical_pages']
    with (references / 'source-version-register.csv').open(
        'w', encoding='utf-8', newline=''
    ) as stream:
        writer = csv.DictWriter(stream, fieldnames=version_fields)
        writer.writeheader()
        for record in authoritative_records:
            writer.writerow({
                'pmid': record['pmid'],
                'supplied_pdf_version': record['source']['supplied_pdf_version'],
                'sha256': record['source']['pdf_sha256'],
                'physical_pages': record['source']['physical_page'] + 2,
            })
    cards = [{'id': 'association'}, {'id': 'null-result'}]
    (references / 'language-usage-cards.json').write_text(
        json.dumps({'cards': cards}, ensure_ascii=False), encoding='utf-8'
    )
    (references / 'language-usage-cards-rechecks.json').write_text(
        json.dumps({'cards': []}, ensure_ascii=False), encoding='utf-8'
    )


class CatalogValidation(unittest.TestCase):
    def test_minimal_fixture_is_valid(self):
        validated = validate_catalog(payload(), {'association', 'null-result'})
        self.assertEqual(len(validated['records']), 2)

    def test_template_slots_must_match_exactly(self):
        broken = payload()
        broken['records'][0]['slots'].pop()
        with self.assertRaisesRegex(CatalogError, 'placeholders and declared slots differ'):
            validate_catalog(broken)

    def test_template_rejects_display_labels_or_unmatched_brackets(self):
        broken = payload()
        broken['records'][0]['rewrite_template'] = broken['records'][0][
            'rewrite_template'
        ].replace('[index_marker]', '[index marker]')
        with self.assertRaisesRegex(CatalogError, 'unsupported slot syntax'):
            validate_catalog(broken)

    def test_source_specific_tokens_cannot_be_template_defaults(self):
        broken = payload()
        broken['records'][0]['rewrite_template'] = (
            'Synthetic marker A was associated with [endpoint] ([statistic]) '
            'in [population] using [index_marker].'
        )
        with self.assertRaisesRegex(CatalogError, 'source-specific token leaked'):
            validate_catalog(broken)

    def test_verified_quote_requires_visual_verification(self):
        broken = payload()
        broken['records'][0]['source']['verification_level'] = 'normalized_pdf_text_match'
        with self.assertRaisesRegex(CatalogError, 'visually_verified_exact'):
            validate_catalog(broken)

    def test_verification_record_cannot_embed_private_absolute_path(self):
        broken = payload()
        broken['records'][0]['source']['verification_record'] = (
            r'audit-source={"pdf_file":"C:\private-audit\pmid-99990001.pdf"}'
        )
        with self.assertRaisesRegex(CatalogError, 'must not contain an absolute path'):
            validate_catalog(broken)

    def test_complete_coverage_requires_every_expected_pmid(self):
        broken = payload()
        broken['records'].pop()
        with self.assertRaisesRegex(CatalogError, 'coverage_complete'):
            validate_catalog(broken)

    def test_usage_cards_validate_against_both_catalogs_union(self):
        broken = payload()
        broken['records'][0]['usage_card_ids'] = ['absent-card']
        with self.assertRaisesRegex(CatalogError, 'unknown usage_card_ids'):
            validate_catalog(broken, {'association', 'null-result'})

    def test_methods_content_requires_noninferential_significance(self):
        value = payload()
        record = value['records'][0]
        record['source']['section'] = 'methods'
        record['target_sections'] = ['methods', 'abstract-methods']
        record['result_type'] = 'sequencing_and_processing'
        with self.assertRaisesRegex(CatalogError, 'not_applicable significance'):
            validate_catalog(value)
        record['significance_status'] = 'not_applicable'
        self.assertEqual(validate_catalog(value)['records'][0]['result_type'],
                         'sequencing_and_processing')

    def test_fulltext_coverage_cannot_be_satisfied_by_abstracts_or_clinical_results(self):
        value = payload()
        value['project_scope']['fulltext_coverage'] = {
            'unit': 'body_methods_and_nonclinical_results_per_paper',
            'methods_minimum': 1, 'results_minimum': 1,
            'coverage_complete': True,
            'audit_resource': 'stk11-ccr-fulltext-sentence-audit.md',
        }
        for index, record in enumerate(value['records'][:]):
            record['source']['section'] = 'results'
            record['evidence_layer'] = 'genomic'
            record['result_type'] = 'genomic_landscape'
            record['source']['verification_level'] = 'visually_verified_exact'
            record['source']['quotation_verified'] = True
            record['source']['verification_record'] = (
                f'stk11-ccr-fulltext-sentence-audit.md#pmid-{record["pmid"]}'
            )
            method = copy.deepcopy(record)
            method['id'] += '-method'
            method['source']['section'] = 'methods'
            method['target_sections'] = ['methods']
            method['significance_status'] = 'not_applicable'
            method['result_type'] = 'sequencing_and_processing'
            value['records'].append(method)
        self.assertEqual(len(validate_catalog(value)['records']), 4)
        for field, alternative in [('section', 'abstract-results'), ('evidence_layer', 'clinical')]:
            with self.subTest(field=field):
                broken = copy.deepcopy(value)
                if field == 'section':
                    broken['records'][0]['source']['section'] = alternative
                else:
                    broken['records'][0][field] = alternative
                with self.assertRaisesRegex(CatalogError, 'fulltext_coverage is incomplete'):
                    validate_catalog(broken)
        mislabeled = copy.deepcopy(value)
        mislabeled['records'][0]['result_type'] = 'adjusted_prognostic_association'
        with self.assertRaisesRegex(CatalogError, 'fulltext_coverage is incomplete'):
            validate_catalog(mislabeled)
        for field, alternative in [
            ('verification_record', 'missing-audit.json'),
            ('quotation_verified', False),
        ]:
            with self.subTest(field=field):
                broken = copy.deepcopy(value)
                broken['records'][0]['source'][field] = alternative
                with self.assertRaisesRegex(CatalogError, 'fulltext_coverage requires'):
                    validate_catalog(broken)
        duplicated = copy.deepcopy(value)
        duplicated['project_scope']['fulltext_coverage']['results_minimum'] = 2
        for record in value['records'][:2]:
            duplicate = copy.deepcopy(record)
            duplicate['id'] += '-second-template'
            duplicated['records'].append(duplicate)
        with self.assertRaisesRegex(CatalogError, 'fulltext_coverage is incomplete'):
            validate_catalog(duplicated)


class RetrievalBehavior(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = validate_catalog(payload())['records']

    def test_default_all_keeps_both_tiers(self):
        result = search(self.records)
        self.assertEqual(result['matched_count'], 2)
        self.assertEqual(
            {record['legacy_origin_tier'] for record in result['records']},
            {'core_highlight', 'topic_support'},
        )

    def test_filters_and_query_use_and_semantics_on_one_record(self):
        result = search(
            self.records,
            pmid='99990001',
            template_id='stk11-ccr-sent-99990001-results-fixture-one',
            result_type='adjusted_prognostic_association',
            significance='significant',
            section='results',
            legacy_origin='core_highlight',
            evidence_layer='genomic',
            query='"associated with" genomic',
        )
        self.assertEqual(result['matched_count'], 1)
        self.assertEqual(result['records'][0]['pmid'], '99990001')
        self.assertEqual(
            search(
                self.records,
                result_type='adjusted_prognostic_association',
                significance='nonsignificant',
            )['matched_count'],
            0,
        )

    def test_section_filters_target_not_source_section(self):
        result = search(self.records, section='results', legacy_origin='topic_support')
        self.assertEqual(result['matched_count'], 1)
        self.assertEqual(result['records'][0]['source']['section'], 'discussion')

    def test_source_section_can_be_combined_with_target_section(self):
        self.assertEqual(search(self.records, section='results', source_section='discussion')
                         ['matched_count'], 1)
        self.assertEqual(search(self.records, section='results', source_section='methods')
                         ['matched_count'], 0)
        with self.assertRaisesRegex(CatalogError, 'unknown source_section'):
            search(self.records, source_section='invented-source-section')

    def test_unknown_enum_and_bad_limit_fail_closed(self):
        with self.assertRaises(CatalogError):
            search(self.records, result_type='invented-result')
        with self.assertRaises(CatalogError):
            search(self.records, template_id='unsafe template id')
        with self.assertRaises(CatalogError):
            search(self.records, limit=0)


class SafeRendering(unittest.TestCase):
    def setUp(self):
        self.record = record_one()
        self.values = {
            'population': 'the prespecified analysis population',
            'index_marker': 'marker X',
            'endpoint': 'time-to-event outcome Y',
            'statistic': 'adjusted estimate and confidence interval',
        }

    def test_renderer_uses_only_explicit_values(self):
        rendered = render_template(self.record, self.values)
        self.assertEqual(
            rendered,
            'In the prespecified analysis population, marker X was associated '
            'with time-to-event outcome Y (adjusted estimate and confidence interval).',
        )
        for source_token in self.record['source_specific_tokens']:
            self.assertNotIn(source_token, rendered)

    def test_missing_and_extra_slots_are_rejected(self):
        missing = copy.deepcopy(self.values)
        missing.pop('statistic')
        with self.assertRaisesRegex(CatalogError, 'missing'):
            render_template(self.record, missing)
        extra = {**self.values, 'source_default': 'forbidden'}
        with self.assertRaisesRegex(CatalogError, 'extra'):
            render_template(self.record, extra)

    def test_source_token_is_allowed_only_when_explicitly_supplied(self):
        values = {**self.values, 'index_marker': 'Synthetic marker A'}
        rendered = render_template(self.record, values)
        self.assertIn('Synthetic marker A', rendered)


class InstalledResourceChecks(unittest.TestCase):
    def test_guide_and_schema_exist(self):
        self.assertTrue((REFERENCES / 'stk11-sentence-rewriting.md').is_file())
        schema = json.loads(
            (REFERENCES / 'stk11-ccr-sentence-templates.schema.json').read_text(
                encoding='utf-8'
            )
        )
        self.assertEqual(schema['properties']['schema_version']['const'], 1)

    def test_real_catalog_when_present(self):
        path = REFERENCES / 'stk11-ccr-sentence-templates.json'
        if not path.is_file():
            self.skipTest('main agent has not integrated the source-verified catalog yet')
        real = load_catalog(SKILL)
        expected = set(real['project_scope']['expected_pmids'])
        self.assertEqual(expected, EXPECTED_CCR_PMIDS)
        self.assertTrue(real['project_scope']['coverage_complete'])
        represented = {record['pmid'] for record in real['records']}
        self.assertEqual(represented, EXPECTED_CCR_PMIDS)
        self.assertEqual(len(expected), 15)
        self.assertEqual(len({record['id'] for record in real['records']}), len(real['records']))
        self.assertTrue(all(
            sum(record['pmid'] == pmid for record in real['records']) >= 1
            for pmid in EXPECTED_CCR_PMIDS
        ))
        self.assertTrue(all(
            record['source']['quotation_verified']
            and record['source']['verification_level'] == 'visually_verified_exact'
            for record in real['records']
        ))

    def test_installed_cross_checks_fail_closed(self):
        authority = payload()
        mutations = [
            ('doi', lambda value: value['records'][0].__setitem__('doi', '10.0000/wrong'), 'doi disagrees'),
            ('title', lambda value: value['records'][0].__setitem__('title', 'Wrong title'), 'title disagrees'),
            ('journal', lambda value: value['records'][0].__setitem__('journal', 'Wrong journal'), 'journal disagrees'),
            ('year', lambda value: value['records'][0].__setitem__('year', '2023'), 'year disagrees'),
            ('tier', lambda value: value['records'][0].__setitem__('legacy_origin_tier', 'topic_support'), 'legacy_origin_tier disagrees'),
            ('relation', lambda value: value['records'][0].__setitem__('stk11_relation', 'contextual_analysis'), 'stk11_relation disagrees'),
            ('hash', lambda value: value['records'][0]['source'].__setitem__('pdf_sha256', 'c' * 64), 'pdf_sha256 disagrees'),
            ('version', lambda value: value['records'][0]['source'].__setitem__('supplied_pdf_version', 'wrong_version'), 'supplied_pdf_version disagrees'),
            ('page', lambda value: value['records'][0]['source'].__setitem__('physical_page', 99), 'physical_page exceeds'),
        ]
        with tempfile.TemporaryDirectory(prefix='sentence-template-authority-') as directory:
            skill = Path(directory) / 'skill'
            write_installed_fixture(skill, authority)
            self.assertEqual(len(load_catalog(skill)['records']), 2)
            for label, mutate, expected_message in mutations:
                with self.subTest(label=label):
                    broken = copy.deepcopy(authority)
                    mutate(broken)
                    write_installed_fixture(skill, broken, authority)
                    with self.assertRaisesRegex(CatalogError, expected_message):
                        load_catalog(skill)

    def test_real_fulltext_catalog_covers_each_paper_and_renders_methods(self):
        real = load_catalog(SKILL)
        coverage = real['project_scope']['fulltext_coverage']
        self.assertTrue(coverage['coverage_complete'])
        self.assertGreaterEqual(coverage['methods_minimum'], 2)
        self.assertGreaterEqual(coverage['results_minimum'], 2)
        for pmid in EXPECTED_CCR_PMIDS:
            methods = search(real['records'], pmid=pmid, section='methods',
                             source_section='methods', limit=100)['records']
            results = search(real['records'], pmid=pmid, section='results',
                             source_section='results', limit=100)['records']
            self.assertGreaterEqual(len(methods), 2, pmid)
            self.assertGreaterEqual(len(results), 2, pmid)
        record = next(item for item in real['records'] if item['id'] ==
                      'stk11-ccr-sent-39545922-methods-sample-level-pseudobulk')
        environment = {**os.environ, 'PYTHONDONTWRITEBYTECODE': '1',
                       'PYTHONIOENCODING': 'utf-8'}
        command = [sys.executable, str(SKILL / 'scripts/search_stk11_sentence_templates.py'),
                   '--source-section', 'methods', '--section', 'methods',
                   '--content-type', record['result_type'], '--template-id', record['id'],
                   '--render', '--json']
        for item in record['slots']:
            command.extend(['--slot', f'{item["name"]}=USER_VALUE_{item["name"].upper()}'])
        result = subprocess.run(command, cwd=SKILL, env=environment, capture_output=True,
                                text=True, encoding='utf-8', check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        output = json.loads(result.stdout)
        self.assertEqual(output['template_id'], record['id'])
        for item in record['slots']:
            self.assertIn(f'USER_VALUE_{item["name"].upper()}', output['rendered_text'])

    def test_markdown_verification_reference_is_relative_and_not_dangling(self):
        installed = payload()
        installed['records'][0]['source']['verification_record'] = (
            'sentence-source-audit.md#pmid-99990001'
        )
        with tempfile.TemporaryDirectory(prefix='sentence-template-audit-ref-') as directory:
            skill = Path(directory) / 'skill'
            write_installed_fixture(skill, installed)
            with self.assertRaisesRegex(CatalogError, 'target is missing'):
                load_catalog(skill)

            (skill / 'references' / 'sentence-source-audit.md').write_text(
                '# Synthetic source audit\n\n## PMID 99990001\n', encoding='utf-8'
            )
            self.assertEqual(len(load_catalog(skill)['records']), 2)

            missing_anchor = copy.deepcopy(installed)
            missing_anchor['records'][0]['source']['verification_record'] = (
                'sentence-source-audit.md#pmid-99999999'
            )
            write_installed_fixture(skill, missing_anchor)
            with self.assertRaisesRegex(CatalogError, 'anchor is missing'):
                load_catalog(skill)

            no_anchor = copy.deepcopy(installed)
            no_anchor['records'][0]['source']['verification_record'] = (
                'sentence-source-audit.md#'
            )
            write_installed_fixture(skill, no_anchor)
            with self.assertRaisesRegex(CatalogError, 'requires a nonempty'):
                load_catalog(skill)

            escaping = copy.deepcopy(installed)
            escaping['records'][0]['source']['verification_record'] = (
                '../sentence-source-audit.md#pmid-99990001'
            )
            write_installed_fixture(skill, escaping)
            with self.assertRaisesRegex(CatalogError, 'escapes references'):
                load_catalog(skill)

    def test_real_cli_retrieval_and_render_smoke(self):
        path = REFERENCES / 'stk11-ccr-sentence-templates.json'
        if not path.is_file():
            self.skipTest('main agent has not integrated the source-verified catalog yet')
        real = load_catalog(SKILL)
        record = next(
            item for item in real['records']
            if item['id'] == (
                'stk11-ccr-sent-41417462-'
                'discussion-bounded-null-interpretation'
            )
        )
        script = SKILL / 'scripts' / 'search_stk11_sentence_templates.py'
        environment = os.environ.copy()
        environment['PYTHONDONTWRITEBYTECODE'] = '1'
        environment['PYTHONIOENCODING'] = 'utf-8'

        retrieval = subprocess.run(
            [
                sys.executable, str(script), '--skill-path', str(SKILL),
                '--pmid', record['pmid'],
                '--template-id', record['id'],
                '--result-type', record['result_type'],
                '--significance', record['significance_status'],
                '--section', record['target_sections'][0],
                '--tier', record['legacy_origin_tier'],
                '--evidence-layer', record['evidence_layer'],
                '--query', record['id'],
                '--limit', '1', '--json',
            ],
            cwd=SKILL,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
            encoding='utf-8',
        )
        self.assertEqual(retrieval.returncode, 0, retrieval.stderr)
        retrieved = json.loads(retrieval.stdout)
        self.assertEqual(retrieved['matched_count'], 1)
        self.assertEqual(retrieved['records'][0]['id'], record['id'])

        command = [
            sys.executable, str(script), '--skill-path', str(SKILL),
            '--template-id', record['id'], '--render', '--json',
        ]
        for slot_record in record['slots']:
            command.extend([
                '--slot', f'{slot_record["name"]}=USER_SUPPLIED_{slot_record["name"].upper()}',
            ])
        rendering = subprocess.run(
            command,
            cwd=SKILL,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
            encoding='utf-8',
        )
        self.assertEqual(rendering.returncode, 0, rendering.stderr)
        rendered = json.loads(rendering.stdout)
        self.assertEqual(rendered['template_id'], record['id'])
        self.assertEqual(rendered['language_pattern_provenance']['pmid'], record['pmid'])
        for slot_record in record['slots']:
            self.assertIn(
                f'USER_SUPPLIED_{slot_record["name"].upper()}',
                rendered['rendered_text'],
            )
        for source_token in record['source_specific_tokens']:
            self.assertNotIn(source_token, rendered['rendered_text'])


if __name__ == '__main__':
    unittest.main()
