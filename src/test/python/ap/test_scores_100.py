import unittest
from ap.scores_100 import scores_100

class TestScores100(unittest.TestCase):
    def test_scores_100(self):
        self.assertTrue(scores_100([1, 100, 100]))             # -> True
        self.assertFalse(scores_100([1, 100, 99, 100]))        # -> False
        self.assertTrue(scores_100([100, 1, 100, 100]))        # -> True
        self.assertFalse(scores_100([100, 1, 100, 1]))         # -> False
        self.assertFalse(scores_100([1, 2, 3, 4, 5]))          # -> False
        self.assertFalse(scores_100([1, 2, 100, 4, 5]))        # -> False

if __name__ == "__main__":
    unittest.main()
