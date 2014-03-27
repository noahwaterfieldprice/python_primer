from scipy.integrate import quad
from scipy import exp, pi, cos, sin, log


def midpointint(f, a, b, n):
    s = 0
    h = (b - a) / float(n)
    for i in range(1, n + 1):
        s += f(a - 0.5 * h + i * h)
    s *= h
    return s

f1 = [exp, 0, log(3)]
f2 = (cos, 0, pi)
f3 = (sin, 0, pi)
f4 = (sin, 0, pi / 2)

functions = [f1, f2, f3, f4]


def verify(f, a, b, n):
    exact = quad(f, a, b)[0]
    approx = midpointint(f, a, b, n)
    error = abs(exact - approx)
    print 'The exact integral of %s(x) between %.5f and %.5f is %.5f. \
           The approximate answer is %.5f giving an error of %.5f' \
        % (f.__name__, a, b, exact, approx, error)

for f in functions:
    verify(f[0], f[1], f[2], 10)

"""
Sample run:
python midpointint.py
The exact integral of exp(x) between 0.00000 and 1.09861 is 2.00000. The approximate answer is 1.99899 giving an error of 0.00101
The exact integral of cos(x) between 0.00000 and 3.14159 is 0.00000. The approximate answer is 0.00000 giving an error of 0.00000
The exact integral of sin(x) between 0.00000 and 3.14159 is 2.00000. The approximate answer is 2.00825 giving an error of 0.00825
The exact integral of sin(x) between 0.00000 and 1.57080 is 1.00000. The approximate answer is 1.00103 giving an error of 0.00103
"""
