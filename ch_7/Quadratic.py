# Exercise 7.6
# Author: Noah Waterfield Price

from numpy import linspace
from cmath import sqrt


class Quadratic:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def value(self, x):
        a, b, c = self.a, self.b, self.c
        return a * x ** 2 + b * x + c

    def table(self, L, R, n=10):
        xlist = linspace(L, R, n)
        print 'y = ax^2 + bx + c'
        print 'a = %g, b = %g, c = %g' % (self.a, self.b, self.c)
        print '-' * 30
        print '%12s %12s' % ('x', 'y')
        print '-' * 30
        for x in xlist:
            print '%12g %12g' % (x, self.value(x))

    def roots(self):
        a, b, c = self.a, self.b, self.c
        d = sqrt(b * b - 4 * a * c)
        r1 = (-b + d) / (2 * a)
        r2 = (-b - d) / (2 * a)
        return r1, r2


quad = Quadratic(2, -6, 12)
print quad.value(0)
print quad.value(5)
print quad.roots()
quad.table(-5, 5, 11)

"""
Sample run:
python Quadratic.py
12
32
((1.5+1.9364916731037085j), (1.5-1.9364916731037085j))
y = ax^2 + bx + c
a = 2, b = -6, c = 12
------------------------------
           x            y
------------------------------
          -5           92
          -4           68
          -3           48
          -2           32
          -1           20
           0           12
           1            8
           2            8
           3           12
           4           20
           5           32
"""
