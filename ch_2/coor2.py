# Exercise 2.11
# Author: Noah Waterfield Price

h = 0.01
x = [1 + i * h for i in range(0, 101)]
for xval in x:
    print '%3.2f' % xval,

"""
Sample run:
python coor1.py
1.00 1.01 1.02 1.03 1.04 1.05 1.06 ... 1.98 1.99 2.00
"""
