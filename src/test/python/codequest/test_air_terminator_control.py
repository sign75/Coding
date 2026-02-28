import unittest
from codequest.air_terminator_control import assess_threat_level

class TestAirTerminatorControl(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            (
                True,
                ["12:00", "12:15", "12:30", "12:45", "13:00", "13:15"],
                "NONE"
            ),
            (
                False,
                ["12:00", "12:15", "12:30", "12:45", "13:00", "13:15"],
                "LOW"
            ),
            (
                False,
                ["09:15", "09:30", "09:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "15:30", "15:45", "16:00"],
                "MEDIUM"
            ),
            (
                False,
                ["07:15", "07:45", "08:30", "09:00", "11:00", "12:15", "13:45", "14:30", "15:00"],
                "HIGH"
            )
        ]

        for i, (is_friendly, times, expected) in enumerate(test_cases):
            with self.subTest(i=i):
                actual_result = assess_threat_level(is_friendly, times)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}"
                )

if __name__ == '__main__':
    unittest.main()