import unittest
from codequest.by_the_book import check_isbn

class TestByTheBook(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            ("0306406152", "VALID"),
            ("0306401652", "INVALID"),
            ("080442957X", "VALID")
        ]

        for i, (isbn, expected) in enumerate(test_cases):
            with self.subTest(i=i, isbn=isbn):
                actual_result = check_isbn(isbn)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input '{isbn}' -> Expected {expected}, got {actual_result}"
                )

if __name__ == '__main__':
    unittest.main()
