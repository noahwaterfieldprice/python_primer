# Exercise 3.28
# Author: Noah Waterfield Price

def heaviside1(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1

# need two step functions as conditions swap round when argument is -x


def heaviside2(x):
    if x >= 0:
        return 0
    elif x < 0:
        return 1


def indicator2(x, a, b):
    return heaviside1(x - a) * heaviside2(x - b)


def piecewise(x, data):
    s = 0
    for i in range(len(data) - 1):
        s += data[i][0] * indicator2(x, data[i][1], data[i + 1][1])
    return s

# need last pair to define final x interval
data = [(20, -2), (-1, 0), (0, 1), (4, 1.5), (-7, 4), (23, 6.3), (None, 7.5)]

for x in range(-1, 8):
    print piecewise(x, data)

"""
Sample run:
python piecewise_constant2.py
20
-1
0
4
4
-7
-7
-7
23
"""
