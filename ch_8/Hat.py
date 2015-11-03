# Exercise 8.21
# Author: Noah Waterfield Price

from random import randint


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

    def draw(self, number_of_balls=1):
        balls = []
        for ball in range(number_of_balls):
            index = randint(0, len(self.balls) - 1)
            ball = self.balls.pop(index)
            balls.append(ball)
        return balls


if __name__ == '__main__':
    hat = Hat(colors=('red', 'blue', 'yellow', 'purple'), number_of_each_color=10)
    N = 500000  # no. of experiments to be performed
    # Run experiments
    M = 0     # no. of sucesses
    for e in xrange(N):
        balls = hat.draw(number_of_balls=10)
        if balls.count('blue') == 2 and balls.count('purple') == 2:
            M += 1
        hat.reset_hat()

    print 'Probability:', float(M)/N

"""
Sample run:
python Hat.py
Probability: 0.092738
"""
    