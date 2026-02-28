import unittest
from codequest.autocorrect import autocorrect

class TestAutocorrect(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            (
                ["computer", "mouse", "program"],
                ["konpuder", "house", "compoooo", "anagram", "oeifeln"],
                ["computer", "mouse", "computer", "program", "program"]
            )
        ]

        for i, (dict_words, misspelled, expected) in enumerate(test_cases):
            with self.subTest(i=i):
                actual_result = autocorrect(dict_words, misspelled)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}"
                )

if __name__ == '__main__':
    unittest.main()