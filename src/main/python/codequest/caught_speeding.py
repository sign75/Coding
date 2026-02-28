#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/caught_speeding.py

import sys

def calculate_ticket(speed, is_birthday):
    """
    Problem Background:
    You are driving a little too fast, and a police officer pulls you over. 
    He needs to determine how big your speeding ticket should be; fortunately 
    for you, he's decided to give you a bit of a break if it happens to be 
    your birthday.

    Problem Description:
    Your program should compute the ticket you are going to receive based on 
    the speed you were travelling:
    - If your speed is 60 or less, you don't get a ticket.
    - If your speed is between 61 and 80 inclusive, you get a small ticket.
    - If your speed is 81 or higher, you get a big ticket.

    If today is your birthday, all of these numbers are increased by 5 
    (for example, you can drive up to 65 without getting a ticket).

    Input Format:
    The first line of your program's input will contain a positive integer 
    representing the number of test cases. Each test case will consist of a 
    single line, including two values separated by spaces:
    - A positive integer representing your speed
    - The word "true", indicating today is your birthday, or the word "false", 
      indicating it is not.

    Output Format:
    For each test case, your program must print a single line:
    - "no ticket" if you do not receive a ticket
    - "small ticket" if you receive a small ticket
    - "big ticket" if you receive a big ticket
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
    lines = get_resource("caught_speeding.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            parts = next(iterator).strip().split()
            speed = int(parts[0])
            is_bday = True if parts[1] == 'true' else False
            
            result = calculate_ticket(speed, is_bday)
            if result is not None:
                print(result)
    except StopIteration:
        pass
