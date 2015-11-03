# Exercise 2.6
# Author: Noah Waterfield Price

v0 = 1
g = 9.81
n = 11
dt = 2 * v0 / g / (n - 1)

print '%6s %6s' % ('t', 'y')
for i in range(0, n):
    t = i * dt
    y = v0 * t - 0.5 * g * t ** 2
    print '%6.3f %6.3f' % (t, y)

"""
Sample run:
python ball_table1.py
     t      y
 0.000  0.000
 0.020  0.018
 0.041  0.033
 0.061  0.043
 0.082  0.049
 0.102  0.051
 0.122  0.049
 0.143  0.043
 0.163  0.033
 0.183  0.018
 0.204  0.000
"""
