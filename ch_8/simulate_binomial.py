# Exercise 8.25
# Author: Noah Waterfield Price

import numpy as np
from scipy.misc import factorial as fact


def binomial(x, n, p):
    B = float(fact(n)) / (fact(x) * fact(n - x)) * \
        p ** x * (1 - p) ** (n - x)
    return B


def simulate_binomial(p, n, x, N=1000):
    r = np.random.rand(N, n)
    outcomes = np.sum(np.where(r <= p, 1, 0), axis=1)
    p_approx = np.sum(outcomes == x) / float(N)
    p_exact = binomial(x, n, p)
    return p_approx, abs(p_approx - p_exact)


print 'What is the probability of gettinger two heads when \
flipping a coin 5 times?'
p, error = simulate_binomial(0.5, 5, 2)
print 'p = %.5f (error: %.5f)\n' % (p, error)
print 'What is the probability of getting fours ones in a rown when \
throwing a die?'
p, error = simulate_binomial(1./6, 4, 4)
print 'p = %.5f (error: %.5f)\n' % (p, error)
print 'What is the probability that a skier will experience a ski \
break during five\n competitions in a world championship?'
p, error = simulate_binomial(1./120, 5, 0)
print 'p = %.5f (error: %.5f)\n' % (1 - p, error)

"""
Sample run:
python simulate_binomial.py
What is the probability of gettinger two heads when flipping a coin 5 times?
p = 0.30600 (error: 0.00650)

What is the probability of getting fours ones in a rown when throwing a die?
p = 0.00000 (error: 0.00077)

What is the probability that a skier will experience a ski break during five
 competitions in a world championship?
p = 0.05300 (error: 0.01202)
"""
