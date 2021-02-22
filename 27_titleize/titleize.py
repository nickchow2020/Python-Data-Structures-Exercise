def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    _phrase = []
    for item in  phrase.split(" "):
        _phrase.append(item.capitalize())

    return " ".join(_phrase)