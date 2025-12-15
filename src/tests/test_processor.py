import unittest
from pathlib import Path

from processor import ProcessorData

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT.parent / "data"


class ProcessorDataTests(unittest.TestCase):
    def test_compute_legislator_stats_counts_support_and_oppose(self):
        processor = ProcessorData()
        processor.get_legislators(str(DATA_DIR / "legislators.csv"))
        processor.get_vote_results(str(DATA_DIR / "vote_results.csv"))

        stats = processor.compute_legislator_stats()

        self.assertEqual(stats[1269767], {"supported": 1, "opposed": 1})
        self.assertEqual(stats[904789], {"supported": 1, "opposed": 1})

    def test_compute_bill_stats_counts_supporters_and_opposers(self):
        processor = ProcessorData()
        processor.get_bills(str(DATA_DIR / "bills.csv"))
        processor.get_votes(str(DATA_DIR / "votes.csv"))
        processor.get_vote_results(str(DATA_DIR / "vote_results.csv"))

        stats = processor.compute_bill_stats()

        self.assertEqual(
            stats[2952375],
            {"supporters": 6, "opposers": 13},
        )
        self.assertEqual(
            stats[2900994],
            {"supporters": 13, "opposers": 6},
        )

    def test_get_bills_handles_missing_primary_sponsor(self):
        processor = ProcessorData()
        processor.get_bills(str(DATA_DIR / "bills.csv"))

        self.assertTrue(
            all(info["primary_sponsor"] is None for info in processor.bills.values())
        )
