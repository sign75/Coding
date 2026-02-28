import unittest
from codequest.adfgvx import decrypt_adfgvx

class TestADFGVX(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            (
                ["qct1o8", "w0bdzk", "4hpm3j", "gs67ev", "l92fxn", "yau5ir"],
                "MARTIN",
                "DDAGAVVXGFAAVAGFGDFVVFDDFV",
                "codequest2022"
            ),
            (
                ["1c62et", "iljvm7", "d8rgko", "suabph", "9y354z", "fnxq0w"],
                "CODE",
                "AFFDVGVDAFXXFFFGGGVFGVDXDGAAXGDAXD",
                "cryptographyisfun"
            ),
            (
                ["3kcdqg", "5iub1f", "92me6a", "h0l7ry", "xto84s", "znjwvp"],
                "QUEST",
                "GVADDXDDDVAVFVXGFFGADAFFVXGVDVDVVGXDDGAVFGGFXVXG",
                "thisiscodequests10thyear"
            )
        ]

        for i, (grid, keyword, msg, expected) in enumerate(test_cases):
            with self.subTest(i=i):
                actual_result = decrypt_adfgvx(grid, keyword, msg)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}"
                )

if __name__ == '__main__':
    unittest.main()