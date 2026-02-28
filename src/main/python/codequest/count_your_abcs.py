#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/count_your_abcs.py

import sys

def count_decal_sets(phrase):
    """
    Problem Background:
    Your friend is running their first marathon next month, and you want to 
    surprise them by sticking letters on their window that read "FUTURE 
    MARATHONER LIVES HERE." When searching for letter decals online, you find 
    that the most affordable set contains 26 letters (A-Z). You need to know 
    how many sets you'll need to buy in order to complete the message... 
    but while you're at it, let's write a program that can calculate that for 
    any message!

    Problem Description:
    Given an input phrase, you need to know how many alphabets worth of letter 
    decals you would need in order to completely spell out the phrase. Each 
    set of decals contains exactly one of each letter in the English alphabet 
    (from A through Z). You can ignore spaces when making your calculations, 
    and messages won't include any punctuation.

    Input Format:
    The first line of your program's input will contain a positive integer 
    representing the number of test cases. Each test case will include a single 
    line containing a message consisting of uppercase letters and spaces.

    Output Format:
    For each test case, your program must print a single line containing an 
    integer representing the number of decal sets needed to complete the 
    message.
    """
    pass

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
    lines = get_resource("count_your_abcs.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            phrase = next(iterator).strip()
            
            result = count_decal_sets(phrase)
            if result is not None:
                print(result)
    except StopIteration:
        pass
