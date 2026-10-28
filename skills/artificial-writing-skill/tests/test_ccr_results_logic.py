import copy
import csv
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


sys.dont_write_bytecode = True

SKILL = Path(__file__).resolve().parents[1]
SCRIPT = SKILL / 'scripts' / 'search_ccr_results_logic.py'
SPEC = importlib.util.spec_from_file_location('search_ccr_results_logic', SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

CatalogError = MODULE.CatalogError
load_catalog = MODULE.load_catalog
render_template = MODULE.render_template
search = MODULE.search
search_papers = MODULE.search_papers
validate_catalog = MODULE.validate_catalog


def record(pmid='99990001', year='2025', suffix='positive'):
    return {
        'id': f'ccr-logic-{pmid}-{suffix}',
        'pmid': pmid,
        'doi': f'10.0000/{pmid}',
        'title': f'Synthetic CCR article {pmid}',
        'journal': 'Clinical Cancer Research',
        'journal_id': 'ccr',
        'year': year,
        'source': {
            'pdf_sha256': ('a' if pmid == '99990001' else 'b') * 64,
            'supplied_pdf_version': 'publisher_main_pdf',
            'physical_page': 4,
            'physical_pages': [4],
            'section': 'results',
            'subheading': 'Synthetic results',
            'source_sentence': f'Marker {pmid} was associated with outcome Z.',
            'verification_level': 'visually_verified_exact',
            'quotation_verified': True,
            'visual_verified': True,
            'verification_record': f'ccr-2025-2026-results-logic-audit.md#pmid-{pmid}',
            'text_extraction_match': 'normalized_literal',
            'verification_note': 'Visual transcription and normalized text match recorded.',
        },
        'domains': ['genomics', 'prognosis'],
        'result_polarity': 'positive',
        'inferential_status': 'significant',
        'result_type': 'survival_prognosis',
        'evidence_layer': 'clinical',
        'rhetorical_function': 'quantify_effect',
        'logic_position': 'development',
        'target_sections': ['results', 'abstract-results'],
        'use_when_zh': '用于报告用户数据中的调整后预后关联。',
        'do_not_use_when_zh': '没有时间起点、比较组或调整信息时不要使用。',
        'rewrite_template': (
            'In [population], [marker] was associated with [outcome] '
            '([effect_estimate]).'
        ),
        'template_language': 'en-US',
        'slots': [
            {'name': 'population', 'description': 'User-supplied population',
             'required': True, 'evidence_source': 'user_supplied'},
            {'name': 'marker', 'description': 'User-supplied marker',
             'required': True, 'evidence_source': 'user_supplied'},
            {'name': 'outcome', 'description': 'User-supplied outcome',
             'required': True, 'evidence_source': 'user_supplied'},
            {'name': 'effect_estimate', 'description': 'User-supplied estimate and uncertainty',
             'required': True, 'evidence_source': 'user_supplied'},
        ],
        'source_specific_tokens': [f'Marker {pmid}', 'outcome Z'],
        'claim_ceiling': 'prognostic_association_only',
        'evidence_boundary': 'Association does not establish treatment prediction or causation.',
        'logic_note_zh': '在分析集之后量化主要预后关联，再单独交代边界。',
    }


def paper(pmid='99990001', year='2025'):
    return {
        'pmid': pmid,
        'doi': f'10.0000/{pmid}',
        'year': year,
        'title': f'Synthetic CCR article {pmid}',
        'journal': 'Clinical Cancer Research',
        'journal_id': 'ccr',
        'pdf_sha256': ('a' if pmid == '99990001' else 'b') * 64,
        'supplied_pdf_version': 'publisher_main_pdf',
        'physical_pages': 12,
        'results_pages_read': [3, 4, 5],
        'visual_pages_checked': [4, 5],
        'result_profile': ['positive'],
        'domains': ['genomics', 'prognosis'],
        'central_results': ['A synthetic positive association was reported.'],
        'narrative_sequence': ['analysis set', 'estimate', 'boundary'],
        'negative_result_handling': 'No central negative result was reported in this fixture.',
        'omics_logic': 'The molecular variable is defined before its outcome association.',
        'efficacy_logic': 'No treatment-efficacy inference is made.',
        'prognosis_logic': 'The time-to-event association is kept prognostic.',
        'claim_boundaries': ['No treatment interaction or causal inference.'],
        'record_ids': [
            f'ccr-logic-{pmid}-positive',
            f'ccr-logic-{pmid}-qualification',
        ],
    }


def payload():
    first = record()
    first_qualification = copy.deepcopy(first)
    first_qualification['id'] = 'ccr-logic-99990001-qualification'
    first_qualification['logic_position'] = 'qualification'
    first_qualification['rhetorical_function'] = 'limit_inference'
    second = record('99990002', '2026', 'positive')
    second_qualification = copy.deepcopy(second)
    second_qualification['id'] = 'ccr-logic-99990002-qualification'
    second_qualification['logic_position'] = 'qualification'
    second_qualification['rhetorical_function'] = 'limit_inference'
    return {
        'schema_version': 1,
        'updated': '2026-10-16',
        'scope': 'Synthetic test fixture.',
        'project_scope': {
            'membership_source': 'library-index.csv',
            'journal_id': 'ccr',
            'issue_years': ['2025', '2026'],
            'eligibility': 'included',
            'expected_pmids': ['99990001', '99990002'],
            'coverage_unit': 'per-paper-results-logic-with-source-sentences',
            'paper_coverage_complete': True,
            'sentence_minimum_per_paper': 2,
            'sentence_maximum_per_paper': 4,
            'audit_resource': 'ccr-2025-2026-results-logic-audit.md',
            'source_scope': 'Actual supplied PDF body Results; synthetic fixture here.',
        },
        'papers': [paper(), paper('99990002', '2026')],
        'records': [first, first_qualification, second, second_qualification],
    }


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_installed_fixture(skill, value):
    references = skill / 'references'
    references.mkdir(parents=True, exist_ok=True)
    (references / 'journal-registry.json').write_text(
        json.dumps({
            'schema_version': 1,
            'journals': {
                'ccr': {
                    'name': 'Clinical Cancer Research',
                    'quality': 'ccr-reading-quality-register.csv',
                },
            },
        }),
        encoding='utf-8',
    )
    write_csv(references / 'ccr-reading-quality-register.csv', [
        {'pmid': paper['pmid'], 'eligibility': 'included', 'review_status': 'passed'}
        for paper in value['papers']
    ])
    (references / 'language-controls.json').write_text(
        json.dumps({'schema_version': 1, 'article_alerts': [], 'entry_rules': []}),
        encoding='utf-8',
    )
    (references / 'ccr-2025-2026-results-logic.json').write_text(
        json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8'
    )
    write_csv(references / 'library-index.csv', [
        {'pmid': '99990001', 'doi': '10.0000/99990001', 'year': '2025',
         'title': 'Synthetic CCR article 99990001', 'journal': 'Clinical Cancer Research',
         'eligibility': 'included'},
        {'pmid': '99990002', 'doi': '10.0000/99990002', 'year': '2026',
         'title': 'Synthetic CCR article 99990002', 'journal': 'Clinical Cancer Research',
         'eligibility': 'included'},
    ])
    write_csv(references / 'source-version-register.csv', [
        {'pmid': '99990001', 'sha256': 'a' * 64,
         'supplied_pdf_version': 'publisher_main_pdf', 'physical_pages': '12'},
        {'pmid': '99990002', 'sha256': 'b' * 64,
         'supplied_pdf_version': 'publisher_main_pdf', 'physical_pages': '12'},
    ])
    (references / 'ccr-2025-2026-results-logic-audit.md').write_text(
        '# Audit\n\n## PMID 99990001\n\nFixture.\n\n## PMID 99990002\n\nFixture.\n',
        encoding='utf-8',
    )


class SchemaBehavior(unittest.TestCase):
    def test_valid_fixture(self):
        value = validate_catalog(payload())
        self.assertEqual(len(value['papers']), 2)
        self.assertEqual(len(value['records']), 4)

    def test_requires_two_to_four_records_per_paper(self):
        value = payload()
        value['records'].pop()
        with self.assertRaisesRegex(CatalogError, 'expected 2-4 records'):
            validate_catalog(value)

    def test_source_quote_requires_visual_verification(self):
        value = payload()
        value['records'][0]['source']['visual_verified'] = False
        with self.assertRaisesRegex(CatalogError, 'visually verified'):
            validate_catalog(value)

    def test_unknown_inferential_status_is_rejected(self):
        value = payload()
        value['records'][0]['inferential_status'] = 'probably_significant'
        with self.assertRaisesRegex(CatalogError, 'inferential_status'):
            validate_catalog(value)

    def test_source_specific_token_cannot_leak_into_template(self):
        value = payload()
        value['records'][0]['rewrite_template'] = (
            'In [population], [marker] was associated with [outcome] and outcome Z '
            '([effect_estimate]).'
        )
        with self.assertRaisesRegex(CatalogError, 'leaked into template'):
            validate_catalog(value)

    def test_paper_profile_must_cover_record_polarities(self):
        value = payload()
        value['records'][0]['result_polarity'] = 'negative'
        with self.assertRaisesRegex(CatalogError, 'result_profile'):
            validate_catalog(value)

    def test_claim_ceiling_must_match_result_type(self):
        for result_type in MODULE.RESULT_TYPES:
            for claim in MODULE.CLAIM_CEILINGS:
                with self.subTest(result_type=result_type, claim=claim):
                    value = payload()
                    value['records'][0]['result_type'] = result_type
                    value['records'][0]['claim_ceiling'] = claim
                    if claim in MODULE.RESULT_CLAIM_COMPATIBILITY[result_type]:
                        validate_catalog(value)
                    else:
                        with self.assertRaisesRegex(CatalogError, 'incompatible'):
                            validate_catalog(value)

    def test_enum_type_errors_are_reported_as_catalog_errors(self):
        fields = (
            'result_polarity', 'inferential_status', 'result_type', 'evidence_layer',
            'rhetorical_function', 'logic_position', 'claim_ceiling', 'template_language',
        )
        for field in fields:
            with self.subTest(field=field):
                value = payload()
                value['records'][0][field] = []
                with self.assertRaises(CatalogError):
                    validate_catalog(value)

    def test_source_pages_must_be_contiguous_and_covered_by_paper_audits(self):
        value = payload()
        value['records'][0]['source']['physical_pages'] = [4, 5]
        validate_catalog(value)

        missing_results = copy.deepcopy(value)
        missing_results['papers'][0]['results_pages_read'].remove(5)
        with self.assertRaisesRegex(CatalogError, 'results_pages_read'):
            validate_catalog(missing_results)

        missing_visual = copy.deepcopy(value)
        missing_visual['papers'][0]['visual_pages_checked'].remove(5)
        with self.assertRaisesRegex(CatalogError, 'visual_pages_checked'):
            validate_catalog(missing_visual)

        noncontiguous = payload()
        noncontiguous['records'][0]['source']['physical_pages'] = [4, 6]
        with self.assertRaisesRegex(CatalogError, 'contiguous'):
            validate_catalog(noncontiguous)

    def test_record_domains_must_be_covered_but_paper_may_have_extras(self):
        value = payload()
        value['papers'][0]['domains'].append('other')
        validate_catalog(value)
        value['papers'][0]['domains'].remove('prognosis')
        with self.assertRaisesRegex(CatalogError, 'paper domains'):
            validate_catalog(value)

    def test_en_us_template_rejects_cjk_literal(self):
        literals = ('在', 'テスト', '검사')
        for literal in literals:
            with self.subTest(literal=literal):
                value = payload()
                value['records'][0]['rewrite_template'] = (
                    f'{literal} [population], [marker] was associated with [outcome] '
                    '([effect_estimate]).'
                )
                with self.assertRaisesRegex(CatalogError, 'contains CJK'):
                    validate_catalog(value)

    def test_template_type_error_is_reported_as_catalog_error(self):
        value = payload()
        value['records'][0]['rewrite_template'] = None
        with self.assertRaises(CatalogError):
            validate_catalog(value)

    def test_template_rejects_literal_numbers_but_allows_digits_in_slot_names(self):
        value = payload()
        item = value['records'][0]
        item['rewrite_template'] = (
            'In [population], [marker2] was associated with [outcome] ([effect_estimate]).'
        )
        next(slot for slot in item['slots'] if slot['name'] == 'marker')['name'] = 'marker2'
        validate_catalog(value)
        item['rewrite_template'] += ' Cohort 2 was retained.'
        with self.assertRaisesRegex(CatalogError, 'literal numeric'):
            validate_catalog(value)

    def test_template_rejects_source_looking_literal_acronym(self):
        value = payload()
        value['records'][0]['rewrite_template'] = (
            'In [population], MET [marker] was associated with [outcome] ([effect_estimate]).'
        )
        with self.assertRaisesRegex(CatalogError, 'acronym leaked'):
            validate_catalog(value)

    def test_verification_anchor_is_exact_for_record_pmid(self):
        value = payload()
        value['records'][0]['source']['verification_record'] = (
            'ccr-2025-2026-results-logic-audit.md#pmid-99990002'
        )
        with self.assertRaisesRegex(CatalogError, 'verification_record must be'):
            validate_catalog(value)


class RetrievalBehavior(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.value = validate_catalog(payload())

    def test_filters_use_and_semantics_on_one_record(self):
        result = search(
            self.value['records'], pmid='99990001', year='2025', domain='prognosis',
            polarity='positive', inferential_status='significant',
            result_type='survival_prognosis', evidence_layer='clinical',
            rhetorical_function='quantify_effect', logic_position='development',
            section='results', query='"association" prognosis', limit=10,
        )
        self.assertEqual(result['matched_count'], 1)
        self.assertEqual(result['records'][0]['id'], 'ccr-logic-99990001-positive')

    def test_paper_logic_filters(self):
        result = search_papers(
            self.value['papers'], year='2026', domain='genomics', polarity='positive'
        )
        self.assertEqual(result['matched_count'], 1)
        self.assertEqual(result['papers'][0]['pmid'], '99990002')

    def test_unknown_filters_and_bad_limits_fail_closed(self):
        with self.assertRaises(CatalogError):
            search(self.value['records'], polarity='trend')
        with self.assertRaises(CatalogError):
            search(self.value['records'], limit=0)

    def test_query_searches_values_not_serialized_field_names(self):
        result = search(self.value['records'], query='verification_record', limit=10)
        self.assertEqual(result['matched_count'], 0)

    def test_paper_query_ignores_field_names_and_sentinel_logic(self):
        papers = [paper(), paper('99990002', '2026')]
        for item in papers:
            item['domains'] = ['other']
            item['central_results'] = ['Neutral result text.']
            item['narrative_sequence'] = ['analysis then boundary']
            item['negative_result_handling'] = 'Neutral handling text.'
            item['claim_boundaries'] = ['Neutral boundary text.']
            item['omics_logic'] = 'Not applicable.'
            item['efficacy_logic'] = 'Not applicable.'
            item['prognosis_logic'] = 'Not applicable.'
        papers[0]['central_results'] = ['The omics prognosis relation was evaluated.']
        result = search_papers(papers, query='omics prognosis', limit=10)
        self.assertEqual(result['matched_count'], 1)
        self.assertEqual(result['papers'][0]['pmid'], '99990001')

        papers[1]['omics_logic'] = 'No omics-specific result logic was applicable.'
        result = search_papers(papers, query='omics-specific', limit=10)
        self.assertEqual(result['matched_count'], 0)

        papers[1]['efficacy_logic'] = 'Nonetheless, the boundary remains clinically important.'
        result = search_papers(papers, query='nonetheless', limit=10)
        self.assertEqual(result['matched_count'], 1)
        self.assertEqual(result['papers'][0]['pmid'], '99990002')

        papers[1]['efficacy_logic'] = '无随机比较，不能作因果疗效推断。'
        result = search_papers(papers, query='随机比较', limit=10)
        self.assertEqual(result['matched_count'], 1)
        self.assertEqual(result['papers'][0]['pmid'], '99990002')


class SafeRendering(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='ccr-render-authority-')
        self.addCleanup(temporary.cleanup)
        self.skill = Path(temporary.name) / 'skill'
        write_installed_fixture(self.skill, payload())

    def test_renderer_uses_only_explicit_slots(self):
        item = record()
        rendered = render_template(item, {
            'population': 'the prespecified cohort',
            'marker': 'user marker X',
            'outcome': 'overall survival',
            'effect_estimate': 'adjusted HR and confidence interval',
        }, skill_path=self.skill)
        self.assertIn('user marker X', rendered)
        self.assertNotIn('Marker 99990001', rendered)

    def test_missing_or_extra_slots_are_rejected(self):
        item = record()
        with self.assertRaisesRegex(CatalogError, 'slot mismatch'):
            render_template(item, {'population': 'cohort'}, skill_path=self.skill)

    def test_one_explicit_slot_can_be_reused_in_a_template(self):
        item = record()
        item['rewrite_template'] = '[marker] was measured, and [marker] was associated with [outcome].'
        item['slots'] = [
            {
                'name': 'marker',
                'description': 'User-supplied marker',
                'required': True,
                'evidence_source': 'user_supplied',
            },
            {
                'name': 'outcome',
                'description': 'User-supplied outcome',
                'required': True,
                'evidence_source': 'user_supplied',
            },
        ]
        rendered = render_template(item, {'marker': 'marker Y', 'outcome': 'overall survival'},
                                   skill_path=self.skill)
        self.assertEqual(rendered.count('marker Y'), 2)


class InstalledChecks(unittest.TestCase):
    def test_installed_fixture_cross_checks_authorities_and_audit_anchor(self):
        with tempfile.TemporaryDirectory(prefix='ccr-results-logic-') as directory:
            skill = Path(directory) / 'skill'
            write_installed_fixture(skill, payload())
            self.assertEqual(len(load_catalog(skill)['records']), 4)

            broken = payload()
            broken['papers'][0]['pdf_sha256'] = 'c' * 64
            for item in broken['records'][:2]:
                item['source']['pdf_sha256'] = 'c' * 64
            write_installed_fixture(skill, broken)
            with self.assertRaisesRegex(CatalogError, 'PDF hash disagrees'):
                load_catalog(skill)

    def test_schema_and_guide_exist(self):
        self.assertTrue((SKILL / 'references' / 'ccr-2025-2026-results-logic.schema.json').is_file())
        self.assertTrue((SKILL / 'references' / 'ccr-2025-2026-results-logic-writing.md').is_file())

    def test_schema_vocabularies_and_required_fields_match_runtime(self):
        schema = json.loads((
            SKILL / 'references' / 'ccr-2025-2026-results-logic.schema.json'
        ).read_text(encoding='utf-8'))
        record_schema = schema['$defs']['record']
        source_schema = schema['$defs']['source']
        self.assertEqual(set(record_schema['required']), set(record().keys()))
        self.assertEqual(set(source_schema['required']), set(record()['source'].keys()))
        self.assertEqual(
            set(record_schema['properties']['result_type']['enum']), MODULE.RESULT_TYPES
        )
        self.assertEqual(
            set(record_schema['properties']['claim_ceiling']['enum']), MODULE.CLAIM_CEILINGS
        )
        self.assertEqual(
            set(record_schema['properties']['inferential_status']['enum']),
            MODULE.INFERENTIAL_STATUSES,
        )
        self.assertEqual(
            set(source_schema['properties']['text_extraction_match']['enum']),
            MODULE.TEXT_EXTRACTION_MATCHES,
        )
        self.assertEqual(
            set(schema['properties']['project_scope']['properties']['issue_years']['items']['enum']),
            MODULE.ISSUE_YEARS,
        )
        self.assertEqual(set(schema['$defs']['paper']['properties']['year']['enum']), MODULE.ISSUE_YEARS)
        self.assertEqual(set(record_schema['properties']['year']['enum']), MODULE.ISSUE_YEARS)
        self.assertEqual(set(schema['$defs']['polarity']['enum']), MODULE.RESULT_POLARITIES)
        self.assertEqual(set(schema['$defs']['domain']['enum']), MODULE.DOMAINS)
        self.assertEqual(
            set(record_schema['properties']['evidence_layer']['enum']), MODULE.EVIDENCE_LAYERS
        )
        self.assertEqual(
            set(record_schema['properties']['rhetorical_function']['enum']),
            MODULE.RHETORICAL_FUNCTIONS,
        )
        self.assertEqual(
            set(record_schema['properties']['logic_position']['enum']), MODULE.LOGIC_POSITIONS
        )
        self.assertEqual(
            set(record_schema['properties']['target_sections']['items']['enum']), MODULE.SECTIONS
        )
        self.assertEqual(
            {record_schema['properties']['template_language']['const']},
            MODULE.TEMPLATE_LANGUAGES,
        )
        self.assertEqual(set(MODULE.RESULT_CLAIM_COMPATIBILITY), MODULE.RESULT_TYPES)
        allowed_claims = set()
        for result_type, claims in MODULE.RESULT_CLAIM_COMPATIBILITY.items():
            with self.subTest(result_type=result_type):
                self.assertTrue(claims)
                self.assertLessEqual(claims, MODULE.CLAIM_CEILINGS)
                allowed_claims.update(claims)
        self.assertEqual(allowed_claims, MODULE.CLAIM_CEILINGS)
        schema_compatibility = {}
        for branch in record_schema['allOf'][0]['oneOf']:
            properties = branch['properties']
            result_type = properties['result_type']['const']
            self.assertNotIn(result_type, schema_compatibility)
            schema_compatibility[result_type] = set(properties['claim_ceiling']['enum'])
        self.assertEqual(schema_compatibility, MODULE.RESULT_CLAIM_COMPATIBILITY)

    def test_real_catalog_when_integrated(self):
        path = SKILL / 'references' / 'ccr-2025-2026-results-logic.json'
        if not path.is_file():
            self.skipTest('main agent has not integrated the completed rereading yet')
        value = load_catalog(SKILL)
        expected = set(value['project_scope']['expected_pmids'])
        self.assertEqual(len(expected), 125)
        self.assertEqual(sum(paper['year'] == '2025' for paper in value['papers']), 48)
        self.assertEqual(sum(paper['year'] == '2026' for paper in value['papers']), 77)
        self.assertEqual({paper['pmid'] for paper in value['papers']}, expected)
        self.assertTrue(all(2 <= len(paper['record_ids']) <= 4 for paper in value['papers']))
        self.assertTrue(all(
            record['source']['quotation_verified']
            and record['source']['visual_verified']
            and record['source']['verification_level'] == 'visually_verified_exact'
            for record in value['records']
        ))
        self.assertTrue(all(record['template_language'] == 'en-US' for record in value['records']))
        self.assertFalse(any(
            re.search(r'[\u3400-\u4dbf\u4e00-\u9fff]', record['rewrite_template'])
            for record in value['records']
        ))
        focused = search_papers(
            value['papers'], domain='integrated_omics', query='survival', limit=500
        )
        self.assertGreater(focused['matched_count'], 0)
        self.assertLess(focused['matched_count'], 125)
        broad = search_papers(value['papers'], query='omics prognosis', limit=500)
        self.assertLess(broad['matched_count'], 125)

    def test_real_cli_retrieval_and_render_smoke(self):
        path = SKILL / 'references' / 'ccr-2025-2026-results-logic.json'
        if not path.is_file():
            self.skipTest('main agent has not integrated the completed rereading yet')
        value = load_catalog(SKILL)
        item = value['records'][0]
        environment = {**os.environ, 'PYTHONDONTWRITEBYTECODE': '1',
                       'PYTHONIOENCODING': 'utf-8'}
        retrieval = subprocess.run(
            [sys.executable, str(SCRIPT), '--skill-path', str(SKILL),
             '--template-id', item['id'], '--json'],
            cwd=SKILL, env=environment, capture_output=True, text=True,
            encoding='utf-8', check=False,
        )
        self.assertEqual(retrieval.returncode, 0, retrieval.stderr)
        self.assertEqual(json.loads(retrieval.stdout)['matched_count'], 1)

        locale_environment = dict(os.environ)
        locale_environment.pop('PYTHONIOENCODING', None)
        locale_environment['PYTHONDONTWRITEBYTECODE'] = '1'
        locale_retrieval = subprocess.run(
            [sys.executable, str(SCRIPT), '--skill-path', str(SKILL),
             '--template-id', item['id'], '--json'],
            cwd=SKILL, env=locale_environment, capture_output=True, check=False,
        )
        self.assertEqual(locale_retrieval.returncode, 0, locale_retrieval.stderr)
        self.assertEqual(
            json.loads(locale_retrieval.stdout.decode('utf-8'))['matched_count'], 1
        )

        command = [sys.executable, str(SCRIPT), '--skill-path', str(SKILL),
                   '--template-id', item['id'], '--render', '--json']
        for slot in item['slots']:
            command.extend(['--slot', f'{slot["name"]}=USER_{slot["name"].upper()}'])
        rendered = subprocess.run(
            command, cwd=SKILL, env=environment, capture_output=True, text=True,
            encoding='utf-8', check=False,
        )
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        output = json.loads(rendered.stdout)
        for slot in item['slots']:
            self.assertIn(f'USER_{slot["name"].upper()}', output['rendered_text'])

        sentence_only_options = (
            ['--template-id', item['id']],
            ['--inferential-status', 'significant'],
            ['--significance', 'significant'],
            ['--result-type', 'survival_prognosis'],
            ['--evidence-layer', 'clinical'],
            ['--rhetorical-function', 'quantify_effect'],
            ['--logic-position', 'development'],
            ['--section', 'results'],
            ['--render'],
            ['--slot', 'value=user'],
        )
        for option in sentence_only_options:
            with self.subTest(option=option):
                rejected = subprocess.run(
                    [sys.executable, str(SCRIPT), '--skill-path', str(SKILL),
                     '--paper-logic', *option, '--json'],
                    cwd=SKILL, env=environment, capture_output=True, text=True,
                    encoding='utf-8', check=False,
                )
                self.assertNotEqual(rejected.returncode, 0)
                self.assertIn('sentence-only options', rejected.stderr)
        allowed = subprocess.run(
            [sys.executable, str(SCRIPT), '--skill-path', str(SKILL), '--paper-logic',
             '--polarity', 'positive', '--limit', '1', '--json'],
            cwd=SKILL, env=environment, capture_output=True, text=True,
            encoding='utf-8', check=False,
        )
        self.assertEqual(allowed.returncode, 0, allowed.stderr)


if __name__ == '__main__':
    unittest.main()
