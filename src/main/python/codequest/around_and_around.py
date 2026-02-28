#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/around_and_around.py

import sys
import math

def calculate_circumference(altitude):
    """
    Problem Background:
    Satellites in orbit travel a much further distance around the Earth than we do on the surface. 
    To properly track them, you need to calculate the exact distance they cover in a single orbit.

    Problem Description:
    You are calculating the circumference of a circular orbit around Earth given its altitude.
    The formula for the circumference of a circle is C = 2 * pi * r.
    Here, the radius 'r' is the Earth's radius PLUS the altitude of the orbit.
    For this problem, the Earth's equatorial circumference is given as approximately 40075 km.
    Thus, Earth's radius can be derived from 40075 = 2 * pi * r_earth, or you can simplify the 
    orbit circumference formula to: C = 40075 + (2 * pi * altitude).

    Input Format:
    - The first line contains a positive integer representing the number of test cases.
    - Each test case consists of a single line containing an integer representing the altitude in km.

    Output Format:
    - For each test case, return the calculated circumference as a float. 
      (The main block will typically print this rounded to 1 decimal place).
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
    input_data = get_resource("around_and_around.in").split()   # for local testing
    if not input_data:
        sys.exit(0)
        
    iterator = iter(input_data)
    try:
        t = int(next(iterator))
        for _ in range(t):
            altitude = int(next(iterator))
            
            result = calculate_circumference(altitude)
            if result is not None:
                print(f"{result:.1f}")
    except StopIteration:
        pass