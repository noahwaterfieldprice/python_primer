# Exercise 6.11
# Author: Noah Waterfield Price

import matplotlib.pyplot as plt

infile = open('lnsum.dat', 'r')
lines = []
for line in infile:
    if line.find('epsilon') != -1:
        lines.append(line)
infile.close()

data = {'epsilon': [], 'exact error': [], 'n': []}
for line in lines:
    errorinfo = line.split(',')
    data['epsilon'].append(float(errorinfo[0].split(':')[-1]))
    data['exact error'].append(float(errorinfo[1].split(':')[-1]))
    data['n'].append(float(errorinfo[2].split('=')[-1]))

plt.plot(data['n'], data['epsilon'], 'o',
         markerfacecolor='#2166ac',
         markeredgecolor='#053061',
         markersize=8,
         markeredgewidth=1.5)
plt.plot(data['n'], data['exact error'], 's',
         markerfacecolor='#d6604d',
         markeredgecolor='#67001f',
         markersize=8,
         markeredgewidth=1.5)
plt.xlabel('n')
plt.yscale('log')
plt.legend(['Epsilon', 'Exact error'])
plt.show()
