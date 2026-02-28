#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/a_matter_of_0s_and_1s.py

import sys

def solve_binary_sudoku(grid):
    """
    Problem Background:
    You've probably heard of Sudoku puzzles, and may have even written a program to attempt to solve them. 
    A slightly simpler version uses only 0's and 1's, and so is called Binary Sudoku.

    As in Sudoku, the puzzle is made up of a grid of numbers in a square pattern. The challenge is to complete 
    the grid in a way that fulfills a simple set of rules:
    - Each box must contain a 0 or a 1.
    - The same number may not appear more than twice consecutively within any row or column; for example, 
      you may see 010 or 0110, but 01110 is illegal, as three 1's appear together without a 0 to separate them.
    - Each row and column should contain an equal number of 0's and 1's.
    - Each row is unique, compared to other rows.
    - Each column is unique, compared to other columns.

    As with Sudoku, Binary Sudoku boils down to a logic problem; using the rules above to make deductions 
    about empty cells. Your task is to write a program that utilizes a series of deductions to determine how 
    complex a particular puzzle is.

    Problem Description:
    There are advanced methods a computer program can use to solve problems, but the aim here is to determine 
    whether the presented problem can be solved by people. Your program should use the methods of deduction 
    outlined below to determine if the puzzle can be solved with those methods alone, and if so, if it can be 
    solved entirely with simple logic or if a degree of deduction is required. Do not use any other methods of 
    deduction when attempting to solve these puzzles.

    Simple Logic:
    There are three scenarios which, based on the rules outlined above, allow you to make immediate decisions 
    regarding which number to place in a cell.
    
    1. Since a number cannot appear three or more times consecutively, any instance of doubled numbers in a 
       row or column must have the opposite number on either side.
       
       |   | 1 | 1 |   |    ->    | 0 | 1 | 1 | 0 |
       | 0 | 0 |   |   |    ->    | 0 | 0 | 1 |   |

    2. Likewise, any time there is a single space between two of the same number, that space must be filled 
       by the opposite number:
       
       | 0 |   | 0 |    ->    | 0 | 1 | 0 |
       | 1 |   | 1 |    ->    | 1 | 0 | 1 |

    3. Finally, since puzzles are square and each row and column must contain an equal number of 0's and 1's, 
       the number of 1's (and 0's) in each row or column must be equal to half the dimensions of the puzzle. 
       In a puzzle measuring eight cells to a side, a row or column must contain four 0's and four 1's. A row 
       or column that already contains the required amount of one number must fill its remaining cells with the 
       opposite number.
       
       |   | 1 |   | 0 | 1 | 1 |    ->    | 0 | 1 | 0 | 0 | 1 | 1 |

    Complex Logic:
    If the three methods above are insufficient to solve a problem, some more advanced methods may be required.
    
    1. Each row and column must be unique. If a row (or column) with two incomplete cells is otherwise identical 
       to an already-completed row (or column), the incomplete cells must be filled with the opposites of their 
       counterparts in the complete row (or column).
       
       | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |    ->    | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
       | 0 | 1 |   |   | 1 | 0 | 1 | 0 |    ->    | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |

    2. Finally, you may be able to identify cases where a cell cannot legally contain a particular value. If a 
       row or column has all but one of its required number of 0's or 1's, you can put the last remaining number 
       in any open space to see if it is a valid move. In the example below, the row already has three of the 
       four required 0's in place. Placing the final 0 in the rightmost cell is not possible, as filling the 
       remaining cells with 1's would cause three 1's to appear in a row. Therefore, the rightmost cell must 
       be a 1.
       
       | 0 | 0 | 1 | 0 | 1 |   |   |    ->    | 0 | 0 | 1 | 0 | 1 |   | 1 |

    Input Format:
    The first line contains a positive integer representing the number of test cases.
    Each test case includes:
    - A positive even integer, N, representing the length of one side of the puzzle.
    - N lines, each containing N characters (0, 1, or .)

    Output Format:
    If a solution was found:
    - N lines of the solved puzzle
    - "Solved with simple logic" OR "Solved with complex logic"
    If not solved:
    - "Unable to solve with the provided logic"
    """
    pass

def get_resource(relative_path):
    """
    To import a text file as a string relative to the script's location, 
    the most stable method involves using the __file__ attribute. 

    This ensures that the script finds the resource regardless of where 
    the user is in the terminal when they execute the command.
    """
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_dir, relative_path)
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: The file at {full_path} was not found."

if __name__ == '__main__':
    # lines = sys.stdin.read().splitlines()   # for online testing
    lines = get_resource("a_matter_of_0s_and_1s.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
    
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            n = int(next(iterator).strip())
            grid = []
            for _ in range(n):
                grid.append(next(iterator).strip())
            
            result = solve_binary_sudoku(grid)
            if result:
                for line in result:
                    print(line)
    except StopIteration:
        pass