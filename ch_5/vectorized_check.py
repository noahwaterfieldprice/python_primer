# Exercise 5.5
# Author: Noah Waterfield Price

from numpy import exp, array

v = array([2, 3, -1])


def f(x):
    return x ** 3 + x * exp(x) + 1

print f(v)[0] == f(v[0])
print f(v)[1] == f(v[1])
print f(v)[2] == f(v[2])

"""
Sample run:
python vectorized_check.py
True
True
True
"""
    