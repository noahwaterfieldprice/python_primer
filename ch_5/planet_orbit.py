# Exercise 5.27
import numpy as np
import matplotlib.pyplot as plt
from scitools.std import movie


def orbit_path(t, a, b, omega):
    return a * np.cos(omega * t), b * np.sin(omega * t)


def inst_vel(t, a, b, omega):
    return omega * np.sqrt((a * np.sin(omega * t)) ** 2 +
                           (b * np.cos(omega * t)) ** 2)


def animate_orbit(a, b, omega, n):
    tlist = np.linspace(0, 2 * np.pi / omega, n)
    xorbit, yorbit = orbit_path(tlist, a, b, omega)
    counter = 0
    for t in tlist:
        x, y = orbit_path(t, a, b, omega)
        plt.plot(xorbit, yorbit, '--', color='#67001f', linewidth=2)
        plt.hold(1)
        plt.plot(x, y, 'ro', markerfacecolor='#2166ac',
                 markeredgecolor='#053061', markeredgewidth=2, markersize=20)
        plt.hold(0)
        plt.xlim([xorbit.min() * 1.1, xorbit.max() * 1.1])
        plt.ylim([yorbit.min() * 1.1, yorbit.max() * 1.1])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Instantaneous velocity = %4f' % inst_vel(t, a, b, omega))
        plt.savefig('tmp_%03d.png' % counter)
        counter += 1

animate_orbit(10, 10, 20, 200)
movie('tmp_*.png', encoder='convert', fps=24)

import glob
import os
# Remove old plot files
for filename in glob.glob('tmp_*.png'):
    os.remove(filename)
