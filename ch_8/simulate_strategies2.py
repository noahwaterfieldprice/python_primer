# Exercise 8.12
# Author: Noah Waterfield Price

import random


class Dice:

    def __init__(self, n=1):
        self.n = n   # no of dice

    def throw(self):
        return [random.randint(1, 6)
                for i in range(self.n)]


class Player:

    def __init__(self, name, capital, guess_function, ndice):
        self.name = name
        self.capital = capital
        self.guess_function = guess_function
        self.dice = Dice(ndice)

    def play_one_round(self):
        self.guess = self.guess_function(self.dice.n)
        self.throw = sum(self.dice.throw())
        if self.guess == self.throw:
            self.capital += self.guess
        else:
            self.capital -= 1

# Guessing strategies


def computer_guess(ndice):
    # Any of the outcomes (sum) is equally likely
    return random.randint(ndice, 6 * ndice)


def player_guess_3(ndice):
    return 12


def player_guess_50(ndice):
    return 3500


def play(nrounds, ndice=2):
    if ndice == 3:
        player = Player('YOU', nrounds, player_guess_3, ndice)
    elif ndice == 50:
        player = Player('YOU', nrounds, player_guess_50, ndice)
    computer = Player('Computer', nrounds, computer_guess, ndice)

    for i in range(nrounds):
        player.play_one_round()
        computer.play_one_round()
        if player.capital == 0 or computer.capital == 0:
            break  # terminate game

    if computer.capital > player.capital:
        winner = 'Machine'
    else:
        winner = 'You'
    return winner

if __name__ == '__main__':
    N = 1000  # no. of games
    for n in (3, 50):
        M = 0  # no. of machine wins
        for game in range(N):
            winner = play(nrounds=10, ndice=n)
            M += (winner == 'Machine')
        print 'Machine won %5.2f%% of games' % (float(M) / N * 100)

"""
Sample run:
python simulate_strategies2.py
Machine won 26.76% of games
Machine won  2.60% of games
"""
