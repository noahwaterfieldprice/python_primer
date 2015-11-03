# Exercise 9.2
# Author: Noah Waterfield Price


class Line:

    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        print 'called Line'
        return self.c0 + self.c1 * x

    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s


class Parabola(Line):

    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)  # let Line store c0 and c1 self.c2 = c2
        self.c2 = c2

    def __call__(self, x):
        print 'called Parabola'
        return Line.__call__(self, x) + self.c2 * x ** 2


class Cubic(Parabola):

    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2)
        self.c3 = c3

    def __call__(self, x):
        print 'called Cubic'
        return Parabola.__call__(self, x) + self.c3 * x ** 3


class Poly4(Cubic):

    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4

    def __call__(self, x):
        print 'called Poly4'
        return Cubic.__call__(self, x) + self.c4 * x ** 4


quartic = Poly4(1, 2, 3, 4, 5)
print quartic(10)

"""
Sample run:
python Cubic_Poly4.py
called Poly4
called Cubic
called Parabola
called Line
54321
"""

