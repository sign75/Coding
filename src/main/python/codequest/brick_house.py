#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/brick_house.py

import sys

def can_build_wall(small_bricks, large_bricks, target_length):
    """
    Problem Background:
    We want to build a row of bricks for our brick house that is a certain number of inches long, and we have a number 
    of small bricks and large bricks with which to do it. You need to write an application that will decide if it is 
    possible to build this row of bricks using some or all of the given bricks. You do not need to use all of the given 
    bricks!

    Problem Description:
    Your program will be given a goal length for the brick wall and the number of small and large bricks available. 
    Small bricks are each 1 inch long. Large bricks are 5 inches long. You will need to determine if it is possible to 
    build a row of bricks exactly as long as the goal using only the available bricks.

    Visual Representation:
      [ ] <- Small brick (1 inch)
      [     ] <- Large brick (5 inches)
      
      Example: If target is 8 inches, and you have 3 small and 1 large:
      [     ] [ ] [ ] [ ] = 5 + 1 + 1 + 1 = 8 (True!)

    Input Format:
    - `small_bricks`: An integer representing the number of small, one-inch-long bricks available.
    - `large_bricks`: An integer representing the number of large, five-inch-long bricks available.
    - `target_length`: An integer representing the target length of the wall, X, in inches.

    Output Format:
    - Return a boolean value `True` if it is possible to build a wall of exactly X inches using only the bricks available. 
      Otherwise, return `False`.
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
    lines = get_resource("brick_house.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            parts = next(iterator).strip().split()
            small = int(parts[0])
            large = int(parts[1])
            target = int(parts[2])
            
            result = can_build_wall(small, large, target)
            if result is not None:
                print("true" if result else "false")
    except StopIteration:
        pass