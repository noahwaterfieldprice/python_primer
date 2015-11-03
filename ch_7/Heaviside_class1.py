# Exercise 7.19
# Author: Noah Waterfield Price

from math import pi, sin


class Heaviside:

    def __init__(self, eps=None):
        self.eps = eps

    def __call__(self, x):
        if self.eps is None:
            if x < 0:
                return 0
            elif x >= 0:
                return 1
        else:
            e = self.eps
            if x < -e:
                return 0
            elif -e <= x <= e:
                return 0.5 + x / (2 * e) + 1 / (2 * pi) * sin(pi * x / e)
            elif x > e:
                return 1


H = Heaviside()
print H(0.1)
H = Heaviside(eps=0.8)
print H(0.1)

"""
Sample run:
python Heaviside_class1.py
1
0.6234059599
"""
