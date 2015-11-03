# Exercise 7.21
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt
import operator


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


H1 = Heaviside()
x1, y1 = H1.plot(-3, 4)
H2 = Heaviside(eps=0.8)
x2, y2 = H2.plot(-3, 4)
fig, ax = plt.subplots(2, sharex=True)
ax[0].plot(x1, y1)
ax[0].set_title('eps = 0')
ax[1].plot(x2, y2)
ax[1].set_title('eps = 0.8')
ax[0].set_ylim([-0.5, 1.5])
ax[1].set_ylim([-0.5, 1.5])
plt.show()
