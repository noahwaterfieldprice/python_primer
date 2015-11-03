# Exercise 7.33
# Author: Noah Waterfield Price

import numpy as np


class Polynomial:

    def __init__(self, coefficients):
        self.coeff = np.array(coefficients)

    def __call__(self, x):
        """Evaluate the polynomial."""
        indices = np.arange(len(self.coeff))
        return np.inner(self.coeff, x ** indices)

    def __add__(self, other):
        # Start with the longest list and add in the other
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff.copy()   # copy!
            result_coeff[:len(other.coeff)] += other.coeff
        else:
            result_coeff = other.coeff.copy()  # copy!
            result_coeff[:len(self.coeff)] += self.coeff
        return Polynomial(result_coeff)

    def __sub__(self, other):
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]  # copy!
            for i in range(len(other.coeff)):
                result_coeff[i] -= other.coeff[i]
        else:
            #ensures subtraction done in right directions
            result_coeff = [-i for i in other.coeff]  # copy!
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)

    def __mul__(self, other):
        # Not quite vectorised entirely but amount of loops reduced
        c, d = self.coeff, other.coeff
        M, N = len(c), len(d)
        coeff_matrix = np.outer(c, d)
        result_coeff = np.zeros(M + N + 1)
        for i in range(-M + 1, N):
                result_coeff[i+M-1] += coeff_matrix[::-1, :].trace(i)
        return Polynomial(result_coeff)

    def differentiate(self):
        """Differentiate this polynomial in-place."""
        n = len(self.coeff)
        self.coeff[:-1] = np.arange(1, n) * self.coeff[1:]
        self.coeff = self.coeff[:-1]

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


def _test():
    p1 = Polynomial([1, -1])
    p2 = Polynomial([0, 1, 0, 0, -6, -1])
    p3 = p1 + p2
    print p1, '  +  ', p2, '  =  ', p3
    p4 = p1 * p2
    print p1, '  *  ', p2, '  =  ', p4
    print 'p2(3) =', p2(3)
    p5 = p2.derivative()
    print 'd/dx', p2, '  =  ', p5
    print 'd/dx', p2,
    p2.differentiate()
    print '  =  ', p5
    p4 = p2.derivative()
    print 'd/dx', p2, '  =  ', p4

if __name__ == '__main__':
    _test()

"""
Sample run:
python Polynomial_array2.py
1 - x^1   +   x - 6*x^4 - x^5   =   1 - 6*x^4 - x^5
1 - x^1   *   x - 6*x^4 - x^5   =   x - x^2 - 6*x^4 + 5*x^5 + x^6
p2(3) = -726
d/dx x - 6*x^4 - x^5   =   1 - 24*x^3 - 5*x^4
d/dx x - 6*x^4 - x^5   =   1 - 24*x^3 - 5*x^4
d/dx 1 - 24*x^3 - 5*x^4   =   -72*x^2 - 20*x^3
"""
    
