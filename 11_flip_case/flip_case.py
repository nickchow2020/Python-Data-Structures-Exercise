def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    the_phrase = []
    for char in phrase:
        if char == to_swap.lower() :
            the_phrase.append(char.upper())
        elif char == to_swap.upper() :
            the_phrase.append(char.lower())
        else:{
            the_phrase.extend(char)
        }
    
    return "".join(the_phrase)
