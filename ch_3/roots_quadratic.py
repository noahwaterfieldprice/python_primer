# Exercise 3.3
# Author: Noah Waterfield Price

def roots(a, b, c):
    from cmath import sqrt
    q = sqrt(b * b - 4 * a * c)
    x1 = (-b + q) / (2 * a)
    x2 = (-b - q) / (2 * a)
    return x1, x2

print roots(1, 3, 2)
print roots(1, -2, 3)

"""
Sample run:
python roots_quadratic.py
((-1+0j), (-2+0j))
((1+1.4142135623730951j), (1-1.4142135623730951j))
"""
