from typing import List

def words_without_list(words: List[str], length: int) -> List[str]:
    """
    Description:
        Given an array of strings, return a new list where all the 
        strings of the given length are omitted.

    Examples:
        words_without_list(["a", "bb", "b", "ccc"], 1) -> ["bb", "ccc"]
        words_without_list(["a", "bb", "b", "ccc"], 3) -> ["a", "bb", "b"]
        words_without_list(["a", "bb", "b", "ccc"], 4) -> ["a", "bb", "b", "ccc"]

    Args:
        words (List[str]): A list of strings.
        length (int): The length of the strings to omit from the list.

    Returns:
        List[str]: A new list with all strings of the given length omitted.
    """
    ### [Your Implementation Here]

    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.
    return []
