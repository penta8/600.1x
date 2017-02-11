def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    total = 0
    for index in range(len(listA)):
        total += listA[index] * listB[index]
    return total


if __name__ == '__main__':
    listA = [1, 2, 3]
    listB = [4, 5, 6]
    assert dotProduct(listA, listB) == 32
