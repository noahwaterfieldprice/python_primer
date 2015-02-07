# Exercise 9.4
import numpy as np


class Polynomial:

    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        """Evaluate the polynomial."""
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i] * x ** i
        return s

    def __add__(self, other):
        # Start with the longest list and add in the other
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]   # copy!
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:]  # copy!
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        result_coeff = np.zeros(M + N + 1)
        for i in range(0, M + 1):
            for j in range(0, N + 1):
                result_coeff[i + j] += c[i] * d[j]
        return Polynomial(result_coeff)

    def differentiate(self):
        """Differentiate this polynomial in-place."""
        for i in range(1, len(self.coeff)):
            self.coeff[i - 1] = i * self.coeff[i]
        del self.coeff[-1]

    def derivative(self):
        """Copy this polynomial and return its derivative."""
        dpdx = Polynomial(self.coeff[:])  # make a copy
        dpdx.differentiate()
        return dpdx

    def __str__(self):
        s = ''
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
        # Fix layout
        s = s.replace('+ -', '- ')
        s = s.replace('x^0', '1')
        s = s.replace(' 1*', ' ')
        s = s.replace('x^1 ', 'x ')
        # s = s.replace('x^1', 'x') # will replace x^100 by x^00
        if s[0:3] == ' + ':  # remove initial +
            s = s[3:]
        if s[0:3] == ' - ':  # fix spaces for initial -
            s = '-' + s[3:]
        return s

    def simplestr(self):
        s = ''
        for i in range(0, len(self.coeff)):
            s += ' + %g*x^%d' % (self.coeff[i], i)
        return s


class Parabola(Polynomial):

    def __init__(self, c0, c1, c2):
        Polynomial.__init__(self, [c0, c1, c2])

    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s


class Line(Parabola):

    def __init__(self, c0, c1):
        Parabola.__init__(self, c0, c1, 0)

p = Parabola(1, 3, 4)
print p(10)
print p.table(0, 10, 10)
print p

"""
Sample run:
python Polynomial_hier.py
431
           0            1
     1.11111       9.2716
     2.22222      27.4198
     3.33333      55.4444
     4.44444      93.3457
     5.55556      141.123
     6.66667      198.778
     7.77778      266.309
     8.88889      343.716
          10          431

1 + 3*x + 4*x^2
"""
