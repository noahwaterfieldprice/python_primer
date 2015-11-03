# Exercise 7.30
# Author: Noah Waterfield Price

class Polynomial:

    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        return sum([c * x ** i for i, c in enumerate(self.coeff)])

    def __add__(self, other):
        # incorrect code was missing .coeff inside len(self) and len(other)
        maxlength = max(len(self.coeff), len(other.coeff))
        # Extend both lists with zeros to this maxlength
        self.coeff += [0] * (maxlength - len(self.coeff))
        other.coeff += [0] * (maxlength - len(other.coeff))
        result_coeff = self.coeff
        for i in range(maxlength):
            result_coeff[i] += other.coeff[i]
        return Polynomial(result_coeff)


P1 = Polynomial([2, 0,  3, 4, 1, 5])
P2 = Polynomial([3, 0, 2, 8])
P3 = P1 + P2
print P3.coeff

"""
Sample run:
python Polynomial_error.py
[5, 0, 5, 12, 1, 5]
"""
