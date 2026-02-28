import unittest
from ap.bunny_ears_2 import bunny_ears_2

class TestBunnyEars2(unittest.TestCase):
    def test_bunny_ears_2(self):
        self.assertEqual(bunny_ears_2(0), 0)
        self.assertEqual(bunny_ears_2(1), 2)
        self.assertEqual(bunny_ears_2(2), 5)
        self.assertEqual(bunny_ears_2(3), 7)
        self.assertEqual(bunny_ears_2(4), 10)
        self.assertEqual(bunny_ears_2(5), 12)
        self.assertEqual(bunny_ears_2(6), 15)
        self.assertEqual(bunny_ears_2(10), 25)

if __name__ == "__main__":
    unittest.main()
