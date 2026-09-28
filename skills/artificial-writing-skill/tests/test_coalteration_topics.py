import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / 'scripts'))
sys.path.insert(0, str(SKILL / 'tests'))

from coalteration_topics import article_topics, load_annotations, topic_matches, topic_summary, validate_record
from library_common import read_csv, read_json
from search_language import load_index, search
from test_retrieval import synthetic_entry


class CoalterationTopics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library = read_csv(SKILL / 'references/library-index.csv')
        cls.data = load_annotations(SKILL, cls.library)

    def test_registry_coverage_and_eligibility(self):
        records = self.data['articles']
        self.assertEqual(set(records), {row['pmid'] for row in self.library})
        for row in self.library:
            record = records[row['pmid']]
            self.assertEqual(record['eligibility'], row['eligibility'])
            self.assertEqual(row['co_mutation_status'], record['co_mutation_status'])
            self.assertEqual(row['co_alteration_status'], record['co_alteration_status'])
            if row['eligibility'] == 'included':
                self.assertNotIn('not_curated', (record['co_mutation_status'], record['co_alteration_status']))
                self.assertTrue(record['pdf']['sha256'])
            else:
                self.assertEqual(record['co_alteration_status'], 'excluded')

    def test_atm_and_smarca_priority_have_actual_topic_tags(self):
        for pmid in ('37733794', '37097610', '32709715'):
            self.assertEqual(self.data['articles'][pmid]['co_mutation_status'], 'analyzed')
            self.assertTrue(topic_matches(self.data['articles'][pmid], co_gene='STK11'))

    def test_copy_loss_not_pure_sequence_comutation(self):
        record = self.data['articles']['39864548']
        self.assertEqual(record['co_alteration_status'], 'analyzed')
        self.assertNotEqual(record['co_mutation_status'], 'analyzed')
        self.assertIn('copy_number_loss', record['alteration_types'])

    def test_fusion_plus_mutation_not_two_sequence_mutations(self):
        record = self.data['articles']['37572870']
        self.assertEqual(record['co_mutation_status'], 'not_identified')
        self.assertTrue(topic_matches(record, co_alteration='analyzed', co_type='fusion_rearrangement'))

    def test_compound_mutation_tag_is_separate(self):
        record = self.data['articles']['37249619']
        self.assertTrue(topic_matches(record, co_mutation='analyzed', co_type='same_gene_compound', co_gene='EGFR'))
        self.assertFalse(topic_matches(record, co_gene='JAK2'))

    def test_genes_do_not_infer_highlight_or_direct_stk11(self):
        record = self.data['articles']['42409117']
        row = next(row for row in self.library if row['pmid'] == '42409117')
        self.assertEqual(row['stk11_highlight'], 'yes')
        self.assertFalse(topic_matches(record, co_gene='STK11'))
        self.assertTrue(topic_matches(record, co_gene='MTAP'))

    def test_background_citation_not_actual_analysis(self):
        for pmid in ('39836411', '41903702', '42485106'):
            self.assertEqual(self.data['articles'][pmid]['co_alteration_status'], 'context_only')

    def test_mtap_inventory_uses_broad_filter_without_omissions(self):
        expected = {'42148883', '42405849', '42507545', '41260457', '42409117'}
        actual = {pmid for pmid, record in self.data['articles'].items()
                  if topic_matches(record, co_alteration='analyzed', co_gene='MTAP')}
        self.assertEqual(actual, expected)

    def test_copy_loss_paper_can_also_analyze_sequence_comutations(self):
        record = self.data['articles']['42507545']
        self.assertTrue(topic_matches(record, co_mutation='analyzed', co_type='copy_number_loss', co_gene='STK11'))
        self.assertIn(['KRAS', 'STK11'], record['gene_contexts'])
        self.assertIn(['KRAS', 'KEAP1'], record['gene_contexts'])
        self.assertTrue(topic_matches(self.data['articles']['41260457'], co_mutation='analyzed', co_type='same_gene_compound'))

    def test_actual_descriptions_do_not_require_validation_or_main_topic(self):
        for pmid in ('33323402', '33020056', '36449664', '34740925', '36729110', '41563386'):
            self.assertEqual(self.data['articles'][pmid]['co_alteration_status'], 'analyzed')
            self.assertTrue(self.data['articles'][pmid]['topic_recheck']['text_pages'])

    def test_bounded_recheck_does_not_promote_background_or_time_unions(self):
        for pmid in ('37725585', '39400264', '39150541', '41403154'):
            self.assertEqual(self.data['articles'][pmid]['co_alteration_status'], 'context_only')
        for pmid in ('42377115', '42440365'):
            self.assertEqual(self.data['articles'][pmid]['co_alteration_status'], 'not_identified')

    def test_mtap_sequence_gene_context_is_not_a_positive_pair_claim(self):
        record = self.data['articles']['42405849']
        self.assertTrue(topic_matches(record, co_alteration='analyzed', co_gene='STK11'))
        self.assertNotEqual(record['co_mutation_status'], 'analyzed')
        self.assertNotIn(['KRAS', 'STK11'], record['gene_contexts'])
        self.assertTrue(topic_matches(self.data['articles']['42409117'], co_type='copy_number_gain', co_gene='ERBB2'))

    def test_protein_radiomics_and_drug_pairs_not_auto_tagged(self):
        for pmid in ('34686497', '34518312', '40499141'):
            self.assertEqual(self.data['articles'][pmid]['co_alteration_status'], 'not_identified')

    def test_germline_and_experimental_sources_qualified(self):
        self.assertIn('germline_somatic', self.data['articles']['38261467']['alteration_types'])
        self.assertIn('engineered_combination', self.data['articles']['34667030']['alteration_types'])
        self.assertIn('different_compartments', self.data['articles']['39932457']['alteration_types'])

    def test_union_not_imputed_to_triple(self):
        record = self.data['articles']['42268349']
        self.assertNotIn(['KRAS', 'STK11', 'KEAP1'], record['gene_contexts'])
        self.assertIn(['KRAS', 'STK11'], record['gene_contexts'])

    def test_unknown_new_article_is_not_curated_not_negative(self):
        record = article_topics({'pmid': '99999999'}, self.data)
        self.assertEqual(record['co_alteration_status'], 'not_curated')
        self.assertFalse(topic_matches(record, co_alteration='not_identified'))

    def test_preprint_keeps_version_specific_key(self):
        identifier = 'medrxiv:10.1101/2025.01.27.25321050:v1'
        self.assertIn(identifier, self.data['preprints'])
        self.assertNotIn(identifier, self.data['articles'])
        self.assertEqual(self.data['preprints'][identifier]['version'], 'v1')

    def test_summary_uses_eligible_same_population(self):
        summary = topic_summary(self.library)
        total = sum(row['eligibility'] == 'included' for row in self.library)
        self.assertEqual(summary['included'], total)
        self.assertEqual(sum(summary['co_mutation'].values()), total)
        self.assertEqual(sum(summary['co_alteration'].values()), total)
        self.assertLessEqual(summary['co_mutation']['analyzed'], summary['co_alteration']['analyzed'])
        self.assertTrue(summary['coverage_complete'])

    def test_invalid_state_and_exclusion_rejected(self):
        record = copy.deepcopy(self.data['articles']['37733794'])
        record['co_alteration_status'] = 'not_identified'
        with self.assertRaises(ValueError):
            validate_record(record, '37733794')
        record['co_alteration_status'] = 'analyzed'
        record['eligibility'] = 'excluded'
        with self.assertRaises(ValueError):
            validate_record(record, '37733794')

    def test_stale_evidence_hash_rejected(self):
        modified = copy.deepcopy(self.data)
        modified['articles']['37733794']['evidence'][0]['source_sha256'] = '0' * 64
        def reader(path):
            return modified if path.name == 'coalteration-annotations.json' else read_json(path)
        with patch('coalteration_topics.read_json', side_effect=reader):
            with self.assertRaisesRegex(ValueError, 'Stale co-alteration evidence'):
                load_annotations(SKILL, self.library)

    def test_invalid_physical_page_rejected(self):
        modified = copy.deepcopy(self.data)
        modified['articles']['37733794']['pdf']['checked_context_pages'] = [999999]
        def reader(path):
            return modified if path.name == 'coalteration-annotations.json' else read_json(path)
        with patch('coalteration_topics.read_json', side_effect=reader):
            with self.assertRaisesRegex(ValueError, 'Invalid topic PDF page'):
                load_annotations(SKILL, self.library)

    def test_stale_pdf_identity_rejected(self):
        modified = copy.deepcopy(self.data)
        modified['articles']['37733794']['pdf']['sha256'] = '0' * 64
        def reader(path):
            return modified if path.name == 'coalteration-annotations.json' else read_json(path)
        with patch('coalteration_topics.read_json', side_effect=reader):
            with self.assertRaisesRegex(ValueError, 'Stale topic PDF identity'):
                load_annotations(SKILL, self.library)

    def test_source_filters_match_same_article(self):
        entry = synthetic_entry()
        entry['source_articles'][0]['co_alteration_topics'] = self.data['articles']['37733794']
        entry['source_articles'][1]['co_alteration_topics'] = self.data['articles']['40499141']
        self.assertEqual(search([entry], co_mutation='analyzed')['matched_count'], 1)
        self.assertEqual(search([entry], co_mutation='analyzed', year='2026')['matched_count'], 0)
        self.assertEqual(search([entry], co_gene='STK11', highlight=True)['matched_count'], 0)
        self.assertEqual(search([entry], co_gene='LKB1', pmid='99990001')['matched_count'], 1)

    def test_missing_tag_and_invalid_filter_fail_closed(self):
        self.assertEqual(search([synthetic_entry()], co_alteration='analyzed')['matched_count'], 0)
        with self.assertRaises(ValueError):
            search([], co_mutation='yes')
        with self.assertRaises(ValueError):
            search([], co_type='drug_combination')

    def test_filters_do_not_upgrade_acceptance(self):
        entry = synthetic_entry()
        for article in entry['source_articles']:
            article['co_alteration_topics'] = self.data['articles']['37733794']
        self.assertEqual(search([entry], co_mutation='analyzed', reviewed=True)['matched_count'], 0)
        self.assertEqual(search([entry], co_mutation='analyzed', context_reviewed=True)['matched_count'], 0)

    def test_real_language_index_contains_topics_and_dependencies(self):
        entries, manifest = load_index(SKILL)
        self.assertIn('coalteration-annotations.json', manifest['dependencies'])
        result = search(entries, co_mutation='analyzed', co_gene='ATM', section='results', pmid='37733794')
        self.assertGreater(result['matched_count'], 0)
        self.assertTrue(all('37733794' in entry['matching_source_pmids'] for entry in result['entries']))
        for entry in result['entries']:
            self.assertTrue(entry['source_articles'][0]['co_alteration_topics']['evidence'])


if __name__ == '__main__':
    unittest.main()
