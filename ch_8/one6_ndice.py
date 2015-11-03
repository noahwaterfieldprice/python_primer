# Exercise 8.6
# Author: Noah Waterfield Price

from random import randint
import sys


def prob_1six(n, N):
    M = 0  # no. of successes
    for exp in xrange(N):
        for dice in xrange(n):
            outcome = randint(1, 6)
            if outcome == 6:
                M += 1
                break  # at least one 6 rolled

    return float(M) / N

n = int(sys.argv[1])  # no. of dice to roll
N = int(sys.argv[2])  # no. of experiments

print 'Probability of at least one 6 when rolling %d dice:' % n, \
    prob_1six(n, N)

"""
Sample run:
python one6_ndice.py 2 10000000
Probability of at least one 6 when rolling 2 dice: 0.3054462
"""
    
