# Exercise 7.2
# Author: Noah Waterfield Price

class Account2:

    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        self._balance = initial_amount
        self._transactions = 0

    def deposit(self, amount):
        self._balance += amount
        self._transactions += 1

    def withdraw(self, amount):
        self._balance -= amount
        self._transactions += 1

    def get_balance(self):
        return self._balance

    def dump(self):
        s = '%s, %s, balance: %s, transactions: %d' % \
            (self._name, self._no, self._balance, self._transactions)
        print s

a1 = Account2('John Olsson', '19371554951', 20000)
a1.deposit(1000)
a1.withdraw(4000)
a1.withdraw(3500)
a1.dump()
a1.deposit(151247)
a1.dump()

"""
Sample run:
python Account2.py
John Olsson, 19371554951, balance: 13500, transactions: 3
John Olsson, 19371554951, balance: 164747, transactions: 4
"""
