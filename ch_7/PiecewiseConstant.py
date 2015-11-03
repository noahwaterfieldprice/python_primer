# Exercise 7.25
# Author: Noah Waterfield Price

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


class Indicator:

    def __init__(self, a, b, eps=None):
        self.a = a
        self.b = b
        self.eps = eps
        # use Heaviside class rather than static functions, allows array args
        self.H = Heaviside(eps)

    def __call__(self, x):
        a, b = self.a, self.b
        return self.H(x - a) * self.H(b - x)

    def plot(self, xmin, xmax):
        a, b = self.a, self.b
        if self.eps is None:
            x = np.array([xmin, a, a, b, b, xmax])
            y = np.array([0, 0, 1, 1, 0, 0])
        else:
            a, b, e = self.a, self.b, self.eps
            lowlim = np.linspace(a - e, a + e, 201)
            upplim = np.linspace(b - e, b + e, 201)
            x = np.concatenate(
                (np.array([xmin]), lowlim, upplim, np.array([xmax])))
            y = self(x)
        return x, y


class Heaviside:

    def __init__(self, eps=None):
        self.eps = eps

    def __call__(self, x):
        if isinstance(x, (float, int)):
            return self.heaviside_scalar(x, self.eps)
        else:
            return self.heaviside_vec(x, self.eps)

    def plot(self, xmin, xmax):
        if self.eps is None:
            x = np.array([xmin, 0, 0, xmax])
            y = np.array([0, 0, 1, 1])
        else:
            e = self.eps
            xmid = np.linspace(-e, e, 201)
            x = np.concatenate((np.array([xmin]), xmid, np.array([xmax])))
            y = self(x)
        return x, y

    @staticmethod
    def heaviside_scalar(x, eps):
        if eps is None:
            if x < 0:
                return 0
            elif x >= 0:
                return 1
        else:
            e = eps
            if x < -e:
                return 0
            elif -e <= x <= e:
                return 0.5 + x / (2 * e) + \
                    1 / (2 * np.pi) * np.sin(np.pi * x / e)
            elif x > e:
                return 1

    @staticmethod
    def heaviside_vec(x, eps):
        r = np.zeros(len(x))
        if eps is None:
            r[x < 0] = 0.0
            r[x >= 0] = 1.0
            return r
        else:
            e = eps
            cond = operator.and_(-e <= x, x <= e)
            r = np.zeros(len(x))
            r[x < -e] = 0.0
            r[cond] = 0.5 + x[cond] / (2 * e) + \
                1 / (2 * np.pi) * np.sin(np.pi * x[cond] / e)
            r[x > e] = 1.0
            return r


def _test():
    PC = PiecewiseConstant([(0.4, 1), (0.2, 1.5), (0.1, 3)], xmax=4)
    I, I_s = Indicator(-3, 5), Indicator(-3, 5, eps=1)
    H, H_s = Heaviside(), Heaviside(eps=1)
    ax1 = plt.subplot(311)
    ax2, ax3 = plt.subplot(323),  plt.subplot(324)
    ax4, ax5 = plt.subplot(325),  plt.subplot(326)

    x, y = PC.plot()
    ax1.plot(x, y)
    ax1.set_ylim([0, 0.5])
    ax1.set_title('PiecewiseConstant')
    titles = ['Indicator', 'Indicator (eps=1)',
              'Heaviside', 'Heaviside (eps=1)']
    for f, ax, title in zip([I, I_s, H, H_s], [ax2, ax3, ax4, ax5], titles):
        x, y = f.plot(-6, 8)
        ax.plot(x, y)
        ax.set_ylim([-0.5, 1.5])
        ax.set_title(title)
    for ax in [ax2, ax3]:
        plt.setp(ax.get_xticklabels(), visible=False)
    plt.show()


if __name__ == '__main__':
    _test()
