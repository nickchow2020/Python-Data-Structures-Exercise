def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    counter_dict = {}
    for char in phrase :
        if char in counter_dict : 
            counter_dict[char] += 1
        else :
            counter_dict[char] = 1

    return counter_dict
