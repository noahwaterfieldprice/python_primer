# Exercise 7.28
import numpy as np
import matplotlib.pyplot as plt


class Integral:

    def __init__(self, f, a, n=100):
        self.f = f
        self.a = a
        self.n = n

    def __call__(self, x):
        if isinstance(x, (float, int)):
            return self.trapezoidal_vecsum(self.f, self.a, x, self.n)
        else:
            return self.difference_equation(self.f, self.a, x)

    @staticmethod
    def trapezoidal_vecsum(f, a, x, n):
        h = (x - a) / float(n)
        I = 0.5 * (f(a) + f(x))
        xlist = np.linspace(a + h, x - h, n - 1)
        I += np.sum(f(xlist))
        I *= h
        return I

    @staticmethod
    def difference_equation(f, a, x):
        f_ = f(x)
        F = np.zeros_like(x)
        F[0] = 0
        for k in xrange(1, len(x)):
            F[k] = F[k - 1] + 0.5 * (x[k] - x[k - 1]) * (f_[k - 1] + f_[k])
        return F


def g(t):
    return 1. / np.sqrt(2 * np.pi) * np.exp(-t ** 2)
F = Integral(g, 0)
x = np.linspace(-3, 3, 201)
plt.plot(x, g(x))
plt.plot(x, F(x))
plt.legend(['g(x)', 'F(x)'], loc=2)
plt.show()
