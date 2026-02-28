#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/adfgvx.py

import sys

def decrypt_adfgvx(grid, keyword, message):
    """
    Problem Background:
    In 1894, an Italian physicist named Guglielmo Marconi discovered a world-changing new technology: the ability to 
    communicate wirelessly through the use of radio waves. This revolutionized communication but also posed a severe 
    security risk during wartime, as enemies could intercept signals.
    Near the end of World War I, Germany believed they'd found a solution to this problem: the ADFGVX cipher, which 
    employed both substitution and transposition. The encrypted message uses only the letters A, D, F, G, V, and X, 
    chosen because they are easily distinguishable from each other in Morse Code.

    Problem Description:
    The ADFGVX cipher works in two steps:
    
    1. Substitution Step:
    A 6-by-6 grid is populated with the digits 0 through 9 and the 26 letters of the English alphabet in random order. 
    Each row and column of the grid is associated with one of the letters A, D, F, G, V, or X.
    
    Substitution Grid Example:
        | A | D | F | G | V | X
      --+---+---+---+---+---+---
      A | q | c | t | 1 | o | 8
      D | w | 0 | b | d | z | k
      F | 4 | h | p | m | 3 | j
      G | g | s | 6 | 7 | e | v
      V | l | 9 | 2 | f | x | n
      X | y | a | u | 5 | i | r
    
    Each letter of the message is located within the grid and replaced with a pair of letters: the labels for that 
    cell's row and column, respectively. For example, 'c' becomes 'AD' because 'c' appears in row A and column D. 
    Thus, "code quest 2022" would be encoded as: "AD AV DG GV AA XF GV GD AF VF DD VF VF".

    2. Transposition Step:
    A new grid is created with the top row filled in with the letters of a keyword. The rest of the grid is populated 
    by listing the individual letters of the semi-enciphered message from left to right, top to bottom:

    Transposition Grid (Keyword: MARTIN):
      | M | A | R | T | I | N |
      |---|---|---|---|---|---|
      | A | D | A | V | D | G |
      | G | V | A | A | X | F |
      | G | V | G | D | A | F |
      | V | F | D | D | V | F |
      | V | F |   |   |   |   |

    Once filled, the columns are reordered so the keyword letters are in alphabetical order (A I M N R T). 
    The final encrypted message is then read from left to right, top to bottom of this newly sorted grid.
    
    Sorted Grid (Keyword Sorted: A I M N R T):
      | A | I | M | N | R | T |
      |---|---|---|---|---|---|
      | D | D | A | G | A | V |
      | V | X | G | F | A | A |
      | V | A | G | F | G | D |
      | F | V | V | F | D | D |
      | F |   | V |   |   |   |

    Reading left to right, top to bottom, the resulting encrypted message is:
    "DDAGAVVXGFAAVAGFGDFVVFDDFV"

    For this problem, your team will need to decrypt messages encoded using the ADFGVX cipher by reversing this 
    entire process.

    Input Format:
    - 6 lines of 6 characters each representing the substitution grid.
    - 1 line containing a single uppercase keyword (no duplicate letters).
    - 1 line containing the encoded message (only A, D, F, G, V, X).

    Output Format:
    - Return a string containing the decrypted plaintext message in lowercase letters and numbers (no spaces).
    """
    print(f"grid: {grid}")
    print(f"keyword: {keyword}")
    print(f"message: {message}")
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
    lines = get_resource("adfgvx.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            grid = []
            for _ in range(6):
                grid.append(next(iterator).strip())
            keyword = next(iterator).strip()
            message = next(iterator).strip()
            
            result = decrypt_adfgvx(grid, keyword, message)
            if result is not None:
                print(result)
    except StopIteration:
        pass