def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    the_true = 0
    for item in lst : 
        if type(item) == list:
            the_true += 1
        else :
            return False
    
    if the_true == len(lst):
        return True
