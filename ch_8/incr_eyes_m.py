# Exercise 8.10
# Author: Noah Waterfield Price

from random import randint


def play_game(n):
    outcomes = [randint(1, 6) for i in range(n)]
    success = False
    for i in range(1, n):
        if outcomes[i] <= outcomes[i - 1]:
            break
        if i == n - 1:
            success = True
    return success


def prob_winning(n, N=1000000):
    M = 0
    for exp in xrange(N):
        M += play_game(n)
    return float(M) / N

m_list = range(2, 6)
p_list = [prob_winning(m) for m in m_list]

print '=' * 29
print '%-3s %-8s %-16s' % ('m', 'p', 'fair game reward')
print '-' * 29
for m, p in zip(m_list, p_list):
    print '%-3d %-8.6f %16.6f' % (m, p, 1 / p)
print '-' * 29

"""
Sample run:
python incr_eyes_m.py
=============================
m   p        fair game reward
-----------------------------
2   0.416359         2.401773
3   0.092347        10.828722
4   0.011559        86.512674
5   0.000803      1245.330012
-----------------------------
"""
