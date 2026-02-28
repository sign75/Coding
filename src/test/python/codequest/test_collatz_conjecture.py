import unittest
from codequest.collatz_conjecture import collatz_length

class TestCollatzConjecture(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            (12, "12:10"),
            (1024, "1024:11"),
            (100, "100:26"),
            (4, "4:3"),
            (12345, "12345:51")
        ]

        for i, (n, expected) in enumerate(test_cases):
            with self.subTest(i=i, n=n):
                actual_result = collatz_length(n)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input {n}"
                )

if __name__ == '__main__':
    unittest.main()
