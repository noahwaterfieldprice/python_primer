# Exercise 2.24
# Author: Noah Waterfield Price

a = 1 / 947.0 * 947
b = 1
if a != b:
    print 'Wrong result!'

a = 1 / 947.0 * 947
b = 1
if abs(a - b) > 1e-15:
    print 'Wrong result!'

"""
Sample run:
python compare_float.py
Wrong result!
"""
