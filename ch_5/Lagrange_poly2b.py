# Exercise 5.16
# Author: Noah Waterfield Price

from Lagrange_poly2 import graph, plt


def f(x):
    return abs(x)

for n in [2, 4, 6, 10]:
    graph(f, n + 1, -2, 2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['n = 2', 'n = 4', 'n = 6', 'n = 8', 'n = 10'])
plt.show()

for n in [13, 20]:
    graph(f, n + 1, -2, 2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['n = 13', 'n = 20'])
plt.show()
