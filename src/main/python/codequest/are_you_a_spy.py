#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/are_you_a_spy.py

import sys

def check_spy(phrase1, phrase2):
    """
    Problem Background:
    You are an undercover agent trying to determine if the person you're talking to is your contact. 
    You have a specific set of rules to determine if their response marks them as a friendly spy.

    Problem Description:
    You are checking if the second phrase is a "secret contact" of the first.
    The rule is: 
    If all the alphabetic characters in the second phrase (case-insensitive) 
    are present in the first phrase, it's a match.
    Non-alphabetic characters (punctuation, spaces, etc.) are ignored.

    Input Format:
    - The first line of input contains a positive integer representing the number of test cases.
    - Each test case consists of a single line containing two phrases separated by a pipe character ('|').
      Format: "Phrase1|Phrase2"

    Output Format:
    - If the second phrase is a match based on the rules, return: "That's my secret contact!"
    - If it is not a match, return: "You're not a secret agent!"
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
    lines = get_resource("are_you_a_spy.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            line = next(iterator).strip()
            if '|' in line:
                parts = line.split('|')
                p1 = parts[0]
                p2 = parts[1]
                
                result = check_spy(p1, p2)
                if result is not None:
                    print(result)
    except StopIteration:
        pass