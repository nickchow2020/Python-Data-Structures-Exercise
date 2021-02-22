def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    _num1 = list(str(num1))
    _num2 = list(str(num2))
    _num1.sort()
    _num2.sort()

    return _num1 == _num2