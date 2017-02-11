def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exp = 0
    while True:
        sq1 = base ** exp
        sq2 = base ** (exp + 1)
        if abs(sq1 - num) < abs(sq2 - num):
            break
        else:
            exp = exp + 1
    return exp

if __name__ == '__main__':
    print(closest_power(3,12))
    print(closest_power(4,12))
    print(closest_power(4,1))
