# Exercise 8.3
# Author: Noah Waterfield Price

from random import choice


def random_color():
    colors = ('red', 'blue', 'yellow', 'purple',
              'green', 'orange', 'black', 'white')
    return choice(colors)

for i in range(5):
    print random_color()

"""
Sample run:
python choose_color.py
orange
blue
yellow
white
black
"""
