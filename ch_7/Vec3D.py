# Exercise 7.37
# Author: Noah Waterfield Price

import math


class Vec3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        other = self.convert2Vec3D(other)
        return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        other = self.convert2Vec3D(other)
        return self.__add__(self, other)

    def __rsub__(self, other):
        other = self.convert2Vec3D(other)
        return other.__sub__(self)

    def __sub__(self, other):
        other = self.convert2Vec3D(other)
        return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        other = self.convert2Vec3D(other)
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __rmul__(self, other):
        other = self.convert2Vec3D(other)
        return self.__rmul__(self, other)

    def cross(self, other):
        other = self.convert2Vec3D(other)
        x1, y1, z1 = self.x, self.y, self.z
        x2, y2, z2 = other.x, other.y, other.z
        return Vec3D(y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - y1 * x2)

    def __eq__(self, other):
        other = self.convert2Vec3D(other)
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __req__(self, other):
        other = self.convert2Vec3D(other)
        return self.__eq__(self, other)

    def __str__(self):
        return '(%g, %g, %g)' % (self.x, self.y, self.z)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __ne__(self, other):
        return not self.__eq__(other)  # reuse __eq__

    @staticmethod
    def convert2Vec3D(other):
        if isinstance(other, (list, tuple)):
            return Vec3D(other[0], other[1], other[2])
        else:
            return other

a = Vec3D(1, 3, 4)
b = Vec3D(3, 8, 2)
c = (0, 2, 1)
print a + b
print a * c
print abs(b)
print a
print a.cross(b)

"""
Sample run:
python Vec3D.py
(4, 11, 6)
10
8.77496438739
(1, 3, 4)
(-26, 10, -1)
"""
