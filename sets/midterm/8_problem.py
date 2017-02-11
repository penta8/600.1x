def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    toDelete = []
    for index in range(len(L)):
        if not g(f(L[index])):
            toDelete.append(index)
    toDelete.reverse()
    for index in toDelete:
        del L[index]

    try:
        return max(L)
    except:
        return -1



def f(i):
    return i + 2

def g(i):
    return i > 5


if __name__ == '__main__':
    L = [0, -10, 5, 6, -4]
    L2 = []
    L3 = [5, 5, 5]
    assert applyF_filterG(L, f, g) == 6
    assert applyF_filterG(L2, f, g) == -1
    assert applyF_filterG(L3, f, g) == 5
