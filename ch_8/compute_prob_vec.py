# Exercise 8.18
# Author: Noah Waterfield Price

import numpy as np
import operator as op

N = 10000000
r = np.random.uniform(size=N)
condition = op.and_(0.5 <= r, r <= 0.6)

print r[condition].size

"""
Sample run:
python compute_prob_vec.py
999802
"""
