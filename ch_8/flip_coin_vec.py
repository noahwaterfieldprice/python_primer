# Exercise 8.17
# Author: Noah Waterfield Price

import numpy as np

N = 10000000
flips = np.random.randint(2, size=N)
print 'Coin flipped %d times, number of tails: %d' % (N, np.sum(flips))

"""
Sample run:
python flip_coin_vec.py
Coin flipped 10000000 times, number of tails: 4996557
"""
