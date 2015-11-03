# Exercise 5.28
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt
from scitools.std import movie


def animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact, exactname):
    x = np.linspace(xmin, xmax, n)
    s = np.zeros(len(x))
    counter = 1
    for k in range(M, N + 1):
        s += fk(x, k)
        plt.plot(x, s, linewidth=2, color='#67001f')
        plt.hold(1)
        plt.plot(x, exact(x), '--', linewidth=2, color='#053061')
        plt.hold(0)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.legend(['Taylor series approximation - %d terms' %
                   counter, exactname])
        plt.savefig('tmp_%04d.png' % counter)
        counter += 1


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def f1(x, k):
    return (-1) ** k * x ** (2 * k + 1) / factorial(2 * k + 1)


def f2(x, k):
    return (-x) ** k / factorial(k)


def exp(x):
    return np.exp(-x)

#animate_series(f1, 0, 40, 0, 13*np.pi, -2, 2, 500, np.sin, 'sin(x)')
animate_series(f2, 0, 30, 0, 15, -0.5, 1.4, 500, exp, 'exp(-x)')
movie('tmp_*.png', encoder='convert', fps=3)

import glob
import os
# Remove old plot files
for filename in glob.glob('tmp_*.png'):
    os.remove(filename)
