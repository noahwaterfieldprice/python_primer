# Exercise 3.20
# Author: Noah Waterfield Price

from math import exp


def kinematics(x, t, dt=1E-6):
    v = (x(t + dt) - x(t - dt)) / (2 * dt)
    a = (x(t + dt) - 2 * x(t) + x(t - dt)) / dt ** 2
    x = x(t)
    return x, v, a

x = lambda t: exp(-(t - 4) ** 2)

print kinematics(x, 5, 1E-5)

"""
Sample run:
python kinematics1.py
(0.36787944117144233, -0.7357588822892723, 0.7357586762068989)
"""
