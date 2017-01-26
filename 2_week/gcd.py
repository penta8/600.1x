def gcd(a, b):
    if a < b:
        temp = a
        a = b
        b = temp

    if a % b == 0:
        return b
    elif a % b == 1:
        return 1
    else:
        return gcd(b, a % b)

print(gcd(2, 12))
print(gcd(6, 12))
print(gcd(9, 12))
print(gcd(17, 12))
