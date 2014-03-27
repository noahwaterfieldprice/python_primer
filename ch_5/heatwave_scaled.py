from scitools.std import linspace, exp, cos, pi, movie, plot
import sys


def animate(tmax, dt, x, function, ymin, ymax, t0=0,
            xlabel='x', ylabel='y', filename='tmp_'):
    t = t0
    counter = 0
    while t <= tmax:
        y = function(x, t)
        plot(x, y,
             axis=[x[0], x[-1], ymin, ymax],
             title='time=%g' % t,
             xlabel=xlabel, ylabel=ylabel,
             savefig=filename + '%04d.png' % counter,
             show=False)
        t += dt
        counter += 1


def T(z, t):
    return exp(-b * z) * cos(t - b * z)  # b is global

b = float(sys.argv[1])
n = 401
z = linspace(0, 1, n)
animate(3 * 2 * pi, 0.01 * 2 * pi, z, T, -1.2, 1.2, 0, 'z', 'T')
movie('tmp_*.png', encoder='convert', fps=12,
      output_file='tmp_heatwave.gif')


import glob
import os
# Remove old plot files
for filename in glob.glob('tmp_*.png'):
    os.remove(filename)
