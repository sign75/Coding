import unittest
from codequest.color_coding import find_color

class TestColorCoding(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            ("This is a line of text that contains no colors", "no color found"),
            ("blue is my favorite color", "blue"),
            ("I do not like the color red", "red"),
            ("This is a secret message, code red", "red"),
            ("A color that exists is BLUE!", "no color found")
        ]

        for i, (text, expected) in enumerate(test_cases):
            with self.subTest(i=i, text=text):
                actual_result = find_color(text)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input '{text}'"
                )

if __name__ == '__main__':
    unittest.main()
