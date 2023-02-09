def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    # define an empty counter
    # loop through phrase
    # increment letter counter / add letter and count of 1
    # return counter

    counter = {}
    vowels = "aeiou"

    phrase = phrase.lower()

    for letter in phrase:
        if letter in vowels:
            counter[letter] = (counter[letter] + 1) if letter in counter else 1

    return counter