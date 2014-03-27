from Lagrange_poly2 import graph, plt


def f(x):
    return abs(x)

for n in [2, 4, 6, 10]:
    graph(f, n + 1, -2, 2)
plt.show()

for n in [13, 20]:
    graph(f, n + 1, -2, 2)
plt.show()
