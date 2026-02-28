#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/chinese_zodiac.py

import sys

def get_zodiac(year):
    """
    Problem Background:
    The Chinese Zodiac is an ancient tradition stemming from the legend of the 
    Jade Emperor. Similar to Western astrology, traditional Chinese beliefs 
    hold that a person's personality is linked to that of the animal associated 
    with the year of their birth.

    Problem Description:
    The Chinese Zodiac consists of a 60-year rotation created by two separate 
    cycles. The Five Elements Wood, Fire, Earth, Metal, and Water - dictate the 
    first cycle. The 12 animals of the Zodiac represent each of the 12 years 
    within a lunar cycle. Additionally, each year is associated with the Yin or 
    Yang from Taoist beliefs.

    To determine the Zodiac sign for a given year:
    - Yin or Yang:
      - Even-numbered years are Yang
      - Odd-numbered years are Yin
    - Element:
      - Subtract 4 from the year, modulo 10, then divide by 2 (round down)
      - 0: Wood, 1: Fire, 2: Earth, 3: Metal, 4: Water
    - Animal:
      - Subtract 4 from the year, modulo 12
      - 0: Rat, 1: Ox, 2: Tiger, 3: Rabbit, 4: Dragon, 5: Snake, 6: Horse, 
        7: Goat, 8: Monkey, 9: Rooster, 10: Dog, 11: Pig

    Input Format:
    The first line contains a positive integer representing the number of test 
    cases. Each test case will include a single line of text containing a four 
    digit year no earlier than 1984.

    Output Format:
    For each test case, your program must print a single line with the calendar 
    year, aspect, element, and animal separated by spaces.
    Example: 1984 Yang Wood Rat
    """
    elements = ["Wood", "Fire", "Earth", "Metal", "Water"]
    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", 
               "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    
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
    lines = get_resource("chinese_zodiac.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            year = int(next(iterator).strip())
            result = get_zodiac(year)
            if result:
                print(result)
    except StopIteration:
        pass
