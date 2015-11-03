# Exercise 3.22
# Author: Noah Waterfield Price

def maxmin(f, a, b, n=1000):
    max_f = max(f(a + i * (b - a) / 100) for i in range(101))
    min_f = min(f(a + i * (b - a) / 100) for i in range(101))
    return max_f, min_f
from math import cos, pi
print maxmin(cos, -pi / 2, 2 * pi, 100001)

"""
Sample run:
python maxmin_f.py
(1.0, -1.0)
"""
