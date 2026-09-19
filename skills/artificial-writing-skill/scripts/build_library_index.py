import argparse
import csv
import json
import io
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True

from validate_reading_quality import read_rows, validate
from library_common import atomic_text, journal_registry


def write_csv(path, rows):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
    atomic_text(path, '\ufeff' + stream.getvalue())


def escape(value):
    return str(value).replace('|', '/').replace('\n', ' ')


def related_formal_state(preprint, formal_by_pmid):
    formal = formal_by_pmid.get(preprint['related_pmid'])
    if formal and formal['doi'].casefold() != preprint['related_doi'].casefold():
        raise ValueError('Related preprint/formal DOI mismatch')
    return formal['reading_stage'] if formal else 'not_indexed'


def group_counts(rows):
    included = [row for row in rows if row['eligibility'] == 'included']
    complete = sum(row['reading_stage'] == 'main_text_deep_read_complete' for row in included)
    return dict(registered=len(rows), included=len(included), complete=complete,
                incomplete=len(included) - complete, excluded=len(rows) - len(included))


def journal_year_counts(rows):
    counts = {}
    for journal in sorted({row['journal'] for row in rows}):
        journal_rows = [row for row in rows if row['journal'] == journal]
        counts[journal] = {
            year: group_counts([row for row in journal_rows if row['year'] == year])
            for year in sorted({row['year'] for row in journal_rows})
        }
    return counts


