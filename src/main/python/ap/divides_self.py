def divides_self(n: int) -> bool:
    """
    Description:
        A positive integer divides itself if every digit in the number 
        divides into the number evenly.
        For example, 128 divides itself since 1, 2, and 8 all divide 
        into 128 evenly.
        A number with a 0 digit does not divide itself, as 0 does not 
        divide into any number.

    Examples:
        divides_self(128) -> True
        divides_self(12) -> True
        divides_self(120) -> False

    Args:
        n (int): A positive integer.

    Returns:
        bool: True if the number divides itself, False otherwise.
    """
    ### [Your Implementation Here]

    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.
    return False
