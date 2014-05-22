import numpy as np
import matplotlib.pyplot as plt


class InverseFunction:

    def __init__(self, f, x):
        self.values = self.compute_inverse(f, x)

    def __call__(self, x):
        pass

    @staticmethod
    def Newton(f, x, dfdx, epsilon=1.0E-7, N=100):
        f_value = f(x)
        n = 0
        while abs(f_value) > epsilon and n <= N:
            dfdx_value = float(dfdx(x))
            x = x - f_value / dfdx_value
            n += 1
            f_value = f(x)
        return x, n, f_value

    @classmethod
    def compute_inverse(cls, f, x):
        g = np.zeros(len(x))
        for i in range(len(x)):
            xi = x[i]
            F_xi = F(f, xi)
            dFdx_xi = dFdx(F_xi)
            # Compute start value (use last g[i-1] if possible)
            if i == 0:
                gamma0 = x[0]
            else:
                gamma0 = g[i - 1]
            gamma, n, F_value = cls.Newton(F_xi, gamma0, dFdx_xi)
            g[i] = gamma
        return g


class F:

    def __init__(self, f, xi):
        self.f = f
        self.xi = xi

    def __call__(self, gamma):
        f, xi = self.f, self.xi
        return f(gamma) - xi


class dFdx:

    def __init__(self, F, h=1E-6):
        self.F = F
        self.h = h

    def __call__(self, gamma):
        F, h = self.F, self.h
        return (F(gamma + h) - F(gamma - h)) / (2 * h)


def f(x):
    return np.log(x)
x = np.linspace(1, 3, 101)
f_inv = InverseFunction(f, x)
plt.plot(x, f(x))
plt.plot(x, f_inv.values)
plt.title('InverseFunction')
plt.legend(['Original', 'Inverse'], loc=2)
plt.show()
