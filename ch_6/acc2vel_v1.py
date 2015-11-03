# Excercise 6.5
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt
import sys


def velocity(a, k, dt):
    v = (a[k]) / 2   # a[0] is assumed to be 0
    for i in xrange(1, k):
        v += a[i]
    v *= dt
    return v

try:
    k = int(sys.argv[1])
    dt = float(sys.argv[2])
except IndexError:
    print 'k and dt must be given on the command line'
    sys.exit(1)

acc = np.loadtxt('acc.dat')
time = np.array([i * dt for i in range(0, len(acc))])
print 'Average velocity over first %d steps = %f' % (k, velocity(acc, k, dt))

plt.plot(time, acc, color='#053061', linewidth=1.5)
plt.xlabel('Time')
plt.ylabel('Acceleration')
plt.title('Time dependence of object acceleration along a straight line')
plt.show()

"""
Sample run:
python acc2vel_v1.py 100 0.1
Average velocity over first 100 steps = 5.617364
"""
