# Exercise 7.1
# Author: Noah Waterfield Price

from math import sin, exp


class F:

    def __init__(self, a, w):
        self.a = a
        self.w = w

    def value(self, x):
        a = self.a
        w = self.w
        return exp(-a * w) * sin(w * x)

from math import pi
f = F(a=1.0, w=0.1)
print f.value(x=pi)
f.a = 2
print f.value(pi)

"""
Sample run:
python F.py
0.279610139319
0.253001716518
"""
