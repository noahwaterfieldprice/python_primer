# Exercise 8.2
# Author: Noah Waterfield Price

from random import random


def compute_prob(N):
    M = 0
    for j in range(N):
        r = random()
        if 0.5 <= r < 0.6:
            M += 1
    return M / float(N)

print '=' * 24
print '%-12s %-8s' % ('N', 'Probability')
print '-' * 24
for N in [10 ** i for i in (1, 2, 3, 6)]:
    print '%-12d %-12g' % (N, compute_prob(N))
print '=' * 24

"""
Sample run:
python
========================
N            Probability
------------------------
10           0.1
100          0.13
1000         0.089
1000000      0.100765
========================
"""
