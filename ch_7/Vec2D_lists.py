# Exercise 7.36
import math


class Vec2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        other = self.convert2Vec2D(other)
        return Vec2D(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        other = self.convert2Vec2D(other)
        return self.__add__(self, other)

    def __rsub__(self, other):
        other = self.convert2Vec2D(other)
        return other.__sub__(self)

    def __sub__(self, other):
        other = self.convert2Vec2D(other)
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        other = self.convert2Vec2D(other)
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        other = self.convert2Vec2D(other)
        return self.__rmul__(self, other)

    def __eq__(self, other):
        other = self.convert2Vec2D(other)
        return self.x == other.x and self.y == other.y

    def __req__(self, other):
        other = self.convert2Vec2D(other)
        return self.__eq__(self, other)

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __ne__(self, other):
        return not self.__eq__(other)  # reuse __eq__

    @staticmethod
    def convert2Vec2D(other):
        if isinstance(other, (list, tuple)):
            return Vec2D(other[0], other[1])
        else:
            return other

u = Vec2D(-2, 4)
v = u + (1, 1.5)
print v
w = [-3, 2] - v
print w

"""
Sample run:
python Vec2D_list.py
(-1, 5.5)
(-2, -3.5)
"""
    
