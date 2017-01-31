def newBalance(balance, anInterest, pay):
    balance = balance - pay
    return balance + (anInterest/12.0) * balance


def yearBalance(balance, anInterest, pay):
    for year in range(12):
        balance = newBalance(balance, anInterest, pay)
    return balance


def payInAYear(balance, anInterest):
    montInt = anInterest / 12.0
    low = balance/12
    upp = (balance * ((1 + montInt)**12)) / 12.0
    pay = (upp + low) / 2
    epsilon = 0.01

    while abs(yearBalance(balance, anInterest, pay)) > epsilon:
        if yearBalance(balance, anInterest, pay) < 0:
            upp = pay
        else:
            low = pay
        pay = (upp + low) / 2.0

    return round(pay, 2)

print(payInAYear(320000, 0.2))
print(payInAYear(999999, 0.18))
print(payInAYear(9999999999, 0.3))
