def dict_interdiff(d1, d2, f):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    return (intersect(d1,d2, f), difference(d1,d2))

def intersect(d1, d2, f):
    inter = {}
    for key in d1.keys():
        if key in d2:
            inter[key] = f(d1[key],  d2[key])
    return inter

def difference(d1,d2):
    diff = {}
    temp2 = d2.copy()
    for key in d1.keys():
        if key not in temp2:
            diff[key] = d1[key]
        else:
            del temp2[key]
    diff.update(temp2)
    return diff

def add(n1, n2):
    return n1 + n2

def isLarger(n1, n2):
    return n1 > n2

if __name__ == '__main__':
    d1 = {1:30, 2:20, 3:30, 5:80}
    d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
    d3 = {1:30, 2:20, 3:30}
    d4 = {1:40, 2:50, 3:60}
    assert intersect(d1, d2, add) == {1: 70, 2: 70, 3: 90}
    assert difference(d1, d2) == {4: 70, 5: 80, 6: 90}
    assert difference(d3, d4) == {}
    assert dict_interdiff(d1, d2, add) == ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
    assert dict_interdiff(d3, d4, isLarger) == ({1: False, 2: False, 3: False}, {})
