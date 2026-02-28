#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/discovering_planets.py

import sys

def check_habitability(temperature, has_water, has_magnetic_field, eccentricity):
    """
    Problem Background:
    A planet has been discovered by a group of astronomers! Now they must work to determine if the 
    planet can support life. There are many determinants in arriving at a conclusion, including the 
    presence of water, and reasonable temperature levels and climates. Astronomers can use decision 
    trees to help inform their conclusions.

    Problem Description:
    For a planet to be considered habitable, it must meet these conditions:
    - Temperature: between 0 C and 100 C.
    - Presence of Water: water is essential.
    - Survivable Surface: presence of a planetary magnetic field is essential.
    - Circular Orbits: eccentricity less than or equal to 0.6.

    Input Format:
    - The first line contains a positive integer representing the number of test cases.
    - Each test case will include a single line with:
      - A decimal value representing average estimated temperature (Celsius).
      - A Boolean value indicating presence of water (true/false).
      - A Boolean value indicating presence of magnetic field (true/false).
      - A decimal value representing eccentricity of the orbit.

    Output Format:
    For each test case, return a single string:
    - If temperature > 100, return "The planet is too hot."
    - Otherwise, if temperature < 0, return "The planet is too cold."
    - Otherwise, if it does not contain water, return "The planet has no water."
    - Otherwise, if it does not have a magnetic field, return "The planet has no magnetic field."
    - Otherwise, if eccentricity > 0.6, return "The planet's orbit is not ideal."
    - Otherwise, return "The planet is habitable."
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
    lines = get_resource("discovering_planets.in").splitlines()
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            parts = next(iterator).strip().split()
            temp = float(parts[0])
            water = (parts[1] == 'true')
            mag = (parts[2] == 'true')
            ecc = float(parts[3])
            
            result = check_habitability(temp, water, mag, ecc)
            if result is not None:
                print(result)
    except StopIteration:
        pass