# Exercise 5.26
# Author: Noah Waterfield Price

from scitools.std import sqrt, pi, cos, sin, plot, movie
import glob
import os


def pathlength(x, y):
    L = 0
    for i in xrange(1, len(x)):
        dL_squared = (x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2
        L += sqrt(dL_squared)
    return L


def points(N):
    x = [0.5 * cos(2 * pi * i / N) for i in range(N + 1)]
    y = [0.5 * sin(2 * pi * i / N) for i in range(N + 1)]
    return x, y


def pi_approx(N):
    x, y = points(N)
    return pi - pathlength(x, y)

circle = points(100000)

for N in xrange(4, 100):
    x, y = points(N)
    plot(x, y, circle[0], circle[1],
         title='Error in approximating pi: %8f' % pi_approx(N),
         xlabel='x',
         ylabel='y',
         savefig='tmp_' + 'N=%03d.png' % N,
         show=False
         )

movie('tmp_*.png', encoder='convert', fps=6, outputfile='pi_polygon_movie.gif')

# Remove frames
for filename in glob.glob('tmp_*.png'):
    os.remove(filename)
