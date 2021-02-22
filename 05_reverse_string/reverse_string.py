def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    letter =  list(phrase)
    letter.reverse()
    return "".join(letter)