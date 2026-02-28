import unittest
from codequest.caught_speeding import calculate_ticket

class TestCaughtSpeeding(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            (60, False, "no ticket"),
            (82, False, "big ticket"),
            (83, True, "small ticket")
        ]

        for i, (speed, is_bday, expected) in enumerate(test_cases):
            with self.subTest(i=i, speed=speed, is_bday=is_bday):
                actual_result = calculate_ticket(speed, is_bday)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input({speed}, {is_bday}) -> Expected {expected}, got {actual_result}"
                )

if __name__ == '__main__':
    unittest.main()
