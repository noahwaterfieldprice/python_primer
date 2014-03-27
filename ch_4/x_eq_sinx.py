# Example 4.6.2 - Bisection Root Finding (File Implementation)
from bisection import bisection
from math import sin


def f(x):
    return x - sin(x)

root, iter = bisection(f, -2, 2, 1E-6)
print root, iter

"""
Sample run:
python x_eq_sinx.py
-9.53674316406e-07 22
"""
