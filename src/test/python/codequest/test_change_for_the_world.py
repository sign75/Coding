import unittest
from codequest.change_for_the_world import calculate_change

class TestChangeForTheWorld(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            (
                "$3.87",
                [
                    "$3.87",
                    "Quarters=15",
                    "Dimes=1",
                    "Nickels=0",
                    "Pennies=2"
                ]
            ),
            (
                "$2.74",
                [
                    "$2.74",
                    "Quarters=10",
                    "Dimes=2",
                    "Nickels=0",
                    "Pennies=4"
                ]
            ),
            (
                "$14.84",
                [
                    "$14.84",
                    "Quarters=59",
                    "Dimes=0",
                    "Nickels=1",
                    "Pennies=4"
                ]
            ),
            (
                "$0.76",
                [
                    "$0.76",
                    "Quarters=3",
                    "Dimes=0",
                    "Nickels=0",
                    "Pennies=1"
                ]
            )
        ]

        for i, (amount_str, expected) in enumerate(test_cases):
            with self.subTest(i=i, amount_str=amount_str):
                actual_result = calculate_change(amount_str)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input '{amount_str}'"
                )

if __name__ == '__main__':
    unittest.main()
