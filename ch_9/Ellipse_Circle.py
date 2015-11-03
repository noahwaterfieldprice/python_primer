# Exercise 9.5
# Author: Noah Waterfield Price

from math import pi, sqrt


class Ellipse:

    def __init__(self, x0, y0, a, b):
        self.x0, self.y0, self.a, self.b = x0, y0, a, b

    def area(self):
        a, b = self.a, self.b
        return pi * a * b

    def circumference(self):
        # Ramanujan approximation
        a, b = self.a, self.b
        return pi * (3 * (a + b) - sqrt((3 * a + b) * (a + 3 * b)))


class Circle(Ellipse):

    def __init__(self, x0, y0, r):
        Ellipse.__init__(self, x0, y0, r, r)

circ = Circle(2, 3, 1)
print circ.area()
print circ.circumference()

"""
Sample run:
python Ellipse_Circle.py
3.14159265359
6.28318530718
"""
