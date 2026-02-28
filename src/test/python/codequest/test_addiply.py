import unittest
from codequest.addiply import addiply

class TestAddiply(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            (2, 2, "4 4"),
            (5, 4, "9 20"),
            (3, 8, "11 24")
        ]

        for i, (a, b, expected) in enumerate(test_cases):
            with self.subTest(i=i, a=a, b=b):
                actual_result = addiply(a, b)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input({a}, {b}) -> Expected '{expected}', got '{actual_result}'"
                )

if __name__ == '__main__':
    unittest.main()