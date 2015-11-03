# Exercise 5.17
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt


def wave_packet(x, t):
    return np.exp(-(x - 3 * t) ** 2) * np.sin(3 * np.pi * (x - t))

xlist = np.linspace(-4, 4, 1001)
ylist = wave_packet(xlist, 0)

plt.plot(xlist, ylist)
plt.xlabel('x')
plt.ylabel('amplitude')
plt.show()
