def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    # iterate over lst
    # check if elem isinstance of "list" - return false if not
    # return true

    return len([elem for elem in lst if isinstance(elem, list)]) == len(lst)