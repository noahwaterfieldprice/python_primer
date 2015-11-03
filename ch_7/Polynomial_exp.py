# Exercise 7.29
# Author: Noah Waterfield Price

from Polynomial import Polynomial
from numpy import exp
import sys


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 

x = float(sys.argv[1])
Nlist = sys.argv[2:]
plist = []
for N in Nlist:
    coeffs = [1. / factorial(k) for k in xrange(int(N) + 1)]
    plist.append(Polynomial(coeffs))

print '=' * 35
print '%-5s %-16s %-16s' % ('N', 'Taylor approx.', 'Exact')
print '-' * 35
for N, p in zip(Nlist, plist):
    print '%-5s %-16.12s %-16.12s' % (N, p(x), exp(x))
print '-' * 35

"""
Sample run:
python Polynomial_exp.py 0.5 2 5 10 15 25
===================================
N     Taylor approx.   Exact
-----------------------------------
2     1.625            1.6487212707
5     1.6486979166    1.6487212707
10    1.6487212706     1.6487212707
15    1.6487212707     1.6487212707
25    1.6487212707     1.6487212707
-----------------------------------
python Polynomial_exp.py 3 2 5 10 15 25
===================================
N     Taylor approx.   Exact
-----------------------------------
2     8.5              20.085536923
5     18.4             20.085536923
10    20.079665178     20.085536923
15    20.085534431     20.085536923
25    20.085536923     20.085536923
-----------------------------------
python Polynomial_exp.py 10 2 5 10 15 25
===================================
N     Taylor approx.   Exact
-----------------------------------
2     61.0             22026.465794
5     1477.6666666     22026.465794
10    12842.305114     22026.465794
15    20952.886968     22026.465794
25    22026.076360     22026.465794
-----------------------------------
"""
