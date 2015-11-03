# Exercise 8.23
# Author: Noah Waterfield Price

import numpy as np

N = 10000000
flips = np.random.randint(2, size=N)

print '%5s %15s' % ('N1', 'Prob. of heads')
for N1 in (10, 100, 500, 1000):
    print '%5d %15.2f' % (N1, np.sum(flips[:N1]) / float(N1))

"""
Sample run:
python flip_coin_prob.py
   N1  Prob. of heads
   10            0.20
  100            0.45
  500            0.48
 1000            0.50
"""
