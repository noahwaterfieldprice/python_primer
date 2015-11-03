# Exercise 4.22
# Author: Noah Waterfield Price

from math import *
import sys
import random
_filename = sys.argv[0]
_usage = """
Usage: python %s exp(a+b) exp(a)*exp(b) -100 100 500
Takes two equivalent expressions involving a and b and
tests their equivalence. Returning the percentage of
failures.
""" % _filename


def equal(expr1, expr2, A, B, n=500):
    failures = n
    for x in xrange(n):
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        if eval(expr1) == eval(expr2):
            failures -= 1
    failure_rate = float(failures) / n * 100
    return failure_rate


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print _usage
        raise IndexError('Two expressions involving a and b and range limits '
                         'must be given on the command-line. Number '
                         'of repetitions may also be given.')
    expr1 = sys.argv[1]
    expr2 = sys.argv[2]
    A = float(sys.argv[3])
    B = float(sys.argv[4])

    if len(sys.argv) == 6:
        n = int(sys.argv[5])
        equal(expr1, expr2, A, B, n)
    else:
        equal(expr1, expr2, A, B)

"""
Sample run:
python math_identities_failures_cml.py \(a*b\)**3 a**3*b**3 -100 100 800
(a*b)**3 and a**3*b**3 - Failure rate = 67.38%
python math_identities_failures_cml.py a/b 1/\(b/a\) -100 100 800
a/b and 1/(b/a) - Failure rate = 25.25%
"""
