def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    even = []
    result = 1
    for env in nums :
        if env % 2 == 0:
            even.append(env)
    

    if len(even) != 0 :
        for num in even:
            result = result * num
        return result
    else:
        return 1