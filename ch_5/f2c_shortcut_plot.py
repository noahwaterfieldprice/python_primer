# Exercise 5.12
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt


def exact_conv(F):
    return 5 / 9. * (F - 32)


def approx_conv(F):
    return 0.5 * (F - 30)

Flist = np.linspace(-20, 120, 141)

ax = plt.subplot(111)

ax.plot(Flist, exact_conv(Flist))
ax.plot(Flist, approx_conv(Flist))
ax.set_xlabel('Farenheit')
ax.set_ylabel('Celsius')

plt.show()
