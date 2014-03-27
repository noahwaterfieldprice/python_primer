from bisection import bisection
from math import sin


def f(x):
    return x - sin(x)

root, iter = bisection(f, -2, 2, 1E-6)
print root, iter
