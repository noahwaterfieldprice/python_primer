# Exercise 5.2
from numpy import sqrt, exp, pi, linspace, zeros
from matplotlib.pyplot import plot, show


def h(x):
    return 1 / sqrt(2 * pi) * exp(-0.5 * x * x)

xlist = linspace(-4, 4, 41)
hlist = zeros(len(xlist))

for i in xrange(len(xlist)):
    hlist[i] = h(xlist[i])

plot(xlist, hlist)
show()
