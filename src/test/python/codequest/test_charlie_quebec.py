import unittest
from codequest.charlie_quebec import translate_to_icao

class TestCharlieQuebec(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            ("Code Quest", "Charlie-Oscar-Delta-Echo Quebec-Uniform-Echo-Sierra-Tango"),
            ("Rocks", "Romeo-Oscar-Charlie-Kilo-Sierra"),
            ("Lockheed", "Lima-Oscar-Charlie-Kilo-Hotel-Echo-Echo-Delta")
        ]

        for i, (text, expected) in enumerate(test_cases):
            with self.subTest(i=i, text=text):
                actual_result = translate_to_icao(text)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}: Input '{text}'"
                )

if __name__ == '__main__':
    unittest.main()
