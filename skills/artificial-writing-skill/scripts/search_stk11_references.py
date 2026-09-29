import argparse
import json
import sys
from pathlib import Path

from library_common import file_hash, journal_registry, read_csv, read_json, reference_path
from validate_reading_quality import validate


def load_records(skill, include_candidates=False):
    validate(skill)
    references = skill / 'references'
    payload = read_json(references / 'stk11-assay-treatment-tags.json')
    if payload.get('schema_version') != 1:
        raise ValueError('Unsupported STK11 tag schema')
    versions = {row['pmid']: row for row in read_csv(references / 'source-version-register.csv')}
    membership = {row['pmid']: row for row in read_json(references / 'stk11-writing-reference-map.json')['records']}
    articles, states = {}, {}
    for journal in journal_registry(skill).values():
        for row in read_csv(references / journal['bibliography']):
            if row['pmid'] in articles:
                raise ValueError('Duplicate registered PMID')
            articles[row['pmid']] = row
        states.update({row['pmid']: row for row in read_csv(references / journal['quality'])})
    records = {}
    if include_candidates:
        candidates = read_json(references / 'stk11-reference-candidates.json')
        if candidates.get('schema_version') != 1:
            raise ValueError('Unsupported candidate schema')
        for candidate in candidates['records']:
            pmid = candidate['pmid']
            if pmid in records:
                raise ValueError('Duplicate candidate PMID')
            records[pmid] = dict(candidate, stable_id='STK11-PMID-' + pmid, primary_classification=candidate['module'], stk11_relation='not_fine_curated', methods=[], treatment_types=[], drugs=[], assays=[], alteration_types=[], gene_contexts=[], classification_level='historical_screening_only', evidence='stk11-reference-candidates.json', boundary=candidate['caution'] + '; specific assays/treatments not fine-curated in this tag set')
        for pmid, member in membership.items():
            if pmid not in records:
                article = articles[pmid]
                records[pmid] = dict(stable_id='STK11-PMID-' + pmid, pmid=pmid, title=article['title'], journal=article['journal'], year=article['year'], doi=article['doi'], primary_classification=';'.join(member['modules']), stk11_relation=member['stk11_relation'], methods=[], treatment_types=[], drugs=[], assays=[], alteration_types=[], gene_contexts=[], classification_level='existing_project_membership_not_new_fine_curation', evidence='stk11-writing-reference-map.json', boundary='Use original project reading references; missing detailed tags are unknown, not absence.')
    detailed_ids = set()
    for row in payload['records']:
        pmid = row['pmid']
        if pmid in detailed_ids or row['stable_id'] != 'STK11-PMID-' + pmid:
            raise ValueError('Duplicate or invalid stable paper ID')
        detailed_ids.add(pmid)
        if pmid not in articles or row['doi'].casefold() != articles[pmid]['doi'].casefold():
            raise ValueError('Unregistered or mismatched detailed article')
        if row['pdf_sha256'] != versions[pmid]['sha256']:
            raise ValueError('Detailed classification refers to a different PDF version')
        if file_hash(reference_path(skill, row['evidence'])) != row['evidence_sha256']:
            raise ValueError('Stale classification evidence: ' + pmid)
        for assay in row['assays']:
            if not all(assay.get(field) for field in ('assay', 'origin', 'sample_context', 'evidence')):
                raise ValueError('Incomplete assay context: ' + pmid)
            if assay['evidence'].split('#')[0] != row['evidence']:
                raise ValueError('Assay evidence mismatch: ' + pmid)
        records[pmid] = dict(records.get(pmid, {}), **row)
    for pmid, row in records.items():
        state = states.get(pmid, {})
        member = membership.get(pmid, {})
        row.update(reading_stage=state.get('reading_stage', 'not_registered_as_read'), main_read_completed_on=state.get('main_read_completed_on', ''), review_status=state.get('review_status', 'not_registered'), supplement_status=state.get('supplement_status', 'not_registered'), eligibility=state.get('eligibility', 'candidate_not_registered'), core_highlight=member.get('tier') == 'core_highlight', project_tier=member.get('tier', 'supplementary_reference' if pmid in detailed_ids else 'screening_candidate'), pdf_registered=pmid in versions, pubmed_url=f'https://pubmed.ncbi.nlm.nih.gov/{pmid}/', doi_url='https://doi.org/' + row['doi'])
    return sorted(records.values(), key=lambda row: (row['journal'], row['year'], row['pmid']))


