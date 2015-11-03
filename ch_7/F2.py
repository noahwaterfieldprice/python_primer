# Exercise 7.11
# Author: Noah Waterfield Price

from math import sin, exp


class F2:

    def __init__(self, a, w):
        self.a = a
        self.w = w

    def __call__(self, x):
        a = self.a
        w = self.w
        return exp(-a * w) * sin(w * x)

    def __str__(self):
        s = 'f(x) = exp(-%gx)sin(%gx)' % (self.a, self.w)
        return s

from math import pi
f = F2(1.0, 0.1)
print f(pi)
f.a = 2
print f(pi)
print f

"""
Sample run:
python F2.py
0.279610139319
0.253001716518
f(x) = exp(-2x)sin(0.1x)
"""
