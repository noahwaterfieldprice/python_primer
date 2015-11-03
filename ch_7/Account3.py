# Exercise 7.12
# Author: Noah Waterfield Price

class Account3:

    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        self._balance = initial_amount
        self._transactions = 0

    def __iadd__(self, amount):
        self._balance += amount
        self._transactions += 1
        return self

    def __isub__(self, amount):
        self._balance -= amount
        self._transactions += 1
        return self

    def get_balance(self):
        return self._balance

    def dump(self):
        s = '%s, %s, balance: %s, transactions: %d' % \
            (self._name, self._no, self._balance, self._transactions)
        print s

a1 = Account3('John Olsson', '19371554951', 20000)
a1 += 1000
a1 -= 4000
a1 -= 3500
a1.dump()
a1 += 151247
a1.dump()

"""
Sample run:
python Account3.py
John Olsson, 19371554951, balance: 13500, transactions: 3
John Olsson, 19371554951, balance: 164747, transactions: 4
"""

