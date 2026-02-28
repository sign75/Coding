#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/aeiou.py

import sys

def count_vowels(text):
    """
    Problem Background:
    The English alphabet contains five vowels - A, E, I, O, and U. 
    The other 21 letters of the alphabet are called consonants. 
    Today, we need you to count how many vowels appear in a series of sentences.

    Problem Description:
    Given a line of text, you need to find the total number of vowels contained within it.
    Vowels are defined strictly as 'a', 'e', 'i', 'o', and 'u'. You should be case-insensitive, 
    meaning 'A' and 'a' both count as vowels.

    Input Format:
    - The first line of input contains a positive integer representing the number of test cases. 
    - Each test case will include a single line with a series of lowercase or uppercase words 
      separated by spaces.

    Output Format:
    - For each test case, your program should return an integer representing the total number of 
      vowels contained in the input.
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
    lines = get_resource("aeiou.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            text = next(iterator).strip()
            
            result = count_vowels(text)
            if result is not None:
                print(result)
    except StopIteration:
        pass