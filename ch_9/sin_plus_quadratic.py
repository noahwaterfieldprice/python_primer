# Exercise 9.3
# Author: Noah Waterfield Price

import numpy as np


class Parabola:

    def __init__(self, c0, c1, c2):
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2

    def __call__(self, x):
        return self.c2 * x ** 2 + self.c1 * x + self.c0

    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s


class SinPlusParabola(Parabola):

    def __init__(self, A, w, a, b, c):
        Parabola.__init__(self, a, b, c)
        self.A = A
        self.w = w

    def __call__(self, x):
        return Parabola.__call__(self, x) + self.A * np.sin(self.w * x)


sinPP = SinPlusParabola(10, 2, 3, 5, 2.5)
print sinPP.table(0, 10, 10)

"""
Sample run:
python sin_plus_quadratic.py
           0            3
     1.11111      19.5942
     2.22222      16.8136
     3.33333       51.186
     4.44444       79.711
     5.55556      98.0049
     6.66667      154.384
     7.77778      194.642
     8.88889      236.195
          10      312.129

"""
