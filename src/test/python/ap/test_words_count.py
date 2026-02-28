import unittest
from ap.words_count import words_count

class TestWordsCount(unittest.TestCase):
    def test_words_count(self):
        self.assertEqual(words_count(["a", "bb", "b", "ccc"], 1), 2)
        self.assertEqual(words_count(["a", "bb", "b", "ccc"], 3), 1)
        self.assertEqual(words_count(["a", "bb", "b", "ccc"], 4), 0)
        self.assertEqual(words_count(["xx", "yyy", "x", "yy", "z"], 1), 2)
        self.assertEqual(words_count(["xx", "yyy", "x", "yy", "z"], 2), 2)
        self.assertEqual(words_count(["xx", "yyy", "x", "yy", "z"], 3), 1)

if __name__ == "__main__":
    unittest.main()
