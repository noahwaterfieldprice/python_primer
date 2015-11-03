# Exercise 6.2
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt
import sys


def load(densityfile):
    infile = open(densityfile, 'r')
    data = {'temperature': [], 'density': []}

    for line in infile:
        if line.isspace() or line.lstrip()[0] == '#':   # blank line or comment
            continue
        else:
            values = line.split()
            data['temperature'].append(float(values[0]))
            data['density'].append(float(values[1]))
    data['temperature'] = np.array(data['temperature'])
    data['density'] = np.array(data['density'])
    infile.close()
    return data


def plot_data(x, y, substance):
    plt.plot(x, y, 'o',
             markerfacecolor='#2166ac',
             markeredgecolor='#053061',
             markersize=8,
             markeredgewidth=1.5)
    plt.xlabel('Temperature')
    plt.ylabel('Density')
    plt.title('Temperature dependence of %s density' % substance)
    # set axis ranges appropriately
    x_range = x.max() - x.min()
    y_range = y.max() - y.min()
    plt.xlim([x.min() - 0.1 * x_range, x.max() + 0.1 * x_range])
    plt.ylim([y.min() - 0.1 * y_range, y.max() + 0.1 * y_range])
    plt.show()


try:
    densityfile = sys.argv[1]
    substance = sys.argv[2]
except IndexError:
    print 'The density file name and substance must be given \
        on the command line'
    sys.exit(1)

data = load(densityfile)
plot_data(data['temperature'], data['density'], substance)
