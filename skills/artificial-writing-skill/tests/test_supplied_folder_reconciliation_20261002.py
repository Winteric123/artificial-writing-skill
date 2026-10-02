"""Version identity, source restrictions and unchanged membership after duplicate intake."""
import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / 'references'
PMID = '34740862'
VOR = '0b949840772064fbcef9db32662636a498819e74e25578b1288b6c67c71828bf'
AM = 'b614e011b1e0ef0709602c6f5c93f57f04552c3fa213d13da15dfce015bbe426'


def data(name):
    return json.loads((REFS / name).read_text(encoding='utf-8-sig'))


def rows(name):
    with (REFS / name).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


class SuppliedFolderReconciliation(unittest.TestCase):
    def test_folder_label_does_not_override_journal_or_inflate_articles(self):
        manifest = data('supplement-ccr-2026-10-02-reconciliation.json')
        articles = manifest['records']
        versions = [version for row in articles for version in row['supplied_versions']]
        self.assertEqual(len(articles), 12)
        self.assertEqual(len({row['pmid'] for row in articles}), 12)
        self.assertEqual(len(versions), 13)
        self.assertEqual(len({version['sha256'] for version in versions}), 13)
        self.assertEqual(sum(len(version['supplied_filenames']) for version in versions), 14)
        self.assertEqual(manifest['newly_registered_articles'], 0)
        self.assertEqual(manifest['new_main_text_completions'], 0)
        self.assertEqual(len({row['journal'] for row in articles}), 7)
        self.assertNotIn('Clinical Cancer Research', {row['journal'] for row in articles})
        library = {row['pmid']: row for row in rows('library-index.csv')}
        for article in articles:
            row = library[article['pmid']]
            self.assertEqual(row['reading_stage'], 'main_text_deep_read_complete')
            self.assertEqual(row['review_status'], 'passed' if row['pmid'] == PMID else 'not_reviewed')

    def test_alternate_manuscript_cannot_replace_primary_physical_anchors(self):
        article = next(row for row in data('supplement-ccr-2026-10-02-reconciliation.json')['records'] if row['pmid'] == PMID)
        versions = {version['sha256']: version for version in article['supplied_versions']}
        self.assertEqual((versions[VOR]['version'], versions[VOR]['physical_pages']), ('version_of_record', 12))
        self.assertEqual((versions[AM]['version'], versions[AM]['physical_pages']), ('author_manuscript', 19))
        self.assertTrue(versions[VOR]['selected_for_language_locators'])
        self.assertFalse(versions[AM]['selected_for_language_locators'])
        selected = next(row for row in rows('source-version-register.csv') if row['pmid'] == PMID)
        self.assertEqual(selected['sha256'], VOR)
        self.assertEqual(selected['archived_pdf_count'], '2')
        self.assertEqual(selected['supplied_pdf_version'], 'version_of_record')
        locator = data('source-pdf-locators.json')['sources'][PMID]
        self.assertEqual(locator['sha256'], VOR)
        self.assertEqual(locator['physical_pages'], 12)

    def test_contexts_preserve_identity_and_correct_ipw_locator(self):
        contexts = [record for record in data('source-context-rechecks.json')['entries'] if record['pmid'] == PMID]
        self.assertEqual(len(contexts), 10)
        ipw = next(record for record in contexts if record['stable_id'] == 'jto-lang-9ef2f23f4c96c69ee658')
        self.assertEqual(ipw['physical_pages'], [10])
        self.assertFalse(ipw['quotation_verified'])
        self.assertEqual(ipw['review_method'], 'independent_agent_source_recheck')
        catalog = [row for row in rows('jto-section-language-catalog.csv') if row['source_article_ids'] == PMID]
        self.assertEqual(len(catalog), 10)
        for row in catalog:
            lines = (REFS / row['source_asset']).read_text(encoding='utf-8-sig').splitlines()
            self.assertIn(row['expression'], lines[int(row['source_line']) - 1])

    def test_review_pass_does_not_erase_conflict_or_supplement_limits(self):
        quality = next(row for row in rows('jto-reading-quality-register.csv') if row['pmid'] == PMID)
        self.assertEqual(quality['review_status'], 'passed')
        self.assertEqual(quality['supplement_status'], 'not_supplied')
        self.assertEqual(quality['main_read_completed_on'], '2026-10-02')
        self.assertTrue((REFS / quality['review_record']).is_file())
        alert = next(record for record in data('language-controls.json')['article_alerts'] if PMID in record['article_ids'])
        for boundary in ('TMB', 'Fig3D', 'xCell', 'interaction', 'not reviewed'):
            self.assertIn(boundary, alert['restriction'])
        member = next(row for row in data('stk11-writing-reference-map.json')['records'] if row['pmid'] == PMID)
        self.assertEqual(member['tier'], 'topic_support')
        self.assertFalse(member['in_cross_gene_16'])

    def test_tcga_and_treatment_tags_do_not_imply_paired_or_randomized_data(self):
        record = next(row for row in data('stk11-assay-treatment-tags.json')['records'] if row['pmid'] == PMID)
        self.assertIn('ici', record['treatment_types'])
        self.assertNotIn('ici_mono', record['treatment_types'])
        self.assertIn('chemotherapy', record['treatment_types'])
        rna = next(item for item in record['assays'] if item['assay'] == 'bulk_rna')
        self.assertEqual(rna['origin'], 'reanalysis')
        self.assertIn('TCGA', rna['sample_context'])
        self.assertNotIn('single_cell_rna', {item['assay'] for item in record['assays']})


if __name__ == '__main__':
    unittest.main()
