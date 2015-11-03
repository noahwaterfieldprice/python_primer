# Exercise 7.3
# Author: Noah Waterfield Price

from math import sqrt


class Rectangle:

    def __init__(self, x0, y0, W, H):
        self.x0 = x0
        self.y0 = y0
        self.W = W
        self.H = H

    def area(self):
        return self.W * self.H

    def circumference(self):
        return 2 * self.W + 2 * self.H


class Triangle:

    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def area(self):
        x1, y1 = self.v1
        x2, y2 = self.v2
        x3, y3 = self.v3
        return 0.5 * abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y1 - x2*y1)

    def circumference(self):
        vertices = (self.v1, self.v2, self.v3)
        circumference = 0
        for i in range(3):
            dx = vertices[i][0] - vertices[(i-1) % 3][0]
            dy = vertices[i][1] - vertices[(i-1) % 3][1]
            circumference += sqrt(dx**2 + dy**2)
        return circumference

rect = Rectangle(1, 0, 4, 3)
print 'Rectangle of dimensions %g x %g, and bottom left corner at (%g, %g). \
\nArea: %g\nCircumference: %g\n' \
% (rect.W, rect.H, rect. W, rect.H, rect.area(), rect.circumference())

tri = Triangle((0, 0), (3, 0), (3, 4))
print 'Triangle with vertices at %s, %s and %s.\
\nArea: %g\nCircumference: %g' \
% (tri.v1, tri.v2, tri.v3, tri.area(), tri.circumference())

"""
Sample run:
python geometric_shapes.py
Rectangle of dimensions 4 x 3, and bottom left corner at (4, 3).
Area: 12
Circumference: 14

Triangle with vertices at (0, 0), (3, 0) and (3, 4).
Area: 6
Circumference: 12
"""
