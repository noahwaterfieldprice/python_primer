# Exercise 3.7
# Author: Noah Waterfield Price

from scipy.integrate import quad
from scipy import exp, pi, cos, sin, log


def trapezint(f, a, b, n):
    s = (f(a) + f(b)) / 2
    h = (b - a) / float(n)
    for i in range(1, n):
        s += f(a + i * h)
    s *= h
    return s

f1 = [exp, 0, log(3)]
f2 = (cos, 0, pi)
f3 = (sin, 0, pi)
f4 = (sin, 0, pi / 2)

functions = [f1, f2, f3, f4]


def verify(f, a, b, n):
    exact = quad(f, a, b)[0]
    approx = trapezint(f, a, b, n)
    error = abs(exact - approx)
    print 'The exact integral of %s between %.5f and %.5f is %.5f. \
           The approximate answer is %.5f giving an error of %.5f' \
        % (f.__name__, a, b, exact, approx, error)

for f in functions:
    verify(f[0], f[1], f[2], 10)

"""
Sample run:
python trapezint.py
The exact integral of exp between 0.00000 and 1.09861 is 2.00000. The approximate answer is 2.00201 giving an error of 0.00201
The exact integral of cos between 0.00000 and 3.14159 is 0.00000. The approximate answer is 0.00000 giving an error of 0.00000
The exact integral of sin between 0.00000 and 3.14159 is 2.00000. The approximate answer is 1.98352 giving an error of 0.01648
The exact integral of sin between 0.00000 and 1.57080 is 1.00000. The approximate answer is 0.99794 giving an error of 0.00206
"""
