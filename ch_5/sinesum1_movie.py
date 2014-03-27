# Exercise 5.31
import numpy as np
import matplotlib.pyplot as plt
import operator
from scitools.std import movie


def animate_series(fk, N, tmax, n, exact, exactname):
    t = np.linspace(0, tmax, n)
    s = np.zeros(len(t))
    counter = 1
    for k in range(0, N + 1):
        s = S(t, k, tmax)
        plt.plot(t, s, linewidth=2, color='#67001f')
        plt.hold(1)
        plt.plot(t, exact(t, tmax), '--', linewidth=2, color='#053061')
        plt.hold(0)
        plt.xlim(0, tmax)
        plt.ylim(-1.3, 1.3)
        plt.legend(['Sine sum - %d terms' %
                   counter, exactname])
        plt.savefig('tmp_%04d.png' % counter)
        counter += 1


def S(t, n, T):
    s = np.zeros(len(t))
    for i in range(1, n + 1):
        s += 1.0 / (2 * i - 1) * np.sin(2 * (2 * i - 1) * np.pi * t / T)
    s *= 4 / np.pi
    return s


def f(t, T):
    cond1 = operator.and_(0 <= t, t < T / 2.)
    cond2 = abs(t - T / 2.) < 1E-16
    cond3 = operator.and_(T / 2. < t, t <= T)
    cond4 = operator.and_(t < 0, t > T)
    r = np.zeros(len(t))
    r[cond1] = 1
    r[cond2] = 0
    r[cond3] = -1
    r[cond4] = 111   # Error code
    if len(r[r == 111]) > 0:
        print 'Error: t must be between 0 and T'
        r = None
    return r

animate_series(S, 50, 20, 1001, f, 'f(t)')
movie('tmp_*.png', encoder='convert', fps=3)

import glob
import os
# Remove old plot files
for filename in glob.glob('tmp_*.png'):
    os.remove(filename)
