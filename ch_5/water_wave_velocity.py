# Exercise 5.20
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt


def c(l, h=5000):
    g = 981
    s = 7.9e-4
    p = 1
    return np.sqrt(g * l / (2 * np.pi) *
                   (1 + s * 4 * np.pi ** 2 / (p * g * l ** 2)) *
                   np.tanh(2 * np.pi * h / l))

l = np.linspace(0.1, 5000, 50000)
plt.plot(l, c(l))
plt.xlabel('wavelength (cm)')
plt.ylabel('speed (cm/s)')
plt.show()

l = np.linspace(100, 200000, 50000)
plt.plot(l, c(l))
plt.xlabel('wavelength (cm)')
plt.ylabel('speed (cm/s)')
plt.show()
