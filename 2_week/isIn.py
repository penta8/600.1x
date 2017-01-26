import doctest


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    >>> isIn('a', '')
    False
    >>> isIn('y', 'dhsxz')
    False
    >>> isIn('h', 'o')
    False
    >>> isIn('n', 'ddgjjkknu')
    True
    >>> isIn('j', 'aeeiijjjklmooptwxxyz')
    True
    '''
    if len(aStr) <= 1:
        return aStr == char

    middle = len(aStr)//2
    if char < aStr[middle]:
        return aStr[middle] == char or isIn(char, aStr[:middle])
    else:
        return aStr[middle] == char or isIn(char, aStr[middle+1:])


doctest.testmod()
