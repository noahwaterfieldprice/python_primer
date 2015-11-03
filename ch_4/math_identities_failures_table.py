# Exercise 4.23
# Author: Noah Waterfield Price

from math_identities_failures_cml import equal

idents = [
    ('a - b', '-(b - a)'),
    ('a/b', '1/(b/a)'),
    ('(a*b)**4', 'a**4*b**4'),
    ('(a + b)**2', '(a**2 + 2*a*b + b**2)'),
    ('(a + b)*(a - b)', 'a**2 - b**2'),
    ('exp(a + b)', 'exp(a)*exp(b)'),
    ('log(a**b)', 'b*log(a)'),
    ('log(a*b)', 'log(a) + log(b)'),
    ('a*b', 'exp(log(a) + log(b))'),
    ('1/(1/a + 1/b)', 'a*b/(a + b)'),
    ('a*(sin(b)**2 + cos(b)**2)', 'a'),
    ('sinh(a + b)', '0.5*(exp(a)*exp(b) - exp(-a)*exp(-b))'),
    ('tan(a + b)', 'sin(a + b)/cos(a + b)'),
    ('sin(a + b)', 'sin(a)*cos(b) + sin(b)*cos(a)')
]

A = 1E-7
B = 2E-7

print '%55s %20s' % ('Expressions', 'Failure Rate')
for i in xrange(len(idents)):
    failure_rate = equal(idents[i][0], idents[i][1], A, B)
    expressions = idents[i][0] + ' and ' + idents[i][1]
    print '%55s %20g%%' % (expressions, failure_rate)
