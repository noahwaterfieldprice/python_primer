# Exercise 5.9
# Author: Noah Waterfield Price

import numpy as np
from scitools.std import plot

v0 = 10
g = 9.81

tlist = np.linspace(0, 2 * v0 / g, 100)


def y(t):
    return v0 * t - 0.5 * g * t ** 2

plot(tlist, y(tlist),
     xlabel='time (s)',
     ylabel='height (m)',
     axis=[tlist[0], tlist[-1], y(tlist).min(), y(tlist).max()]
     )

raw_input()
