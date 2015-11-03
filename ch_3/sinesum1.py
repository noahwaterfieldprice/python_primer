# Exercise 3.13
# Author: Noah Waterfield Price

from math import sin, pi


def S(t, n, T):
    s = 0
    for i in range(1, n + 1):
        s += 1.0 / (2 * i - 1) * sin(2 * (2 * i - 1) * pi * t / T)
    s *= 4 / pi
    return s


def f(t, T):
    if 0 < t < T / 2:
        ans = 1
    elif abs(t - T / 2) < 1E-14:
        ans = 0
    elif T / 2 < t < T:
        ans = -1
    else:
        print 'Error: t must be between 0 and T'
        ans = None
    return ans

n_list = [1, 3, 5, 10, 30, 100]
alpha_list = 0.01, 0.25, 0.49
T = 2 * pi
t_list = [2 * alpha * T for alpha in alpha_list]

for n in n_list:
    print 'n = %d' % n
    print '  Function t=%.2f*pi t=%.2f*pi t=%.2f*pi' % (0.01, 0.25, 0.49)
    print '%10s %.7f %.7f %.7f' % ('f(t, T)',
                                   f(t_list[0], T),
                                   f(t_list[1], T),
                                   f(t_list[2], T))
    print '%10s %.7f %.7f %.7f' % ('S(t, n, T)',
                                   S(t_list[0], n, T),
                                   S(t_list[1], n, T),
                                   S(t_list[2], n, T))
    print '%10s %.7f %.7f %.7f' % ('Error',
                                   abs(S(t_list[0], n, T) - f(t_list[0], T)),
                                   abs(S(t_list[0], n, T) - f(t_list[0], T)),
                                   abs(S(t_list[0], n, T) - f(t_list[0], T)))
    print ''

"""
Sample run:
python sinesum1.py
n = 1
  Function t=0.01*pi t=0.25*pi t=0.49*pi
   f(t, T) 1.0000000 0.0000000 -1.0000000
S(t, n, T) 0.1595792 0.0000000 -0.1595792
     Error 0.8404208 0.8404208 0.8404208

n = 3
  Function t=0.01*pi t=0.25*pi t=0.49*pi
   f(t, T) 1.0000000 0.0000000 -1.0000000
S(t, n, T) 0.4654944 0.0000000 -0.4654944
     Error 0.5345056 0.5345056 0.5345056

n = 5
  Function t=0.01*pi t=0.25*pi t=0.49*pi
   f(t, T) 1.0000000 0.0000000 -1.0000000
S(t, n, T) 0.7336510 0.0000000 -0.7336510
     Error 0.2663490 0.2663490 0.2663490

n = 10
  Function t=0.01*pi t=0.25*pi t=0.49*pi
   f(t, T) 1.0000000 0.0000000 -1.0000000
S(t, n, T) 1.1349367 0.0000000 -1.1349367
     Error 0.1349367 0.1349367 0.1349367

n = 30
  Function t=0.01*pi t=0.25*pi t=0.49*pi
   f(t, T) 1.0000000 0.0000000 -1.0000000
S(t, n, T) 0.9648738 0.0000000 -0.9648738
     Error 0.0351262 0.0351262 0.0351262

n = 100
  Function t=0.01*pi t=0.25*pi t=0.49*pi
   f(t, T) 1.0000000 0.0000000 -1.0000000
S(t, n, T) 0.9746817 0.0000000 -0.9746817
     Error 0.0253183 0.0253183 0.0253183
"""
