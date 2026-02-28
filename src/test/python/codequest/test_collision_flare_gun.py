import unittest
from codequest.collision_flare_gun import calculate_final_velocity

class TestCollisionFlareGun(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            (1.0, 2.0, 3.0, 4.0, "2.33"),
            (1.0, 2.5, 1.2, 2.5, "1.10"),
            (1.1, 2.2, 3.3, 4.4, "2.57")
        ]

        for i, (v1, m1, v2, m2, expected) in enumerate(test_cases):
            with self.subTest(i=i, v1=v1, m1=m1, v2=v2, m2=m2):
                actual_result = calculate_final_velocity(v1, m1, v2, m2)
                
                # if the user returns a float, we format it to match the expected string
                if isinstance(actual_result, float) or isinstance(actual_result, int):
                    actual_result = f"{actual_result:.2f}"
                    
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}"
                )

if __name__ == '__main__':
    unittest.main()
