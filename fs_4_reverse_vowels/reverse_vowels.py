def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = []
    string = list(s)

    for char in string:
        if char.lower() in "aeiou":
            vowels.append(char)
    
    for i in range(len(string)):
        if string[i].lower() in "aeiou":
            string[i] = vowels[len(vowels) - 1]
            vowels.pop(len(vowels) - 1)

    
    return "".join(string)
