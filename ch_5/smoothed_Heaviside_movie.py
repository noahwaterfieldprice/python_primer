# Exercise 5.23
# Author: Noah Waterfield Price

import numpy as np
from scitools.std import pi, sin, plot, movie
import glob
import os
import operator


def smoothed_Heaviside(x, e=1E-2):
    cond = operator.and_(-e <= x, x <= e)
    r = np.zeros(len(x))
    r[x < -e] = 0.0
    r[cond] = 0.5 + x[cond] / (2 * e) + 1 / (2 * pi) * sin(pi * x[cond] / e)
    r[x > e] = 1.0
    return r

x = np.linspace(-2, 2, 2001)

counter = 0
for eps in np.linspace(2, 1e-15, 101):
    y = smoothed_Heaviside(x, eps)
    plot(x, y,
         axis=[x[-1], x[0], -1.5, 1.5],
         xlabel='x',
         ylabel='Heaviside(x)',
         savefig='tmp_%04d.png' % counter)
    counter += 1

movie('tmp_*.png')

# Clean up frames
for name in glob.glob('tmp_*.png'):
    os.remove(name)
