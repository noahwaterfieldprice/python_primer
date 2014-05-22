# Exercise 7.16
class Derivative_protected:

    def __init__(self, f, h=1E-5):
        self._f = f
        self._h = float(h)

    def __call__(self, x):
        f, h = self._f, self._h
        return (f(x + h) - f(x)) / h

    def get_precision(self):
        return self._h

    def set_precision(self, h):
        self._h = h


def table(f, x, hlist, dfdx):
    d = Derivative_protected(f)
    print '=' * 57
    print '%-14s %-14s %-15s %-15s' \
        % ('x=%g' % x, "f' (exact)", "f' (approx.)", 'Error')
    print '-' * 57
    for h in hlist:
        d.set_precision(h)
        print 'h = %-8.2E | %11.6E   %11.6E   %11.6E' \
            % (h, dfdx(x), d(x), dfdx(x) - d(x))
    print '=' * 57 + '\n'

from math import log
hlist = [2 ** (-k) for k in range(1, 49, 4)]
table(log, 1, hlist, lambda x: 1. / x)

"""
Sample run:
python Derivative_protected.py
=========================================================
x=1            f' (exact)     f' (approx.)    Error
---------------------------------------------------------
h = 5.00E-01 | 1.000000E+00   8.109302E-01   1.890698E-01
h = 3.12E-02 | 1.000000E+00   9.846931E-01   1.530692E-02
h = 1.95E-03 | 1.000000E+00   9.990247E-01   9.752928E-04
h = 1.22E-04 | 1.000000E+00   9.999390E-01   6.103019E-05
h = 7.63E-06 | 1.000000E+00   9.999962E-01   3.814678E-06
h = 4.77E-07 | 1.000000E+00   9.999998E-01   2.384185E-07
h = 2.98E-08 | 1.000000E+00   1.000000E+00   1.490116E-08
h = 1.86E-09 | 1.000000E+00   1.000000E+00   9.313226E-10
h = 1.16E-10 | 1.000000E+00   1.000000E+00   5.820766E-11
h = 7.28E-12 | 1.000000E+00   1.000000E+00   3.637979E-12
h = 4.55E-13 | 1.000000E+00   1.000000E+00   2.273737E-13
h = 2.84E-14 | 1.000000E+00   1.000000E+00   1.421085E-14
=========================================================
"""
