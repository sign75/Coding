#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/bigger_is_better.py

import sys

def find_max_score(scores):
    """
    Problem Background:
    Sometimes the simplest task is just finding the best among the rest. 
    In this case, bigger is always better!

    Problem Description:
    Given a list of scores (integers), you need to find and return the highest score in the list.

    Input Format:
    - The first line contains a positive integer representing the number of test cases.
    - Each test case consists of a single line containing space-separated integers.

    Output Format:
    - For each test case, return the maximum integer from the list.
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
    lines = get_resource("bigger_is_better.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            line = next(iterator).strip()
            if not line:
                continue
            scores = list(map(int, line.split()))
            
            result = find_max_score(scores)
            if result is not None:
                print(result)
    except StopIteration:
        pass