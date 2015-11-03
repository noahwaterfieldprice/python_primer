# Exercise 1.17
# Author: Noah Waterfield Price

from cmath import sqrt

a = 2
b = 1
c = 2
q = sqrt(b * b - 4 * a * c)
x1 = (-b + q) / (2 * a)
x2 = (-b - q) / (2 * a)

print x1
print x2

"""
Sample run:
python quadratic_find_errors.py
(-0.25+0.968245836552j)
(-0.25-0.968245836552j)
"""
