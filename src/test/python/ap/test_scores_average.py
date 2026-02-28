import unittest
from ap.scores_average import scores_average

class TestScoresAverage(unittest.TestCase):
    def test_scores_average(self):
        self.assertEqual(scores_average([2, 2, 4, 4]), 4)
        self.assertEqual(scores_average([4, 4, 4, 2, 2, 2]), 4)
        self.assertEqual(scores_average([3, 4, 5, 1, 2, 3]), 4)
        self.assertEqual(scores_average([1, 2, 3, 4]), 3)
        self.assertEqual(scores_average([10, 20, 30, 40]), 35)
        self.assertEqual(scores_average([5, 4, 5, 6, 2, 1, 2, 3]), 5)

if __name__ == "__main__":
    unittest.main()
