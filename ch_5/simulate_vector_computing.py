# Exercise 5.6
# Author: Noah Waterfield Price

from numpy import cos, sin, exp, array, zeros, meshgrid

x = array([0, 2])
t = array([1, 1.5])

ylist = zeros([2, 2])


def y(x, t):
    return cos(sin(x) + exp(1 / t))

for i in xrange(2):
    for j in xrange(2):
        ylist[i, j] = y(x[i], t[j])

print ylist

print '\n'

xv, tv = meshgrid(x, t)
ylist_check = y(xv, tv)

print ylist_check

"""
Sample run:
python simulate_vector_computing.py
[[-0.91173391 -0.3680749 ]
 [-0.88421456 -0.95978494]]


[[-0.91173391 -0.88421456]
 [-0.3680749  -0.95978494]]
"""
