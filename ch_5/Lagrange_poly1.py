import numpy as np


def L_k(x, k, xp, yp):
    ans = 1
    # if x > xp[-1]:
    #   raise ValueError('x out of range of function domain')
    for i in range(len(xp)):
        if i != k:
            ans *= (x - xp[i]) / (xp[k] - xp[i])
    return ans


def p_L(x, xp, yp):
    ans = 0
    # if x > xp[-1]:
    #   raise ValueError('x out of range of function domain')
    for k in range(len(yp)):
        ans += yp[k] * L_k(x, k, xp, yp)
    return ans


def verify(xp, yp):
    status = 'Verified!'
    for k in range(len(xp)):
        if abs(p_L(xp[k], xp, yp) - yp[k]) > 1e-15:
            status = 'Error!'
            break
    print status


def verbose_verify(xp, yp):
    verify(xp, yp)
    print '%10s %10s %10s %10s' % ('x', 'Exact', 'Approx', 'Difference')
    for k in range(len(xp)):
        x = xp[k]
        exact = yp[k]
        approx = p_L(xp[k], xp, yp)
        diff = abs(p_L(xp[k], xp, yp) - yp[k])
        print '%10f %10f %10f %10f' % (x, exact, approx, diff)

xlist = np.linspace(0, np.pi, 5)
ylist = np.sin(xlist)

if __name__ == '__main__':
    verify(xlist, ylist)
    verbose_verify(xlist, ylist)

"""
Sample run:
python Lagrange_poly1.py
Verified!
         x      Exact     Approx Difference
  0.000000   0.000000   0.000000   0.000000
  0.785398   0.707107   0.707107   0.000000
  1.570796   1.000000   1.000000   0.000000
  2.356194   0.707107   0.707107   0.000000
  3.141593   0.000000   0.000000   0.000000
"""
