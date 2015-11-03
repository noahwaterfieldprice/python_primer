# Exercise 7.18
# Author: Noah Waterfield Price

import numpy as np


class Derivative:

    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x + h) - f(x)) / h


class VelocityProfile:

    def __init__(self, beta, mu0, R, r):
        self.beta = beta
        self.mu0 = mu0
        self.R = R
        self.r = r

    def __call__(self, n):
        beta, mu0, R, r = self.beta, self.mu0, self.R, self.r
        v = (beta / (2.0 * mu0)) ** (1 / n) * (n / (n + 1)) * \
            ((R ** (1 + 1 / n)) - r ** (1 + 1 / n))
        return v

    def exact_derivative(self, n):
        beta, mu0, R, r = self.beta, self.mu0, self.R, self.r
        dv_dn = (beta / (2.0 * mu0)) ** (1 / n) * (1 / (n * (n + 1) ** 2)) * \
            ((R ** (1 + 1 / n)) *
                (n - (1 + n) * np.log((r * beta) / (2 * mu0)))
             - (r ** (1 + 1 / n)) *
             (n - (1 + n) * np.log((r * beta) / (2 * mu0))))
        return dv_dn

v = VelocityProfile(50, 1, 1, 2)
dv_dn = Derivative(v)

print '=' * 50
print '%-6s %-14s %-15s %-15s' \
    % ('r', "f' (exact)", "f' (approx.)", 'Error')
print '-' * 50
for r in np.linspace(0.1, 1, 10):
    exact, approx = v.exact_derivative(r), dv_dn(r)
    error = exact - approx
    print '%-4.1f | %11.6E   %11.6E   %13.6E' \
        % (r, exact, approx, error)
print '=' * 50 + '\n'

"""
Sample run:
python VelocityProfile_deriv.py
==================================================
r      f' (exact)     f' (approx.)    Error
--------------------------------------------------
0.1  | 6.781335E+18   6.768312E+18    1.302363E+16
0.2  | 9.601133E+09   9.624330E+09   -2.319684E+07
0.3  | 8.262245E+06   8.341441E+06   -7.919668E+04
0.4  | 2.087092E+05   2.125473E+05   -3.838107E+03
0.5  | 2.087569E+04   2.145130E+04   -5.756119E+02
0.6  | 4.212970E+03   4.367005E+03   -1.540356E+02
0.7  | 1.280682E+03   1.338467E+03   -5.778508E+01
0.8  | 5.057201E+02   5.326066E+02   -2.688651E+01
0.9  | 2.386649E+02   2.531473E+02   -1.448239E+01
1.0  | 1.279509E+02   1.366113E+02   -8.660478E+00
==================================================
"""
