# Exercise 5.19
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt


def viscosity(T):
    A = 2.414e-5
    B = 247.8
    C = 140.0
    return A * 10 ** (B / (T + 273.15 - C))

T = np.linspace(0, 100, 10000)

plt.plot(T, viscosity(T))
plt.ylabel('viscosity (Pa s)')
plt.xlabel('temperature (C)')
plt.show()
