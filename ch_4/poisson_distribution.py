# Exercise 4.26
# Author: Noah Waterfield Price

from math import exp
import sys


def fact(n):
    ans = 1
    if n == 0 or n == 1:
        return ans
    else:
        while n > 0:
            ans *= n
            n -= 1
    return ans


def poisson(x, t, nu):
    P = (1. / fact(x)) * (nu * t) ** x * exp(-nu * t)
    return P

try:
    x = int(sys.argv[1])
    t = float(sys.argv[2])
    nu = float(sys.argv[3])
except IndexError:
    print 'x, t and nu must be provided on the command line'
    sys.exit(1)
except ValueError:
    print 'x, t and nu must be pure numbers'
    sys.exit(1)

print poisson(x, t, nu)

"""
Sample run:
python poisson_distribution.py 0 0.5 5
0.0820849986239
python poisson_distribution.py 0 2 5
4.53999297625e-05
python poisson_distribution.py 2 0.333333333 5
0.262327226076
python poisson_distribution.py 3 10 0.2
0.180447044315
python poisson_distribution.py 0 0.01923  0.2
0.996161386386
python poisson_distribution.py 0 6 6
2.31952283024e-16
"""
