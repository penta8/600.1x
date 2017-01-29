def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup
    '''
    oddTup = ()
    for index in range(len(aTup)):
        if index % 2 == 0:
            oddTup += (aTup[index],)
    return oddTup

tup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(tup))
