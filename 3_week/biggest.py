def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict) > 0:
        quantity = 0
        biggest = ''
        for dic in aDict:
            if len(aDict[dic]) > quantity:
                biggest = dic
        return biggest
    else:
        return None


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(biggest(animals))
print(biggest({}))
