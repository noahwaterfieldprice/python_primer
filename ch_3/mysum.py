# Exercise 3.4
# Author: Noah Waterfield Price

def mysum(L):
    s = 0
    for e in L:
        s += e
    return s

print mysum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
"""
Sample run:
python mysum.py
55
55
"""
