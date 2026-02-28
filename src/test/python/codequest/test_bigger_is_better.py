import unittest
from codequest.bigger_is_better import find_max_score

class TestBiggerIsBetter(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            ([1, 2, 3, 4], 4),
            ([30, 15, 20, 10], 30),
            ([55, 10, 45, 60, 15, 45, 25, 30], 60)
        ]

        for i, (scores, expected) in enumerate(test_cases):
            with self.subTest(i=i, scores=scores):
                actual_result = find_max_score(scores)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input {scores} -> Expected {expected}, got {actual_result}"
                )

if __name__ == '__main__':
    unittest.main()