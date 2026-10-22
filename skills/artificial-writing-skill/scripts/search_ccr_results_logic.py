import argparse
import csv
import json
import re
import shlex
import sys
from pathlib import Path

sys.dont_write_bytecode = True
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from sentence_live_controls import (
    CatalogError, apply_live_controls, control_markdown, control_metadata,
    is_accepted, require_renderable,
)


CATALOG_NAME = 'ccr-2025-2026-results-logic.json'
SCHEMA_VERSION = 1
JOURNAL = 'Clinical Cancer Research'
JOURNAL_ID = 'ccr'
ISSUE_YEARS = {'2025', '2026'}
RESULT_POLARITIES = {'positive', 'negative', 'mixed', 'inconclusive', 'descriptive'}
INFERENTIAL_STATUSES = {
    'significant', 'nonsignificant', 'mixed', 'not_reported', 'not_applicable'
}
LOGIC_POSITIONS = {'opening', 'development', 'contrast', 'qualification', 'closure'}
EVIDENCE_LAYERS = {
    'clinical', 'genomic', 'transcriptomic', 'protein', 'single_cell', 'spatial',
    'metabolomic', 'integrated', 'preclinical', 'modeling', 'imaging',
}
DOMAINS = {
    'genomics', 'transcriptomics', 'single_cell', 'spatial_omics', 'proteomics',
    'metabolomics', 'integrated_omics', 'liquid_biopsy', 'clinical_efficacy',
    'prognosis', 'safety', 'pk_pd', 'diagnostic_model',
    'preclinical_functional', 'imaging', 'other',
}
RESULT_TYPES = {
    'omics_landscape', 'differential_feature', 'pathway_or_state',
    'cross_layer_concordance', 'assay_concordance', 'treatment_efficacy',
    'treatment_activity', 'survival_prognosis', 'biomarker_association',
    'subgroup_signal', 'negative_primary_endpoint', 'null_biomarker',
    'safety_tolerability', 'pk_pd_exposure', 'diagnostic_performance',
    'model_performance', 'functional_perturbation', 'resistance_mechanism',
    'descriptive_frequency', 'other',
}
RHETORICAL_FUNCTIONS = {
    'establish_analysis_set', 'state_primary_finding', 'quantify_effect',
    'report_null_result', 'contrast_groups', 'contrast_modalities',
    'qualify_uncertainty', 'state_exception', 'integrate_evidence_layers',
    'connect_to_outcome', 'limit_inference', 'justify_follow_up',
}
SECTIONS = {'abstract-results', 'results', 'discussion', 'conclusion'}
CLAIM_CEILINGS = {
    'descriptive_only', 'association_only', 'exploratory_hypothesis',
    'model_performance_only', 'preclinical_mechanism_only',
    'clinical_activity_only', 'comparative_efficacy_only',
    'prognostic_association_only',
}
TEXT_EXTRACTION_MATCHES = {'normalized_literal', 'punctuation_insensitive', 'none'}
TEMPLATE_LANGUAGES = {'en-US'}
GENERIC_TEMPLATE_ACRONYMS = {
    'AUC', 'BOR', 'CI', 'CR', 'CT', 'DCR', 'DFS', 'DNA', 'DOR', 'FDR', 'HR',
    'IQR', 'ITT', 'MHC', 'MRI', 'MRD', 'OR', 'ORR', 'OS', 'PD', 'PET', 'PFS',
    'PK', 'PR', 'RECIST', 'RFS', 'RNA', 'ROC', 'SD', 'TMB', 'VAF',
}
RESULT_CLAIM_COMPATIBILITY = {
    'omics_landscape': {'descriptive_only', 'association_only'},
    'differential_feature': {'descriptive_only', 'association_only', 'preclinical_mechanism_only'},
    'pathway_or_state': {'descriptive_only', 'association_only', 'exploratory_hypothesis', 'preclinical_mechanism_only'},
    'cross_layer_concordance': {'descriptive_only', 'association_only'},
    'assay_concordance': {'descriptive_only', 'association_only', 'model_performance_only'},
    'treatment_efficacy': {'comparative_efficacy_only', 'exploratory_hypothesis', 'association_only'},
    'treatment_activity': {'clinical_activity_only'},
    'survival_prognosis': {'prognostic_association_only'},
    'biomarker_association': {'association_only', 'exploratory_hypothesis', 'preclinical_mechanism_only', 'prognostic_association_only'},
    'subgroup_signal': {'exploratory_hypothesis'},
    'negative_primary_endpoint': {'clinical_activity_only', 'comparative_efficacy_only'},
    'null_biomarker': {'descriptive_only', 'association_only', 'exploratory_hypothesis', 'prognostic_association_only'},
    'safety_tolerability': {'clinical_activity_only', 'association_only'},
    'pk_pd_exposure': {'association_only', 'clinical_activity_only', 'model_performance_only'},
    'diagnostic_performance': {'model_performance_only', 'exploratory_hypothesis'},
    'model_performance': {'model_performance_only', 'exploratory_hypothesis'},
    'functional_perturbation': {'preclinical_mechanism_only', 'association_only', 'exploratory_hypothesis'},
    'resistance_mechanism': {'preclinical_mechanism_only', 'association_only', 'exploratory_hypothesis'},
    'descriptive_frequency': {'descriptive_only'},
    'other': {'descriptive_only', 'association_only', 'exploratory_hypothesis'},
}

