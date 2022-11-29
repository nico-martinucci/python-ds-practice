def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    upper_phrase = [char for char in phrase]
    upper_phrase[0] = upper_phrase[0].upper()

    return ''.join(upper_phrase)

    # there's a method for that
    # phrase[:1].upper() + phrase[1:]