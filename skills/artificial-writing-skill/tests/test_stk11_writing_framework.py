import csv
import json
import re
import unittest
from pathlib import Path


class Stk11WritingFramework(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.references = Path(__file__).resolve().parents[1] / 'references'
        cls.mapping = json.loads((cls.references / 'stk11-writing-reference-map.json').read_text(encoding='utf-8'))
        cls.records = cls.mapping['records']
        with (cls.references / 'library-index.csv').open(encoding='utf-8-sig', newline='') as source:
            cls.library = {row['pmid']: row for row in csv.DictReader(source)}

    def test_unique_membership_and_source_identity(self):
        identifiers = [record['pmid'] for record in self.records]
        self.assertEqual(len(identifiers), len(set(identifiers)))
        for identifier in identifiers:
            with self.subTest(pmid=identifier):
                self.assertIn(identifier, self.library)
                self.assertEqual(self.library[identifier]['eligibility'], 'included')
                self.assertTrue(self.library[identifier]['title'])
                self.assertTrue(self.library[identifier]['journal'])
                self.assertTrue(self.library[identifier]['doi'])

    def test_core_priority_is_not_promoted_by_topic_support(self):
        priority = (self.references / self.mapping['core_authority']).read_text(encoding='utf-8-sig')
        highlighted = set(re.findall(r'^\| 1 \| [^|]+ \| \d{4} \| (\d{8}) \|', priority, re.M))
        mapped_core = {record['pmid'] for record in self.records if record['tier'] == 'core_highlight'}
        support = {record['pmid'] for record in self.records if record['tier'] == 'topic_support'}
        self.assertEqual(mapped_core, highlighted)
        self.assertFalse(highlighted & support)
        self.assertEqual(support, {'36775193', '36494075', '37806385', '39804166', '39545922', '42507545'})

    def test_cross_gene_set_preserves_copy_context_additions(self):
        cross_gene = {record['pmid'] for record in self.records if record['in_cross_gene_16']}
        self.assertEqual(len(cross_gene), 16)
        extra = {record['pmid'] for record in self.records} - cross_gene
        self.assertEqual(extra, {'39864548', '41870274', '42409117'})
        self.assertEqual(len(self.records), 19)

    def test_scoped_source_evidence_resolves_without_private_paths(self):
        for record in self.records:
            with self.subTest(pmid=record['pmid']):
                self.assertTrue(record['source_refs'])
                for relative in record['source_refs']:
                    self.assertFalse(Path(relative).is_absolute())
                    source = (self.references / relative).resolve()
                    self.assertTrue(source.is_relative_to(self.references.resolve()))
                    self.assertTrue(source.is_file())
                    self.assertIn(record['pmid'], source.read_text(encoding='utf-8-sig'))
        for field in ('guide', 'study_map', 'core_authority', 'identity_and_reading_authority'):
            self.assertTrue((self.references / self.mapping[field]).is_file())

    def test_modules_and_analogue_boundaries(self):
        allowed_modules = {'sequence_context', 'clinical_outcomes', 'functional_state', 'immune_mechanism', 'longitudinal', 'copy_number'}
        allowed_relations = {'direct_analysis', 'contextual_analysis', 'structural_analogue'}
        for record in self.records:
            self.assertIn(record['tier'], {'core_highlight', 'topic_support'})
            self.assertIn(record['stk11_relation'], allowed_relations)
            self.assertTrue(record['modules'])
            self.assertTrue(set(record['modules']) <= allowed_modules)
            self.assertNotIn('reading_stage', record)
            self.assertNotIn('review_status', record)
        by_pmid = {record['pmid']: record for record in self.records}
        self.assertEqual(by_pmid['42409117']['stk11_relation'], 'structural_analogue')
        self.assertEqual(by_pmid['37806385']['stk11_relation'], 'structural_analogue')
        self.assertIn('copy_number', by_pmid['42507545']['modules'])
        self.assertIn('sequence_context', by_pmid['42507545']['modules'])


if __name__ == '__main__':
    unittest.main()
