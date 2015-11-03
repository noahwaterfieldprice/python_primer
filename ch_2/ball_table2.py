# Exercise 2.7
# Author: Noah Waterfield Price

v0 = 10
g = 9.81
n = 81
dt = 2 * v0 / g / (n - 1)

t = [i * dt for i in range(0, n)]
y = [v0 * t[i] - 0.5 * g * t[i] ** 2 for i in range(0, n)]

print '%6s %6s' % ('t', 'y')
for tval, yval in zip(t, y):
    print '%6.3f %6.3f' % (tval, yval)
"""
Sample run:
python ball_table2.py
     t      y
 0.000  0.000
 0.025  0.252
 0.051  0.497
 0.076  0.736
 ....
 1.962  0.736
 1.988  0.497
 2.013  0.252

"""
