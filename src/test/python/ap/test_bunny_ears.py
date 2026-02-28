import unittest
from ap.bunny_ears import bunny_ears

class TestBunnyEars(unittest.TestCase):
    def test_bunny_ears(self):
        self.assertEqual(bunny_ears(0), 0)
        self.assertEqual(bunny_ears(1), 2)
        self.assertEqual(bunny_ears(2), 4)
        self.assertEqual(bunny_ears(3), 6)
        self.assertEqual(bunny_ears(4), 8)
        self.assertEqual(bunny_ears(5), 10)
        self.assertEqual(bunny_ears(12), 24)
        self.assertEqual(bunny_ears(50), 100)
        self.assertEqual(bunny_ears(234), 468)

if __name__ == "__main__":
    unittest.main()
