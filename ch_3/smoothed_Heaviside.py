# Exercise 3.25
# Author: Noah Waterfield Price

from math import sin, pi


def smoothed_Heaviside(x, e=1E-2):
    if x < -e:
        return 0
    elif -e <= x <= e:
        return 0.5 + x / (2 * e) + 1 / (2 * pi) * sin(pi * x / e)
    elif x > e:
        return 1

print smoothed_Heaviside(-1)
print smoothed_Heaviside(-0.01)
print smoothed_Heaviside(-0.001)
print smoothed_Heaviside(0.001)
print smoothed_Heaviside(0.01)
print smoothed_Heaviside(1)

"""
Sample run:
python smoothed_Heaviside.py
0
-1.94908591626e-17
0.400818417846
0.599181582154
1.0
1
"""
