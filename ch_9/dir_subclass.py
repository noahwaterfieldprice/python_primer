# Exercise 9.1
# Author: Noah Waterfield Price


class Line:

    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
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
    pass


l = Line(2, 5)
p = Parabola(2, 5)

print 'Line:    ', dir(l)
print 'Parabola:', dir(p)

print 'Line:    ', l.__dict__
print 'Parabola:', p.__dict__

"""
Sample run:
python dir_subclass.py
Line:     ['__call__', '__doc__', '__init__', '__module__', 'c0', 'c1', 'table']
Parabola: ['__call__', '__doc__', '__init__', '__module__', 'c0', 'c1', 'table']
Line:     {'c1': 5, 'c0': 2}
Parabola: {'c1': 5, 'c0': 2}
"""
