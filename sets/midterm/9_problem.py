def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if aList == []:
        return []
    else:
        if not isinstance(aList[0], list):
            return [aList[0]] + flatten(aList[1:])
        else:
            return flatten(aList[0]) + flatten(aList[1:])



if __name__ == '__main__':
    aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    aList2 = [1,2,3,4]
    aList3 = []
    aList4 = [3, 9, [4, 4], 9]
    assert flatten(aList) == [1,'a','cat',2,3,'dog',4,5]
    assert flatten(aList2) == aList2
    assert flatten(aList3) == aList3
    assert flatten(aList4) == [3, 9, 4, 4, 9]
