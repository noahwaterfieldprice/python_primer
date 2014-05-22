# Exercise 7.24
import numpy as np
import matplotlib.pyplot as plt
import operator


class PiecewiseConstant:

    def __init__(self, data, xmax):
        self.data = data + [(None, xmax)]

    def __call__(self, x):
        if isinstance(x, (float, int)):
            return self.piecewise(x, self.data)
        else:
            return self.piecewise_vec(x, self.data)

    def plot(self):
        data = self.data
        # create lists of points to exactly reproduce discontinuities
        x = [data[0][1]]
        y = [data[0][0], data[0][0]]
        for i in range(1, len(data) - 1):
            x.append(data[i][1])
            x.append(data[i][1])
            y.append(data[i][0])
            y.append(data[i][0])
        x.append(data[-1][1])
        return x, y

    @staticmethod
    def piecewise(x, data):
        for i in range(len(data) - 1):
            if data[i][1] <= x < data[i + 1][1] or x == data[-1][1]:
                return data[i][0]

    @staticmethod
    def piecewise_vec(x, data):
        r = np.zeros(len(x))
        for i in xrange(len(data) - 1):
            cond = operator.and_(data[i][1] <= x, x < data[i + 1][1])
            cond = operator.or_(cond, x == data[-1][1])
            r[cond] = data[i][0]
        return r


f = PiecewiseConstant([(0.4, 1), (0.2, 1.5), (0.1, 3)], xmax=4)
x, y = f.plot()
plt.plot(x, y)
# set appropriate y limits
range = max(y) - min(y)
plt.ylim([min(y) - 0.1 * range, max(y) + 0.1 * range])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Piecewise constant function')
plt.show()
