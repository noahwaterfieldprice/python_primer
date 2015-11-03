# Exercise 5.13
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt
import sys

g = 9.81
params = np.array(sys.argv[1:], dtype=np.float)
try:
    v0, theta, y0 = params[0], params[1] * np.pi / 180, params[2]
except ValueError:
    print 'v0, theta and y0 must be provided on the command-line'
    sys.exit(1)


def y(x, y0, theta, v0):
    return x * np.tan(theta) - 1. / (2 * v0 ** 2) * g * x ** 2 / \
        (np.cos(theta) ** 2) + y0

vh = v0 * np.cos(theta)
vv = v0 * np.sin(theta)

t_land = (vv + np.sqrt(vv ** 2 + 2 * g * y0)) / g

xlist = np.linspace(0, t_land * vh, 2000)
ylist = y(xlist, y0, theta, v0)

ax = plt.subplot(111)
ax.plot(xlist, ylist)
ax.set_xlabel('Horizontal Distance (m)')
ax.set_ylabel('Height (m)')
ax.set_ylim([0, ylist.max() + 10])
ax.set_xlim([0, xlist[-1]])
plt.show()
