#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/data_lockdown.py

import sys

def filter_logs(logs):
    """
    Problem Background:
    Corporations around the world deal with a lot of information that they need to keep relatively secret. 
    If information about business proposals, active projects, or employee records gets released to the 
    public - either deliberately or accidentally- it can have a serious impact on a company's ability to 
    do business.

    Problem Description:
    You're working with Lockheed Martin's Enterprise Business Services company to monitor internet 
    traffic by Lockheed employees. You need to write a tool that will automatically flag such requests 
    for additional review. The proxy logs will indicate the website being accessed and the amount of 
    data being transferred in the request (in kilobytes). Requests to Lockheed websites - which all 
    end with ".lmco.com" - can be ignored. However, any request to another website that transfers 
    more than a megabyte of data (1000 kilobytes) should be reviewed.

    Input Format:
    - The first line contains a positive integer representing the number of test cases.
    - Each test case will include:
      - A line containing a positive integer, X, indicating the number of records in the log.
      - X lines, each representing an entry in the proxy log. Entries contain the URL and the amount 
        of data in kilobytes, separated by a space.

    Output Format:
    - For each test case, your program must print the log entries that require additional review, 
      following the rules described above. Log entries should be printed in the order received.
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
    lines = get_resource("data_lockdown.in").splitlines()
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            x = int(next(iterator).strip())
            logs = []
            for _ in range(x):
                logs.append(next(iterator).strip())
            
            result = filter_logs(logs)
            if result:
                for res in result:
                    print(res)
    except StopIteration:
        pass