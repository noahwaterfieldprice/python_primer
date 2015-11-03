# Exercise 5.29
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt
from scitools.std import movie

R = 1
beta = 0.02
mu0 = 0.02


def vel_prof(r, n):
    return (beta / 2 * mu0) ** (1. / n) * float(n) / (n + 1) * \
        ((R ** (1 + 1. / n) - r ** (1 + 1. / n)))

r = np.linspace(0, R, 100)
counter = 0
plt.hold(0)
for n in np.linspace(1, 0.1, 100):
    plt.plot(r, vel_prof(r, n) / vel_prof(0, n))
    plt.xlabel('radius')
    plt.ylabel('velocity')
    plt.title('Velocity profile: n = %1.2f' % n)
    plt.savefig('tmp_%03d.png' % counter)
    counter += 1

movie('tmp_*.png', encoder='convert', fps=24)

import glob
import os
# Remove old plot files
for filename in glob.glob('tmp_*.png'):
    os.remove(filename)
