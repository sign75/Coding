#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/collatz_conjecture.py

import sys

def collatz_length(n):
    """
    Problem Background:
    Can you believe that there are some math problems that still remain unsolved 
    today? The Collatz Conjecture is one such problem.

    Problem Description:
    To create a Collatz Sequence, start with any positive integer n. 
    Each term in the sequence is derived from the previous term using the 
    following rules: 
    - if the previous term is even, then the next term is one half the previous. 
    - Otherwise, the next term is 3 times the previous term plus 1. 
    The Collatz Conjecture states that no matter what value you pick for n, the 
    series will eventually reach the number 1.

    For example, starting with 12, the full sequence is:
    12, 6, 3, 10, 5, 16, 8, 4, 2, 1
    So starting with 12, the sequence length is 10. Your task is to write a 
    program that will provide the length of a Collatz Sequence starting from a 
    given number.

    Input Format:
    The first line of your program's input will contain a positive integer 
    representing the number of test cases. Each test case will include:
    - A single positive integer N, which will be greater than or equal to 2, 
      and less than or equal to 1,000,000.

    Output Format:
    Your program should output the length of each sequence in the following format:
    <Start Number>:<Sequence Length>
    """
    print(f"Calculating Collatz sequence length for: {n}")
    x = n
    loops = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        loops = loops + 1    
    return f"{x}:{loops}" 

# Add 1 every time one loop is complete
#sequence uses modulus: if input mod 2 = 0, divide by 2, else, 3x +1
# if the sequence reaches 0, break or something and exit loop, return the number of time the loop was completed
 











def get_resource(relative_path):
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
    lines = get_resource("collatz_conjecture.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            n = int(next(iterator).strip())
            result = collatz_length(n)
            if result:
                print(result)
    except StopIteration:
        pass
