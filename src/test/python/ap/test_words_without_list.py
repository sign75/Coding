import unittest
from ap.words_without_list import words_without_list

class TestWordsWithoutList(unittest.TestCase):
    """
    Unit tests for the words_without_list function.
    """
    def test_words_without_list(self):
        # This single test method runs multiple assertions for words_without_list
        self.assertEqual(words_without_list(["a", "bb", "b", "ccc"], 1), ["bb", "ccc"])
        self.assertEqual(words_without_list(["a", "bb", "b", "ccc"], 3), ["a", "bb", "b"])
        self.assertEqual(words_without_list(["a", "bb", "b", "ccc"], 4), ["a", "bb", "b", "ccc"])
        self.assertEqual(words_without_list(["xx", "yyy", "x", "yy", "z"], 1), ["xx", "yyy", "yy"])
        self.assertEqual(words_without_list(["xx", "yyy", "x", "yy", "z"], 2), ["yyy", "x", "z"])

if __name__ == "__main__":
    unittest.main()
