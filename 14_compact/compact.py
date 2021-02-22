def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    truethy = []
    for item in lst:
        if not not item :
            truethy.append(item)
    return truethy