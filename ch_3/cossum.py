# Exercise 3.30
# Author: Noah Waterfield Price

def C(x, n):
    term = 1
    s = term
    for j in xrange(1, n + 1):
        term *= -x ** 2 / (2. * j * (2. * j - 1.))
        s += term
    return s


def table(x_list):
    from math import cos
    print '%7s %9s %9s %9s %9s %9s ' % ('x', 'n=5', 'n=25', 'n=50', 'n=100',
                                        'n=200')
    for x in x_list:
        errors = [x]
        for n in [5, 25, 50, 100, 200]:
            errors.append(cos(x) - C(x, n))
        print '%.4f %9.2e %9.2e %9.2e %9.2e %9.2e' % tuple(errors)

from math import pi
x_list = [4 * pi, 6 * pi, 8 * pi, 10 * pi]

table(x_list)
"""
Sample run:
python cossum.py
      x       n=5      n=25      n=50     n=100     n=200 
12.5664  1.61e+04  1.45e-11 -2.44e-12 -2.44e-12 -2.44e-12
18.8496  1.22e+06  2.28e-02  2.34e-10  2.34e-10  2.34e-10
25.1327  2.41e+07  6.58e+04 -2.40e-08 -2.40e-08 -2.40e-08
31.4159  2.36e+08  6.52e+09 -1.20e-04 -1.20e-04 -1.20e-04
"""
# slightly different to book - why??
