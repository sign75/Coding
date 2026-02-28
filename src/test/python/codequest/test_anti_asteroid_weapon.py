import unittest
from codequest.anti_asteroid_weapon import sort_asteroids

class TestAntiAsteroidWeapon(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            (
                [(2, 1), (1, 1), (5, 5)], 
                [(1, 1), (2, 1), (5, 5)]
            ),
            (
                [(2, 2), (1, 7), (-1, 0), (1, 1)], 
                [(-1, 0), (1, 1), (2, 2), (1, 7)]
            )
        ]

        for i, (input_asteroids, expected_asteroids) in enumerate(test_cases):
            with self.subTest(i=i):
                actual_result = sort_asteroids(input_asteroids)
                self.assertEqual(
                    actual_result, 
                    expected_asteroids, 
                    f"Failed on case {i+1}: Input {input_asteroids} -> Expected {expected_asteroids}, got {actual_result}"
                )

if __name__ == '__main__':
    unittest.main()