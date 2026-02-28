#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/air_terminator_control.py

import sys

def assess_threat_level(is_friendly, observation_times):
    """
    Problem Background:
    You're working with Lockheed Martin Missiles & Fire Control and the Royal Air Force to develop an artificial 
    intelligence system to monitor protected airspace around the British Isles. While eventually the system will be 
    able to make judgements about encroaching aircraft on its own, it needs to be trained to know what to look for first.

    Problem Description:
    The AI system and your algorithm will be provided with tracking information for a series of aircraft that have been 
    observed flying in and around protected airspace. Every 15 minutes, the radar system reports the aircraft that are 
    currently within that protected airspace. Your data will consist of the times at which each aircraft was observed. 
    Gaps in these times - for example, if an aircraft was observed at 01:00 and again at 01:30, but not at 01:15 - 
    indicate that the aircraft left, then re-entered protected airspace.

    Using this information, you must determine the threat level associated with that aircraft (NONE, LOW, MEDIUM, or HIGH) 
    using the following criteria:

    - If the aircraft's transponder identifies it as a friendly aircraft, it poses no threat (NONE). Otherwise, the 
      aircraft has a minimum threat level of NONE, but that may be increased by other conditions in this list.
      
    - The total number of data points within protected airspace affects the minimum threat level:
      - At least 12 data points: LOW
      - At least 24 data points: MEDIUM
      - At least 36 data points: HIGH
      
    - The length of the longest continuous series of data points within protected airspace affects the minimum threat level:
      - At least 4 continuous data points: LOW
      - At least 8 continuous data points: MEDIUM
      - At least 12 continuous data points: HIGH
      
    - The number of times the aircraft entered protected airspace affects the minimum threat level:
      - Entered on at least 4 separate occasions: MEDIUM
      - Entered on at least 8 separate occasions: HIGH

    Input Format:
    - `is_friendly`: A Boolean value indicating if the aircraft is (TRUE), or is not (FALSE), identified as friendly.
    - `observation_times`: A list of strings containing times in 24-hour HH:MM format, representing the times at 
      which the aircraft was observed within protected airspace. Times are given in chronological order and have a 
      minimum interval of 15 minutes.

    Output Format:
    - Return a single string (NONE, LOW, MEDIUM, or HIGH) representing the ultimate threat level presented by the aircraft.
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
    lines = get_resource("air_terminator_control.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            parts = next(iterator).strip().split()
            is_friendly = (parts[0] == 'TRUE')
            n = int(parts[1])
            
            times = []
            for _ in range(n):
                times.append(next(iterator).strip())
                
            result = assess_threat_level(is_friendly, times)
            if result is not None:
                print(result)
    except StopIteration:
        pass