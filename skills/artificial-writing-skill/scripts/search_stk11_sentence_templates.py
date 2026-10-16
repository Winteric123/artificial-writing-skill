import argparse
import csv
import json
import re
import shlex
import sys
from pathlib import Path


sys.dont_write_bytecode = True


CATALOG_NAME = 'stk11-ccr-sentence-templates.json'
SCHEMA_VERSION = 1

RESULT_TYPES = {
    'adjusted_prognostic_association',
    'coalteration_enrichment',
    'cross_omics_concordance',
    'assay_concordance',
    'exploratory_subgroup_signal',
    'frequency',
    'group_comparison',
    'mechanistic_readout',
    'model_performance',
    'null_or_inconclusive',
    'observational_treatment_association',
    'cohort_assembly',
    'sequencing_and_processing',
    'signature_construction',
    'immune_deconvolution',
    'cell_state_annotation',
    'pathway_enrichment',
    'genomic_landscape',
    'validation_design',
    'functional_perturbation',
    'spatial_heterogeneity',
}
NONCLINICAL_RESULT_TYPES = {
    'assay_concordance', 'cell_state_annotation', 'coalteration_enrichment',
    'cross_omics_concordance', 'frequency', 'functional_perturbation',
    'genomic_landscape', 'group_comparison', 'immune_deconvolution',
    'mechanistic_readout', 'model_performance', 'pathway_enrichment',
    'signature_construction', 'spatial_heterogeneity',
}
SIGNIFICANCE_STATUSES = {
    'mixed',
    'not_applicable',
    'nonsignificant',
    'significant',
    'undetermined',
}
SECTIONS = {
    'abstract-background',
    'abstract-conclusion',
    'abstract-methods',
    'abstract-results',
    'conclusion',
    'discussion',
    'figure-caption',
    'introduction',
    'methods',
    'results',
    'table',
    'translational-relevance',
}
TIERS = {'core_highlight', 'topic_support'}
EVIDENCE_LAYERS = {
    'clinical',
    'genomic',
    'integrated',
    'preclinical',
    'protein',
    'single_cell',
    'transcriptomic',
}
STK11_RELATIONS = {
    'contextual_analysis',
    'direct_analysis',
    'direct_function',
    'structural_analogue',
}
VERIFICATION_LEVELS = {
    'normalized_pdf_text_match',
    'visually_verified_exact',
}
CLAIM_CEILINGS = {
    'association_only',
    'descriptive_only',
    'exploratory_hypothesis',
    'mechanistic_model_only',
    'model_performance_only',
}

TEMPLATE_ID = re.compile(r'^stk11-ccr-sent-[a-z0-9]+(?:-[a-z0-9]+)*$')
PMID = re.compile(r'^\d{8}$')
SHA256 = re.compile(r'^[0-9a-f]{64}$')
SLOT_NAME = re.compile(r'^[a-z][a-z0-9_]*$')
PLACEHOLDER = re.compile(r'\[([a-z][a-z0-9_]*)\]')
MARKDOWN_ANCHOR = re.compile(r'^[A-Za-z0-9][A-Za-z0-9._:-]*$')


class CatalogError(ValueError):
    pass


def _require_string(value, label):
    if not isinstance(value, str) or not value.strip():
        raise CatalogError(f'{label} must be a nonempty string')


def _require_string_list(value, label, *, nonempty=True):
    if not isinstance(value, list) or (nonempty and not value):
        raise CatalogError(f'{label} must be a nonempty list')
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise CatalogError(f'{label} contains an empty or non-string value')
    if len(value) != len(set(value)):
        raise CatalogError(f'{label} contains duplicate values')


