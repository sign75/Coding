import unittest
from ap.scores_increasing import scores_increasing

class TestScoresIncreasing(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(scores_increasing([1, 3, 4]))            # -> True
        self.assertFalse(scores_increasing([1, 3, 2]))           # -> False
        self.assertTrue(scores_increasing([1, 1, 4]))            # -> True
        self.assertTrue(scores_increasing([1, 1, 2, 4, 4, 7]))   # -> True
        self.assertFalse(scores_increasing([1, 1, 2, 4, 3, 7]))  # -> False
        self.assertTrue(scores_increasing([-5, 4, 11]))          # -> True

if __name__ == "__main__":
    unittest.main()
