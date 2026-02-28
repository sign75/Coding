import unittest
from codequest.ai_robot import simulate_robot

class TestAIRobot(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            (0, 0, 'N', 'RAAL', "2 0 N"),
            (7, 3, 'N', 'RAALAL', "9 4 W")
        ]

        for i, (x, y, facing, commands, expected) in enumerate(test_cases):
            with self.subTest(i=i, commands=commands):
                actual_result = simulate_robot(x, y, facing, commands)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Start({x},{y},{facing}) Cmds({commands}) -> Expected '{expected}', got '{actual_result}'"
                )

if __name__ == '__main__':
    unittest.main()