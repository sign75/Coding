#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/collision_flare_gun.py

import sys

def calculate_final_velocity(v1, m1, v2, m2):
    """
    Problem Background:
    Lockheed Martin is testing two new compounds that when they come into 
    contact will ignite after a short delay and produce a very bright blue 
    light capable of illuminating a large area. Two synchronized pneumatic guns 
    will shoot the compounds into the air with predefined trajectories that 
    will make them collide at a known point.

    Problem Description:
    Once the compounds collide, we need to know their final velocity so we can 
    know where exactly they will be in the air as they ignite. Using the 
    formula for inelastic collisions below, your team needs to write a program 
    that can determine this final velocity of the mixed compound given the 
    initial velocities (v1 and v2) and masses (m1 and m2) of the two original 
    compounds.
    
    Formula: 
    V = (m1 * v1 + m2 * v2) / (m1 + m2)

    Input Format:
    The first line of your program's input will contain a positive integer 
    representing the number of test cases. Each test case will include a single 
    line, containing the following values separated by commas:
    - v1: the initial velocity of the first compound in meters/second
    - m1: the mass of the first compound in kilograms
    - v2: the initial velocity of the second compound in meters/second
    - m2: the mass of the second compound in kilograms

    Output Format:
    For each test case, your program must print a single line containing the 
    final velocity, in meters per second, of the combined mass. Round values 
    to two decimal places and include any trailing zeroes (e.g. 2.33).
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
    lines = get_resource("collision_flare_gun.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            parts = next(iterator).strip().split(',')
            v1 = float(parts[0])
            m1 = float(parts[1])
            v2 = float(parts[2])
            m2 = float(parts[3])
            
            result = calculate_final_velocity(v1, m1, v2, m2)
            if result is not None:
                # Assuming the function returns the float or formatted string
                if isinstance(result, float):
                    print(f"{result:.2f}")
                else:
                    print(result)
    except StopIteration:
        pass
