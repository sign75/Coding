#!/bin/python3

# LOCAL EXECUTION: 
#    python src/main/python/codequest/by_the_book.py

import sys

def check_isbn(isbn):
    """
    Problem Background:
    When searching for books in the library, it can sometimes be difficult to 
    be certain if you've gotten the correct book. Particularly with reference 
    books or other textbooks, titles can be the same or similar and it's not 
    always easy to tell who the author is. Fortunately, publishers have 
    developed a way to be certain you've got not only the correct book, but 
    the correct version of it: the International Standard Book Number, or ISBN.

    An ISBN is a 10- or 13- digit code (books published since 2007 have 13-digit 
    codes) that is supposed to uniquely identify a particular edition of a book. 
    Since accurately remembering or writing down a long string of numbers is not 
    guaranteed, the ISBN contains a built-in error-checking mechanism. The last 
    digit in an ISBN is known as a "check digit" and can be used to verify that 
    all of the preceding digits represent a valid ISBN.

    Problem Description:
    To calculate the check digit of an ISBN-10, each of the first nine digits 
    is multiplied by an "integer weight," a number calculated by subtracting 
    the index of the digit from 10. These products are then added together to 
    form a single number. The check digit is the number that must be added to 
    that sum to reach a multiple of 11 (if that number is 10, the check digit 
    is the letter 'X').

    Input Format:
    The first line of your program's input will contain a positive integer 
    representing the number of test cases. Each test case will include a single 
    line containing an ISBN-10 number to be checked. ISBNs can include numeric 
    digits and the uppercase letter X.

    Output Format:
    For each test case, your program must print the word VALID if the given 
    ISBN number has a valid check digit, or the word INVALID if it does not.
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
    lines = get_resource("by_the_book.in").splitlines()   # for local testing
    if not lines:
        sys.exit(0)
        
    iterator = iter(lines)
    try:
        t = int(next(iterator).strip())
        for _ in range(t):
            isbn = next(iterator).strip()
            
            result = check_isbn(isbn)
            if result is not None:
                print(result)
    except StopIteration:
        pass
