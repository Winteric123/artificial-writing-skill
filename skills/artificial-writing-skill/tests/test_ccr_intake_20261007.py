import csv
import json
import unittest
from collections import Counter
from pathlib import Path

REF = Path(__file__).resolve().parents[1] / 'references'
PMIDS = {'34074656', '33272981', '35802677', '34921025', '32241817', '31694835'}


def rows(name):
    with (REF / name).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


class October7CCRIntake(unittest.TestCase):
    def test_identity_page_scope_and_separate_acceptance(self):
        manifest = rows('ccr-2026-10-07-reading-manifest.csv')
        quality = {x['pmid']: x for x in rows('ccr-reading-quality-register.csv')}
        library = {x['pmid']: x for x in rows('library-index.csv')}
        self.assertEqual({x['pmid'] for x in manifest}, PMIDS)
        self.assertEqual(len(manifest), 6)
        self.assertEqual(sum(int(x['physical_pages']) for x in manifest), 79)
        self.assertEqual(Counter(x['year'] for x in manifest), {'2020': 2, '2021': 2, '2022': 2})
        for article in manifest:
            pmid = article['pmid']
            self.assertEqual(library[pmid]['journal'], 'Clinical Cancer Research')
            self.assertEqual(library[pmid]['title'], article['title'])
            self.assertEqual(library[pmid]['main_read_completed_on'], '2026-10-07')
            self.assertEqual(library[pmid]['reading_stage'], 'main_text_deep_read_complete')
            self.assertEqual(library[pmid]['review_status'], 'not_reviewed')
            self.assertEqual(library[pmid]['supplement_status'], 'not_supplied')
            self.assertEqual(library[pmid]['stk11_highlight'], 'no')
            for gate in ('coverage', 'evidence', 'results', 'language', 'traceability', 'transfer'):
                self.assertEqual(quality[pmid][gate + '_check'], 'pending')
        self.assertNotIn('35504291', PMIDS)

    def test_historical_scope_is_not_legacy_quantitative_learning(self):
        bibliography = {x['pmid']: x for x in rows('ccr-corpus-bibliography.csv')}
        for pmid in PMIDS:
            self.assertEqual(bibliography[pmid]['standardized_section_corpus_included'], 'no')
            self.assertEqual(bibliography[pmid]['phrase_example_bank_included'], 'no')
        for pmid in ('32241817', '31694835'):
            self.assertIn('historical_scope_exception', bibliography[pmid]['corpus_genre_status'])

    def test_language_sections_and_source_alerts(self):
        catalog = rows('ccr-section-language-catalog.csv')
        controls = json.loads((REF / 'language-controls.json').read_text(encoding='utf-8-sig'))
        sections = {'abstract-background', 'abstract-methods', 'abstract-results', 'abstract-conclusion',
                    'introduction', 'methods', 'results', 'discussion', 'conclusion', 'translational-relevance'}
        for pmid in PMIDS:
            entries = [x for x in catalog if x['source_article_ids'] == pmid]
            self.assertTrue(entries, pmid)
            self.assertTrue(sections <= {x['primary_section'] for x in entries}, pmid)
            self.assertTrue({'vocabulary', 'sentence-frame', 'paragraph-model'} <= {x['unit_type'] for x in entries}, pmid)
            self.assertTrue(any(pmid in x['article_ids'] for x in controls['article_alerts']), pmid)
        notch = [x['restriction'] for x in controls['article_alerts'] if '32241817' in x['article_ids']]
        self.assertTrue(any('.255' in x and '9.3%' in x and '5.6%' in x for x in notch))

    def test_exact_pdf_versions_and_safe_modality_tags(self):
        versions = {x['pmid']: x for x in rows('source-version-register.csv')}
        locators = json.loads((REF / 'source-pdf-locators.json').read_text(encoding='utf-8-sig'))
        for article in rows('ccr-2026-10-07-reading-manifest.csv'):
            pmid = article['pmid']
            self.assertEqual(article['sha256'], versions[pmid]['sha256'])
            self.assertEqual(article['sha256'], locators['sources'][pmid]['sha256'])
            self.assertEqual(int(article['physical_pages']), locators['sources'][pmid]['physical_pages'])
            self.assertEqual(article['pdf_version'], 'publisher_typeset_pdf')
            self.assertNotIn('single-cell', article['secondary_domain_tags'].split(';'))
            self.assertNotIn('proteomics', article['secondary_domain_tags'].split(';'))
            self.assertNotIn('\\', locators['sources'][pmid]['filename'])

    def test_topic_and_experimental_model_boundaries(self):
        topics = json.loads((REF / 'coalteration-annotations.json').read_text(encoding='utf-8-sig'))['articles']
        for pmid in PMIDS:
            self.assertEqual(topics[pmid]['co_alteration_status'], 'analyzed')
        for pmid in ('34074656', '33272981', '31694835'):
            self.assertEqual(topics[pmid]['co_mutation_status'], 'not_identified')
        self.assertIn('copy_number_loss', topics['34074656']['alteration_types'])
        self.assertIn('fusion_rearrangement', topics['33272981']['alteration_types'])
        self.assertIn('same_gene_compound', topics['34921025']['alteration_types'])
        scope = json.loads((REF / 'source-scope-backfill.json').read_text(encoding='utf-8-sig'))['articles']
        self.assertNotIn('mouse', scope['34921025']['model_ids'])
        self.assertNotIn('cdx', scope['34921025']['model_ids'])
        self.assertIn('pdx', scope['31694835']['model_ids'])
        self.assertIn('mouse', scope['31694835']['model_ids'])


if __name__ == '__main__':
    unittest.main()
