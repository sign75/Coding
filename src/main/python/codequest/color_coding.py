#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/color_coding.py

import sys

def find_color(text):
    """
    Problem Background:
    You and your coworker have developed secret signals to communicate between 
    each other so others don't know the information you are conveying. The two 
    key words used in your communications are "red" and "blue". You are tired 
    of constantly searching all of your messages for these signals so you 
    decide to write a program to find out if a line of text contains either of 
    these strings.

    Problem Description:
    Your task is to write a program that searches a given line of text for the 
    strings "red" or "blue" (each string contains at most one of those colors). 
    If red is found, return "red"; if blue is found, return "blue"; otherwise 
    return "no color found". These strings are case sensitive, so if "RED" or 
    "bLuE" is found then the program should still return "no color found".

    Input Format:
    The first line of your program's input will contain a positive integer 
    representing the number of test cases. Each test case will include a line 
    of text which should be analyzed to see if "red" or "blue" are present.

    Output Format:
    For each test case, your program must print a single line containing either 
    "red", "blue", or "no color found" (in lowercase letters).
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
    lines = get_resource("color_coding.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            text = next(iterator).strip()
            
            result = find_color(text)
            if result is not None:
                print(result)
    except StopIteration:
        pass
