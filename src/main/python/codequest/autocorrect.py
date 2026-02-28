#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/autocorrect.py

import sys

def autocorrect(dictionary_words, misspelled_words):
    """
    Problem Background:
    Typos are an inevitable part of typing. Thankfully, most typos happen for the same reason - a user presses one key 
    when they mean to press a different one. Fortunately, most autocorrect algorithms are excellent at identifying when 
    this sort of typo happens. One approach they can use for this is measuring the Hamming distance between what you 
    typed and a word in the dictionary.

    Problem Description:
    The Hamming distance between two strings of text is the number of character substitutions that need to be made to 
    change one string to the other. For example, the words "apple" and "applr" have a Hamming distance of one - they 
    are identical, except for the last letter. The words "computer" and "kompudir" have a Hamming distance of three due 
    to the three character differences; k/c, t/d, and e/i, respectively.

    Lockheed Martin is working on implementing a new autocorrect feature for their internal communication tools. You will 
    be given a "dictionary" of correctly spelled words, followed by a list of potentially misspelled words that need 
    correction. For each of these misspelled words, your program will need to identify the dictionary word of the same 
    length that has the smallest Hamming distance to the misspelled word. (Ties will not occur, and words will not change 
    length as a result of their misspelling.)

    Input Format:
    - `dictionary_words`: A list of strings representing correctly spelled words.
    - `misspelled_words`: A list of strings representing potentially misspelled words.

    Output Format:
    - Return a list of strings, where each string is the dictionary word that has the shortest Hamming distance 
      to the correspondingly ordered misspelled word.
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
    lines = get_resource("autocorrect.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            parts = next(iterator).strip().split()
            d = int(parts[0])
            w = int(parts[1])
            
            dictionary_words = []
            for _ in range(d):
                dictionary_words.append(next(iterator).strip())
                
            misspelled_words = []
            for _ in range(w):
                misspelled_words.append(next(iterator).strip())
                
            result = autocorrect(dictionary_words, misspelled_words)
            if result:
                for word in result:
                    print(word)
    except StopIteration:
        pass