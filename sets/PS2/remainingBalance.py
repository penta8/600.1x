def newBalance(balance, anIntRate, monPayRate):
    minimum = balance * monPayRate
    balance = balance - minimum
    return balance + (anIntRate/12)*balance


def balanceYear(balance, anIntRate, monPayRate):
    for year in range(12):
        balance = newBalance(balance, anIntRate, monPayRate)
    return balance

print('Remaining balance: ' + str(round(balanceYear(42, 0.2, 0.04), 2)))
print('Remaining balance: ' + str(round(balanceYear(484, 0.2, 0.04), 2)))
