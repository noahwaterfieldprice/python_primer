# Exercise 3.10
# Author: Noah Waterfield Price

from math import sqrt


def pathlength(x, y):
    L = 0
    for i in range(1, len(x)):
        dL_squared = (x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2
        L += sqrt(dL_squared)
    return L

points = [(1, 1), (2, 1), (1, 2), (1, 1)]

x = [points[i][0] for i in range(len(points))]
y = [points[i][1] for i in range(len(points))]

print pathlength(x, y)

"""
Sample run:
python pathlength.py
3.41421356237
"""
