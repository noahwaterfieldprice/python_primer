# Exercise 8.1
# Author: Noah Waterfield Price

from random import randint


def flip_coin(N=100):
    HEADS, TAILS = 1, 2
    n_heads = 0
    for i in xrange(N):
        coin_flip = randint(1, 2)
        if coin_flip == HEADS:
            n_heads += 1
    return n_heads

print '=' * 21
print '%-12s %-8s' % ('Coin flips', 'Heads')
print '-' * 21
for N in [10 ** i for i in range(2, 7)]:
    print '%-12d %-8g' % (N, flip_coin(N))
print '=' * 21

"""
Sample run:
python flip_coin.py
=====================
Coin flips   Heads
---------------------
100          52
1000         517
10000        4853
100000       49888
1000000      499253
=====================
"""
