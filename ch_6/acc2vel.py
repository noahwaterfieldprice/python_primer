# Excercise 6.6
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt
import sys


def velocity(a, dt):
    n = len(a)
    v = np.zeros(n)
    for k in xrange(1, n):
        v[k] = v[k-1] + (a[k-1] + a[k])/2
    v *= dt
    return v

try:
    dt = float(sys.argv[1])
except IndexError:
    print 'dt must be given on the command line'
    sys.exit(1)

acc = np.loadtxt('acc.dat')
vel = velocity(acc, dt)
time = np.array([i * dt for i in range(0, len(acc))])

plt.plot(time, acc, color='#053061', linewidth=1.5)
plt.plot(time, vel, color='#67001f', linewidth=1.5)
plt.xlabel('Time')
plt.legend(['Acceleration', 'Velocity'], loc=2)
plt.title('Time dependence of object acceleration and velocity')
plt.show()