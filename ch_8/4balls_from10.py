# Exercise 8.4
# Author: Noah Waterfield Price

from random import randint


def new_hat():
    hat = []
    for color in ('red', 'blue', 'yellow', 'purple'):
        for i in range(10):
            hat.append(color)
    return hat


def draw_ball(hat):
    index = randint(0, len(hat) - 1)
    color = hat.pop(index)
    return color, hat


n = 10    # no. of balls to be drawn
N = 500000  # no. of experiments to be performed

# Run experiments
M = 0     # no. of sucesses
for e in xrange(N):
    hat = new_hat()
    balls = []  # balls drawn from hat
    for i in xrange(n):
        color, hat = draw_ball(hat)
        balls.append(color)
    if balls.count('blue') == 2 and balls.count('purple') == 2:
        M += 1

print 'Probability:', float(M)/N

"""
Sample run:
python 4balls_from10.py
Probability: 0.092486
"""
    