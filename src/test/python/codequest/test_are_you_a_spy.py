import unittest
from codequest.are_you_a_spy import check_spy

class TestAreYouASpy(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            ("Good evening.", "Hello there.", "You're not a secret agent!"),
            ("Dogs can't fly without umbrellas.", "Bread is a stale food.", "That's my secret contact!"),
            ("It's nice to meet you, George.", "Greetings to you too, Tim!", "That's my secret contact!"),
            ("It's raining.", "I sang in a train.", "That's my secret contact!")
        ]

        for i, (p1, p2, expected) in enumerate(test_cases):
            with self.subTest(i=i, p1=p1, p2=p2):
                actual_result = check_spy(p1, p2)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input '{p1}|{p2}' -> Expected '{expected}', got '{actual_result}'"
                )

if __name__ == '__main__':
    unittest.main()