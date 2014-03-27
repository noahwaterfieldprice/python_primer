import numpy as np
import matplotlib.pyplot as plt
colorset = [
    '#d6604d', '#2166ac', '#1a9850', '#762a83', '#c51b7d', '#01665e',
    '#ec7014', '#878787', '#8c510a', '#543005', '#4d4d4d', '#993404',
    '#003c30', '#8e0152', '#40004b', '#006837', '#053061', '#67001f']


def viz_rect(f, a, b, n, N):
    h = (b - a) / float(n)
    data = []
    for i in range(1, n + 1):
        for j in range(50):
            data.append(f(a + (i - 0.5) * h))

    x = np.linspace(a, b, n * N)
    plt.plot(x, f(x), linewidth=2, color=colorset[-1])
    plt.plot(x, data, color=colorset[-2], linestyle='--')
    for i in range(n):
        plt.plot([h * i, h * i], [0, data[i * N]],
                 color=colorset[-2], linestyle='--')

    plt.fill_between(x, f(x), data, color=colorset[1])
    plt.show()


def f(x):
    return 0.5 * x * (12 - x) + np.sin(2.5 * np.pi * x)

a = 0    # xmax
b = 6    # xmin
n = 3   # segments
N = 50   # points per segment

viz_rect(f, a, b, n, N)
