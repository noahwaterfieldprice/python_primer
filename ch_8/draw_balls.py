# Exercise 8.14
# Author: Noah Waterfield Price

from random import randint
from math import sqrt


class Hat:

    def __init__(self, colors, number_of_each_color):
        self.colors = colors
        if isinstance(number_of_each_color, int):
            self.number_of_each_color = [number_of_each_color] * len(colors)
        else:
            self.number_of_each_color = number_of_each_color
        self.reset_hat()

    def reset_hat(self):
        self.balls = []
        for color, n in zip(self.colors, self.number_of_each_color):
            for ball in range(n):
                self.balls.append(color)

    def draw_ball(self):
        index = randint(0, len(self.balls) - 1)
        ball = self.balls.pop(index)
        return ball


class Game:

    def __init__(self, hat, player):
        self.hat = hat
        self.player = player

    def play_game(self):
        hat, player = self.hat, self.player
        player.money -= 2 * player.n  # subtract cost of game
        for draw in range(player.n):  # draw n balls
            player.balls.append(hat.draw_ball())
        win, prize = player.option(player.balls)
        player.wins += win
        player.money += prize
        hat.reset_hat()  # reset hat
        player.balls = []  # resent player balls


class Player:

    def __init__(self, n, option):
        self.n = n  # no. of balls to pick from hat
        self.option = option  # prize option
        self.wins = 0
        self.money = 0
        self.balls = []


# prize options player can choose from
# each option returns True/False for win/lose and the amount won
def option1(balls):
    if balls.count('red') == 3:
        return True, 60
    else:
        return False, 0


def option2(balls):
    if balls.count('brown') >= 3:
        return True, 7 + 5 * sqrt(len(balls))
    else:
        return False, 0


def option3(balls):
    if all([balls.count(color) == 1
            for color in ('yellow', 'brown')]):
        return True, len(balls) ** 3 - 26
    else:
        return False, 0


def option4(balls):
    if all([balls.count(color) >= 1
            for color in ('red', 'yellow', 'green', 'brown')]):
        return True, 23
    else:
        return False, 0

# simulate games and store results
options = {'option1': option1, 'option2': option2,
           'option3': option3, 'option4': option4}
N = 100000  # no. of games to simulate
n_list = range(4, 11)
win_probabilities = {option: {} for option in options}
income_per_play = {option: {} for option in options}

hat = Hat(['red', 'yellow', 'green', 'brown'], [5, 5, 3, 7])
for option in options:
    for n in n_list:
        player = Player(n, options[option])
        game = Game(hat, player)
        for i in range(N):
            game.play_game()
        win_probabilities[option][n] = player.wins / float(N)
        income_per_play[option][n] = player.money / float(N)

# print results
print '=' * 98
header = '%28s' % '|'
header += '%10s' * 7 % tuple(n_list)
print header
for option in ('option1', 'option2', 'option3', 'option4'):
    print '-' * 98
    s1 = '%-10s %-17s' % (option.capitalize(), 'Income per play |')
    s2 = '%-10s %-17s' % (' ', 'Win probability |')
    for n in n_list:
        s1 += '%10.2f' % income_per_play[option][n]
        s2 += '%10.2f' % win_probabilities[option][n]
    print s1 + '\n' + s2
print '=' * 98

"""
Sample run:
python draw_balls.py
==================================================================================================
                           |         4         5         6         7         8         9        10
--------------------------------------------------------------------------------------------------
Option1    Income per play |     -6.15     -5.95     -4.89     -3.44     -1.78      0.07      1.06
           Win probability |      0.03      0.07      0.12      0.18      0.24      0.30      0.35
--------------------------------------------------------------------------------------------------
Option2    Income per play |     -6.26     -6.19     -5.51     -4.42     -3.07     -2.00     -1.19
           Win probability |      0.10      0.21      0.34      0.47      0.61      0.73      0.82
--------------------------------------------------------------------------------------------------
Option3    Income per play |     -0.31      2.47      0.03     -6.21    -12.09    -16.78    -19.73
           Win probability |      0.20      0.13      0.06      0.02      0.01      0.00      0.00
--------------------------------------------------------------------------------------------------
Option4    Income per play |     -5.54     -3.74     -1.88     -0.60      0.18      0.28     -0.19
           Win probability |      0.11      0.27      0.44      0.58      0.70      0.79      0.86
==================================================================================================
"""
