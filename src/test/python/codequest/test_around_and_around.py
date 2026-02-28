import unittest
from codequest.around_and_around import calculate_circumference

class TestAroundAndAround(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            (160, 41080.3),
            (200, 41331.6),
            (265, 41740.0)
        ]

        for i, (altitude, expected) in enumerate(test_cases):
            with self.subTest(i=i, altitude=altitude):
                actual_result = calculate_circumference(altitude)
                self.assertIsNotNone(actual_result, msg=f"calculate_circumference returned None; implement the function.")
                # Allow small floating point error, though rounding should match exactly
                self.assertAlmostEqual(
                    actual_result, 
                    expected, 
                    places=1,
                    msg=f"Failed on case {i+1}: Input {altitude} -> Expected {expected}, got {actual_result}"
                )

if __name__ == '__main__':
    unittest.main()