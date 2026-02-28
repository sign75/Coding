#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/detecting_multipaction.py

import sys

def detect_multipaction(phase_null, third_harmonic):
    """
    Problem Background:
    Multipaction is a phenomenon experienced by radio frequency (RF) devices exposed to the vacuum of 
    space. Free electrons floating around can be accelerated by the energy in the RF field... Luckily, 
    it's possible to detect when multipaction events occur in order to protect the integrity of these 
    devices.

    Problem Description:
    You've noticed during testing that a multipaction event results in abnormally high readings in both 
    the phase null and third harmonic channels, between 60% and 85% of their maximum power output. 
    Your team needs to develop a subroutine and test it. If, for a given time index, both channels 
    show a power reading between .6 and .85 of their maximum outputs (inclusive), that indicates an 
    event which should be reported.

    Input Format:
    - The first line contains a positive integer representing the number of test cases.
    - Each test case will include two lines of text, containing the readings obtained from the phase 
      null and third harmonic channels, respectively. Each line will consist of a list of decimal 
      values between 0 and 1 exclusive, separated by spaces. Both lines will contain the same number 
      of values.

    Output Format:
    - If no multipaction events were detected, return "No multipaction events detected."
    - If one multipaction event was detected, return "A multipaction event was detected at time index X."
    - If more than one multipaction event was detected, return "N multipaction events were detected at 
      time indices: X.", where N is the number of events, and X is a space-delimited list of indices.
    Index numbers correspond to the position of the values within the provided arrays of data (0-based).
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
    lines = get_resource("detecting_multipaction.in").splitlines()
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            pn = list(map(float, next(iterator).strip().split()))
            th = list(map(float, next(iterator).strip().split()))
            
            result = detect_multipaction(pn, th)
            if result is not None:
                print(result)
    except StopIteration:
        pass