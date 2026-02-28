#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/anti_asteroid_weapon.py

import sys

def sort_asteroids(asteroids):
    """
    Problem Background:
    Earth is under attack... and you're our only hope!
    A cluster of asteroids is quickly approaching Earth's atmosphere.

    Problem Description:
    You'll need to return a list of the incoming asteroids in order of increasing distance from Earth.
    Earth is at coordinate (0,0). You can calculate the distance from Earth using the distance formula: 
    d = sqrt(x^2 + y^2).
    
    In the case of a tie in distance, their original relative order from the input can be preserved.

    Input Format:
    - The first line contains a positive integer representing the number of test cases.
    - Each test case starts with a positive integer N representing the number of asteroids.
    - Followed by N lines, each containing X and Y coordinates of an asteroid separated by a space.

    Output Format:
    - For each test case, return a list of tuples containing the coordinates of the asteroids 
      sorted by increasing distance from Earth.
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
    input_data = get_resource("anti_asteroid_weapon.in").split()   # for local testing
    if not input_data:
        sys.exit(0)
        
    iterator = iter(input_data)
    try:
        t = int(next(iterator))
        for _ in range(t):
            n = int(next(iterator))
            asteroids = []
            for _ in range(n):
                x = int(next(iterator))
                y = int(next(iterator))
                asteroids.append((x, y))
            
            result = sort_asteroids(asteroids)
            
            if result:
                for ax, ay in result:
                    print(f"{ax} {ay}")
    except StopIteration:
        pass