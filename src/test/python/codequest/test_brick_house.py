import unittest
from codequest.brick_house import can_build_wall

class TestBrickHouse(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            (3, 1, 8, True),
            (3, 1, 9, False),
            (3, 2, 10, True)
        ]

        for i, (small, large, target, expected) in enumerate(test_cases):
            with self.subTest(i=i, small=small, large=large, target=target):
                actual_result = can_build_wall(small, large, target)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input({small}, {large}, {target}) -> Expected {expected}, got {actual_result}"
                )

if __name__ == '__main__':
    unittest.main()