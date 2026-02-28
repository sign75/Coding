import unittest
from codequest.aeiou import count_vowels

class TestAEIOU(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            ("code quest is fun", 6),
            ("good luck programming today", 8),
            ("queueing has five vowels in a row", 13)
        ]

        for i, (text, expected) in enumerate(test_cases):
            with self.subTest(i=i, text=text):
                actual_result = count_vowels(text)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input '{text}' -> Expected {expected}, got {actual_result}"
                )

if __name__ == '__main__':
    unittest.main()