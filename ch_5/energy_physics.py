# Exercise 5.34
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt
import sys

m = float(sys.argv[1])
v0 = float(sys.argv[2])
g = 9.81

t = np.linspace(0, 2 * v0 / g, 501)
y = v0 * t - 0.5 * g * t ** 2
v = v0 - g * t
P = m * g * y
K = 0.5 * m * v ** 2

plt.plot(t, P, linewidth=2, color='#67001f')
plt.plot(t, K, linewidth=2, color='#053061')
plt.plot(t, P + K, '--', linewidth=2, color='#006837')
plt.xlim([t[0], t[-1]])
plt.ylim([0, 1.3 * P.max()])
plt.legend(['Potential Energy', 'Kinetic Energy', 'Total Energy'])
plt.show()
