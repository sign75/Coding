import unittest
from ap.scores_clump import scores_clump

class TestScoresClump(unittest.TestCase):
    def test_scores_clump(self):
        self.assertTrue(scores_clump([3, 4, 5]))           # -> True
        self.assertFalse(scores_clump([3, 4, 6]))          # -> False
        self.assertTrue(scores_clump([1, 3, 5, 5]))         # -> True
        self.assertTrue(scores_clump([2, 4, 5, 6]))         # -> True
        self.assertFalse(scores_clump([2, 4, 5, 7]))         # -> False
        self.assertTrue(scores_clump([2, 4, 4, 7]))         # -> True
        self.assertFalse(scores_clump([3, 3, 6, 7, 9]))      # -> False
        self.assertTrue(scores_clump([3, 3, 7, 7, 9]))       # -> True
        self.assertFalse(scores_clump([4, 5, 8]))            # -> False

if __name__ == "__main__":
    unittest.main()
