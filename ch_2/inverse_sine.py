# Exercise 2.15
# Author: Noah Waterfield Price

from math import asin, pi

n = 10
x_list = [i * 1. / n for i in range(n + 1)]

print '------------------'
print '%-3s %13s ' % ('x', 'arcsin(x)')
for x in x_list:
    print '%-3.2f %12.2f' % (x, asin(x) * 180 / pi)
print '------------------'

"""
Sample run:
python inverse_sin.py
------------------
x       arcsin(x)
0.00         0.00
0.10         5.74
0.20        11.54
0.30        17.46
0.40        23.58
0.50        30.00
0.60        36.87
0.70        44.43
0.80        53.13
0.90        64.16
1.00        90.00
------------------*
"""