def _validate_project_scope(scope):
    if not isinstance(scope, dict):
        raise CatalogError('project_scope must be an object')
    required = {
        'membership_source', 'journal_id', 'legacy_origin_tiers', 'expected_pmids',
        'coverage_unit', 'coverage_complete', 'coverage_statement',
    }
    missing = required - set(scope)
    if missing:
        raise CatalogError(f'project_scope is missing fields: {sorted(missing)}')
    _require_string(scope['membership_source'], 'project_scope.membership_source')
    if scope['journal_id'] != 'ccr':
        raise CatalogError('project_scope.journal_id must be ccr for this catalog')
    _require_string_list(scope['legacy_origin_tiers'], 'project_scope.legacy_origin_tiers')
    if set(scope['legacy_origin_tiers']) != TIERS:
        raise CatalogError('project_scope.legacy_origin_tiers must contain core_highlight and topic_support')
    _require_string_list(scope['expected_pmids'], 'project_scope.expected_pmids')
    if any(not PMID.fullmatch(value) for value in scope['expected_pmids']):
        raise CatalogError('project_scope.expected_pmids contains an invalid PMID')
    if scope['coverage_unit'] != 'at_least_one_template_per_expected_paper':
        raise CatalogError('project_scope.coverage_unit is unsupported')
    if not isinstance(scope['coverage_complete'], bool):
        raise CatalogError('project_scope.coverage_complete must be boolean')
    _require_string(scope['coverage_statement'], 'project_scope.coverage_statement')
    fulltext = scope.get('fulltext_coverage')
    if fulltext is not None:
        if not isinstance(fulltext, dict) or set(fulltext) != {
            'unit', 'methods_minimum', 'results_minimum', 'coverage_complete', 'audit_resource'
        }:
            raise CatalogError('project_scope.fulltext_coverage fields are invalid')
        if fulltext['unit'] != 'body_methods_and_nonclinical_results_per_paper':
            raise CatalogError('project_scope.fulltext_coverage.unit is unsupported')
        for field in ('methods_minimum', 'results_minimum'):
            if type(fulltext[field]) is not int or not 1 <= fulltext[field] <= 10:
                raise CatalogError(f'fulltext_coverage.{field} must be between 1 and 10')
        if not isinstance(fulltext['coverage_complete'], bool):
            raise CatalogError('fulltext_coverage.coverage_complete must be boolean')
        if fulltext['audit_resource'] != 'stk11-ccr-fulltext-sentence-audit.md':
            raise CatalogError('fulltext_coverage.audit_resource is unsupported')


def _validate_source(record_id, source):
    if not isinstance(source, dict):
        raise CatalogError(f'{record_id}: source must be an object')
    required = {
        'pdf_sha256', 'supplied_pdf_version', 'physical_page', 'section',
        'source_sentence', 'verification_level', 'quotation_verified',
        'verification_record',
    }
    missing = required - set(source)
    if missing:
        raise CatalogError(f'{record_id}: source is missing fields: {sorted(missing)}')
    if not isinstance(source['pdf_sha256'], str) or not SHA256.fullmatch(source['pdf_sha256']):
        raise CatalogError(f'{record_id}: source.pdf_sha256 must be a lowercase SHA-256')
    _require_string(source['supplied_pdf_version'], f'{record_id}: source.supplied_pdf_version')
    if not isinstance(source['physical_page'], int) or source['physical_page'] < 1:
        raise CatalogError(f'{record_id}: source.physical_page must be a positive integer')
    if source['section'] not in SECTIONS:
        raise CatalogError(f'{record_id}: unknown source.section {source["section"]!r}')
    _require_string(source['source_sentence'], f'{record_id}: source.source_sentence')
    if PLACEHOLDER.search(source['source_sentence']):
        raise CatalogError(f'{record_id}: source sentence must not contain template slots')
    if source['verification_level'] not in VERIFICATION_LEVELS:
        raise CatalogError(f'{record_id}: unknown verification_level')
    if not isinstance(source['quotation_verified'], bool):
        raise CatalogError(f'{record_id}: quotation_verified must be boolean')
    if source['quotation_verified'] and source['verification_level'] != 'visually_verified_exact':
        raise CatalogError(
            f'{record_id}: quotation_verified requires visually_verified_exact'
        )
    _require_string(source['verification_record'], f'{record_id}: source.verification_record')
    verification_record = source['verification_record'].strip()
    if (re.search(r'(?<![A-Za-z0-9])[A-Za-z]:[\\/]', verification_record)
            or verification_record.startswith(('/', '\\\\'))):
        raise CatalogError(
            f'{record_id}: source.verification_record must not contain an absolute path'
        )


