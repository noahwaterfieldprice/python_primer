# Exercise 7.8
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt


class LagrangeInterpolation:

    def __init__(self, xp, yp):
        self.xp = xp
        self.yp = yp

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

# compute some interpolation points along y = sin(x)
xp = np.linspace(0, np.pi, 5)
yp = np.sin(xp)

# Lagrange's interpolation polynomial
p_L = LagrangeInterpolation(xp, yp)
x = 1.2
print 'p_L(%g)=%g' % (x, p_L(x))
print 'sin(%g)=%g' % (x, np.sin(x))

verbose_verify(xp, yp, p_L)
p_L.graph(np.sin, 5, 0, np.pi)

"""
Sample run:
python Lagrange_poly3.py
p_L(1.2)=0.93224
sin(1.2)=0.932039
---------------------------------------------
         x      Exact     Approx   Difference
---------------------------------------------
  0.000000   0.000000   0.000000     0.000000
  0.785398   0.707107   0.707107     0.000000
  1.570796   1.000000   1.000000     0.000000
  2.356194   0.707107   0.707107     0.000000
  3.141593   0.000000   0.000000     0.000000
---------------------------------------------
"""
