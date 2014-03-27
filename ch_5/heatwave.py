# Example 5.8.2 - Animating a Function

from scitools.std import *


def animate(tmax, dt, x, function, ymin, ymax, t0=0,
            xlabel='x', ylabel='y', filename='tmp_'):
    t = t0
    counter = 0
    while t <= tmax:
        y = function(x, t)
        plot(x, y,
             axis=[x[0], x[-1], ymin, ymax],
             title='time-%2d h' % (t / 3600.0),
             xlabel=xlabel, ylabel=ylabel,
             savefig=filename + '%04d.png' % counter,
             show=False)
        t += dt
        counter += 1


def T(z, t):
    # T0, A, k, and omega are global variables
    a = sqrt(omega / (2 * k))
    return T0 + A * exp(-a * z) * cos(omega * t - a * z)

k = 1E-6     # thermal diffusivity (in m**2/s)
P = 24 * 60 * 60.  # oscillation period of 24 h (in seconds)
omega = 2 * pi / P
dt = P / 48    # time lag: 1 h
tmax = 3 * P   # 3 day/night simulations
T0 = 10      # mean surface temperature in Celsius
A = 10       # amplitude of the temperature variations (in C)
a = sqrt(omega / (2 * k))
D = -(1 / a) * log(0.001)  # max depth
n = 501      # no of points in the z direction

# set T0, A, k, omega, D, n, tmax, dt
z = linspace(0, D, n)
animate(tmax, dt, z, T, T0 - a, T0 + a, 0, 'z', 'T')

movie('tmp_*.png', encoder='convert', fps=12, outputfile='tmp_heatwave.gif')

import glob
import os
# Remove old plot files
for filename in glob.glob('tmp_*.png'):
    os.remove(filename)
