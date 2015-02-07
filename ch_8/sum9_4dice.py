# Exercise 8.8
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
r = int(sys.argv[1])  # prize for winning game round
N = int(sys.argv[2])  # no. of experiments

p = prob_winning(N)

print 'Probability of winning the game: p =', p
print 'Cost of playing game: q =', q
print 'Prize for winning game: r =', r

if abs(r - q / p) < 1E-3:
    print "\nr = q/p therefore the game is fair"
elif r < q / p:
    print "\nr < q/p therefore the game is not fair (in house's favour)"
elif r > q / p:
    print "\nr < q/p therefore the game is not fair (in player's favour)"

"""
Sample run:
python sum9_4dice.py 10 1000000
Probability of winning the game: p = 0.054221
Cost of playing game: q = 1
Prize for winning game: r = 10

r < q/p therefore the game is not fair (in house's favour)
"""
