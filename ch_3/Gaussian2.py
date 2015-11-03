# Exercise 3.14
# Author: Noah Waterfield Price

from math import sqrt, exp, pi


def gauss(x, m=0, s=1):
    gaussian = 1 / (sqrt(2 * pi) * s) * exp(-0.5 * ((x - m) / s) ** 2)
    return gaussian
print '%8s' % 'x',
for x in range(-5, 6):
    print '%9d' % x,
print "\nGaussian",
for x in range(-5, 6):
    print '%.7f' % gauss(x),
