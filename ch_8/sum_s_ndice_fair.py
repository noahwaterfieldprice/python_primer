# Exercise 8.9
from random import randint
import sys


def play_game(n):
    outcomes = [randint(1, 6) for i in range(n)]
    success = sum(outcomes) < 9
    return success


def prob_winning(N=100000, n=4):
    M = 0
    for exp in xrange(N):
        M += play_game(n)
    return float(M) / N


q = 1  # cost of playing game
r = float(sys.argv[1])  # prize for winning game round
n = int(sys.argv[2])  # no. of dice per game
N = int(sys.argv[3])  # no. of experiments

p = prob_winning(N)

print 'Probability of winning the game: p =', p
print 'Cost of playing game: q =', q
print 'Prize for winning game: r =', r
print 'Net profit per game is: s = ', p*r - q

if abs(r - q / p) < 1E-3:
    print "\nr = q/p therefore the game is fair"
elif r < q / p:
    print "\nr < q/p therefore the game is not fair (in house's favour)"
elif r > q / p:
    print "\nr < q/p therefore the game is not fair (in player's favour)"

"""
Sample run:
python sum_s_ndice_fair.py
python ch_8/sum_s_ndice_fair.py 18.59 4 1000000
Probability of winning the game: p = 0.053796
Cost of playing game: q = 1
Prize for winning game: r = 18.59
Net profit per game is: s =  6.76399999999e-05

r = q/p therefore the game is fair
"""
    