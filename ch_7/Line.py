# Exercise 7.4
# Author: Noah Waterfield Price

class Line:

    def __init__(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        self.m = float(y2 - y1)/(x2 - x1)
        self.c = float(x2*y1 - x1*y2)/(x2 - x1)

    def value(self, x):
        return self.m*x + self.c

line = Line((0, -1), (2, 4))
print line.value(0.5), line.value(0), line.value(1)


"""
Sample run:
python Line.py
0.25 -1.0 1.5
"""
