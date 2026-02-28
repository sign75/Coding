import unittest
from codequest.count_your_abcs import count_decal_sets

class TestCountYourABCs(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            ("FUTURE MARATHONER LIVES HERE", 5),
            ("CODE QUEST IS FUN", 2),
            ("LOCKHEED MARTIN CORPORATION", 4),
            ("HELLO WORLD", 3)
        ]

        for i, (phrase, expected) in enumerate(test_cases):
            with self.subTest(i=i, phrase=phrase):
                actual_result = count_decal_sets(phrase)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input '{phrase}'"
                )

if __name__ == '__main__':
    unittest.main()
