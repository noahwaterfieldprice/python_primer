from numpy import sqrt, exp, pi
from matplotlib.pyplot import plot, show


def h(x):
    return 1 / sqrt(2 * pi) * exp(-0.5 * x * x)

n = 41
dx = 8. / (n - 1)

xlist = [-4 + i * dx for i in range(n)]
hlist = [h(x) for x in xlist]

plot(xlist, hlist)
show()
