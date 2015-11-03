# Exercise 7.22
# Author: Noah Waterfield Price

from math import pi, sin


class Indicator:

    def __init__(self, a, b, eps=None):
        self.a = a
        self.b = b
        self.eps = eps

    def __call__(self, x):
        a, b = self.a, self.b
        if self.eps is None:
            return self.heaviside(x - a) * self.heaviside(b - x)
        else:
            e = self.eps
            return self.smoothed_heaviside(x - a, e) * \
                self.smoothed_heaviside(b - x, e)

    @staticmethod
    def heaviside(x):
        if x < 0:
            return 0
        elif x >= 0:
            return 1

    @staticmethod
    def smoothed_heaviside(x, e):
        if x < -e:
            return 0
        elif -e <= x <= e:
            return 0.5 + x / (2 * e) + 1 / (2 * pi) * sin(pi * x / e)
        elif x > e:
            return 1


a = 0
b = 2
I = Indicator(a, b)
print I(b + 0.1), I((a + b) / 2.0)
I = Indicator(0, 2, eps=1)
print I(0), I(1), I(1.9)

"""
Sample run:
python Indicator.py
0 1
0.5 0.25 0.599181582154
"""
