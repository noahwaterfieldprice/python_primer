# Exercise 8.19
# Author: Noah Waterfield Price

import numpy as np

N = 10000000
rolls = np.random.randint(1, 7, size=(N, 7))
sixes = np.sum(rolls == 6, axis=1)
seven_sixes = np.sum(sixes == 7)
print '7 dice rolled %d times - number of times all dice = 6: %d' \
    % (N, seven_sixes)

"""
Sample run:
python roll_7dice.py
7 dice rolled 10000000 times - number of times all dice = 6: 36
"""
