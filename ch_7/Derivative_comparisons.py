# Exercise 7.15
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt


class Central:

    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x + h) - f(x - h)) / (2 * h)


class Derivative:

    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x + h) - f(x)) / h


def table(f, x, hlist, dfdx=None):
    print '=' * 54
    header = '%-11s %-14s %-15s' % ('x=%g' % x, "f' (deriv.)", "f' (cent.)")
    if dfdx is not None:
        header += '%-14s' % "f' (exact)"
    print header
    print '-' * 54
    for h in hlist:
        d = Derivative(f, h)
        c = Central(f, h)
        row = 'h = %-5.0E | %11.6E   %11.6E   ' % (h, d(x), c(x))
        if dfdx is not None:
            row += '%12.6E' % dfdx(x)
        print row
    print '=' * 54 + '\n'


def plot_derivaties(axes, f, x, dfdx, h=1E-5, title=None):
    c = Central(f, h)
    d = Derivative(f, h)
    axes.plot(x, dfdx(x))
    axes.plot(x, d(x))
    axes.plot(x, c(x))
    axes.legend(['Exact', 'Derivative', 'Central'])
    axes.set_title(title)

fig, ax = plt.subplots(3, sharex=True)
xlist = np.linspace(-1, 1, 500)

# compare numerical derivates of x^2
print '\nf = x^2'
hlist = (0.5, 0.1, 1E-3, 1E-5, 1E-7, 1E-9)
f = lambda x: x ** 2
dfdx = lambda x: 2 * x
table(f, 0, hlist, dfdx)
table(f, 0.25, hlist, dfdx)
plot_derivaties(ax[0], f, xlist, dfdx, h=0.1, title='df/dx = 2x')

# compare numerical derivates of sech^6(pi*x)
print '\nf = sinh^6(pi*x)'
f = lambda x: np.sin(np.pi * x) ** 6
dfdx = lambda x: 6 * np.pi * np.sin(np.pi * x) ** 5 * np.cos(np.pi * x)
table(f, 0, hlist, dfdx)
table(f, 0, hlist, dfdx)
plot_derivaties(ax[1], f, xlist, dfdx, h=0.1,
                title='df/dx = 6pi*cos(pi*x)*sin^5(pi*x)')

# compare numerical derivates of tanh(10x)
print '\nf = tanh(10x)'
f = lambda x: np.tanh(10 * x)
dfdx = lambda x: 10 / np.cosh(10 * x) ** 2
table(f, 0, hlist, dfdx)
table(f, 0.25, hlist, dfdx)
plot_derivaties(ax[2], f, xlist, dfdx, h=0.1,  title='df/dx = 10sech^2(10x)')

plt.show()

"""
Sample run:
python Derivative_comparisons.py

f = x^2
======================================================
x=0         f' (deriv.)    f' (cent.)     f' (exact)
------------------------------------------------------
h = 5E-01 | 5.000000E-01   0.000000E+00   0.000000E+00
h = 1E-01 | 1.000000E-01   0.000000E+00   0.000000E+00
h = 1E-03 | 1.000000E-03   0.000000E+00   0.000000E+00
h = 1E-05 | 1.000000E-05   0.000000E+00   0.000000E+00
h = 1E-07 | 1.000000E-07   0.000000E+00   0.000000E+00
h = 1E-09 | 1.000000E-09   0.000000E+00   0.000000E+00
======================================================

======================================================
x=0.25      f' (deriv.)    f' (cent.)     f' (exact)
------------------------------------------------------
h = 5E-01 | 1.000000E+00   5.000000E-01   5.000000E-01
h = 1E-01 | 6.000000E-01   5.000000E-01   5.000000E-01
h = 1E-03 | 5.010000E-01   5.000000E-01   5.000000E-01
h = 1E-05 | 5.000100E-01   5.000000E-01   5.000000E-01
h = 1E-07 | 5.000001E-01   5.000000E-01   5.000000E-01
h = 1E-09 | 5.000000E-01   5.000000E-01   5.000000E-01
======================================================


f = sinh^6(pi*x)
======================================================
x=0         f' (deriv.)    f' (cent.)     f' (exact)
------------------------------------------------------
h = 5E-01 | 2.000000E+00   0.000000E+00   0.000000E+00
h = 1E-01 | 8.707514E-03   0.000000E+00   0.000000E+00
h = 1E-03 | 9.613797E-13   0.000000E+00   0.000000E+00
h = 1E-05 | 9.613892E-23   0.000000E+00   0.000000E+00
h = 1E-07 | 9.613892E-33   0.000000E+00   0.000000E+00
h = 1E-09 | 9.613892E-43   0.000000E+00   0.000000E+00
======================================================

======================================================
x=0         f' (deriv.)    f' (cent.)     f' (exact)
------------------------------------------------------
h = 5E-01 | 2.000000E+00   0.000000E+00   0.000000E+00
h = 1E-01 | 8.707514E-03   0.000000E+00   0.000000E+00
h = 1E-03 | 9.613797E-13   0.000000E+00   0.000000E+00
h = 1E-05 | 9.613892E-23   0.000000E+00   0.000000E+00
h = 1E-07 | 9.613892E-33   0.000000E+00   0.000000E+00
h = 1E-09 | 9.613892E-43   0.000000E+00   0.000000E+00
======================================================


f = tanh(10x)
======================================================
x=0         f' (deriv.)    f' (cent.)     f' (exact)
------------------------------------------------------
h = 5E-01 | 1.999818E+00   1.999818E+00   1.000000E+01
h = 1E-01 | 7.615942E+00   7.615942E+00   1.000000E+01
h = 1E-03 | 9.999667E+00   9.999667E+00   1.000000E+01
h = 1E-05 | 1.000000E+01   1.000000E+01   1.000000E+01
h = 1E-07 | 1.000000E+01   1.000000E+01   1.000000E+01
h = 1E-09 | 1.000000E+01   1.000000E+01   1.000000E+01
======================================================

======================================================
x=0.25      f' (deriv.)    f' (cent.)     f' (exact)
------------------------------------------------------
h = 5E-01 | 2.677018E-02   1.986614E+00   2.659223E-01
h = 1E-01 | 1.156360E-01   4.651482E-01   2.659223E-01
h = 1E-03 | 2.633156E-01   2.659393E-01   2.659223E-01
h = 1E-05 | 2.658960E-01   2.659223E-01   2.659223E-01
h = 1E-07 | 2.659220E-01   2.659223E-01   2.659223E-01
h = 1E-09 | 2.659223E-01   2.659223E-01   2.659223E-01
======================================================
"""
