import unittest
from codequest.discovering_planets import check_habitability

class TestDiscoveringPlanets(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            (13.81, True, True, 0.0167, "The planet is habitable."),
            (-12.51, True, True, 0.6124, "The planet is too cold."),
            (53.4, False, True, 0.5116, "The planet has no water."),
            (23.1, True, True, 0.7234, "The planet's orbit is not ideal.")
        ]

        for i, (temp, water, mag, ecc, expected) in enumerate(test_cases):
            with self.subTest(i=i):
                actual_result = check_habitability(temp, water, mag, ecc)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}"
                )

if __name__ == '__main__':
    unittest.main()