# Exercise 3.26
# Author: Noah Waterfield Price

def indicator1(x, a, b):
    if a <= x <= b:
        return 1
    else:
        return 0


def heaviside(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1


def indicator2(x, a, b):
    return heaviside(x - a) * heaviside(b - x)

a = -1
b = 2
for x in xrange(-3, 4):
    print indicator1(x, a, b) == indicator2(x, a, b)

"""
Sample run:
python indicator_func.py
True
True
True
True
True
True
True
"""
