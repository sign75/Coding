import unittest
from codequest.anagram_checker import check_anagram

class TestAnagramChecker(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            ("STOP|POTS", "STOP|POTS = ANAGRAM"),
            ("ADMIRER|MARRIED", "ADMIRER|MARRIED = ANAGRAM"),
            ("CAT|DOG", "CAT|DOG = NOT AN ANAGRAM"),
            ("CREATIVE|REACTIVE", "CREATIVE|REACTIVE = ANAGRAM"),
            ("LISTEN|SILENT", "LISTEN|SILENT = ANAGRAM"),
            ("ANGERED|ENRAGED", "ANGERED|ENRAGED = ANAGRAM"),
            ("ELVIS|LIVES", "ELVIS|LIVES = ANAGRAM"),
            ("RUN|FLY", "RUN|FLY = NOT AN ANAGRAM"),
            ("DEDUCTIONS|DISCOUNTED", "DEDUCTIONS|DISCOUNTED = ANAGRAM"),
            ("PATERNAL|PARENTAL", "PATERNAL|PARENTAL = ANAGRAM"),
            ("MIKE|MIKE", "MIKE|MIKE = NOT AN ANAGRAM")
        ]

        for i, (line, expected) in enumerate(test_cases):
            with self.subTest(i=i, line=line):
                actual_result = check_anagram(line)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input '{line}' -> Expected '{expected}', got '{actual_result}'"
                )

if __name__ == '__main__':
    unittest.main()