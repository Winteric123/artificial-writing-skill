import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / 'scripts'))

from library_common import read_json
from retrieval_metadata import article_scope, detected_terms, query_clauses, query_matches
from search_language import load_index, search
import test_retrieval

synthetic_entry = test_retrieval.synthetic_entry


class ExpressionScope(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries, cls.manifest = load_index(SKILL)
        cls.vocabulary = read_json(SKILL / 'references/retrieval-vocabulary.json')

    def test_exact_domain_prevents_sclc_nsclc_collision(self):
        entry = synthetic_entry()
        entry['domain'] = 'NSCLC;genomics'
        self.assertEqual(search([entry], domain='SCLC')['matched_count'], 0)
        self.assertEqual(search([entry], domain='NSCLC')['matched_count'], 1)

    def test_full_disease_phrase_does_not_match_substring(self):
        for phrase in ['non-small cell lung cancer', 'non–small-cell lung cancer', 'NSCLC']:
            found = detected_terms(phrase, self.vocabulary['diseases'])
            self.assertIn('nsclc', found)
            self.assertNotIn('sclc', found)

    def test_chinese_disease_longest_match(self):
        found = detected_terms('非小细胞肺癌', self.vocabulary['diseases'])
        self.assertEqual(found, ['nsclc'])

    def test_parent_expansion_is_explicit(self):
        entry = synthetic_entry()
        entry['_vocabulary'] = self.vocabulary
        entry['source_articles'][0]['source_scope'] = {'disease_ids': ['lung-adenocarcinoma']}
        self.assertEqual(search([entry], disease='lung-cancer')['matched_count'], 0)
        self.assertEqual(search([entry], disease='lung-cancer', include_subtypes=True)['matched_count'], 1)
        self.assertEqual(search([entry], disease='SCLC', include_subtypes=True)['matched_count'], 0)

    def test_facets_match_same_source(self):
        entry = synthetic_entry()
        entry['_vocabulary'] = self.vocabulary
        entry['source_articles'][0]['source_scope'] = {'disease_ids': ['nsclc'], 'tissue_ids': ['tumor'], 'model_ids': ['human-clinical'], 'use_roles': ['lung-primary']}
        entry['source_articles'][1]['source_scope'] = {'disease_ids': ['sclc'], 'tissue_ids': ['plasma']}
        self.assertEqual(search([entry], disease='NSCLC', tissue='plasma')['matched_count'], 0)
        self.assertEqual(search([entry], disease='NSCLC', year='2026')['matched_count'], 0)
        self.assertEqual(search([entry], disease='NSCLC', tissue='tumor', model='human-clinical', source_role='lung-primary')['matched_count'], 1)

    def test_unknown_facets_fail_closed(self):
        entry = synthetic_entry()
        for field in ['disease', 'tissue', 'model', 'source_role']:
            self.assertEqual(search([entry], **{field: 'unrecorded'})['matched_count'], 0)

    def test_no_scope_from_title_or_negative_comparator(self):
        for article in [{'title': 'A NSCLC study'}, {'disease_scope': 'MPN; not NSCLC'}, {'disease_scope': 'NEPC versus SCLC comparator'}]:
            self.assertEqual(article_scope(article, self.vocabulary)['disease_ids'], [])

    def test_bilingual_concepts_equivalent_on_entire_index(self):
        for chinese, english in [('克隆性造血', 'clonal hematopoiesis'), ('剂量依赖', 'dose-dependent'), ('无进展生存期', 'progression-free survival')]:
            first = search(self.entries, query=chinese, limit=100)
            second = search(self.entries, query=english, limit=100)
            self.assertGreater(first['matched_count'], 0)
            self.assertEqual(first['matched_count'], second['matched_count'])
            self.assertEqual([entry['stable_id'] for entry in first['entries']], [entry['stable_id'] for entry in second['entries']])

    def test_query_synonyms_do_not_conflate_perturbations(self):
        for query, wrong, correct in [('敲低', 'knockout', 'knockdown'), ('靶点作用验证', 'target occupancy', 'target engagement')]:
            clauses = query_clauses(query, self.vocabulary['concepts'])
            self.assertFalse(query_matches(wrong, clauses))
            self.assertTrue(query_matches(correct, clauses))

    def test_query_hyphens_and_concept_and_semantics(self):
        clauses = query_clauses('PFS adjusted', self.vocabulary['concepts'])
        self.assertTrue(query_matches('adjusted progression–free survival', clauses))
        self.assertFalse(query_matches('overall survival adjusted', clauses))
        self.assertFalse(query_matches('progression-free survival', clauses))

    def test_article_topics_do_not_automatically_tag_expression(self):
        all_hits = search(self.entries, pmid='37756581', limit=100)['entries']
        hits = search(self.entries, pmid='37756581', domain='scRNA', limit=100)['entries']
        self.assertLess(len(hits), len(all_hits))
        self.assertTrue(all('single-cell' in entry['expression_domains'] for entry in hits))
        nearest = next(entry for entry in all_hits if entry['expression'] == 'nearest-neighbor distance')
        self.assertEqual(nearest['expression_domains'], ['spatial-protein'])
        self.assertEqual(nearest['expression_annotation_status'], 'curated-expression-topic')

    def test_mixed_cohort_boundary_survives_retrieval(self):
        hits = search(self.entries, pmid='37756581', tissue='tonsil')['entries']
        self.assertTrue(hits)
        scope = hits[0]['source_articles'][0]['source_scope']
        self.assertIn('NSCLC: bulk RNA', scope['boundary'])
        self.assertIn('sarcoma', scope['disease_ids'])
        self.assertEqual(scope['annotation_status'], 'curated-source-scope')

    def test_rppa_not_untargeted_proteomics(self):
        entry = next(entry for entry in self.entries if entry['source_article_ids'] == '37289191' and entry['expression'] == 'reverse-phase protein array')
        self.assertEqual(entry['expression_domains'], ['targeted-protein-assay'])
        self.assertEqual(search([entry], domain='proteomics')['matched_count'], 0)

    def test_incidental_nsclc_and_nen_not_misclassified(self):
        self.assertEqual(search(self.entries, pmid='36537918', disease='NSCLC')['matched_count'], 0)
        self.assertGreater(search(self.entries, pmid='36537918', disease='MPN')['matched_count'], 0)
        self.assertEqual(search(self.entries, pmid='36255391', disease='SCLC')['matched_count'], 0)

    def test_original_wording_not_claimed_verified(self):
        self.assertTrue(all(entry['original_wording_verified'] is False for entry in self.entries))
        self.assertTrue(all(entry['source_locator']['original_pdf_location_verified'] is False for entry in self.entries))
        self.assertTrue(any(entry['source_locator']['precision'] == 'section-context' for entry in self.entries))
        for entry in self.entries:
            if entry['unit_type'].replace('_', '-') not in {'vocabulary', 'collocation'}:
                self.assertEqual(entry['expression_origin'], 'synthetic-expression')

    def test_private_vocabulary_not_duplicated_in_results(self):
        result = search(self.entries, limit=1)['entries'][0]
        self.assertNotIn('_vocabulary', result)
        self.assertIn('source_scope', result['source_articles'][0])

    def test_exact_function_unit_and_evidence_tier(self):
        entry = synthetic_entry()
        for field, fragment in [('function', 'compar'), ('unit', 'vocab'), ('evidence_tier', 'observ')]:
            self.assertEqual(search([entry], **{field: fragment})['matched_count'], 0)


class MetadataIntegrity(unittest.TestCase):
    setUp = test_retrieval.IsolatedMaintenance.setUp
    tearDown = test_retrieval.IsolatedMaintenance.tearDown

    def test_stale_vocabulary_fails_closed(self):
        path = self.skill / 'references/retrieval-vocabulary.json'
        path.write_text(path.read_text(encoding='utf-8') + '\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Stale language index'):
            load_index(self.skill)

    def test_stale_annotations_fail_closed(self):
        path = self.skill / 'references/retrieval-annotations.json'
        path.write_text(path.read_text(encoding='utf-8') + '\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Stale language index'):
            load_index(self.skill)


if __name__ == '__main__':
    unittest.main()
