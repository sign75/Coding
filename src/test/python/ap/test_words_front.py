import unittest
from ap.words_front import words_front

class TestWordsFront(unittest.TestCase):
    """
    Unit tests for the words_front function.
    """
    def test_words_front(self):
        # This single test method runs multiple assertions for words_front
        self.assertEqual(words_front(["a", "b", "c", "d"], 1), ["a"])
        self.assertEqual(words_front(["a", "b", "c", "d"], 2), ["a", "b"])
        self.assertEqual(words_front(["a", "b", "c", "d"], 3), ["a", "b", "c"])
        self.assertEqual(words_front(["a", "b", "c", "d"], 4), ["a", "b", "c", "d"])
        self.assertEqual(words_front(["Hi", "There"], 1), ["Hi"])
        self.assertEqual(words_front(["Hi", "There"], 2), ["Hi", "There"])

if __name__ == "__main__":
    unittest.main()
