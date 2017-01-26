def newBalance(balance, anInterest, pay):
    balance = balance - pay
    return balance + (anInterest/12) * balance


def yearBalance(balance, anInterest, pay):
    for year in range(12):
        balance = newBalance(balance, anInterest, pay)
    return balance


def payInAYear(balance, anInterest):
    pay = 0
    increase = 10
    while yearBalance(balance, anInterest, pay) >= 0:
        pay += increase
    return pay

print('Lowest Payment: ' + str(payInAYear(3329, 0.2)))
print('Lowest Payment: ' + str(payInAYear(4773, 0.2)))
