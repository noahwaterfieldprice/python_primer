# Exercise 2.14
# Author: Noah Waterfield Price

"""
This program calculated the amount of years
it takes for an amount of money to reach 1.5
times its value, given and interest rate of p

To solve the integer division error if p is an 
int, it was necessary to change p/100 to p/100.
"""

initial_amount = 100
p = 5.5  # interest rate
amount = initial_amount
years = 0
while amount <= 1.5 * initial_amount:
    amount += p / 100. * initial_amount
    years += 1
print years

"""
Sample run:
python interest_rate_loop.py
10
"""
