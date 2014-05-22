# Exercise 7.9
import numpy as np
import matplotlib.pyplot as plt


class LagrangeInterpolation:

    def __init__(self, arg1, arg2, arg3=None):
        if isinstance(arg1, np.ndarray) and isinstance(arg2, np.ndarray):
            self.xp = arg1
            self.yp = arg2
        elif callable(arg1) and isinstance(arg2, (list, tuple)) \
                and isinstance(arg3, int):
            f, x, n = arg1, arg2, arg3
            self.xp = np.linspace(x[0], x[1], n)
            self.yp = f(self.xp)

    def __call__(self, x):
        xp, yp = self.xp, self.yp
        ans = 0
        for k in range(len(yp)):
            ans += yp[k] * self.L_k(x, k)
        return ans

    def L_k(self, x, k):
        xp = self.xp
        ans = 1
        for i in range(len(xp)):
            if i != k:
                ans *= (x - xp[i]) / (xp[k] - xp[i])
        return ans

    def graph(self, f, n, xmin, xmax, resolution=1001):
        xlist = np.linspace(xmin, xmax, n)
        ylist = f(xlist)
        xlist_fine = np.linspace(xmin, xmax, resolution)
        ylist_fine = self(xlist_fine)
        plt.plot(xlist, ylist, 'ro')
        plt.plot(xlist_fine, ylist_fine)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend(['f(x)', 'Interpolated'])
        plt.show()


# function to verify accuracy of interpolation at interpolation points
def verbose_verify(xp, yp, p_L):
    print '-' * 45
    print '%10s %10s %10s %12s' % ('x', 'Exact', 'Approx', 'Difference')
    print '-' * 45
    for k in range(len(xp)):
        x = xp[k]
        exact = yp[k]
        approx = p_L(xp[k])
        diff = abs(p_L(xp[k]) - yp[k])
        print '%10f %10f %10f %12f' % (x, exact, approx, diff)
    print '-' * 45


def myfunction(x):
    return np.exp(-x / 2.0) * np.sin(x)

# Lagrange's interpolation polynomial
p_L = LagrangeInterpolation(myfunction, [0, np.pi], 11)
x = 1.2
print 'p_L(%g)=%g' % (x, p_L(x))
print 'sin(%g)=%g' % (x, np.sin(x))

verbose_verify(p_L.xp, p_L.yp, p_L)
p_L.graph(myfunction, 5, 0, np.pi)

"""
Sample run:
python Lagrange_poly4.py
p_L(1.2)=0.511514
sin(1.2)=0.932039
---------------------------------------------
         x      Exact     Approx   Difference
---------------------------------------------
  0.000000   0.000000   0.000000     0.000000
  0.314159   0.264097   0.264097     0.000000
  0.628319   0.429320   0.429320     0.000000
  0.942478   0.505011   0.505011     0.000000
  1.256637   0.507377   0.507377     0.000000
  1.570796   0.455938   0.455938     0.000000
  1.884956   0.370590   0.370590     0.000000
  2.199115   0.269418   0.269418     0.000000
  2.513274   0.167289   0.167289     0.000000
  2.827433   0.075165   0.075165     0.000000
  3.141593   0.000000   0.000000     0.000000
---------------------------------------------
"""
