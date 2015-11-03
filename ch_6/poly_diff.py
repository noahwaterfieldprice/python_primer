# Exercise 6.17
# Author: Noah Waterfield Price

def diff(p):
    dp = {}
    for index, coeff in p.iteritems():
        if index != 0:
            dp[index - 1] = index*coeff
    return dp

p = {0: -3, 3: 2, 5: -1}
print diff(p)

"""
Sample run:
python poly_diff.py
{2: 6, 4: -5}
"""
