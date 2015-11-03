# Exercise 5.22
# Author: Noah Waterfield Price

import numpy as np
from scitools.std import plot, movie
import glob
import os

# Clean up old frames
for name in glob.glob('tmp_*.png'):
    os.remove(name)


def wave_packet(x, t):
    return np.exp(-(x - 3 * t) ** 2) * np.sin(3 * np.pi * (x - t))

x = np.linspace(-10, 10, 1001)

counter = 0
for t in np.linspace(-2, 2, 61):
    y = wave_packet(x, t)
    plot(x, y,
         axis=[x[0], x[-1], -1, 1],
         xlabel='x',
         ylabel='Amplitude',
         savefig='tmp_%04d.png' % counter)
    counter += 1

movie('tmp*.png')

# Clean up new frames
for name in glob.glob('tmp_*.png'):
    os.remove(name)
