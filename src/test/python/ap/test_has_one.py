import unittest
from ap.has_one import has_one

class TestHasOne(unittest.TestCase):
    def test_has_one(self):
        self.assertTrue(has_one(10))
        self.assertFalse(has_one(22))
        self.assertFalse(has_one(220))
        self.assertTrue(has_one(1))
        self.assertFalse(has_one(2))
        self.assertTrue(has_one(212))
        self.assertTrue(has_one(211112))
        self.assertTrue(has_one(121121))
        self.assertFalse(has_one(222222))
        self.assertTrue(has_one(56156))
        self.assertFalse(has_one(56556))

if __name__ == "__main__":
    unittest.main()
