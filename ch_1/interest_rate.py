# Exercise 1.6
# Author: Noah Waterfield Price

interest_rate = 5.0  # in percent
years = 3
initial_amount = 1000
# Calculate final amount due to interest rate
final_amount = initial_amount * (1 + interest_rate / 100) ** years
print final_amount

"""
Sample run:
python interest_rate.py
1157.625
"""
