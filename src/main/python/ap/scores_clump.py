def scores_clump(scores: list[int]) -> bool:
    """
    Description:
        Given an array of scores sorted in increasing order, 
        return True if the array contains 
        3 adjacent scores that differ from each other by at 
        most 2. In other words, if any 
        consecutive triplet of scores has a maximum difference 
        (between the highest and lowest) 
        of 2 or less, the function returns True.

    Examples:
        scores_clump([3, 4, 5]) -> True
        scores_clump([3, 4, 6]) -> False
        scores_clump([1, 3, 5, 5]) -> True

    Args:
        scores (list[int]): A list of integer scores, sorted in increasing order.

    Returns:
        bool: True if there exists a triplet of adjacent scores with a max difference of 2 or less,
              otherwise False.
    """
    ### [Your Implementation Here]

    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.
    return False
