import unittest
from codequest.a_matter_of_0s_and_1s import solve_binary_sudoku

class TestAMatterOf0sAnd1s(unittest.TestCase):
    def test_sample_cases(self):
        # Hardcoded test cases based on 1.in and 1.ans
        test_cases = [
            (
                [
                    "0.1.",
                    "..1.",
                    "...0",
                    "0..."
                ],
                [
                    "0011",
                    "1010",
                    "1100",
                    "0101",
                    "Solved with simple logic"
                ]
            ),
            (
                [
                    "0..1",
                    "0...",
                    "...0",
                    "...1"
                ],
                [
                    "Unable to solve with the provided logic"
                ]
            ),
            (
                [
                    "......",
                    "..0..1",
                    "..11..",
                    "....0.",
                    ".0...1",
                    "0....0"
                ],
                [
                    "101001",
                    "010011",
                    "101100",
                    "110100",
                    "001011",
                    "010110",
                    "Solved with complex logic"
                ]
            )
        ]

        for i, (grid, expected) in enumerate(test_cases):
            with self.subTest(i=i):
                actual_result = solve_binary_sudoku(grid)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}"
                )

if __name__ == '__main__':
    unittest.main()