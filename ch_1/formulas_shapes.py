# Exercise 1.8
# Author: Noah Waterfield Price

from math import pi

h = 5.0  # height
b = 2.0  # base
r = 1.5  # radius

area_parallelogram = h * b
print 'The area of the parallelogram is %.3f' % area_parallelogram

area_square = b ** 2
print 'The area of the square is %g' % area_square

area_circle = pi * r ** 2
print 'The area of the circle is %.f' % area_circle

volume_cone = 1.0 / 3 * pi * r ** 2 * h
print 'The volume of the cone is %.3f' % volume_cone

"""
Sample run:
python formulas_shapes.py
The area of the parallelogram is 10.000
The area of the square is 4
The area of the circle is 7
The volume of the cone is 11.781
"""
