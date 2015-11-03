# Exercise 5.7
# Author: Noah Waterfield Price

import numpy as np

w = np.linspace(0, 3, 31)

print w[:]
print ''
print w[:-2]
print ''
print w[::5]
print ''
print w[2:-2:6]

"""
Sample run:
python slicing.py
[ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.   1.1  1.2  1.3  1.4
  1.5  1.6  1.7  1.8  1.9  2.   2.1  2.2  2.3  2.4  2.5  2.6  2.7  2.8  2.9
  3. ]

[ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.   1.1  1.2  1.3  1.4
  1.5  1.6  1.7  1.8  1.9  2.   2.1  2.2  2.3  2.4  2.5  2.6  2.7  2.8]

[ 0.   0.5  1.   1.5  2.   2.5  3. ]

[ 0.2  0.8  1.4  2.   2.6]
"""
    