def _validate_record(record, expected_pmids, valid_usage_card_ids=None):
    if not isinstance(record, dict):
        raise CatalogError('each record must be an object')
    required = {
        'id', 'pmid', 'doi', 'title', 'journal', 'journal_id', 'year',
        'legacy_origin_tier', 'stk11_relation', 'source', 'result_type',
        'significance_status', 'evidence_layer', 'rhetorical_function',
        'target_sections', 'use_when_zh', 'do_not_use_when_zh',
        'rewrite_template', 'slots', 'source_specific_tokens',
        'usage_card_ids', 'claim_ceiling', 'evidence_boundary',
        'transfer_notes',
    }
    missing = required - set(record)
    if missing:
        raise CatalogError(f'record is missing fields: {sorted(missing)}')

    record_id = record['id']
    if not isinstance(record_id, str) or not TEMPLATE_ID.fullmatch(record_id):
        raise CatalogError(f'invalid template id: {record_id!r}')
    if not isinstance(record['pmid'], str) or not PMID.fullmatch(record['pmid']):
        raise CatalogError(f'{record_id}: invalid PMID')
    if record['pmid'] not in expected_pmids:
        raise CatalogError(f'{record_id}: PMID is outside project_scope.expected_pmids')
    for field in ('doi', 'title', 'journal', 'rhetorical_function', 'use_when_zh',
                  'do_not_use_when_zh', 'evidence_boundary', 'transfer_notes'):
        _require_string(record[field], f'{record_id}: {field}')
    if record['journal_id'] != 'ccr':
        raise CatalogError(f'{record_id}: journal_id must be ccr')
    if not isinstance(record['year'], str) or not re.fullmatch(r'\d{4}', record['year']):
        raise CatalogError(f'{record_id}: year must be a four-digit string')
    if record['legacy_origin_tier'] not in TIERS:
        raise CatalogError(f'{record_id}: unknown legacy_origin_tier')
    if record['stk11_relation'] not in STK11_RELATIONS:
        raise CatalogError(f'{record_id}: unknown stk11_relation')
    if record['result_type'] not in RESULT_TYPES:
        raise CatalogError(f'{record_id}: unknown result_type')
    if record['significance_status'] not in SIGNIFICANCE_STATUSES:
        raise CatalogError(f'{record_id}: unknown significance_status')
    if record['evidence_layer'] not in EVIDENCE_LAYERS:
        raise CatalogError(f'{record_id}: unknown evidence_layer')
    if record['claim_ceiling'] not in CLAIM_CEILINGS:
        raise CatalogError(f'{record_id}: unknown claim_ceiling')

    _validate_source(record_id, record['source'])
    if (record['source']['section'] == 'methods'
            and record['significance_status'] != 'not_applicable'):
        raise CatalogError(f'{record_id}: Methods description requires not_applicable significance')
    _require_string_list(record['target_sections'], f'{record_id}: target_sections')
    if not set(record['target_sections']).issubset(SECTIONS):
        raise CatalogError(f'{record_id}: target_sections contains an unknown section')
    _require_string(record['rewrite_template'], f'{record_id}: rewrite_template')
    placeholder_free_template = PLACEHOLDER.sub('', record['rewrite_template'])
    if '[' in placeholder_free_template or ']' in placeholder_free_template:
        raise CatalogError(
            f'{record_id}: rewrite_template contains malformed or unsupported slot syntax'
        )

    if not isinstance(record['slots'], list) or not record['slots']:
        raise CatalogError(f'{record_id}: slots must be a nonempty list')
    slot_names = []
    for slot in record['slots']:
        if not isinstance(slot, dict):
            raise CatalogError(f'{record_id}: every slot must be an object')
        if set(slot) != {'name', 'description', 'required', 'evidence_source'}:
            raise CatalogError(f'{record_id}: slot fields are invalid')
        if not isinstance(slot['name'], str) or not SLOT_NAME.fullmatch(slot['name']):
            raise CatalogError(f'{record_id}: invalid slot name')
        _require_string(slot['description'], f'{record_id}: slot description')
        if slot['required'] is not True:
            raise CatalogError(f'{record_id}: every rendered slot must be required')
        if slot['evidence_source'] != 'user_supplied':
            raise CatalogError(f'{record_id}: slot evidence_source must be user_supplied')
        slot_names.append(slot['name'])
    if len(slot_names) != len(set(slot_names)):
        raise CatalogError(f'{record_id}: duplicate slot names')
    placeholders = set(PLACEHOLDER.findall(record['rewrite_template']))
    if placeholders != set(slot_names):
        raise CatalogError(
            f'{record_id}: template placeholders and declared slots differ '
            f'(template={sorted(placeholders)}, slots={sorted(slot_names)})'
        )

    _require_string_list(record['source_specific_tokens'], f'{record_id}: source_specific_tokens')
    source_text = record['source']['source_sentence'].casefold()
    literal_template = placeholder_free_template.casefold()
    for token in record['source_specific_tokens']:
        if token.casefold() not in source_text:
            raise CatalogError(f'{record_id}: protected source token is absent from source_sentence')
        if token.casefold() in literal_template:
            raise CatalogError(
                f'{record_id}: source-specific token leaked into rewrite_template: {token!r}'
            )

    _require_string_list(record['usage_card_ids'], f'{record_id}: usage_card_ids', nonempty=False)
    if valid_usage_card_ids is not None:
        unknown = set(record['usage_card_ids']) - valid_usage_card_ids
        if unknown:
            raise CatalogError(f'{record_id}: unknown usage_card_ids: {sorted(unknown)}')


