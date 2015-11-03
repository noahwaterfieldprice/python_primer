# Exercise 2.5
# Author: Noah Waterfield Price

n = 12
odd_nos = [2 * i + 1 for i in range(0, int(round(n / 2.)))]
for no in odd_nos:
    print no,

"""
Sample run:
python odd_list2.py
1 3 5 7 9 11
"""
