# Exercise 6.25
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt


def fit(x, y):
    plt.plot(x, y, 'o',
             markerfacecolor='#2166ac',
             markeredgecolor='#053061',
             markersize=8,
             markeredgewidth=1.5)

    for deg, linecol in [(1, '#67001f'), (2, '#006837'), (3, '#40004b')]:
        coeff = np.polyfit(x, y, deg)
        y_fit = np.poly1d(coeff)
        print y_fit
        plt.plot(x, y_fit(x), '--',
                 color=linecol,
                 linewidth=1.5)

    # set axis ranges appropriately
    x_range = x.max() - x.min()
    y_range = y.max() - y.min()
    plt.xlim([x.min() - 0.1 * x_range, x.max() + 0.1 * x_range])
    plt.ylim([y.min() - 0.1 * y_range, y.max() + 0.1 * y_range])
    plt.xlabel('Period')
    plt.ylabel('Length')
    plt.title('Length dependence of pendulum period')
    plt.legend(['data',
                'fitted degree 1 polynomial',
                'fitted degree 2 polynomial',
                'fitted degree 3 polynomial'],
               loc=2)
    plt.ylim([0, 1.1])
    plt.show()


length, period = np.loadtxt('pendulum.dat', unpack=True, skiprows=1)
fit(period, length)

"""
Polynomials:

degree 1: 0.6512*x - 0.3813
degree 2: 0.2885*x**2 - 0.1134*x + 0.06792 (Best fit)
degree 3: 0.07176*x**3 + 0.008071*x**2 + 0.2258*x - 0.05583
"""
