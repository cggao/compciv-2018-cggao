from datastubs import PEOPLE_LIST

def longest_name():
    """
        sort by length of name in descending order
        """
    def foolen(p):
        return len(p['name'])
    return sorted(PEOPLE_LIST, key=foolen, reverse=True)

def youngest():
    """
        sort by age in ascending order
        """
# fill it out
    def ages(p):
        return p['age']
    return sorted(PEOPLE_LIST, key=ages)

def oldest():
    """
        sort by age in descending order
        """
# fill it out
    def ages(p):
        return p['age']
    return sorted(PEOPLE_LIST, key=ages, reverse=True)


def name_reverse_alpha():
# fill it out
    def names(p):
        return p['name']
    return sorted(PEOPLE_LIST, key=names, reverse=True)

def country_then_age():
# fill it out
    def countryage(p):
        return (p['country'], p['age'])
    return sorted(PEOPLE_LIST, key=countryage)
