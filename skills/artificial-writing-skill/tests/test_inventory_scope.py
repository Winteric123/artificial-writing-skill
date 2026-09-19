import copy
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

from build_library_index import group_counts, journal_year_counts


class InventoryScope(unittest.TestCase):
    def setUp(self):
        self.rows = [
            dict(journal='CCR', year='2025', eligibility='included', reading_stage='main_text_deep_read_complete'),
            dict(journal='CCR', year='2025', eligibility='included', reading_stage='indexed'),
            dict(journal='CCR', year='2025', eligibility='excluded', reading_stage='indexed'),
            dict(journal='JTO', year='2025', eligibility='included', reading_stage='main_text_deep_read_complete'),
            dict(journal='CCR', year='2026', eligibility='included', reading_stage='main_text_deep_read_complete'),
        ]

    def test_cross_journal_year_is_not_single_journal_year(self):
        all_2025 = group_counts([row for row in self.rows if row['year'] == '2025'])
        grouped = journal_year_counts(self.rows)
        self.assertEqual(all_2025, dict(registered=4, included=3, complete=2, incomplete=1, excluded=1))
        self.assertEqual(grouped['CCR']['2025'], dict(registered=3, included=2, complete=1, incomplete=1, excluded=1))
        self.assertEqual(grouped['JTO']['2025']['complete'], 1)
        self.assertEqual(grouped['CCR']['2026']['complete'], 1)
        for field in all_2025:
            self.assertEqual(all_2025[field], sum(years['2025'][field] for years in grouped.values()))

    def test_excluded_rows_are_not_pending_or_complete(self):
        rows = [dict(journal='CCR', year='2025', eligibility='excluded', reading_stage='main_text_deep_read_complete')]
        self.assertEqual(group_counts(rows), dict(registered=1, included=0, complete=0, incomplete=0, excluded=1))

    def test_summary_does_not_change_reading_records(self):
        before = copy.deepcopy(self.rows)
        journal_year_counts(self.rows)
        self.assertEqual(self.rows, before)
        self.assertEqual(journal_year_counts([]), {})
        self.assertEqual(group_counts([]), dict(registered=0, included=0, complete=0, incomplete=0, excluded=0))


if __name__ == '__main__':
    unittest.main()
