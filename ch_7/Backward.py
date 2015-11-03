# Exercise 7.14
# Author: Noah Waterfield Price

from math import sin, cos, exp


class Backward:
# error was in assignment of h. 'h=e-9' should've been 'h=1e-9'

    def __init__(self, f, h=1e-9):
        self.f = f
        self.h = h

    def __call__(self, x):
        h, f = self.h, self.f
        return (f(x) - f(x - h)) / h  # finite difference

dsin = Backward(sin)
e = dsin(0) - cos(0)
print 'error:', e
dexp = Backward(exp, h=1e-7)
e = dexp(0) - exp(0)
print 'error:', e

"""
Sample run:
python Backward.py
error: 0.0
error: -5.04863919559e-08
"""
