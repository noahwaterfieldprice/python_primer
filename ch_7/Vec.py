# Exercise 7.38
# Author: Noah Waterfield Price

import numpy as np


class Vec:

    def __init__(self, *args):
            if len(args) == 1:
                self.v = np.array(args[0])
            else:
                self.v = np.array(args)

    def __add__(self, other):
        return Vec(self.v + other.v)

    def __sub__(self, other):
        return Vec(self.v - other.v)

    def __mul__(self, other):
        return np.inner(self.v, other.v)

    def cross(self, other):
        if len(self.v) != 3:
            raise ArithmeticError(
                'Vector must be 3 dimensional to calculate cross product')
        return Vec(np.cross(self.v, other.v))

    def __eq__(self, other):
        return np.array_equal(self.v, other.v)

    def __str__(self):
        return str(tuple(self.v))

    def __abs__(self):
        return np.abs(self.v)

    def __ne__(self, other):
        return not self.__eq__(other)  # reuse __eq__

v1 = Vec(np.array([1, -1, 4], float))
v2 = Vec([1, -1, 4])
v3 = Vec((1, -1, 4))
v4 = Vec(1, -1)
a = Vec(1, 3, 4)
b = Vec(3, 8, 2)
print a + b
print a * b
print abs(b)
print a
print a.cross(b)
print a != b

"""
Sample run:
python Vec.py
print a + b
print a * b
print abs(b)
print a
print a.cross(b)
print a != b
"""
