# Exercise 3.18
# Author: Noah Waterfield Price

roots = [-1, 1, 2]


def poly(roots, x):
    p = 1
    for i in range(len(roots)):
        p *= (x - roots[i])
    return p

print poly(roots, 3)

"""
Sample run:
python polyprod.py
8
"""
