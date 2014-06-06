# Exercise 7.35
class Polynomial:

    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        """Evaluate the polynomial."""
        s = 0
        for k in self.coeff:
            s += self.coeff[k] * x ** k
        return s

    def __add__(self, other):
        result_coeff = self.coeff.copy()
        for k in other.coeff:
            result_coeff[k] = result_coeff.get(k, 0) + other.coeff[k]
        # strip out zero coefficients
        result_coeff = {k: c for k, c in result_coeff.items() if c != 0}
        return Polynomial(result_coeff)

    def __sub__(self, other):
        result_coeff = self.coeff.copy()
        for k in other.coeff:
            result_coeff[k] = result_coeff.get(k, 0) - other.coeff[k]
        # strip out zero coefficients
        result_coeff = {k: c for k, c in result_coeff.items() if c != 0}
        return Polynomial(result_coeff)

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        result_coeff = {}
        for i in c:
            for j in d:
                result_coeff[i + j] = result_coeff.get(i+j, 0) + c[i]*d[j]
        return Polynomial(result_coeff)

    def differentiate(self):
        """Differentiate this polynomial in-place."""
        d_coeff = {}
        for k in self.coeff:
            d_coeff[k - 1] = k * self.coeff[k]
        # strip out zero coefficients
        self.coeff = {k: c for k, c in d_coeff.items() if c != 0}

    def derivative(self):
        """Copy this polynomial and return its derivative."""
        dpdx = Polynomial(self.coeff.copy())  # make a copy
        dpdx.differentiate()
        return dpdx

    def __str__(self):
        s = ''
        for k in self.coeff:
            s += ' + %g*x^%d' % (self.coeff[k], k)
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
        for k in self.coeff:
            s += ' + %g*x^%d' % (self.coeff[k], k)
        return s


def _test():
    p1 = Polynomial({1: 1, 100: -3})
    p2 = Polynomial({1: -1, 20: 1, 100: 4})
    p3 = p1 + p2
    print p1, '  +  ', p2, '  =  ', p3
    p4 = p1 * p2
    print p1, '  *  ', p2, '  =  ', p4
    p5 = p2.derivative()
    print 'd/dx', p2, '  =  ', p5
    print 'd/dx', p2,
    p2.differentiate()
    print '  =  ', p5
    p4 = p2.derivative()
    print 'd/dx', p2, '  =  ', p4
    p4.simplestr()

if __name__ == '__main__':
    _test()

"""
Sample run:
python Polynomial_dict2.py
x - 3*x^100   +   -x + x^20 + 4*x^100   =   x^20 + x^100
x - 3*x^100   *   -x + x^20 + 4*x^100   =   -3*x^120 - 12*x^200 - x^2 + x^21 + 7*x^101
d/dx -x + x^20 + 4*x^100   =   -1 + 20*x^19 + 400*x^99
d/dx -x + x^20 + 4*x^100   =   -1 + 20*x^19 + 400*x^99
d/dx -1 + 20*x^19 + 400*x^99   =   39600*x^98 + 380*x^18
"""