def build(skill):
    validate(skill)
    references = skill / 'references'
    highlight_text = (references / 'stk11-priority-references.md').read_text(encoding='utf-8-sig')
    highlight_ids = set(re.findall(r'^\| 1 \| [^|]+ \| \d{4} \| (\d{8}) \|', highlight_text, re.M))
    if not highlight_ids:
        raise ValueError('Highlight table changed; verify its parser before proceeding')
    version_path = references / 'source-version-register.csv'
    versions = {row['pmid']: row for row in read_rows(version_path)} if version_path.exists() else {}
    rows = []
    for prefix, configuration in journal_registry(skill).items():
        bibliography_name, ledger_name = configuration['bibliography'], configuration['ledger']
        quality = {row['pmid']: row for row in read_rows(references / configuration['quality'])}
        domains = defaultdict(set)
        catalog_path = references / f'{prefix}-section-language-catalog.csv'
        if catalog_path.exists():
            for entry in read_rows(catalog_path):
                identifiers = entry.get('source_article_ids', '').split(';')
                if len(identifiers) == 1 and identifiers[0] in quality:
                    domains[identifiers[0]].add(entry.get('domain', ''))
        for article in read_rows(references / bibliography_name):
            pmid = article['pmid']
            status = quality[pmid]
            rows.append(dict(
                year=article['year'], journal=article['journal'], title=article['title'], pmid=pmid,
                doi=article['doi'], publication_status=article.get('publication_status', 'see source bibliography and intake manifest'),
                supplied_pdf_version=versions.get(pmid, {}).get('supplied_pdf_version', 'not_recorded'),
                eligibility=status['eligibility'], official_category=article.get('ccr_official_category', ''),
                official_category_status=article.get('ccr_category_status', 'not_recorded_for_this_journal'),
                primary_content_class=article.get('primary_classification', article.get('article_type', '')),
                secondary_content_tags=article.get('secondary_classifications', '') or '; '.join(sorted(domains[pmid])),
                tag_basis='bibliography content classification' if article.get('secondary_classifications') else ('single-paper curated language domains' if domains[pmid] else 'no secondary topic verification recorded'),
                reading_stage=status['reading_stage'], main_read_completed_on=status['main_read_completed_on'],
                review_status=status['review_status'], supplement_status=status['supplement_status'],
                stk11_highlight='yes' if pmid in highlight_ids else 'no',
                bibliography=bibliography_name, reading_ledger=ledger_name, reading_evidence=status['reading_evidence'],
            ))
    rows.sort(key=lambda row: (row['year'], row['journal'], row['title'].casefold()))
    identifiers = [row['pmid'] for row in rows]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError('Duplicate PMID across journal bibliographies')
    if not highlight_ids.issubset(identifiers):
        raise ValueError('Highlight PMID absent from journal bibliographies')
    included = [row for row in rows if row['eligibility'] == 'included']
    excluded = [row for row in rows if row['eligibility'] == 'excluded']
    complete = [row for row in included if row['reading_stage'] == 'main_text_deep_read_complete']
    years = sorted({row['year'] for row in rows})
    summary = dict(scope=dict(journals='all_registered_formal_journals', years='all_indexed_issue_years',
                             topic_filter=None, preprints_included=False),
                   registered=len(rows), included=len(included), excluded_legacy=len(excluded),
                   main_text_complete=len(complete), eligible_incomplete=len(included) - len(complete),
                   source_recheck_passed=sum(row['review_status'] == 'passed' for row in rows),
                   stk11_highlights=len(highlight_ids), years={}, journal_years=journal_year_counts(rows))
    text = ['# 文献总目录：按期刊、年份与阅读状态', '',
            '本目录由各期刊 bibliography、权威阅读 ledger 和质量 register 联表生成；不是再次精读或全期刊查全报告。年份沿用正式出版卷期年，在线年/版本见原始书目及批次manifest。', '',
            f'正式期刊登记{len(rows)}篇；当前纳入{len(included)}篇；历史排除评论{len(excluded)}篇。已完成正文精读{len(complete)}篇，合格但尚未完成精读{len(included)-len(complete)}篇。来源复核验收通过{summary["source_recheck_passed"]}篇；STK11 highlight {len(highlight_ids)}篇。', '',
            '“已精读”指登记的正文及相应主图表范围，不等于补充材料全读、验收通过或独立审查。旧登记状态保留，不因本次目录重建自动升级。', '',
            '完整机器可筛选清单：[library-index.csv](library-index.csv)。预印本另见[preprint-source-register.csv](preprint-source-register.csv)，不进入下方正式期刊分母。候选参考目录亦不算已纳入或已读。', '',
            '统计口径：下方年份汇总涵盖全部已登记正式期刊，不等于CCR单刊；期刊汇总涵盖所有已登记年份。两者均不限定专题。指定期刊和年份请查交叉汇总，指定专题或批次须另按PMID集合筛选。', '',
            '## 年份汇总（全部正式期刊）', '', '| 年份 | 登记 | 纳入 | 已精读 | 合格待完成 | 历史排除 |', '|---|---:|---:|---:|---:|---:|']
    for year in years:
        year_rows = [row for row in rows if row['year'] == year]
        eligible = [row for row in year_rows if row['eligibility'] == 'included']
        done = sum(row['reading_stage'] == 'main_text_deep_read_complete' for row in eligible)
        summary['years'][year] = group_counts(year_rows)
        text.append(f'| {year} | {len(year_rows)} | {len(eligible)} | {done} | {len(eligible)-done} | {len(year_rows)-len(eligible)} |')
    text.extend(['', '## 期刊汇总（全部登记年份）', '', '| 期刊 | 登记 | 纳入 | 已精读 |', '|---|---:|---:|---:|'])
    for journal in sorted({row['journal'] for row in rows}):
        group = [row for row in rows if row['journal'] == journal]
        text.append(f'| {journal} | {len(group)} | {sum(row["eligibility"] == "included" for row in group)} | {sum(row["reading_stage"] == "main_text_deep_read_complete" for row in group)} |')
    text.extend(['', '## 期刊与年份交叉汇总（不限定专题）', '',
                 '| 期刊 | 年份 | 登记 | 纳入 | 已精读 | 合格待完成 | 历史排除 |', '|---|---|---:|---:|---:|---:|---:|'])
    for journal, journal_years in summary['journal_years'].items():
        for year, counts in journal_years.items():
            text.append(f'| {escape(journal)} | {year} | {counts["registered"]} | {counts["included"]} | {counts["complete"]} | {counts["incomplete"]} | {counts["excluded"]} |')
    text.extend(['', '## 全部纳入名单', '', '每篇均保留完整题名、年份、期刊、PMID、DOI、官方栏目/内容标签、阅读状态和highlight。官方栏目与自建主题标签是两个不同字段；空缺主题标签表示未记录，不能从标题推断已精读。'])
    for journal in sorted({row['journal'] for row in included}):
        text.extend(['', f'### {journal}'])
        for year in years:
            group = [row for row in included if row['journal'] == journal and row['year'] == year]
            if not group:
                continue
            text.extend(['', f'#### {year}（{len(group)}篇）', '', '| PMID | 完整题名 | DOI | 栏目或已记录内容分类 | 正文精读 | STK11 highlight |', '|---|---|---|---|---|---|'])
            for row in group:
                status = '已完成' if row['reading_stage'] == 'main_text_deep_read_complete' else '尚未完成'
                category = row['official_category'] or row['primary_content_class']
                text.append(f'| {row["pmid"]} | {escape(row["title"])} | {row["doi"]} | {escape(category)} | {status} | {row["stk11_highlight"]} |')
    text.extend(['', '## 历史排除记录（不作为阅读队列）', '', '| 年份 | PMID | 完整题名 |', '|---|---|---|'])
    text.extend(f'| {row["year"]} | {row["pmid"]} | {escape(row["title"])} |' for row in excluded)
    preprints = read_rows(references / 'preprint-source-register.csv')
    text.extend(['', '## 单独登记的预印本', '', '这些版本不计入正式期刊纳入/阅读数量；不能替代对应正式论文。'])
    if len({row['source_id'] for row in preprints}) != len(preprints):
        raise ValueError('Duplicate version-specific preprint source ID')
    formal_by_pmid = {row['pmid']: row for row in rows}
    for row in preprints:
        formal_state = related_formal_state(row, formal_by_pmid)
        text.extend(['', f'- {row["year"]} | {row["source"]} {row["version"]} ({row["version_date"]}) | {row["title"]} | DOI {row["doi"]} | 本版本：{row["reading_stage"]}；对应正式版 PMID{row["related_pmid"]}：{formal_state}。两者阅读状态独立。'])
    ccr_rows = [row for row in rows if row['journal'] == 'Clinical Cancer Research']
    category_text = ['# CCR official category index', '',
                     'Generated from the bibliography and quality register, not inferred from article titles. Current overall inventory: [library-index.md](library-index.md). Historical category names remain distinct; topic tags do not rename official CCR sections.', '',
                     '| Official category | Indexed | Included | Main-text complete |', '|---|---:|---:|---:|']
    for category in sorted({row['official_category'] or 'Official category unverified' for row in ccr_rows}):
        group = [row for row in ccr_rows if (row['official_category'] or 'Official category unverified') == category]
        category_text.append(f'| {category} | {len(group)} | {sum(row["eligibility"] == "included" for row in group)} | {sum(row["reading_stage"] == "main_text_deep_read_complete" for row in group)} |')
    category_text.extend(['', '## Verification status', ''])
    for status, count in sorted(Counter(row['official_category_status'] for row in ccr_rows).items()):
        category_text.append(f'- {status}: {count}')
    category_text.extend(['', '## Unverified or generic labels', ''])
    for row in ccr_rows:
        if row['official_category_status'] != 'official_section':
            category_text.append(f'- PMID {row["pmid"]}: {row["official_category"] or "unverified"}; {row["official_category_status"]}; {row["title"]}. Do not infer a more specific official category from content.')
    category_text.extend(['', '## Boundaries', '',
                         'The 2020 SMARCA4 article remains an explicit user-priority historical exception. Eight legacy CCR Translations commentaries remain excluded and are not future reading tasks. No replies, editorials or response-only correspondence are newly included. Main-text completion and source-recheck acceptance are separate states; supplements require their own evidence.', '',
                         'Use ccr_official_category, ccr_category_source, ccr_category_status and ccr_category_verified_on in [ccr-corpus-bibliography.csv](ccr-corpus-bibliography.csv) for the article-level classification evidence. The latest author-manuscript category for PMID39561276 was verified at the [official article page](https://aacrjournals.org/clincancerres/article/31/2/376/751103/Analysis-of-Shared-Variants-between-Cancer); the other seven latest additions use their publisher PDF headers.'])
    write_csv(references / 'library-index.csv', rows)
    atomic_text(references / 'library-index.md', '\n'.join(text) + '\n')
    atomic_text(references / 'library-summary.json', json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    atomic_text(references / 'ccr-category-index.md', '\n'.join(category_text) + '\n')
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rebuild journal/year inventory without changing any reading status.')
    parser.add_argument('--skill-path', type=Path, default=Path(__file__).resolve().parents[1])
    arguments = parser.parse_args()
    print(json.dumps(build(arguments.skill_path), ensure_ascii=False, indent=2))
