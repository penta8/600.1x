x = -256

if x < 0:
    isNeg = True
    result = abs(x)
else:
    isNeg = False
    result = x

binary = ''

if result == 0:
    binary = '0'

while result != 0:
    binary = str(result % 2) + binary
    result = result // 2

if isNeg:
    binary = '-' + binary

print(str(x) + ' is binary ' + binary)
