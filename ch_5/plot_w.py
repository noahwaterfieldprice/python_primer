# Exercise 5.35
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    r = np.zeros(len(x))
    r[x < 0] = -x[x < 0] - 5
    r[x >= 0] = x[x >= 0] - 5
    return abs(r)

x = np.linspace(-10, 10, 101)
plt.plot(x, f(x))
plt.show()
