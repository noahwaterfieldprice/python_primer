# Exercise 8.20
# Author: Noah Waterfield Price

from time import time
from scitools.std import plot, compute_histogram


def diff_eq(x, a, c, m):
    xn = (a * x + c) % m
    yn = float(xn) / m
    return xn, yn


def rand_gen(a, c, m, N=10, x=time()):
    r = []
    for i in range(N):
        x, y = diff_eq(x, a, c, m)
        r.append(y)
    return r

a = 8121
c = 28411
m = 134456
N = 1000000
random_nos = rand_gen(a, c, m, N)
x, y = compute_histogram(random_nos, nbins=50)
plot(x, y, title='%d samples of psuedo-random numbers generated on (0, 1)' % N)
raw_input()
