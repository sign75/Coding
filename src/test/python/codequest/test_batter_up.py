import unittest
from codequest.batter_up import calculate_slugging_percentage

class TestBatterUp(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            ("Moreland", ["K", "2B", "1B", "HR"], 1.750),
            ("Andrus", ["BB", "BB", "2B", "K"], 1.000),
            ("Chirinos", ["1B", "1B", "3B"], 1.667),
            ("Odor", ["1B", "K", "3B"], 1.333)
        ]

        for i, (name, stats, expected) in enumerate(test_cases):
            with self.subTest(i=i, name=name):
                actual_result = calculate_slugging_percentage(name, stats)
                self.assertIsNotNone(actual_result, msg=f"calculate_slugging_percentage returned None; implement the function.")
                self.assertAlmostEqual(
                    actual_result, 
                    expected, 
                    places=3,
                    msg=f"Failed on case {i+1}: Input {name}:{stats} -> Expected {expected}, got {actual_result}"
                )

if __name__ == '__main__':
    unittest.main()