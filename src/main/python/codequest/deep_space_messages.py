#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/deep_space_messages.py

import sys

def decode_message(message):
    """
    Problem Background:
    While you and your team of astronauts are in orbit around Earth, one of the space station's 
    communication arrays receives a series of messages. This isn't unusual... but what is unusual 
    is that the messages didn't come from Earth! Your team needs to quickly decipher the messages 
    to report them back to command.

    Problem Description:
    You're able to determine that the messages contain a jumbled mass of letters, but occasionally 
    contain a few numbers. The letters appear to be mostly background interference, but the numbers 
    seem to be relevant. To decipher the message, you assign each number to a letter based on its 
    position in the English alphabet (e.g. 1=A, 2=B, etc., up to 26=Z).

    Write a program that will translate numbers within each message string to their corresponding 
    letters, then print the resulting text. You may assume that if two numbers are next to each 
    other that they are part of the same integer.

    Input Format:
    - The first line contains a positive integer representing the number of test cases.
    - Each test case will include a line representing a received message, containing lowercase 
      letters and numbers.

    Output Format:
    - For each test case, your program must print a single line containing the text deciphered 
      from the received message using the process outlined above. Print text in lowercase letters.
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
    lines = get_resource("deep_space_messages.in").splitlines()
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            msg = next(iterator).strip()
            
            result = decode_message(msg)
            if result is not None:
                print(result)
    except StopIteration:
        pass