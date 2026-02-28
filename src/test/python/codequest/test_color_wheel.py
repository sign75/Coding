import unittest
from codequest.color_wheel import get_color_mix

class TestColorWheel(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            ("violet", "In order to make violet, blue and red must be mixed."),
            ("blue-green", "In order to make blue-green, blue and yellow must be mixed."),
            ("yellow", "No colors need to be mixed to make yellow."),
            ("orange", "In order to make orange, red and yellow must be mixed.")
        ]

        for i, (color, expected) in enumerate(test_cases):
            with self.subTest(i=i, color=color):
                actual_result = get_color_mix(color)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input '{color}'"
                )

if __name__ == '__main__':
    unittest.main()
