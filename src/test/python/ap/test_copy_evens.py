import unittest
from ap.copy_evens import copy_evens

class TestCopyEvens(unittest.TestCase):
    def test_copy_evens(self):
        self.assertEqual(copy_evens([3, 2, 4, 5, 8], 2), [2, 4])
        self.assertEqual(copy_evens([3, 2, 4, 5, 8], 3), [2, 4, 8])
        self.assertEqual(copy_evens([6, 1, 2, 4, 5, 8], 3), [6, 2, 4])
        self.assertEqual(copy_evens([6, 1, 2, 4, 5, 8], 4), [6, 2, 4, 8])
        self.assertEqual(copy_evens([3, 1, 4, 1, 5], 1), [4])
        self.assertEqual(copy_evens([2], 1), [2])
        self.assertEqual(copy_evens([6, 2, 4, 8], 2), [6, 2])
        self.assertEqual(copy_evens([6, 2, 4, 8], 3), [6, 2, 4])
        self.assertEqual(copy_evens([6, 2, 4, 8], 4), [6, 2, 4, 8])
        self.assertEqual(copy_evens([1, 8, 4], 1), [8])
        self.assertEqual(copy_evens([1, 8, 4], 2), [8, 4])
        self.assertEqual(copy_evens([2, 8, 4], 2), [2, 8])

if __name__ == "__main__":
    unittest.main()
