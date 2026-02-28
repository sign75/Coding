import unittest
from codequest.animal_farm import count_legs

class TestAnimalFarm(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            (2, 3, 5, 36),
            (2, 2, 2, 20),
            (3, 2, 4, 30)
        ]

        for i, (t, g, h, expected) in enumerate(test_cases):
            with self.subTest(i=i, t=t, g=g, h=h):
                actual_result = count_legs(t, g, h)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input({t}, {g}, {h}) -> Expected {expected}, got {actual_result}"
                )

if __name__ == '__main__':
    unittest.main()