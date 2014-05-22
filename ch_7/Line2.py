# Exercise 7.5
class Line2:

    def __init__(self, p1, p2):
        if isinstance(p1, (tuple, list)) and isinstance(p2, (tuple, list)):
            # p1 and p2 are both points
            x1, y1 = p1
            x2, y2 = p2
            self.c = float(x2 * y1 - x1 * y2) / (x2 - x1)
            self.m = float(y2 - y1) / (x2 - x1)
        elif isinstance(p1, (tuple, list)) and isinstance(p2, (float, int)):
            # p1 is a point and p2 is slope
            x1, y1 = p1
            self.c = y1 - p2 * x1
            self.m = p2
        elif isinstance(p1, (float, int)) and isinstance(p2, (float, int)):
            # p1 is y-intercept and p2 is slope
            self.c = p1
            self.m = p2

    def value(self, x):
        return self.m * x + self.c

print '2 points: Line2((0, -1), (2, 4))'
lineA = Line2((0, -1), (2, 4))
print lineA.value(0.5), lineA.value(0), lineA.value(1)
print '\nA point and a slope: Line2((0, -1), 2.5)'
lineB = Line2((0, -1), 2.5)
print lineA.value(0.5), lineA.value(0), lineA.value(1)
print '\nA y-intercept and a slope: Line2(-1, 2.5)'
lineC = Line2(-1, 2.5)
print lineA.value(0.5), lineA.value(0), lineA.value(1)

"""
Sample run:
python Line2.py
2 points: Line2((0, -1), (2, 4))
0.25 -1.0 1.5

A point and a slope: Line2((0, -1), 2.5)
0.25 -1.0 1.5

A y-intercept and a slope: Line2(-1, 2.5)
0.25 -1.0 1.5
"""
