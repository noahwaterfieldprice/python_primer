# Exercise 5.37
# Author: Noah Waterfield Price

import numpy as np
import operator


def piecewise(x, data):
    r = np.zeros(len(x))
    for i in xrange(len(data) - 1):
        cond = operator.and_(data[i][1] <= x, x < data[i + 1][1])
        r[cond] = data[i][0]
    return r


# need last pair to define final x interval
data = [(20, -2), (-1, 0), (0, 1), (4, 1.5), (-7, 4), (23, 6.3), (None, 7.5)]

print piecewise(np.linspace(-1, 7, 9), data)

"""
Sample run:
python piecewise_vec.py
[ 20.  -1.   0.   4.   4.  -7.  -7.  -7.  23.]
"""
