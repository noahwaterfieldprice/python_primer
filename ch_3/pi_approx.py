# Exercise 3.11
from math import sin, cos, pi, sqrt


def pathlength(x, y):
    L = 0
    for i in range(1, len(x)):
        dL_squared = (x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2
        L += sqrt(dL_squared)
    return L


def points(N):
    x = [0.5 * cos(2 * pi * i / N) for i in range(N + 1)]
    y = [0.5 * sin(2 * pi * i / N) for i in range(N + 1)]
    return x, y

N_list = [2 ** k for k in range(2, 11)]

for N in N_list:
    x, y = points(N)
    approx = pathlength(x, y)
    print 'For %4d points on the circle, pi approximates to %.8f \
giving and error of %.8f' % \
        (N, approx, pi - approx)

"""
Sample run:
python pi_approx.py
For    4 points on the circle, pi approximates to 2.82842712 giving and error pf 0.31316553
For    8 points on the circle, pi approximates to 3.06146746 giving and error pf 0.08012519
For   16 points on the circle, pi approximates to 3.12144515 giving and error pf 0.02014750
For   32 points on the circle, pi approximates to 3.13654849 giving and error pf 0.00504416
For   64 points on the circle, pi approximates to 3.14033116 giving and error pf 0.00126150
For  128 points on the circle, pi approximates to 3.14127725 giving and error pf 0.00031540
For  256 points on the circle, pi approximates to 3.14151380 giving and error pf 0.00007885
For  512 points on the circle, pi approximates to 3.14157294 giving and error pf 0.00001971
For 1024 points on the circle, pi approximates to 3.14158773 giving and error pf 0.00000493
"""
