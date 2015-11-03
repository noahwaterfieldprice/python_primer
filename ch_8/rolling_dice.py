# Exercise 8.5
# Author: Noah Waterfield Price

from random import randint


def roll_die(success, N):
    M = 0  # no. of successes
    for roll in xrange(N):
        outcome = randint(1, 6)
        if outcome == success:
            M += 1
    return M


def prob_six(N=1000):
    return roll_die(6, N) / float(N)


def prob_four_sixes(N=1000):
    P = 0  # no. of four sixes in a row
    for exp in xrange(N):
        sixes = roll_die(6, 4)
        if sixes == 4:
            P += 1
    return P / float(N)


def prob_fourth_six(N=1000):
    P = 0  # no. of three sixes in a row
    L = 0  # no. of sixes on fourth roll after three sixes in a row
    for exp in xrange(N):
        sixes = roll_die(6, 3)
        if sixes == 3:
            P += 1
            fourth_six = roll_die(6, 1)
            if fourth_six == 1:
                L += 1
    return L / float(P)

print 'Probability of getting a six:', prob_six(1000000)
print 'Exact probability: 0.166666667\n'
print 'Probability of getting four sixes in a row:', prob_four_sixes(1000000)
print 'Exact probability: 0.00077160493827\n'
print 'Probability of getting a six after rolling three sixes in a row:', \
    prob_fourth_six(1000000)
print 'Exact probability: 0.166666667\n'

"""
Sample run:
python rolling_dice.py
Probability of getting a six: 0.166749
Exact probability: 0.166666667

Probability of getting four sixes in a row: 0.000817
Exact probability: 0.00077160493827

Probability of getting a six after rolling three sixes in a row: 0.166811657242
Exact probability: 0.166666667
"""