def validate_catalog(payload, valid_usage_card_ids=None):
    if not isinstance(payload, dict):
        raise CatalogError('catalog must be a JSON object')
    required = {'schema_version', 'updated', 'scope', 'project_scope', 'records'}
    missing = required - set(payload)
    if missing:
        raise CatalogError(f'catalog is missing fields: {sorted(missing)}')
    if payload['schema_version'] != SCHEMA_VERSION:
        raise CatalogError(f'unsupported schema_version: {payload["schema_version"]!r}')
    if not isinstance(payload['updated'], str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', payload['updated']):
        raise CatalogError('updated must use YYYY-MM-DD')
    _require_string(payload['scope'], 'scope')
    _validate_project_scope(payload['project_scope'])
    if not isinstance(payload['records'], list):
        raise CatalogError('records must be a list')

    expected_pmids = set(payload['project_scope']['expected_pmids'])
    seen_ids = set()
    for record in payload['records']:
        _validate_record(record, expected_pmids, valid_usage_card_ids)
        if record['id'] in seen_ids:
            raise CatalogError(f'duplicate template id: {record["id"]}')
        seen_ids.add(record['id'])
    represented = {record['pmid'] for record in payload['records']}
    if payload['project_scope']['coverage_complete'] and represented != expected_pmids:
        missing_pmids = sorted(expected_pmids - represented)
        extra_pmids = sorted(represented - expected_pmids)
        raise CatalogError(
            f'coverage_complete does not match expected_pmids; '
            f'missing={missing_pmids}, extra={extra_pmids}'
        )
    fulltext = payload['project_scope'].get('fulltext_coverage')
    if fulltext and fulltext['coverage_complete']:
        for pmid in expected_pmids:
            methods, results = set(), set()
            for record in payload['records']:
                source = record['source']
                if record['pmid'] != pmid or source['section'] not in {'methods', 'results'}:
                    continue
                expected_reference = f'{fulltext["audit_resource"]}#pmid-{pmid}'
                if (source['verification_record'] != expected_reference
                        or source['verification_level'] != 'visually_verified_exact'
                        or source['quotation_verified'] is not True):
                    raise CatalogError(
                        f'{record["id"]}: fulltext_coverage requires a visually verified '
                        'source sentence linked to its declared per-paper full-text audit'
                    )
                identity = (source['pdf_sha256'], source['physical_page'],
                            re.sub(r'\s+', ' ', source['source_sentence']).strip().casefold())
                if source['section'] == 'methods' and 'methods' in record['target_sections']:
                    methods.add(identity)
                if (source['section'] == 'results' and 'results' in record['target_sections']
                        and record['evidence_layer'] != 'clinical'
                        and record['result_type'] in NONCLINICAL_RESULT_TYPES):
                    results.add(identity)
            if (len(methods) < fulltext['methods_minimum']
                    or len(results) < fulltext['results_minimum']):
                raise CatalogError(
                    f'fulltext_coverage is incomplete for PMID {pmid}: '
                    f'Methods={len(methods)}, nonclinical Results={len(results)}'
                )
    return payload


def _usage_card_ids(skill):
    identifiers = set()
    for name in ('language-usage-cards.json', 'language-usage-cards-rechecks.json'):
        path = skill / 'references' / name
        if not path.is_file():
            continue
        payload = json.loads(path.read_text(encoding='utf-8-sig'))
        identifiers.update(card['id'] for card in payload.get('cards', []))
    return identifiers


def _read_csv_by_pmid(path):
    if not path.is_file():
        raise CatalogError(f'installed authority is missing: {path.name}')
    with path.open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    if not rows or 'pmid' not in rows[0]:
        raise CatalogError(f'installed authority has no PMID rows: {path.name}')
    indexed = {}
    for row in rows:
        pmid = row.get('pmid', '').strip()
        if not pmid:
            continue
        if pmid in indexed:
            raise CatalogError(f'duplicate PMID in {path.name}: {pmid}')
        indexed[pmid] = row
    return indexed


def _normalized_text(value):
    return re.sub(r'\s+', ' ', value.strip())


def _validate_installed_verification_reference(references, record):
    verification_record = record['source']['verification_record'].strip()
    relative_path, separator, anchor = verification_record.partition('#')
    if not relative_path.casefold().endswith('.md'):
        return
    if not separator or not anchor or not MARKDOWN_ANCHOR.fullmatch(anchor):
        raise CatalogError(
            f'{record["id"]}: Markdown verification_record requires a nonempty, '
            'well-formed anchor'
        )

    relative = Path(relative_path)
    if relative.is_absolute():
        raise CatalogError(
            f'{record["id"]}: Markdown verification_record must be relative to references'
        )
    references = references.resolve()
    target = (references / relative).resolve()
    try:
        target.relative_to(references)
    except ValueError as error:
        raise CatalogError(
            f'{record["id"]}: Markdown verification_record escapes references'
        ) from error
    if not target.is_file():
        raise CatalogError(
            f'{record["id"]}: Markdown verification_record target is missing: '
            f'{relative_path}'
        )
    document = target.read_text(encoding='utf-8-sig')
    headings = re.findall(r'(?m)^#{1,6}\s+(.+?)\s*#*$', document)
    anchors = {re.sub(r'[^\w-]', '', heading.casefold().replace(' ', '-'))
               for heading in headings}
    anchors.update(re.findall(r'<a\s+(?:id|name)=[\"\x27]([^\"\x27]+)', document))
    if anchor not in anchors:
        raise CatalogError(f'{record["id"]}: Markdown verification_record anchor is missing: {anchor}')


def validate_installed_catalog(skill, payload):
    """Cross-check sentence records against installed, relative-path authorities."""
    skill = Path(skill)
    references = skill / 'references'
    library = _read_csv_by_pmid(references / 'library-index.csv')
    versions = _read_csv_by_pmid(references / 'source-version-register.csv')

    membership_path = references / 'stk11-writing-reference-map.json'
    if not membership_path.is_file():
        raise CatalogError(f'installed authority is missing: {membership_path.name}')
    membership_payload = json.loads(membership_path.read_text(encoding='utf-8-sig'))

    membership = {}
    for row in membership_payload.get('records', []):
        pmid = row.get('pmid', '')
        if pmid in membership:
            raise CatalogError(f'duplicate PMID in stk11-writing-reference-map.json: {pmid}')
        membership[pmid] = row
    derived_ccr_pmids = {
        pmid for pmid in membership
        if pmid in library and library[pmid].get('journal', '').strip() == 'Clinical Cancer Research'
    }
    expected_pmids = set(payload['project_scope']['expected_pmids'])
    represented_pmids = {record['pmid'] for record in payload['records']}
    if payload['project_scope']['membership_source'] != 'stk11-writing-reference-map.json':
        raise CatalogError('project_scope.membership_source must name stk11-writing-reference-map.json')
    if not payload['project_scope']['coverage_complete']:
        raise CatalogError('installed catalog must declare coverage_complete=true')
    if expected_pmids != derived_ccr_pmids:
        raise CatalogError(
            'installed expected_pmids do not equal the CCR subset of the STK11 membership map; '
            f'missing={sorted(derived_ccr_pmids - expected_pmids)}, '
            f'extra={sorted(expected_pmids - derived_ccr_pmids)}'
        )
    if represented_pmids != expected_pmids:
        raise CatalogError(
            'installed records do not provide at least one template for every expected PMID; '
            f'missing={sorted(expected_pmids - represented_pmids)}, '
            f'extra={sorted(represented_pmids - expected_pmids)}'
        )

    for record in payload['records']:
        record_id = record['id']
        pmid = record['pmid']
        _validate_installed_verification_reference(references, record)
        if pmid not in library or pmid not in membership or pmid not in versions:
            missing = [
                label for label, authority in (
                    ('library-index.csv', library),
                    ('stk11-writing-reference-map.json', membership),
                    ('source-version-register.csv', versions),
                ) if pmid not in authority
            ]
            raise CatalogError(f'{record_id}: PMID is missing from {", ".join(missing)}')

        article = library[pmid]
        member = membership[pmid]
        version = versions[pmid]
        comparisons = (
            ('doi', record['doi'].casefold(), article.get('doi', '').strip().casefold()),
            ('title', _normalized_text(record['title']), _normalized_text(article.get('title', ''))),
            ('journal', _normalized_text(record['journal']), _normalized_text(article.get('journal', ''))),
            ('year', record['year'], article.get('year', '').strip()),
            ('legacy_origin_tier', record['legacy_origin_tier'], member.get('tier', '')),
            ('stk11_relation', record['stk11_relation'], member.get('stk11_relation', '')),
            ('pdf_sha256', record['source']['pdf_sha256'], version.get('sha256', '').strip()),
            ('supplied_pdf_version', record['source']['supplied_pdf_version'], version.get('supplied_pdf_version', '').strip()),
        )
        for field, actual, authoritative in comparisons:
            if actual != authoritative:
                raise CatalogError(
                    f'{record_id}: {field} disagrees with installed authority '
                    f'(record={actual!r}, authority={authoritative!r})'
                )
        try:
            physical_pages = int(version.get('physical_pages', ''))
        except (TypeError, ValueError) as error:
            raise CatalogError(
                f'{record_id}: source-version-register.csv has invalid physical_pages'
            ) from error
        if physical_pages < 1:
            raise CatalogError(
                f'{record_id}: source-version-register.csv has invalid physical_pages'
            )
        if record['source']['physical_page'] > physical_pages:
            raise CatalogError(
                f'{record_id}: physical_page exceeds registered PDF page count '
                f'({record["source"]["physical_page"]}>{physical_pages})'
            )
    return payload


def load_catalog(skill, catalog_path=None):
    skill = Path(skill)
    path = Path(catalog_path) if catalog_path else skill / 'references' / CATALOG_NAME
    if not path.is_file():
        raise CatalogError(
            f'sentence-template catalog not found: {path}; '
            'integrate source-verified records before retrieval'
        )
    payload = json.loads(path.read_text(encoding='utf-8-sig'))
    validate_catalog(payload, _usage_card_ids(skill))
    return validate_installed_catalog(skill, payload)


def _query_terms(query):
    if not query.strip():
        return []
    try:
        terms = shlex.split(query)
    except ValueError as error:
        raise CatalogError(f'invalid query quoting: {error}') from error
    return [re.sub(r'\s+', ' ', term).strip().casefold() for term in terms if term.strip()]


def _searchable_text(record):
    fields = [
        record['id'], record['pmid'], record['doi'], record['title'],
        record['journal'], record['legacy_origin_tier'], record['stk11_relation'],
        record['result_type'], record['significance_status'],
        record['evidence_layer'], record['rhetorical_function'],
        record['use_when_zh'], record['do_not_use_when_zh'],
        record['rewrite_template'], record['claim_ceiling'],
        record['evidence_boundary'], record['transfer_notes'],
        record['source']['source_sentence'], record['source']['section'],
        *record['target_sections'], *record['usage_card_ids'],
    ]
    return re.sub(r'\s+', ' ', json.dumps(fields, ensure_ascii=False)).casefold()


def search(records, *, pmid='', template_id='', result_type='', significance='',
           section='', legacy_origin='all', evidence_layer='', query='', limit=10,
           source_section=''):
    if not isinstance(limit, int) or not 1 <= limit <= 100:
        raise CatalogError('limit must be between 1 and 100')
    if pmid and not PMID.fullmatch(pmid):
        raise CatalogError('pmid must be eight digits')
    if template_id and not TEMPLATE_ID.fullmatch(template_id):
        raise CatalogError('template_id is not a valid stable template ID')
    if result_type and result_type not in RESULT_TYPES:
        raise CatalogError(f'unknown result_type: {result_type}')
    if significance and significance not in SIGNIFICANCE_STATUSES:
        raise CatalogError(f'unknown significance: {significance}')
    if section and section not in SECTIONS:
        raise CatalogError(f'unknown section: {section}')
    if source_section and source_section not in SECTIONS:
        raise CatalogError(f'unknown source_section: {source_section}')
    if legacy_origin not in {'all', *TIERS}:
        raise CatalogError(f'unknown legacy_origin: {legacy_origin}')
    if evidence_layer and evidence_layer not in EVIDENCE_LAYERS:
        raise CatalogError(f'unknown evidence_layer: {evidence_layer}')

    terms = _query_terms(query)
    matches = []
    for record in records:
        if pmid and record['pmid'] != pmid:
            continue
        if template_id and record['id'] != template_id:
            continue
        if result_type and record['result_type'] != result_type:
            continue
        if significance and record['significance_status'] != significance:
            continue
        if section and section not in record['target_sections']:
            continue
        if source_section and source_section != record['source']['section']:
            continue
        if legacy_origin != 'all' and record['legacy_origin_tier'] != legacy_origin:
            continue
        if evidence_layer and record['evidence_layer'] != evidence_layer:
            continue
        searchable = _searchable_text(record)
        if any(term not in searchable for term in terms):
            continue
        matches.append(record)

    matches.sort(key=lambda record: (record['year'], record['pmid'], record['id']))
    return {
        'matched_count': len(matches),
        'records': matches[:limit],
        'boundary': (
            'Source sentences document a writing pattern. Rewrite templates may be '
            'filled only with user-supplied evidence; source-paper genes, treatments, '
            'endpoints, numbers, and claims are never defaults for a new result.'
        ),
    }


def parse_slot_arguments(arguments):
    values = {}
    for argument in arguments:
        if '=' not in argument:
            raise CatalogError(f'slot must use NAME=VALUE: {argument!r}')
        name, value = argument.split('=', 1)
        name, value = name.strip(), value.strip()
        if not SLOT_NAME.fullmatch(name) or not value:
            raise CatalogError(f'invalid slot assignment: {argument!r}')
        if name in values:
            raise CatalogError(f'duplicate slot assignment: {name}')
        values[name] = value
    return values


def render_template(record, slot_values):
    if not isinstance(slot_values, dict):
        raise CatalogError('slot_values must be an object')
    expected = {slot['name'] for slot in record['slots']}
    supplied = set(slot_values)
    missing = expected - supplied
    extra = supplied - expected
    if missing or extra:
        raise CatalogError(
            f'slot mismatch; missing={sorted(missing)}, extra={sorted(extra)}'
        )
    for name, value in slot_values.items():
        if not isinstance(value, str) or not value.strip():
            raise CatalogError(f'slot {name} must have a nonempty user-supplied value')
    rendered = PLACEHOLDER.sub(lambda match: slot_values[match.group(1)].strip(),
                               record['rewrite_template'])
    if PLACEHOLDER.search(rendered):
        raise CatalogError('rendered text contains unresolved template slots')

    supplied_text = json.dumps(list(slot_values.values()), ensure_ascii=False).casefold()
    for token in record['source_specific_tokens']:
        if token.casefold() in rendered.casefold() and token.casefold() not in supplied_text:
            raise CatalogError(
                f'source-specific token appeared without explicit user input: {token!r}'
            )
    return rendered


def _markdown(result):
    lines = [
        '# STK11/CCR source-linked sentence templates', '',
        f'Matched: {result["matched_count"]}', '',
        result['boundary'], '',
    ]
    for record in result['records']:
        source = record['source']
        lines.extend([
            f'## {record["id"]}', '',
            f'- Article: PMID {record["pmid"]}; {record["title"]}',
            f'- Legacy origin tier: {record["legacy_origin_tier"]}',
            f'- Source: {source["section"]}, physical PDF page {source["physical_page"]}; '
            f'{source["verification_level"]}',
            f'- Source sentence: {source["source_sentence"]}',
            f'- Content/result type: {record["result_type"]}; significance: '
            f'{record["significance_status"]}; evidence: {record["evidence_layer"]}',
            f'- Use when: {record["use_when_zh"]}',
            f'- Do not use when: {record["do_not_use_when_zh"]}',
            f'- Rewrite template: {record["rewrite_template"]}',
            f'- Boundary: {record["evidence_boundary"]}', '',
        ])
    return '\n'.join(lines).rstrip() + '\n'


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=(
            'Retrieve source-verified STK11/CCR sentence patterns and render a '
            'selected template using explicit user-supplied slot values.'
        )
    )
    parser.add_argument('--skill-path', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--catalog-path', type=Path)
    parser.add_argument('--pmid', default='')
    parser.add_argument('--template-id', default='')
    parser.add_argument('--result-type', '--content-type', dest='result_type', default='',
                        help='Result or Methods content type; both option names are supported.')
    parser.add_argument('--significance', default='')
    parser.add_argument('--section', default='')
    parser.add_argument('--source-section', default='',
                        help='Section containing the actual source sentence, independent of target section.')
    parser.add_argument(
        '--legacy-origin', '--tier', dest='legacy_origin', default='all',
        help='Historical admission origin; --tier is a compatibility alias.',
    )
    parser.add_argument('--evidence-layer', default='')
    parser.add_argument('--query', default='')
    parser.add_argument('--limit', type=int, default=10)
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--render', action='store_true')
    parser.add_argument('--slot', action='append', default=[], metavar='NAME=VALUE')
    args = parser.parse_args(argv)

    try:
        payload = load_catalog(args.skill_path, args.catalog_path)
        result = search(
            payload['records'], pmid=args.pmid, template_id=args.template_id,
            result_type=args.result_type, significance=args.significance,
            section=args.section, legacy_origin=args.legacy_origin, evidence_layer=args.evidence_layer,
            query=args.query, limit=args.limit,
            source_section=args.source_section,
        )
        if args.render:
            if not args.template_id:
                raise CatalogError('--render requires --template-id')
            if result['matched_count'] != 1:
                raise CatalogError('--render requires exactly one matching template')
            record = result['records'][0]
            rendered = render_template(record, parse_slot_arguments(args.slot))
            output = {
                'template_id': record['id'],
                'rendered_text': rendered,
                'language_pattern_provenance': {
                    'pmid': record['pmid'],
                    'doi': record['doi'],
                    'physical_page': record['source']['physical_page'],
                },
                'boundary': (
                    'The cited article is provenance for the language pattern only. '
                    'It does not support the new study result; every rendered value '
                    'came from an explicit --slot argument.'
                ),
            }
            print(json.dumps(output, ensure_ascii=False, indent=2) if args.json
                  else rendered + '\n\n' + output['boundary'])
        else:
            if args.slot:
                raise CatalogError('--slot requires --render')
            print(json.dumps(result, ensure_ascii=False, indent=2) if args.json
                  else _markdown(result), end='')
    except (CatalogError, OSError, json.JSONDecodeError) as error:
        parser.exit(1, f'Sentence-template retrieval failed: {error}\n')


if __name__ == '__main__':
    main()
