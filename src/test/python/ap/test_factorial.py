import unittest
from ap.factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(12), 479001600)

if __name__ == "__main__":
    unittest.main()
