def factorial(n: int) -> int:
    """
    Description:
        Given n of 1 or more, return the factorial of n, which is 
        n * (n-1) * (n-2) ... 1. Compute the result recursively 
        (without loops).

    Examples:
        factorial(1) -> 1
        factorial(2) -> 2
        factorial(3) -> 6

    Args:
        n (int): A positive integer for which to compute the factorial.

    Returns:
        int: The factorial of n.
    """
    ### [Your Implementation Here]

    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.
    if (n <= 1): return 1
    return factorial(n-1) * n
