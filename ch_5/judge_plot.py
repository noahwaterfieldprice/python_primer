# Exercise 5.18
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 20)
y = np.cos(18 * np.pi * x)
plt.plot(x, y)

x = np.linspace(0, 2, 1000)
y = np.cos(18 * np.pi * x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['20 points','2000 points'])
plt.title('y = cos(18*pi*x')
plt.show()
