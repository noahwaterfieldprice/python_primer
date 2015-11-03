# Exercise 8.16
# Author: Noah Waterfield Price

import numpy as np

r = np.random.uniform(size=6)

print '%-24s' % 'r:', r
print '%-24s' % 'r <= 0.5:', r <= 0.5
print '%-24s' % 'r[r <= 0.5]:', r[r <= 0.5]
print '%-24s' % 'where(r <= 0.5, 1, 0):', np.where(r <= 0.5, 1, 0)

# how many elements in r are less than or equal to 0.5?
print '%-24s' % 'no. of elements <= 0.5:', np.sum(r <= 0.5)

"""
Sample run:
python bool_vec.py
r:                       [ 0.59375738  0.36512709  0.53113878  0.67508657  0.31524544  0.23286909]
r <= 0.5:                [False  True False False  True  True]
r[r <= 0.5]:             [ 0.36512709  0.31524544  0.23286909]
where(r <= 0.5, 1, 0):   [0 1 0 0 1 1]
no. of elements <= 0.5:  3
"""
