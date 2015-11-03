# Exercise 5.21
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def S(x, n):
    ans = 0
    for j in range(n + 1):
        ans += (-1) ** j * x ** (2 * j + 1) / factorial(2 * j + 1)
    return ans

x = np.linspace(0, 4 * np.pi, 1001)

plt.plot(x, np.sin(x), '--k', linewidth=2)
for n in [1, 2, 3, 6, 12]:
    plt.plot(x, S(x, n))

plt.ylim([-1.1, 1.1])
plt.legend(['n = 1', 'n = 2', 'n = 3', 'n = 6', 'n = 12', 'sin(x)'])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
