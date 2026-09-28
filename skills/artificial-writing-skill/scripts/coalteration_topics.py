from collections import Counter
import re

from library_common import file_hash, read_csv, read_json, reference_path


STATES = {'analyzed', 'context_only', 'not_identified', 'not_curated', 'excluded'}
TYPES = {'sequence_mutation', 'copy_number_loss', 'copy_number_gain', 'fusion_rearrangement',
         'same_gene_compound', 'engineered_combination', 'germline_somatic', 'origin_unresolved',
         'mixed_or_unspecified', 'between_sample_identity', 'different_compartments'}
USES = {'genomic_landscape', 'immune_context', 'prognosis', 'treatment_outcomes', 'resistance',
        'preclinical_mechanism', 'assay_or_method', 'variant_origin', 'background_or_eligibility', 'model_genotype'}
LABELS = {'analyzed': '实际分析/描述', 'context_only': '仅背景/模型/方法上下文',
          'not_identified': '本轮未识别', 'not_curated': '尚未标注', 'excluded': '排除/不适用'}
GENE_ALIASES = {'LKB1': 'STK11', 'BRG1': 'SMARCA4', 'HER2': 'ERBB2', 'NRF2': 'NFE2L2'}


def canonical_gene(value):
    value = value.strip().upper()
    return GENE_ALIASES.get(value, value)


def validate_record(record, identifier):
    for field in ('co_mutation_status', 'co_alteration_status'):
        if record.get(field) not in STATES:
            raise ValueError(f'Invalid co-alteration status: {identifier}/{field}')
    for field, allowed in (('alteration_types', TYPES), ('analysis_uses', USES)):
        values = record.get(field, [])
        if not isinstance(values, list) or len(values) != len(set(values)) or not set(values) <= allowed:
            raise ValueError(f'Invalid topic vocabulary: {identifier}/{field}')
    if record['co_mutation_status'] == 'analyzed':
        if record['co_alteration_status'] != 'analyzed' or 'sequence_mutation' not in record.get('alteration_types', []):
            raise ValueError(f'Sequence co-mutation requires analyzed co-alteration: {identifier}')
    if record.get('eligibility') == 'excluded' and any(record[field] != 'excluded' for field in ('co_mutation_status', 'co_alteration_status')):
        raise ValueError(f'Excluded source promoted by topic annotation: {identifier}')
    if not record.get('boundary') or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', record.get('curated_on', '')):
        raise ValueError(f'Missing topic boundary/date: {identifier}')
    contexts = record.get('gene_contexts', [])
    if not isinstance(contexts, list):
        raise ValueError(f'Invalid gene contexts: {identifier}')
    for context in contexts:
        if not isinstance(context, list) or not context or len(context) != len(set(context)) or any(not re.fullmatch(r'[A-Z][A-Z0-9-]*', gene) for gene in context):
            raise ValueError(f'Invalid gene context: {identifier}')


def load_annotations(skill, library_rows):
    data = read_json(reference_path(skill, 'coalteration-annotations.json'))
    if data.get('schema_version') != 1:
        raise ValueError('Unsupported co-alteration annotations schema')
    library = {row['pmid']: row for row in library_rows}
    if set(data['articles']) - set(library):
        raise ValueError('Co-alteration annotation PMID absent from registry')
    pdf_sources = read_json(reference_path(skill, 'source-pdf-locators.json'))['sources']
    cache = {}

    def check_evidence(record, identifier):
        if not record.get('evidence') and record.get('eligibility') != 'excluded':
            raise ValueError(f'Missing topic evidence: {identifier}')
        for evidence in record.get('evidence', []):
            relative = evidence['source']
            if relative not in cache:
                path = reference_path(skill, relative)
                cache[relative] = (file_hash(path), len(path.read_text(encoding='utf-8-sig').splitlines()))
            digest, line_count = cache[relative]
            if evidence['source_sha256'] != digest or not 1 <= evidence['first_line'] <= evidence['last_line'] <= line_count:
                raise ValueError(f'Stale co-alteration evidence: {identifier}/{relative}')

    for identifier, record in data['articles'].items():
        validate_record(record, identifier)
        row = library[identifier]
        if record['eligibility'] != row['eligibility'] or record['doi'].casefold() != row['doi'].casefold():
            raise ValueError(f'Stale co-alteration source identity: {identifier}')
        if row['eligibility'] == 'included' and 'excluded' in (record['co_mutation_status'], record['co_alteration_status']):
            raise ValueError(f'Included source has excluded topic state: {identifier}')
        check_evidence(record, identifier)
        if row['eligibility'] == 'included':
            pdf = record.get('pdf', {})
            expected = pdf_sources.get(identifier, {})
            if not expected or pdf.get('sha256') != expected.get('sha256') or pdf.get('physical_pages') != expected.get('physical_pages'):
                raise ValueError(f'Stale topic PDF identity: {identifier}')
            if any(not isinstance(page, int) or not 1 <= page <= pdf['physical_pages'] for page in pdf.get('checked_context_pages', [])):
                raise ValueError(f'Invalid topic PDF page: {identifier}')
    preprints = {row['source_id']: row for row in read_csv(reference_path(skill, 'preprint-source-register.csv'))}
    if set(data.get('preprints', {})) - set(preprints):
        raise ValueError('Unregistered preprint topic annotation')
    for identifier, record in data.get('preprints', {}).items():
        validate_record(record, identifier)
        source = preprints[identifier]
        if any(record[field] != source[field] for field in ('doi', 'version')) or record['source_sha256'] != source['sha256']:
            raise ValueError(f'Stale preprint topic identity: {identifier}')
        check_evidence(record, identifier)
    return data


