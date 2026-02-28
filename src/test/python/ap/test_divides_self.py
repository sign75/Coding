import unittest
from ap.divides_self import divides_self

class TestDividesSelf(unittest.TestCase):
    def test_divides_self(self):
        self.assertTrue(divides_self(128))
        self.assertTrue(divides_self(12))
        self.assertFalse(divides_self(120))
        self.assertTrue(divides_self(13))
        self.assertTrue(divides_self(22))
        self.assertFalse(divides_self(100))
        self.assertFalse(divides_self(105))
        self.assertFalse(divides_self(42))
        self.assertTrue(divides_self(212))
        self.assertFalse(divides_self(213))
        self.assertTrue(divides_self(162))

if __name__ == "__main__":
    unittest.main()
