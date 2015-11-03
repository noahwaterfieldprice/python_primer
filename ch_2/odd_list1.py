# Exercise 2.4
# Author: Noah Waterfield Price

n = 12
i = 0
odd_nos = []
while i < int(round(n / 2.)):
    odd_nos.append(2 * i + 1)
    i += 1

for no in odd_nos:
    print no,

"""
Sample run:
python odd_list2.py
1 3 5 7 9 11
"""
