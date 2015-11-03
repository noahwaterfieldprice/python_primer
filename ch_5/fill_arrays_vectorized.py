# Exercise 5.3
# Author: Noah Waterfield Price

from numpy import sqrt, exp, pi, linspace
from matplotlib.pyplot import plot, show, xlabel, ylabel


def h(x):
    return 1 / sqrt(2 * pi) * exp(-0.5 * x * x)

xlist = linspace(-4, 4, 41)
hlist = h(xlist)

plot(xlist, hlist)
xlabel('x')
ylabel('h')
show()
