#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/change_for_the_world.py

import sys

def calculate_change(amount_str):
    """
    Problem Background:
    Some people really like coins. You happen to be one of those people! In a 
    world filled with electronic payments and banking from your cell phone, you 
    prefer to deal exclusively in cold, hard cash specifically, common coins. 
    However, you are also practical. I mean, paying for your lunch in pennies? 
    That's just silly. In order to strike the right balance of quirky and 
    practical, you need to be able to pay for things using the fewest number 
    of coins possible - and you'll write a program to do just that.

    Problem Description:
    Given a dollar value, you'll need to calculate the minimum number of coins 
    necessary to pay the bill. The coins you'll have available are those most 
    commonly seen in the United States - quarters (worth $0.25), dimes 
    (worth $0.10), nickels (worth $0.05), and pennies (worth $0.01). 

    Input Format:
    The first line of your program's input will contain a positive integer 
    representing the number of test cases. Each test case will include a single 
    line containing dollar amount to convert to coinage. The amount will start 
    with a dollar sign ($) and contain two decimal places.

    Output Format:
    For each test case, your program should output the following lines:
    - A line containing the dollar amount being converted, as provided
    - A line reading "Quarters=X", where X is the number of quarters required
    - A line reading "Dimes=X", where X is the number of dimes required
    - A line reading "Nickels=X", where X is the number of nickels required
    - A line reading "Pennies=X", where X is the number of pennies required
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
    lines = get_resource("change_for_the_world.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            amount_str = next(iterator).strip()
            
            result_lines = calculate_change(amount_str)
            if result_lines:
                for r_line in result_lines:
                    print(r_line)
    except StopIteration:
        pass
