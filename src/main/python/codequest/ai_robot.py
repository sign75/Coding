#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/ai_robot.py

import sys

def simulate_robot(x, y, facing, commands):
    """
    Problem Background:
    Lockheed Martin is working on developing a reconnaissance robot that will eventually 
    receive orders from an AI system. You need to write a program to simulate the orders 
    that will be sent from the AI, then indicate the robot's expected position.

    Problem Description:
    The robot operates on a coordinate grid:
    - North (+Y)
    - East (+X)
    - South (-Y)
    - West (-X)

    The robot accepts three types of commands:
    - R: Turn right 90 degrees.
    - L: Turn left 90 degrees.
    - A: Advance 1 unit in the direction it is currently facing.

    You must take the robot's initial X and Y coordinates, its initial facing direction, 
    and a sequence of commands, and return its final coordinates and facing direction.

    Input Format:
    - The first line contains a positive integer representing the number of test cases.
    - Each test case is a single line containing:
      `X Y Facing Commands` (space separated)
      - X and Y: Integers representing the starting coordinates.
      - Facing: A single character ('N', 'E', 'S', or 'W') representing the starting direction.
      - Commands: A string containing only 'R', 'L', and 'A'.

    Output Format:
    - Return a string formatted exactly as "FinalX FinalY FinalFacing" (e.g., "2 0 N").
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
    input_data = get_resource("ai_robot.in").split()   # for local testing
    if not input_data:
        sys.exit(0)
        
    iterator = iter(input_data)
    try:
        t = int(next(iterator))
        for _ in range(t):
            x = int(next(iterator))
            y = int(next(iterator))
            facing = next(iterator)
            commands = next(iterator)
            
            result = simulate_robot(x, y, facing, commands)
            if result is not None:
                print(result)
    except StopIteration:
        pass