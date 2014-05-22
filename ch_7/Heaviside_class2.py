# Exercise 7.20
import numpy as np
import operator


class Heaviside:

    def __init__(self, eps=None):
        self.eps = eps

    def __call__(self, x):
        if isinstance(x, (float, int)):
            return self.heaviside_scalar(x, self.eps)
        else:
            return self.heaviside_vec(x, self.eps)

    @staticmethod
    def heaviside_scalar(x, eps):
        if eps is None:
            if x < 0:
                return 0
            elif x >= 0:
                return 1
        else:
            e = eps
            if x < -e:
                return 0
            elif -e <= x <= e:
                return 0.5 + x / (2 * e) + \
                    1 / (2 * np.pi) * np.sin(np.pi * x / e)
            elif x > e:
                return 1

    @staticmethod
    def heaviside_vec(x, eps):
        r = np.zeros(len(x))
        if eps is None:
            r[x < 0] = 0.0
            r[x >= 0] = 1.0
            return r
        else:
            e = eps
            cond = operator.and_(-e <= x, x <= e)
            r = np.zeros(len(x))
            r[x < -e] = 0.0
            r[cond] = 0.5 + x[cond] / (2 * e) + \
                1 / (2 * np.pi) * np.sin(np.pi * x[cond] / e)
            r[x > e] = 1.0
            return r


H = Heaviside()
x = np.linspace(-1, 1, 11)
print H(x)
H = Heaviside(eps=0.8)
print H(x)

"""
Sample run:
python Heaviside_class2.py
[ 0.  0.  0.  0.  0.  1.  1.  1.  1.  1.  1.]
[  0.00000000e+00  -1.94908592e-17   1.24604605e-02   9.08450569e-02
   2.62460460e-01   5.00000000e-01   7.37539540e-01   9.09154943e-01
   9.87539540e-01   1.00000000e+00   1.00000000e+00]
"""
