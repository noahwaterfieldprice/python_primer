# Exercise 3.17
# Author: Noah Waterfield Price

from scipy.integrate import quad
from scipy import exp, pi, cos, log, sqrt


def diff2(f, x, h=1E-6):
    r = (f(x - h) - 2 * f(x) + f(x + h)) / (h ** 2)
    return r


def adaptive_trapezint(f, a, b, eps=1E-4):
    ddf = []
    for i in range(101):
        ddf.append(abs(diff2(f, a + i * (b - a) / 100)))
    max_ddf = max(ddf)
    h = sqrt(12 * eps) * 1 / sqrt((b - a) * max_ddf)
    n = (b - a) / h
    s = (f(a) + f(b)) / 2
    for i in range(1, int(n)):
        s += f(a + i * h)
    s *= h
    return s


f1 = [exp, 0, log(3)]
f2 = (cos, 0, pi)

functions = [f1, f2]


def verify(f, a, b, n):
    exact = quad(f, a, b)[0]
    approx = adaptive_trapezint(f, a, b)
    error = abs(exact - approx)
    print 'The exact integral of %s between %.5f and %.5f is %.5f.\
     The approximate answer is %.5f giving an error of %.5f' \
        % (f.__name__, a, b, exact, approx, error)

for f in functions:
    verify(f[0], f[1], f[2], 10)

"""
Sample run:
python adaptive_trapezint.py
The exact integral of exp between 0.00000 and 1.09861 is 2.00000. The approximate answer is 1.96771 giving an error of 0.03229
The exact integral of cos between 0.00000 and 3.14159 is 0.00000. The approximate answer is 0.01467 giving an error of 0.01467
"""
