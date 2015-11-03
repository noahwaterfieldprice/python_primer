# Exercise 2.22
# Author: Noah Waterfield Price

from math import sqrt
for n in range(1, 60):
    r = 2.0
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r ** 2
    print '%d times sqrt and **2: %.16f' % (n, r)

"""
Sample run:
python repeated_sqrt.py
1 times sqrt and **2: 2.0000000000000004
2 times sqrt and **2: 1.9999999999999996
3 times sqrt and **2: 1.9999999999999996
....
58 times sqrt and **2: 1.0000000000000000
59 times sqrt and **2: 1.0000000000000000
"""

"""
1 is returned for n >= 52 as square rooting 2 52 times reduces
it to 1.0 to the degree of accuracy available in a Python float.
1 squared any number of times is still 1 so the second operation
leaves the number unchanged and 2 is not recovered
"""
