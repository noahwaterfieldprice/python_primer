# Excercise 6.1
# Author: Noah Waterfield Price

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

infile = open('write_cml_function.txt', 'r')
for line in infile:
    coords = line.split()
    x.append(float(coords[0]))
    y.append(float(coords[1]))
infile.close()

x, y = np.array(x), np.array(y)

print 'Minimum x value = %f' % x.min()
print 'Maximum x value = %f' % x.max()
print 'Minimum y value = %f' % y.min()
print 'Maximum y value = %f' % y.max()

plt.plot(x, y, color='#053061', linewidth=1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""
Sample run:
python read_2columns.py
Minimum x value = -1.000000
Maximum x value = 1.000000
Minimum y value = -0.948200
Maximum y value = 0.948200
"""
    