TEMPLATE_ID = re.compile(r'^ccr-logic-[0-9]{8}-[a-z0-9]+(?:-[a-z0-9]+)*$')
PMID = re.compile(r'^\d{8}$')
SHA256 = re.compile(r'^[0-9a-f]{64}$')


def _configure_cli_streams():
    """Emit deterministic UTF-8 on Windows consoles and redirected pipes."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, 'reconfigure', None)
        if callable(reconfigure):
            reconfigure(encoding='utf-8', errors='backslashreplace')
SLOT_NAME = re.compile(r'^[a-z][a-z0-9_]*$')
PLACEHOLDER = re.compile(r'\[([a-z][a-z0-9_]*)\]')
MARKDOWN_ANCHOR = re.compile(r'^[A-Za-z0-9][A-Za-z0-9._:-]*$')


def _require_string(value, label):
    if not isinstance(value, str) or not value.strip():
        raise CatalogError(f'{label} must be a nonempty string')


def _require_string_list(value, label, *, nonempty=True, allowed=None):
    if not isinstance(value, list) or (nonempty and not value):
        raise CatalogError(f'{label} must be a {"nonempty " if nonempty else ""}list')
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise CatalogError(f'{label} contains an empty or non-string value')
    if len(value) != len(set(value)):
        raise CatalogError(f'{label} contains duplicate values')
    if allowed is not None and not set(value).issubset(allowed):
        raise CatalogError(f'{label} contains unsupported values: {sorted(set(value) - allowed)}')


def _normalize(value):
    return re.sub(r'\s+', ' ', value.strip())


def _split_authority_values(value):
    return {item.strip() for item in value.split(';') if item.strip()}


def _read_csv_by_pmid(path):
    if not path.is_file():
        raise CatalogError(f'installed authority is missing: {path.name}')
    with path.open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    indexed = {}
    for row in rows:
        pmid = row.get('pmid', '').strip()
        if not pmid:
            continue
        if pmid in indexed:
            raise CatalogError(f'duplicate PMID in {path.name}: {pmid}')
        indexed[pmid] = row
    return indexed


def _validate_scope(scope):
    required = {
        'membership_source', 'journal_id', 'issue_years', 'eligibility',
        'expected_pmids', 'coverage_unit', 'paper_coverage_complete',
        'sentence_minimum_per_paper', 'sentence_maximum_per_paper',
        'audit_resource', 'source_scope',
    }
    if not isinstance(scope, dict) or set(scope) != required:
        raise CatalogError('project_scope fields are invalid')
    if scope['membership_source'] != 'library-index.csv':
        raise CatalogError('membership_source must be library-index.csv')
    if scope['journal_id'] != JOURNAL_ID:
        raise CatalogError('project_scope.journal_id must be ccr')
    _require_string_list(scope['issue_years'], 'project_scope.issue_years')
    if set(scope['issue_years']) != ISSUE_YEARS:
        raise CatalogError('project_scope.issue_years must contain 2025 and 2026')
    if scope['eligibility'] != 'included':
        raise CatalogError('project_scope.eligibility must be included')
    _require_string_list(scope['expected_pmids'], 'project_scope.expected_pmids')
    if any(not PMID.fullmatch(item) for item in scope['expected_pmids']):
        raise CatalogError('project_scope.expected_pmids contains an invalid PMID')
    if scope['coverage_unit'] != 'per-paper-results-logic-with-source-sentences':
        raise CatalogError('unsupported coverage_unit')
    if scope['paper_coverage_complete'] is not True:
        raise CatalogError('installed catalog must declare paper_coverage_complete=true')
    minimum, maximum = scope['sentence_minimum_per_paper'], scope['sentence_maximum_per_paper']
    if type(minimum) is not int or type(maximum) is not int or not (1 <= minimum <= maximum <= 10):
        raise CatalogError('invalid per-paper sentence coverage bounds')
    if scope['audit_resource'] != 'ccr-2025-2026-results-logic-audit.md':
        raise CatalogError('unsupported audit_resource')
    _require_string(scope['source_scope'], 'project_scope.source_scope')


def _validate_source(record, source):
    record_id = record['id']
    required = {
        'pdf_sha256', 'supplied_pdf_version', 'physical_page', 'physical_pages', 'section',
        'subheading', 'source_sentence', 'verification_level',
        'quotation_verified', 'visual_verified', 'verification_record',
        'text_extraction_match', 'verification_note',
    }
    if not isinstance(source, dict) or set(source) != required:
        raise CatalogError(f'{record_id}: source fields are invalid')
    if not isinstance(source['pdf_sha256'], str) or not SHA256.fullmatch(source['pdf_sha256']):
        raise CatalogError(f'{record_id}: invalid source.pdf_sha256')
    _require_string(source['supplied_pdf_version'], f'{record_id}: source.supplied_pdf_version')
    if type(source['physical_page']) is not int or source['physical_page'] < 1:
        raise CatalogError(f'{record_id}: source.physical_page must be positive')
    if (not isinstance(source['physical_pages'], list) or not source['physical_pages']
            or any(type(page) is not int or page < 1 for page in source['physical_pages'])
            or source['physical_pages'] != sorted(set(source['physical_pages']))
            or source['physical_page'] != source['physical_pages'][0]
            or source['physical_pages'] != list(range(
                source['physical_pages'][0], source['physical_pages'][-1] + 1
            ))):
        raise CatalogError(
            f'{record_id}: source.physical_pages must be sorted, unique, contiguous and '
            'start at physical_page'
        )
    if source['section'] != 'results':
        raise CatalogError(f'{record_id}: source.section must be body results')
    _require_string(source['subheading'], f'{record_id}: source.subheading')
    _require_string(source['source_sentence'], f'{record_id}: source.source_sentence')
    if PLACEHOLDER.search(source['source_sentence']):
        raise CatalogError(f'{record_id}: source sentence must not contain template slots')
    if source['verification_level'] != 'visually_verified_exact':
        raise CatalogError(f'{record_id}: source sentence must be visually_verified_exact')
    if source['quotation_verified'] is not True or source['visual_verified'] is not True:
        raise CatalogError(f'{record_id}: source quote and page must be visually verified')
    expected_record = f'ccr-2025-2026-results-logic-audit.md#pmid-{record["pmid"]}'
    if source['verification_record'] != expected_record:
        raise CatalogError(f'{record_id}: verification_record must be {expected_record}')
    if (not isinstance(source['text_extraction_match'], str)
            or source['text_extraction_match'] not in TEXT_EXTRACTION_MATCHES):
        raise CatalogError(f'{record_id}: unsupported source.text_extraction_match')
    _require_string(source['verification_note'], f'{record_id}: source.verification_note')


def _validate_slots(record):
    record_id = record['id']
    template = record['rewrite_template']
    _require_string(template, f'{record_id}: rewrite_template')
    if re.search(r'[\u3040-\u30ff\u31f0-\u31ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af]', template):
        raise CatalogError(f'{record_id}: en-US rewrite_template contains CJK text')
    placeholder_free = PLACEHOLDER.sub('', template)
    if '[' in placeholder_free or ']' in placeholder_free:
        raise CatalogError(f'{record_id}: malformed template slot')
    if re.search(r'\d', placeholder_free):
        raise CatalogError(f'{record_id}: literal numeric value leaked into rewrite_template')
    acronyms = set(re.findall(r'\b[A-Z][A-Z0-9/-]{1,}\b', placeholder_free))
    unsupported = acronyms - GENERIC_TEMPLATE_ACRONYMS
    if unsupported:
        raise CatalogError(
            f'{record_id}: source-looking acronym leaked into rewrite_template: {sorted(unsupported)}'
        )
    if not isinstance(record['slots'], list) or not record['slots']:
        raise CatalogError(f'{record_id}: slots must be nonempty')
    names = []
    for slot in record['slots']:
        if not isinstance(slot, dict) or set(slot) != {
            'name', 'description', 'required', 'evidence_source'
        }:
            raise CatalogError(f'{record_id}: slot fields are invalid')
        if not isinstance(slot['name'], str) or not SLOT_NAME.fullmatch(slot['name']):
            raise CatalogError(f'{record_id}: invalid slot name')
        _require_string(slot['description'], f'{record_id}: slot description')
        if slot['required'] is not True or slot['evidence_source'] != 'user_supplied':
            raise CatalogError(f'{record_id}: every slot must be required and user_supplied')
        names.append(slot['name'])
    if len(names) != len(set(names)):
        raise CatalogError(f'{record_id}: duplicate slot names')
    if set(names) != set(PLACEHOLDER.findall(template)):
        raise CatalogError(f'{record_id}: template placeholders and declared slots differ')


def _validate_record(record, expected_pmids):
    required = {
        'id', 'pmid', 'doi', 'title', 'journal', 'journal_id', 'year', 'source',
        'domains', 'result_polarity', 'inferential_status', 'result_type',
        'evidence_layer', 'rhetorical_function', 'logic_position',
        'target_sections', 'use_when_zh', 'do_not_use_when_zh',
        'rewrite_template', 'template_language', 'slots', 'source_specific_tokens', 'claim_ceiling',
        'evidence_boundary', 'logic_note_zh',
    }
    if not isinstance(record, dict) or set(record) != required:
        missing = required - set(record) if isinstance(record, dict) else required
        extra = set(record) - required if isinstance(record, dict) else set()
        raise CatalogError(f'record fields are invalid; missing={sorted(missing)}, extra={sorted(extra)}')
    record_id = record['id']
    if not isinstance(record_id, str) or not TEMPLATE_ID.fullmatch(record_id):
        raise CatalogError(f'invalid template id: {record_id!r}')
    if not isinstance(record['pmid'], str) or not PMID.fullmatch(record['pmid']):
        raise CatalogError(f'{record_id}: invalid PMID')
    if record['pmid'] not in expected_pmids:
        raise CatalogError(f'{record_id}: PMID outside expected scope')
    for field in ('doi', 'title', 'journal', 'use_when_zh', 'do_not_use_when_zh',
                  'evidence_boundary', 'logic_note_zh'):
        _require_string(record[field], f'{record_id}: {field}')
    if record['journal_id'] != JOURNAL_ID or record['journal'] != JOURNAL:
        raise CatalogError(f'{record_id}: journal identity is not CCR')
    if not isinstance(record['year'], str) or record['year'] not in ISSUE_YEARS:
        raise CatalogError(f'{record_id}: year is outside 2025-2026')
    _require_string_list(record['domains'], f'{record_id}: domains', allowed=DOMAINS)
    for field, allowed in (
        ('result_polarity', RESULT_POLARITIES),
        ('inferential_status', INFERENTIAL_STATUSES),
        ('result_type', RESULT_TYPES),
        ('evidence_layer', EVIDENCE_LAYERS),
        ('rhetorical_function', RHETORICAL_FUNCTIONS),
        ('logic_position', LOGIC_POSITIONS),
        ('claim_ceiling', CLAIM_CEILINGS),
    ):
        if not isinstance(record[field], str) or record[field] not in allowed:
            raise CatalogError(f'{record_id}: unsupported {field}={record[field]!r}')
    _require_string_list(record['target_sections'], f'{record_id}: target_sections', allowed=SECTIONS)
    if not isinstance(record['template_language'], str) or record['template_language'] not in TEMPLATE_LANGUAGES:
        raise CatalogError(f'{record_id}: unsupported template_language')
    if record['claim_ceiling'] not in RESULT_CLAIM_COMPATIBILITY[record['result_type']]:
        raise CatalogError(
            f'{record_id}: claim_ceiling={record["claim_ceiling"]!r} is incompatible '
            f'with result_type={record["result_type"]!r}'
        )
    _validate_source(record, record['source'])
    _validate_slots(record)
    _require_string_list(record['source_specific_tokens'], f'{record_id}: source_specific_tokens')
    source_text = record['source']['source_sentence'].casefold()
    literal_template = PLACEHOLDER.sub('', record['rewrite_template']).casefold()
    for token in record['source_specific_tokens']:
        if token.casefold() not in source_text:
            raise CatalogError(f'{record_id}: protected source token is absent from source sentence')
        if token.casefold() in literal_template:
            raise CatalogError(f'{record_id}: source-specific token leaked into template: {token!r}')


def _validate_paper(paper, expected_pmids):
    required = {
        'pmid', 'doi', 'year', 'title', 'journal', 'journal_id', 'pdf_sha256',
        'supplied_pdf_version', 'physical_pages', 'results_pages_read',
        'visual_pages_checked', 'result_profile', 'domains', 'central_results',
        'narrative_sequence', 'negative_result_handling', 'omics_logic',
        'efficacy_logic', 'prognosis_logic', 'claim_boundaries', 'record_ids',
    }
    if not isinstance(paper, dict) or set(paper) != required:
        raise CatalogError(f'paper record fields are invalid for {paper.get("pmid") if isinstance(paper, dict) else "unknown"}')
    pmid = paper['pmid']
    if pmid not in expected_pmids:
        raise CatalogError(f'paper PMID outside scope: {pmid}')
    for field in ('doi', 'title', 'journal', 'supplied_pdf_version',
                  'negative_result_handling', 'omics_logic', 'efficacy_logic',
                  'prognosis_logic'):
        _require_string(paper[field], f'{pmid}: paper.{field}')
    if paper['journal'] != JOURNAL or paper['journal_id'] != JOURNAL_ID:
        raise CatalogError(f'{pmid}: paper journal identity is not CCR')
    if not isinstance(paper['year'], str) or paper['year'] not in ISSUE_YEARS:
        raise CatalogError(f'{pmid}: paper year outside scope')
    if not isinstance(paper['pdf_sha256'], str) or not SHA256.fullmatch(paper['pdf_sha256']):
        raise CatalogError(f'{pmid}: invalid paper PDF hash')
    if type(paper['physical_pages']) is not int or paper['physical_pages'] < 1:
        raise CatalogError(f'{pmid}: invalid paper physical_pages')
    for field in ('results_pages_read', 'visual_pages_checked'):
        values = paper[field]
        if not isinstance(values, list) or not values or any(
            type(value) is not int or not 1 <= value <= paper['physical_pages'] for value in values
        ):
            raise CatalogError(f'{pmid}: invalid {field}')
        if len(values) != len(set(values)):
            raise CatalogError(f'{pmid}: duplicate page in {field}')
    _require_string_list(paper['result_profile'], f'{pmid}: result_profile', allowed=RESULT_POLARITIES)
    _require_string_list(paper['domains'], f'{pmid}: domains', allowed=DOMAINS)
    _require_string_list(paper['central_results'], f'{pmid}: central_results')
    _require_string_list(paper['narrative_sequence'], f'{pmid}: narrative_sequence')
    _require_string_list(paper['claim_boundaries'], f'{pmid}: claim_boundaries')
    _require_string_list(paper['record_ids'], f'{pmid}: record_ids')


def validate_catalog(payload):
    if not isinstance(payload, dict) or set(payload) != {
        'schema_version', 'updated', 'scope', 'project_scope', 'papers', 'records'
    }:
        raise CatalogError('catalog top-level fields are invalid')
    if payload['schema_version'] != SCHEMA_VERSION:
        raise CatalogError('unsupported schema_version')
    if not isinstance(payload['updated'], str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', payload['updated']):
        raise CatalogError('updated must use YYYY-MM-DD')
    _require_string(payload['scope'], 'scope')
    _validate_scope(payload['project_scope'])
    if not isinstance(payload['papers'], list) or not isinstance(payload['records'], list):
        raise CatalogError('papers and records must be lists')
    expected_pmids = set(payload['project_scope']['expected_pmids'])
    seen_papers, seen_records = set(), set()
    for paper in payload['papers']:
        _validate_paper(paper, expected_pmids)
        if paper['pmid'] in seen_papers:
            raise CatalogError(f'duplicate paper PMID: {paper["pmid"]}')
        seen_papers.add(paper['pmid'])
    for record in payload['records']:
        _validate_record(record, expected_pmids)
        if record['id'] in seen_records:
            raise CatalogError(f'duplicate template ID: {record["id"]}')
        seen_records.add(record['id'])
    if seen_papers != expected_pmids:
        raise CatalogError(
            f'paper coverage differs from expected scope; missing={sorted(expected_pmids-seen_papers)}, '
            f'extra={sorted(seen_papers-expected_pmids)}'
        )
    minimum = payload['project_scope']['sentence_minimum_per_paper']
    maximum = payload['project_scope']['sentence_maximum_per_paper']
    by_pmid = {pmid: [] for pmid in expected_pmids}
    for record in payload['records']:
        by_pmid[record['pmid']].append(record)
    papers = {paper['pmid']: paper for paper in payload['papers']}
    for pmid, records in by_pmid.items():
        if not minimum <= len(records) <= maximum:
            raise CatalogError(f'{pmid}: expected {minimum}-{maximum} records, found {len(records)}')
        ids = {record['id'] for record in records}
        if ids != set(papers[pmid]['record_ids']):
            raise CatalogError(f'{pmid}: paper record_ids disagree with sentence records')
        if not {record['result_polarity'] for record in records}.issubset(
            set(papers[pmid]['result_profile'])
        ):
            raise CatalogError(f'{pmid}: paper result_profile omits a record polarity')
        record_domains = {domain for record in records for domain in record['domains']}
        if not record_domains.issubset(set(papers[pmid]['domains'])):
            raise CatalogError(f'{pmid}: paper domains omit one or more record domains')
        results_pages = set(papers[pmid]['results_pages_read'])
        visual_pages = set(papers[pmid]['visual_pages_checked'])
        for record in records:
            source_pages = set(record['source']['physical_pages'])
            if not source_pages.issubset(results_pages):
                raise CatalogError(f'{record["id"]}: source pages are outside results_pages_read')
            if not source_pages.issubset(visual_pages):
                raise CatalogError(f'{record["id"]}: source pages are outside visual_pages_checked')
    return payload


def _validate_markdown_reference(references, record):
    relative_path, separator, anchor = record['source']['verification_record'].partition('#')
    if not separator or not anchor or not MARKDOWN_ANCHOR.fullmatch(anchor):
        raise CatalogError(f'{record["id"]}: malformed verification_record anchor')
    target = (references / relative_path).resolve()
    references = references.resolve()
    if not target.is_relative_to(references) or not target.is_file():
        raise CatalogError(f'{record["id"]}: verification_record target is missing or unsafe')
    text = target.read_text(encoding='utf-8-sig')
    headings = re.findall(r'(?m)^#{1,6}\s+(.+?)\s*#*$', text)
    anchors = {re.sub(r'[^\w-]', '', heading.casefold().replace(' ', '-')) for heading in headings}
    if anchor not in anchors:
        raise CatalogError(f'{record["id"]}: verification_record anchor is missing')


def validate_installed_catalog(skill, payload):
    skill = Path(skill)
    references = skill / 'references'
    library = _read_csv_by_pmid(references / 'library-index.csv')
    versions = _read_csv_by_pmid(references / 'source-version-register.csv')
    expected = {
        pmid for pmid, row in library.items()
        if row.get('journal', '').strip() == JOURNAL
        and row.get('year', '').strip() in ISSUE_YEARS
        and row.get('eligibility', '').strip() == 'included'
    }
    declared = set(payload['project_scope']['expected_pmids'])
    if declared != expected:
        raise CatalogError(
            f'expected_pmids do not equal current included CCR 2025-2026 scope; '
            f'missing={sorted(expected-declared)}, extra={sorted(declared-expected)}'
        )
    papers = {paper['pmid']: paper for paper in payload['papers']}
    for record in payload['records']:
        _validate_markdown_reference(references, record)
    for pmid in expected:
        article, version, paper = library[pmid], versions.get(pmid), papers[pmid]
        if version is None:
            raise CatalogError(f'{pmid}: missing source-version row')
        comparisons = (
            ('doi', paper['doi'].casefold(), article.get('doi', '').strip().casefold()),
            ('title', _normalize(paper['title']), _normalize(article.get('title', ''))),
            ('year', paper['year'], article.get('year', '').strip()),
        )
        for field, actual, authority in comparisons:
            if actual != authority:
                raise CatalogError(f'{pmid}: paper {field} disagrees with installed authority')
        if paper['pdf_sha256'] not in _split_authority_values(version.get('sha256', '')):
            raise CatalogError(f'{pmid}: paper PDF hash disagrees with installed authority')
        if str(paper['physical_pages']) not in _split_authority_values(version.get('physical_pages', '')):
            raise CatalogError(f'{pmid}: paper page count disagrees with installed authority')
        if paper['supplied_pdf_version'] not in _split_authority_values(
            version.get('supplied_pdf_version', '')
        ):
            raise CatalogError(f'{pmid}: supplied PDF version disagrees with installed authority')
        for record in (item for item in payload['records'] if item['pmid'] == pmid):
            if record['doi'].casefold() != paper['doi'].casefold():
                raise CatalogError(f'{record["id"]}: DOI disagrees with paper record')
            if _normalize(record['title']) != _normalize(paper['title']):
                raise CatalogError(f'{record["id"]}: title disagrees with paper record')
            if record['year'] != paper['year']:
                raise CatalogError(f'{record["id"]}: year disagrees with paper record')
            if record['source']['pdf_sha256'] != paper['pdf_sha256']:
                raise CatalogError(f'{record["id"]}: source hash disagrees with paper record')
            if record['source']['supplied_pdf_version'] != paper['supplied_pdf_version']:
                raise CatalogError(f'{record["id"]}: source version disagrees with paper record')
            if record['source']['physical_page'] > paper['physical_pages']:
                raise CatalogError(f'{record["id"]}: source page exceeds PDF bounds')
    return payload


def load_catalog(skill, catalog_path=None):
    skill = Path(skill)
    path = Path(catalog_path) if catalog_path else skill / 'references' / CATALOG_NAME
    if not path.is_file():
        raise CatalogError(f'results-logic catalog not found: {path}')
    payload = json.loads(path.read_text(encoding='utf-8-sig'))
    validate_catalog(payload)
    return validate_installed_catalog(skill, payload)


def _query_terms(query):
    if not query.strip():
        return []
    try:
        terms = shlex.split(query)
    except ValueError as error:
        raise CatalogError(f'invalid query quoting: {error}') from error
    return [_normalize(term).casefold() for term in terms if term.strip()]


def _searchable(record):
    source = record['source']
    values = [
        record['title'], record['journal'], *record['domains'], record['result_polarity'],
        record['inferential_status'], record['result_type'], record['evidence_layer'],
        record['rhetorical_function'], record['logic_position'], *record['target_sections'],
        record['use_when_zh'], record['do_not_use_when_zh'], record['rewrite_template'],
        record['claim_ceiling'], record['evidence_boundary'], record['logic_note_zh'],
        source['subheading'], source['source_sentence'],
    ]
    return ' '.join(str(value) for value in values).casefold()


def _meaningful_paper_logic(value):
    normalized = _normalize(value).casefold().rstrip(' .;:。；：')
    exact_sentinels = {'not applicable', 'none', '无', '未报告'}
    generic_sentinels = {
        'no omics-specific result logic',
        'no omics-specific result logic was applicable',
        'no omics-specific result logic was reported',
        'no treatment-efficacy result logic',
        'no treatment-efficacy result logic was applicable',
        'no treatment-efficacy result logic was reported',
        'no prognostic result logic',
        'no prognostic result logic was applicable',
        'no prognostic result logic was reported',
    }
    return bool(normalized) and normalized not in exact_sentinels | generic_sentinels


def _paper_searchable(paper):
    values = [
        paper['title'], *paper['domains'], *paper['result_profile'],
        *paper['central_results'], *paper['narrative_sequence'],
        paper['negative_result_handling'], *paper['claim_boundaries'],
    ]
    for field in ('omics_logic', 'efficacy_logic', 'prognosis_logic'):
        if _meaningful_paper_logic(paper[field]):
            values.append(paper[field])
    return ' '.join(str(value) for value in values).casefold()


def search(records, *, pmid='', template_id='', year='', domain='', polarity='',
           inferential_status='', result_type='', evidence_layer='',
           rhetorical_function='', logic_position='', section='', query='', limit=10,
           accepted_only=False, skill_path=None):
    if type(limit) is not int or not 1 <= limit <= 500:
        raise CatalogError('limit must be between 1 and 500')
    if pmid and not PMID.fullmatch(pmid):
        raise CatalogError('pmid must be eight digits')
    if template_id and not TEMPLATE_ID.fullmatch(template_id):
        raise CatalogError('invalid template_id')
    validations = (
        (year, ISSUE_YEARS, 'year'), (domain, DOMAINS, 'domain'),
        (polarity, RESULT_POLARITIES, 'polarity'),
        (inferential_status, INFERENTIAL_STATUSES, 'inferential_status'),
        (result_type, RESULT_TYPES, 'result_type'),
        (evidence_layer, EVIDENCE_LAYERS, 'evidence_layer'),
        (rhetorical_function, RHETORICAL_FUNCTIONS, 'rhetorical_function'),
        (logic_position, LOGIC_POSITIONS, 'logic_position'),
        (section, SECTIONS, 'section'),
    )
    for value, allowed, label in validations:
        if value and value not in allowed:
            raise CatalogError(f'unknown {label}: {value}')
    terms = _query_terms(query)
    matches = []
    for record in apply_live_controls(records, skill_path):
        if accepted_only and not is_accepted(record):
            continue
        if pmid and record['pmid'] != pmid:
            continue
        if template_id and record['id'] != template_id:
            continue
        if year and record['year'] != year:
            continue
        if domain and domain not in record['domains']:
            continue
        if polarity and record['result_polarity'] != polarity:
            continue
        if inferential_status and record['inferential_status'] != inferential_status:
            continue
        if result_type and record['result_type'] != result_type:
            continue
        if evidence_layer and record['evidence_layer'] != evidence_layer:
            continue
        if rhetorical_function and record['rhetorical_function'] != rhetorical_function:
            continue
        if logic_position and record['logic_position'] != logic_position:
            continue
        if section and section not in record['target_sections']:
            continue
        searchable = _searchable(record)
        if any(term not in searchable for term in terms):
            continue
        matches.append(record)
    matches.sort(key=lambda item: (item['year'], item['pmid'], item['id']))
    return {
        'matched_count': len(matches),
        'records': matches[:limit],
        'boundary': (
            'The source sentence documents a literature writing pattern. The rewrite '
            'template may be filled only with user-supplied evidence; source-paper '
            'variables, treatments, estimates, endpoints, and interpretations are not defaults.'
        ),
    }


def search_papers(papers, *, pmid='', year='', domain='', polarity='', query='', limit=10,
                  accepted_only=False, skill_path=None, sentence_records=None):
    if type(limit) is not int or not 1 <= limit <= 500:
        raise CatalogError('limit must be between 1 and 500')
    if pmid and not PMID.fullmatch(pmid):
        raise CatalogError('pmid must be eight digits')
    for value, allowed, label in (
        (year, ISSUE_YEARS, 'year'), (domain, DOMAINS, 'domain'),
        (polarity, RESULT_POLARITIES, 'polarity'),
    ):
        if value and value not in allowed:
            raise CatalogError(f'unknown {label}: {value}')
    terms = _query_terms(query)
    matches = []
    controlled_records = apply_live_controls(sentence_records or [], skill_path)
    for paper in apply_live_controls(papers, skill_path, text_builder=_paper_searchable):
        # A sentence-specific rule applies to this narrative only when the
        # narrative itself matches; linked records keep their individual states.
        paper['control_compatibility'] = {
            **paper['control_compatibility'],
            'article_regex_rules': 'evaluated_against_paper_narrative_text_only',
        }
        paper['linked_record_controls'] = [
            {'id': item['id'], 'pmid': item['pmid'], **control_metadata(item)}
            for item in controlled_records
            if item['id'] in paper['record_ids'] and item['pmid'] == paper['pmid']
        ]
        paper['linked_record_controls_status'] = (
            'evaluated_individually_without_source_wording'
            if sentence_records is not None else 'sentence_records_not_supplied'
        )
        if accepted_only and not is_accepted(paper):
            continue
        if pmid and paper['pmid'] != pmid:
            continue
        if year and paper['year'] != year:
            continue
        if domain and domain not in paper['domains']:
            continue
        if polarity and polarity not in paper['result_profile']:
            continue
        searchable = _paper_searchable(paper)
        if any(term not in searchable for term in terms):
            continue
        matches.append(paper)
    matches.sort(key=lambda item: (item['year'], item['pmid']))
    return {'matched_count': len(matches), 'papers': matches[:limit]}


def parse_slot_arguments(arguments):
    values = {}
    for argument in arguments:
        if '=' not in argument:
            raise CatalogError(f'slot must use NAME=VALUE: {argument!r}')
        name, value = (item.strip() for item in argument.split('=', 1))
        if not SLOT_NAME.fullmatch(name) or not value or name in values:
            raise CatalogError(f'invalid or duplicate slot assignment: {argument!r}')
        values[name] = value
    return values


def render_template(record, values, *, skill_path=None):
    expected = {slot['name'] for slot in record['slots']}
    supplied = set(values)
    if expected != supplied:
        raise CatalogError(
            f'slot mismatch; missing={sorted(expected-supplied)}, extra={sorted(supplied-expected)}'
        )
    if any(not isinstance(value, str) or not value.strip() for value in values.values()):
        raise CatalogError('all slot values must be nonempty user-supplied strings')
    rendered = PLACEHOLDER.sub(lambda match: values[match.group(1)].strip(), record['rewrite_template'])
    supplied_text = json.dumps(list(values.values()), ensure_ascii=False).casefold()
    for token in record['source_specific_tokens']:
        if token.casefold() in rendered.casefold() and token.casefold() not in supplied_text:
            raise CatalogError(f'source-specific token appeared without explicit user input: {token!r}')
    current = apply_live_controls([record], skill_path)[0]
    require_renderable(current)
    return rendered


def _markdown(result):
    lines = ['# CCR 2025-2026 source-linked Results logic', '',
             f'Matched: {result["matched_count"]}', '', result['boundary'], '']
    for record in result['records']:
        source = record['source']
        lines.extend([
            f'## {record["id"]}', '',
            f'- Article: PMID {record["pmid"]}; {record["title"]}',
            *control_markdown(record),
            f'- Source: body Results, physical PDF page(s) '
            f'{", ".join(map(str, source["physical_pages"]))}; '
            f'{source["subheading"]}',
            f'- Source sentence: {source["source_sentence"]}',
            f'- Verification: {source["verification_level"]}; text extraction '
            f'{source["text_extraction_match"]}.',
            f'- Logic: {record["result_polarity"]}; {record["inferential_status"]}; '
            f'{record["result_type"]}; {record["rhetorical_function"]}; '
            f'{record["logic_position"]}',
            f'- Use when: {record["use_when_zh"]}',
            f'- Do not use when: {record["do_not_use_when_zh"]}',
            f'- Rewrite template: {record["rewrite_template"]}',
            f'- Boundary: {record["evidence_boundary"]}', '',
        ])
    return '\n'.join(lines).rstrip() + '\n'


def main(argv=None):
    _configure_cli_streams()
    parser = argparse.ArgumentParser(
        description='Retrieve source-verified CCR 2025-2026 Results logic and templates.'
    )
    parser.add_argument('--skill-path', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--catalog-path', type=Path)
    parser.add_argument('--paper-logic', action='store_true')
    parser.add_argument('--pmid', default='')
    parser.add_argument('--template-id', default='')
    parser.add_argument('--year', default='')
    parser.add_argument('--domain', default='')
    parser.add_argument('--result-polarity', '--polarity', dest='polarity', default='')
    parser.add_argument('--inferential-status', '--significance', dest='inferential_status', default='')
    parser.add_argument('--result-type', default='')
    parser.add_argument('--evidence-layer', default='')
    parser.add_argument('--rhetorical-function', default='')
    parser.add_argument('--logic-position', default='')
    parser.add_argument('--section', default='')
    parser.add_argument('--query', default='')
    parser.add_argument('--limit', type=int, default=10)
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--accepted-only', action='store_true',
                        help='Return only live passed/usable records; default retrieval is an audit view.')
    parser.add_argument('--render', action='store_true')
    parser.add_argument('--slot', action='append', default=[], metavar='NAME=VALUE')
    arguments = parser.parse_args(argv)
    try:
        catalog = load_catalog(arguments.skill_path, arguments.catalog_path)
        if arguments.paper_logic:
            sentence_only = {
                '--template-id': arguments.template_id,
                '--inferential-status': arguments.inferential_status,
                '--result-type': arguments.result_type,
                '--evidence-layer': arguments.evidence_layer,
                '--rhetorical-function': arguments.rhetorical_function,
                '--logic-position': arguments.logic_position,
                '--section': arguments.section,
            }
            rejected = [name for name, value in sentence_only.items() if value]
            if arguments.render or arguments.slot:
                rejected.append('--render/--slot')
            if rejected:
                raise CatalogError(
                    '--paper-logic cannot be combined with sentence-only options: '
                    + ', '.join(rejected)
                )
            result = search_papers(
                catalog['papers'], pmid=arguments.pmid, year=arguments.year,
                domain=arguments.domain, polarity=arguments.polarity,
                query=arguments.query, limit=arguments.limit,
                accepted_only=arguments.accepted_only, skill_path=arguments.skill_path,
                sentence_records=catalog['records'],
            )
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return
        result = search(
            catalog['records'], pmid=arguments.pmid, template_id=arguments.template_id,
            year=arguments.year, domain=arguments.domain, polarity=arguments.polarity,
            inferential_status=arguments.inferential_status,
            result_type=arguments.result_type, evidence_layer=arguments.evidence_layer,
            rhetorical_function=arguments.rhetorical_function,
            logic_position=arguments.logic_position, section=arguments.section,
            query=arguments.query, limit=arguments.limit,
            accepted_only=arguments.accepted_only and not arguments.render,
            skill_path=arguments.skill_path,
        )
        if arguments.render:
            if not arguments.template_id or result['matched_count'] != 1:
                raise CatalogError('--render requires one exact --template-id match')
            record = result['records'][0]
            rendered = render_template(record, parse_slot_arguments(arguments.slot),
                                       skill_path=arguments.skill_path)
            output = {
                'template_id': record['id'],
                'rendered_text': rendered,
                **control_metadata(record),
                'language_pattern_provenance': {
                    'pmid': record['pmid'], 'doi': record['doi'],
                    'physical_page': record['source']['physical_page'],
                    'physical_pages': record['source']['physical_pages'],
                },
                'boundary': (
                    'The article supplies language-pattern provenance only; every '
                    'rendered value came from an explicit user slot.'
                ),
            }
            print(json.dumps(output, ensure_ascii=False, indent=2) if arguments.json
                  else rendered + '\n\n' + '\n'.join(control_markdown(record))
                  + '\n\n' + output['boundary'])
        else:
            if arguments.slot:
                raise CatalogError('--slot requires --render')
            print(json.dumps(result, ensure_ascii=False, indent=2) if arguments.json
                  else _markdown(result), end='')
    except (CatalogError, OSError, json.JSONDecodeError) as error:
        parser.exit(1, f'CCR Results-logic retrieval failed: {error}\n')


if __name__ == '__main__':
    main()
