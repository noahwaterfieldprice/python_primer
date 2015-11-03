# Exercise 7.27
# Author: Noah Waterfield Price

import numpy as np
import time


class Integral:

    def __init__(self, f, a, n=100):
        self.f = f
        self.a = a
        self.n = n

    def __call__(self, x):
        return self.vecsum_integrate(self, x)

    def scalar_integrate(self, x):
        return self.trapezoidal_scalar(self.f, self.a, x, self.n)

    def vec_integrate(self, x):
        return self.trapezoidal_vec(self.f, self.a, x, self.n)

    def vecsum_integrate(self, x):
        return self.trapezoidal_vecsum(self.f, self.a, x, self.n)

    @staticmethod
    def trapezoidal_scalar(f, a, x, n):
        h = (x - a) / float(n)
        I = 0.5 * (f(a) + f(x))
        for i in xrange(1, n):
            I += f(a + i * h)
        I *= h
        return I

    @staticmethod
    def trapezoidal_vec(f, a, x, n):
        h = (x - a) / float(n)
        I = 0.5 * (f(a) + f(x))
        xlist = np.linspace(a + h, x - h, n - 1)
        I += sum(f(xlist))
        I *= h
        return I

    @staticmethod
    def trapezoidal_vecsum(f, a, x, n):
        h = (x - a) / float(n)
        I = 0.5 * (f(a) + f(x))
        xlist = np.linspace(a + h, x - h, n - 1)
        I += np.sum(f(xlist))
        I *= h
        return I


def f(x):
    return np.exp(-x ** 2) * np.sin(10 * x)
F = Integral(f, 0, 2000000)

t0 = time.time()
F.scalar_integrate(100)
t1 = time.time()
F.vec_integrate(100)
t2 = time.time()
F.vecsum_integrate(100)
t3 = time.time()

print '=' * 43
print '%-28s %14s' % ('Integration method', 'Time taken (s)')
print '-' * 43
for s, t in zip(['Scalar', 'Vectorized', 'Vectorized + numpy.sum()'],
                [t1 - t0, t2 - t1, t3 - t2]):
    print '%-28s %14g' % (s, t)
print '=' * 43

"""
Sample run:
python Integral_vec.py
===========================================
Integration method           Time taken (s)
-------------------------------------------
Scalar                              12.1405
Vectorized                         0.781012
Vectorized + numpy.sum()          0.0828331
===========================================
"""
