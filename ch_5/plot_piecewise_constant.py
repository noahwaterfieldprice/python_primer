# Exercise 5.36
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt
import operator


def piecewise(x, data):
    r = np.zeros(len(x))
    for i in xrange(len(data) - 1):
        cond = operator.and_(data[i][1] <= x, x < data[i + 1][1])
        r[cond] = data[i][0]
    return r


def plot_piecewise(data, xmax):
    x = np.linspace(data[0][1], xmax, 1001)
    plt.plot(x, piecewise(x, data))
    plt.xlabel('x')
    plt.ylabel('piecewise(x)')
    plt.show()

# need last pair to define final x interval
data = [(20, -2), (-1, 0), (0, 1), (4, 1.5), (-7, 4), (23, 6.3), (None, 7.5)]

plot_piecewise(data, data[-1][1])