def matches(row, *, assays=(), origin='', treatments=(), methods=(), relation='', pmid='', core_only=False):
    if pmid and row['pmid'] != pmid:
        return False
    if core_only and not row['core_highlight']:
        return False
    if relation and row['stk11_relation'] != relation:
        return False
    for assay in assays:
        if not any(item['assay'] == assay and (not origin or item['origin'] == origin) for item in row['assays']):
            return False
    if origin and not assays and not any(item['origin'] == origin for item in row['assays']):
        return False
    return set(treatments) <= set(row['treatment_types']) and set(methods) <= set(row['methods'])


def markdown(rows):
    lines = ['# STK11写作参考：分层分类目录', '', '主文精读、独立验收、核心highlight与候选资格分别显示。组学细标签目前覆盖2026-09-29本批19篇；其他条目缺标签是待补，不是缺少该技术。依据见逐篇笔记与stk11-assay-treatment-guide.md。', '', '| 稳定编号 / PMID | 年份·期刊·题名 | 内容及STK11关系 | 技术（来源/样本） | 治疗 / 药物 | 研究方式 | 状态 / 核心highlight |', '|---|---|---|---|---|---|---|']
    for row in rows:
        assay_text = '; '.join(f'{item["assay"]} ({item["origin"]}/{item["sample_context"]})' for item in row['assays']) or '待精细标注；不代表未开展'
        values = [f'[{row["stable_id"]}]({row["pubmed_url"]})', f'{row["year"]} · {row["journal"]} · {row["title"]} [DOI]({row["doi_url"]})', row['primary_classification'] + ' / ' + row['stk11_relation'], assay_text, '; '.join(row['treatment_types'] + row['drugs']) or '待标注', '; '.join(row['methods']) or '见历史筛选', row['reading_stage'] + '; review=' + row['review_status'] + '; core=' + str(row['core_highlight'])]
        lines.append('| ' + ' | '.join(value.replace('|', '/').replace('\n', ' ') for value in values) + ' |')
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description='Retrieve source-grounded STK11 preparation tags without changing reading/highlight status.')
    parser.add_argument('--skill-path', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--all-candidates', action='store_true')
    parser.add_argument('--assay', action='append', default=[])
    parser.add_argument('--origin', default='')
    parser.add_argument('--treatment', action='append', default=[])
    parser.add_argument('--method', action='append', default=[])
    parser.add_argument('--relation', default='')
    parser.add_argument('--pmid', default='')
    parser.add_argument('--core-only', action='store_true')
    output = parser.add_mutually_exclusive_group()
    output.add_argument('--json', action='store_true')
    output.add_argument('--markdown', action='store_true')
    args = parser.parse_args()
    try:
        records = load_records(args.skill_path, args.all_candidates)
        for values, field in ((args.treatment, 'treatment_types'), (args.method, 'methods')):
            allowed = {item for row in records for item in row[field]}
            if set(values) - allowed:
                raise ValueError(f'Unknown {field} filter: {set(values) - allowed}')
        allowed_assays = {item['assay'] for row in records for item in row['assays']}
        if set(args.assay) - allowed_assays:
            raise ValueError('Unknown assay filter')
        if args.origin and args.origin not in {item['origin'] for row in records for item in row['assays']}:
            raise ValueError('Unknown origin filter')
        if args.relation and args.relation not in {row['stk11_relation'] for row in records}:
            raise ValueError('Unknown relation filter')
        rows = [row for row in records if matches(row, assays=args.assay, origin=args.origin, treatments=args.treatment, methods=args.method, relation=args.relation, pmid=args.pmid, core_only=args.core_only)]
    except (ValueError, KeyError, OSError) as error:
        parser.exit(1, f'Classification retrieval failed: {error}\n')
    print(json.dumps(dict(count=len(rows), records=rows), ensure_ascii=False, indent=2) if args.json else markdown(rows))


if __name__ == '__main__':
    sys.dont_write_bytecode = True
    main()
