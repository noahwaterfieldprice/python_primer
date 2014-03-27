from scitools.std import sqrt, pi, exp, linspace, plot, movie
import time
import glob
import os

# Clean up old frames
for name in glob.glob('tmp_*.png'):
    os.remove(name)


def f(x, m, s):
    return (1.0 / (sqrt(2 * pi) * s)) * exp(-0.5 * ((x - m) / s) ** 2)

m = 0
s_min = 0.2
s_max = 2
x = linspace(m - 3 * s_max, m + 3 * s_max, 1000)
s_values = linspace(s_min, s_max, 30)
# f is max for x=m; smaller s gives a larger max value
max_f = f(m, m, s_min)

# Show the movie on the screen
# and make hardcopies of frames simultaneously

counter = 0
for s in s_values:
    y = f(x, m, s)
    plot(x, y, axis=[x[0], x[-1], -0.1, max_f],
         xlabel='x', ylabel='f', legend='s=%4.2f' % s,
         savefig='tmp_%04d.png' % counter)
    counter += 1

movie('tmp*.png')
