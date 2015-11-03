# Exercise 9.6
# Author: Noah Waterfield Price

from math import sin, cos, radians


class Point:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return '(x, y) = (%g, %g)' % (self.x, self.y)


class PolarPoint(Point):

    def __init__(self, r, theta):
        self.r, self.theta = r, theta
        Point.__init__(self, r * cos(radians(theta)), r * sin(radians(theta)))

    def __str__(self):
        return '(r, theta) = (%g, %g) \n (x, y) = (%g, %g) ' % \
            (self.r, self.theta, round(self.x, 3), round(self.y, 3))

p1 = PolarPoint(1, 90)
print p1
p1 = PolarPoint(1, 45)
print p1
p1 = PolarPoint(1, 270)
print p1

"""
Sample run:
python PolarPoint.py
(r, theta) = (1, 90)
 (x, y) = (0, 1)
(r, theta) = (1, 45)
 (x, y) = (0.707, 0.707)
(r, theta) = (1, 270)
 (x, y) = (-0, -1)
"""
