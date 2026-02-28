#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/batter_up.py

import sys

def calculate_slugging_percentage(player_name, stats):
    """
    Problem Background:
    In baseball, the Slugging Percentage (SLG) is a popular measure of the power of a hitter. 
    Unlike batting average, which values all hits equally, slugging percentage weights hits 
    based on the total number of bases the batter safely reaches.

    Problem Description:
    Calculate the Slugging Percentage (SLG) for a given baseball player.
    Formula: SLG = Total Bases / Total At Bats.
    
    Stat Values:
    - 1B (Single) = 1 base, 1 At Bat
    - 2B (Double) = 2 bases, 1 At Bat
    - 3B (Triple) = 3 bases, 1 At Bat
    - HR (Home Run) = 4 bases, 1 At Bat
    - K (Strikeout) = 0 bases, 1 At Bat
    - BB (Walk) = 0 bases, 0 At Bats (Walks do not count as an At Bat)

    Input Format:
    - The first line contains a positive integer representing the number of test cases.
    - Each test case is a single string formatted as "PlayerName:Stat1,Stat2,..."

    Output Format:
    - For each test case, return the calculated SLG as a float. 
      (The main block will format this as "PlayerName=X.XXX" with 3 decimal places).
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
    lines = get_resource("batter_up.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            line = next(iterator).strip()
            if ':' in line:
                parts = line.split(':')
                player_name = parts[0]
                stats_str = parts[1]
                stats = stats_str.split(',')
                
                slg = calculate_slugging_percentage(player_name, stats)
                if slg is not None:
                    print(f"{player_name}={slg:.3f}")
    except StopIteration:
        pass