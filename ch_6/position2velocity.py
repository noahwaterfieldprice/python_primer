# Exercise 6.7
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt

# Read first line (dt) into variable s
infile = open('pos.dat', 'r')
s = float(infile.readline().strip())
infile.close()
# Read rest of file into x and y
x, y = np.loadtxt('pos.dat', skiprows=1, unpack=True)
plt.plot(x, y, '.--', color='#053061', markersize=10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('GPS position (%is time steps)' % s)
plt.show()

vx, vy = [], []
for k in range(len(x) - 1):
    vx.append((x[k + 1] - x[k]) / s)
    vy.append((y[k + 1] - y[k]) / s)
t = [i * s for i in xrange(len(x) - 1)]

plt.plot(t, vx, color='#053061', linewidth=1.5)
plt.plot(t, vy, color='#67001f', linewidth=1.5)
plt.xlabel('Time (s)')
plt.legend(['x-velocity', 'y-velocity'])
plt.title('GPS velocity (%is time steps)' % s)
plt.show()
