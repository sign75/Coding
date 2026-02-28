import unittest
from codequest.detecting_multipaction import detect_multipaction

class TestDetectingMultipaction(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            (
                [0.3, 0.61, 0.4, 0.15, 0.81, 0.47, 0.98],
                [0.2, 0.64, 0.7, 0.36, 0.63, 0.71, 0.09],
                "2 multipaction events were detected at time indices: 1 4."
            ),
            (
                [0.45, 0.53, 0.59, 0.13, 0.21, 0.78, 0.34, 0.78, 0.91],
                [0.87, 0.71, 0.32, 0.33, 0.58, 0.61, 0.79, 0.86, 0.62],
                "A multipaction event was detected at time index 5."
            ),
            (
                [0.5, 0.71, 0.42, 0.36, 0.49, 0.82, 0.6, 0.21],
                [0.67, 0.41, 0.76, 0.83, 0.85, 0.12, 0.51, 0.92],
                "No multipaction events detected."
            )
        ]

        for i, (pn, th, expected) in enumerate(test_cases):
            with self.subTest(i=i):
                actual_result = detect_multipaction(pn, th)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}"
                )

if __name__ == '__main__':
    unittest.main()