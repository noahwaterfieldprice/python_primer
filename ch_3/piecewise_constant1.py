# Exercise 3.27
# Author: Noah Waterfield Price

def piecewise(x, data):
    for i in range(len(data) - 1):
        if data[i][1] <= x < data[i + 1][1]:
            return data[i][0]

# need last pair to define final x interval
data = [(20, -2), (-1, 0), (0, 1), (4, 1.5), (-7, 4), (23, 6.3), (None, 7.5)]

for x in range(-1, 8):
    print piecewise(x, data)

"""
Sample run:
python piecewise_constant1.py
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
