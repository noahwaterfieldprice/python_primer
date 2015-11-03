# Exercise 7.23
# Author: Noah Waterfield Price

import numpy as np
import operator


class PiecewiseConstant:

    def __init__(self, data, xmax):
        self.data = data + [(None, xmax)]

    def __call__(self, x):
        if isinstance(x, (float, int)):
            return self.piecewise(x, self.data)
        else:
            return self.piecewise_vec(x, self.data)

    @staticmethod
    def piecewise(x, data):
        for i in range(len(data) - 1):
            # catch values equal to the largest upper limit
            if data[i][1] <= x < data[i + 1][1] or x == data[-1][1]:
                return data[i][0]

    @staticmethod
    def piecewise_vec(x, data):
        r = np.zeros(len(x))
        for i in xrange(len(data) - 1):
            cond = operator.and_(data[i][1] <= x, x < data[i + 1][1])
            # catch values equal to the largest upper limit
            cond = operator.or_(cond, x == data[-1][1])
            r[cond] = data[i][0]
        return r


f = PiecewiseConstant([(0.4, 1), (0.2, 1.5), (0.1, 3)], xmax=4)
print f(1.5), f(1.75), f(4)

x = np.linspace(0, 4, 21)
print f(x)

"""
Sample run:
python PiecewiseConstant1.py
0.2 0.2 0.4
[ 0.   0.   0.   0.   0.   0.4  0.4  0.4  0.2  0.2  0.2  0.2  0.2  0.2  0.2
  0.1  0.1  0.1  0.1  0.1  0.1]
"""
