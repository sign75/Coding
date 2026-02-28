#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/anagram_checker.py

import sys

def check_anagram(line):
    """
    Problem Background:
    An anagram is a type of word play, the result of rearranging the letters of a word 
    or phrase to produce a new word or phrase using all of the original letters exactly once.
    For example, the word STOP can be rearranged into the words TOPS and POTS.

    Problem Description:
    Anagrammy only wants to check word anagrams, not phrases. 
    CRITICAL RULE: In order to really be considered an anagram, the two words have to be different! 
    For example, "MIKE" and "MIKE" are NOT anagrams of each other.

    You need to check if the two words provided are anagrams.

    Input Format:
    - The first line of input contains a positive integer representing the number of test cases.
    - Each test case will include a single line containing two words separated by a pipe character ('|').
    - Words will contain uppercase letters only.

    Output Format:
    - If they are anagrams, return the string: "WORD1|WORD2 = ANAGRAM"
    - If they are not anagrams, return the string: "WORD1|WORD2 = NOT AN ANAGRAM"
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
    lines = get_resource("anagram_checker.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            line = next(iterator).strip()
            
            result = check_anagram(line)
            if result is not None:
                print(result)
    except StopIteration:
        pass