def article_topics(row, data):
    return data['articles'].get(row['pmid'], dict(co_mutation_status='not_curated', co_alteration_status='not_curated',
        alteration_types=[], gene_contexts=[], analysis_uses=[], evidence=[], curated_on='',
        boundary='New source has no curated co-alteration annotation; do not infer absence or inherit another version.'))


def topic_columns(record):
    return dict(co_mutation_status=record['co_mutation_status'], co_alteration_status=record['co_alteration_status'],
                co_alteration_types=';'.join(record['alteration_types']),
                co_gene_contexts=';'.join('+'.join(context) for context in record['gene_contexts']),
                co_analysis_uses=';'.join(record['analysis_uses']), co_curated_on=record['curated_on'],
                co_topic_reference='coalteration-annotations.json', co_topic_boundary=record['boundary'])


def topic_matches(record, *, co_mutation='', co_alteration='', co_gene='', co_use='', co_type=''):
    if co_mutation and record.get('co_mutation_status') != co_mutation:
        return False
    if co_alteration and record.get('co_alteration_status') != co_alteration:
        return False
    if co_gene and canonical_gene(co_gene) not in {gene for context in record.get('gene_contexts', []) for gene in context}:
        return False
    return (not co_use or co_use in record.get('analysis_uses', [])) and (not co_type or co_type in record.get('alteration_types', []))


def validate_filters(co_mutation='', co_alteration='', co_use='', co_type=''):
    for value, allowed in ((co_mutation, STATES), (co_alteration, STATES), (co_use, USES), (co_type, TYPES)):
        if value and value not in allowed:
            raise ValueError(f'Unknown co-alteration filter: {value}')


def topic_summary(rows):
    included = [row for row in rows if row['eligibility'] == 'included']
    return dict(scope='included formal articles only; current registry; not all journal publications',
                included=len(included),
                co_mutation=dict(Counter(row['co_mutation_status'] for row in included)),
                co_alteration=dict(Counter(row['co_alteration_status'] for row in included)),
                coverage_complete=all(row['co_alteration_status'] != 'not_curated' for row in included))


def topic_markdown(rows, data):
    summary = topic_summary(rows)
    lines = ['# 全库共突变与共改变专题目录', '',
             '按真实期刊、出版年保留原分类；以下是叠加的文章级主题标签，不更改阅读/验收/highlight。', '',
             '标签依据及用法：[coalteration-topics.md](coalteration-topics.md)。权威逐篇记录：[coalteration-annotations.json](coalteration-annotations.json)。机器表：[library-index.csv](library-index.csv)。', '',
             f'纳入正式论文 {summary["included"]} 篇；序列共突变实际分析/描述 {summary["co_mutation"].get("analyzed", 0)} 篇；广义共改变实际分析/描述 {summary["co_alteration"].get("analyzed", 0)} 篇。前者是后者子集，不能相加。', '',
             '“实际分析/描述”包括描述性oncoplot/少数病例，并非全是共突变主题主文或阳性机制结果。“本轮未识别”不是全文绝无相关内容。列示基因上下文非穷尽，包含互斥检验和模型，不表示每一组合均正共现。', '']
    for journal in sorted({row['journal'] for row in rows if row['eligibility'] == 'included'}):
        lines.extend([f'## {journal}', '', '| 年份 | PMID / 题名 | 序列共突变 | 广义共改变 | 基因上下文（非穷尽） | 用途 | STK11重点 |', '|---|---|---|---|---|---|---|'])
        for row in rows:
            if row['eligibility'] != 'included' or row['journal'] != journal:
                continue
            title = row['title'].replace('|', '/')
            lines.append(f'| {row["year"]} | [{row["pmid"]} — {title}](https://pubmed.ncbi.nlm.nih.gov/{row["pmid"]}/) | {LABELS[row["co_mutation_status"]]} | {LABELS[row["co_alteration_status"]]} | {row["co_gene_contexts"] or "—"} | {row["co_analysis_uses"] or "—"} | {row["stk11_highlight"]} |')
        lines.append('')
    lines.extend(['## 排除与预印本', '', f'正式登记中另有 {sum(row["eligibility"] == "excluded" for row in rows)} 条排除记录；不进入以上纳入分母。', ''])
    for identifier, record in data.get('preprints', {}).items():
        lines.append(f'- [{identifier}](https://doi.org/{record["doi"]})：{LABELS[record["co_alteration_status"]]}；{record["boundary"]}')
    return '\n'.join(lines) + '\n'
