#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/addiply.py

import sys

def addiply(a, b):
    """
    Problem Background:
    Nowadays if you put two things together you need to come up with a cool name 
    to describe the two things together, like Bennifer or Brangelina. 
    In this problem, you will deal with the concepts of addition and multiplication. 
    You will Addiply!

    Problem Description:
    Your task is to write a program which does simple addition and multiplication 
    based on 2 input numbers.

    Input Format:
    - The first line of input contains a positive integer representing the number of test cases.
    - Each test case includes a single line containing two positive integers separated by a space.

    Output Format:
    - For each test case, return a string with 2 numbers separated by a single space: 
      1. The result of adding the two input numbers.
      2. The result of multiplying the two input numbers.
    """
    print(f"a: {a}")
    print(f"b: {b}")
    added = a + b
    multiplied = a * b
    
    return f"{added} {multiplied}"
    
    














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
    # input_data = sys.stdin.read().split()   # for online testing
    input_data = get_resource("addiply.in").split()   # for local testing
    if not input_data:
        sys.exit(0)
        
    iterator = iter(input_data)
    try:
        t = int(next(iterator))
        for _ in range(t):
            a = int(next(iterator))
            b = int(next(iterator))
            
            result = addiply(a, b)
            if result is not None:
                print(result)
    except StopIteration:
        pass