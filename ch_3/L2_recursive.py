def L(x, n):
    term = x / (1. + x)
    s = term
    for i in range(2, n + 1):
        # recursive relation between ci and c(i-1)
        term *= (i - 1.) / i * x / (1. + x)
        s += term
    value_of_sum = s
    first_neglected_term = term * n / (n + 1.) * x / (1. + x)
    from math import log
    exact_error = log(1 + x) - value_of_sum
    return value_of_sum, first_neglected_term, exact_error


def table(x):
    from math import log
    print '\nx=%g, ln(1+x)=%g' % (x, log(1 + x))
    for n in [1, 2, 10, 100, 500]:
        value, next, error = L(x, n)
        print 'n=%-4d %-10g  (next term: %8.2e  '\
              'error: %8.2e)' % (n, value, next, error)

table(10)
table(100)
table(1000)


def L2(x, epsilon=1.0E-6):
    term = x / (1. + x)
    s = term
    i = 1
    while abs(term) > epsilon:
        i += 1
        # recursive relation between ci and c(i-1)
        term *= (i - 1.) / i * x / (1. + x)
        s += term
    return s, i

print '\n\n'
from math import log
x = 10
for k in range(4, 14, 2):
    epsilon = 10 ** (-k)
    approx, n = L2(x, epsilon=epsilon)
    exact = log(1 + x)
    exact_error = exact - approx
    print 'epsilon: %5.0e, exact error: %8.2e, n=%d' % \
          (epsilon, exact_error, n)

"""
Sample run:
python L2_recursive.py

x=10, ln(1+x)=2.3979
n=1    0.909091    (next term: 4.13e-01  error: 1.49e+00)
n=2    1.32231     (next term: 2.50e-01  error: 1.08e+00)
n=10   2.17907     (next term: 3.19e-02  error: 2.19e-01)
n=100  2.39789     (next term: 6.53e-07  error: 6.59e-06)
n=500  2.3979      (next term: 3.65e-24  error: 5.77e-15)

x=100, ln(1+x)=4.61512
n=1    0.990099    (next term: 4.90e-01  error: 3.63e+00)
n=2    1.48025     (next term: 3.24e-01  error: 3.13e+00)
n=10   2.83213     (next term: 8.15e-02  error: 1.78e+00)
n=100  4.39574     (next term: 3.62e-03  error: 2.19e-01)
n=500  4.61395     (next term: 1.37e-05  error: 1.18e-03)

x=1000, ln(1+x)=6.90875
n=1    0.999001    (next term: 4.99e-01  error: 5.91e+00)
n=2    1.498       (next term: 3.32e-01  error: 5.41e+00)
n=10   2.919       (next term: 8.99e-02  error: 3.99e+00)
n=100  5.08989     (next term: 8.95e-03  error: 1.82e+00)
n=500  6.34928     (next term: 1.21e-03  error: 5.59e-01)



epsilon: 1e-04, exact error: 8.18e-04, n=55
epsilon: 1e-06, exact error: 9.02e-06, n=97
epsilon: 1e-08, exact error: 8.70e-08, n=142
epsilon: 1e-10, exact error: 9.20e-10, n=187
"""
