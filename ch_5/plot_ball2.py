# Exercise 5.10
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
plt.legend(['v0 = %g' % v0 for v0 in velocities])
plt.show()
