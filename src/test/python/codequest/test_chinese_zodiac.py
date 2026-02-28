import unittest
from codequest.chinese_zodiac import get_zodiac

class TestChineseZodiac(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            (1984, "1984 Yang Wood Rat"),
            (2012, "2012 Yang Water Dragon"),
            (2020, "2020 Yang Metal Rat"),
            (2043, "2043 Yin Water Pig")
        ]

        for i, (year, expected) in enumerate(test_cases):
            with self.subTest(i=i, year=year):
                actual_result = get_zodiac(year)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input {year}"
                )

if __name__ == '__main__':
    unittest.main()
