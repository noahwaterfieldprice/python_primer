# Exercise 5.11
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt
import sys

g = 9.81


def y(t, v0):
    return v0 * t - 0.5 * g * t ** 2

ax = plt.subplot(111)
plt.hold(1)


def plot_trajectory(v0):
    tlist = np.linspace(0, 2 * v0 / g, 100)
    ax.plot(tlist, y(tlist, v0))

ax.set_xlabel('time (s)')
ax.set_ylabel('height (m)')

velocities = np.array(sys.argv[1:], dtype=np.float)

for x in xrange(len(velocities)):
    plot_trajectory(velocities[x])

# Plots generated in order with v0 increasing
# hence last tlist stores the list for the largest v0

vmax = velocities.max()

max_yval = y(np.linspace(0, 2 * vmax / g, 100), vmax).max()

ax.set_xlim([0, 2 * velocities.max() / g])
ax.set_ylim([0, max_yval + 0.1])
plt.legend(['v0 = %g' % v0 for v0 in velocities])
plt.show()
