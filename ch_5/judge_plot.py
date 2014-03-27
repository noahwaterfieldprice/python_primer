import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 20)
y = np.cos(18 * np.pi * x)
plt.plot(x, y)

x = np.linspace(0, 2, 1000)
y = np.cos(18 * np.pi * x)
plt.plot(x, y)

plt.show()
