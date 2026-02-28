#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/charlie_quebec.py

import sys

def translate_to_icao(text):
    """
    Problem Background:
    The International Civil Aviation Organization (ICAO) developed a system in 
    the 1950s so that critical combinations of letters and numbers can be 
    pronounced and understood by those exchanging voice messages by radio or 
    telephone regardless of language or quality of the communication channel.

    Problem Description:
    It is made up of 26 words that are assigned to the 26 letters of the 
    English alphabet. Your application should convert a string of text into 
    its phonetic alphabet code.

    Input Format:
    The first line contains a positive integer representing the number of test 
    cases. Each test case will include:
    - A line containing a positive integer, N, representing how many lines of 
      text the message contains.
    - N lines, each containing a string of text to convert.

    Output Format:
    Your program should print out the ICAO version of each string from the input. 
    Preserve spaces, and add a dash between letters of a word. 
    There will not be any punctuation in the input, only letters and spaces.
    """
    icao_dict = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet', 
        'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee', 
        'Z': 'Zulu'
    }
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
    lines = get_resource("charlie_quebec.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            n = int(next(iterator).strip())
            for _ in range(n):
                text_line = next(iterator).strip()
                result = translate_to_icao(text_line)
                if result:
                    print(result)
    except StopIteration:
        pass
