#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/color_wheel.py

import sys

def get_color_mix(target_color):
    """
    Problem Background:
    Maria is painting, but the only colors she has are the primary colors: 
    yellow, red, and blue. Write a program that gives Maria the colors she 
    needs in order to mix her desired colors.

    Problem Description:
    A color wheel depicts the relationship between colors. Primary colors are 
    red, yellow, and blue. 
    Secondary colors are:
    - violet (red and blue)
    - orange (red and yellow)
    - green (blue and yellow)
    Tertiary colors are named by combining the primary and secondary colors:
    - red-violet
    - red-orange
    - yellow-orange
    - yellow-green
    - blue-green
    - blue-violet

    Input Format:
    The first line of your program's input will contain a positive integer 
    representing the number of test cases. Each test case will include:
    - A color that Maria needs to make.

    Output Format:
    For each test case, print out the colors that Maria needs to use if she 
    needs to mix colors. The colors needed must be presented in ALPHABETICAL 
    order.
    - If it's a primary color: "No colors need to be mixed to make {color}."
    - If it needs mixing: "In order to make {color}, {c1} and {c2} must be mixed."
    """
    
    # You may find this dictionary helpful:
    color_map = {
        "red": ["red"],
        "yellow": ["yellow"],
        "blue": ["blue"],
        "violet": ["blue", "red"],
        "orange": ["red", "yellow"],
        "green": ["blue", "yellow"],
        "red-violet": ["blue", "red"],
        "red-orange": ["red", "yellow"],
        "yellow-orange": ["red", "yellow"],
        "yellow-green": ["blue", "yellow"],
        "blue-green": ["blue", "yellow"],
        "blue-violet": ["blue", "red"]
    }
    
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
    lines = get_resource("color_wheel.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            color = next(iterator).strip()
            
            result = get_color_mix(color)
            if result is not None:
                print(result)
    except StopIteration:
        pass
