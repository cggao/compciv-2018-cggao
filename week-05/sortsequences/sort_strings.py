from datastubs import STRING_LIST


def reverse_alpha():
    """
        return the list of strings sorted in
        reverse alphabetical order.
        """
    
    return sorted(STRING_LIST, reverse=True)


def alpha_case_insensitive():
    """
        return the list of strings sorted in
        alphabetical order, but without regard to
        capitalization
        """
# fill it out
    return sorted(STRING_LIST, key=lambda s: s.lower())

def by_longest_length():
    """
        Sort in descending order of length of strings
        """
# fill it out
    return sorted(STRING_LIST, key = lambda s: len(s), reverse=True)


def filter_and_sort_number_strings():
    """
        Filter the original list for strings that
        contain numbers. Then sort that list of number
        strings but as strings (i.e. alphaebtical order)
        """
# fill it out
    result = []
    for s in STRING_LIST:
        if (s.isnumeric()):
            result.append(s)
    return sorted(result)

def filter_and_sort_number_strings_as_numbers():
    """
        Filter the list for strings that contain numbers
        and then sort that list of strings in *numerical* order
        """
# fill it out
    result = []
    for s in STRING_LIST:
        if (s.isnumeric()):
            result.append(s)
    return sorted(result, key = lambda s: int(s))

