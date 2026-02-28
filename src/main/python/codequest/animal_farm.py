#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/animal_farm.py

import sys

def count_legs(turkeys, goats, horses):
    """
    Problem Background:
    You live on a farm where you have turkeys, goats, and horses. 
    The local government is starting a new tax based on the number of animal legs on a farm.
    You must calculate the number of legs shared between the three types of animals.

    Problem Description:
    To calculate the total number of legs, you must know how many legs each animal has:
    - Turkeys = 2 legs
    - Goats = 4 legs
    - Horses = 4 legs

    Given the number of turkeys, goats, and horses on your farm, calculate the total 
    number of animal legs.

    Input Format:
    - The first line contains a positive integer representing the number of test cases.
    - Each test case consists of a single line containing three integers separated by spaces:
      `Turkeys Goats Horses`

    Output Format:
    - Return an integer representing the total number of animal legs on the farm.
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
    # input_data = sys.stdin.read().split()   # for online testing
    input_data = get_resource("animal_farm.in").split()   # for local testing
    if not input_data:
        sys.exit(0)
        
    iterator = iter(input_data)
    try:
        t = int(next(iterator))
        for _ in range(t):
            turkeys = int(next(iterator))
            goats = int(next(iterator))
            horses = int(next(iterator))
            
            result = count_legs(turkeys, goats, horses)
            if result is not None:
                print(result)
    except StopIteration:
        pass