# Exercise 3.21
# Author: Noah Waterfield Price

from math import cos, sin, pi


def kinematics(x, y, t, dt=1E-6):
    v = (x(t + dt) - x(t - dt)) / (2 * dt), (y(t + dt) - y(t - dt)) / (2 * dt)
    a = (x(t + dt) - 2 * x(t) + x(t - dt)) / \
        dt ** 2, (y(t + dt) - 2 * y(t) + y(t - dt)) / dt ** 2
    r = x(t), y(t)
    return r, v, a

t = 1
R = 1
w = 2 * pi
x = lambda t: R * w * cos(w * t)
y = lambda t: R * sin(w * t)

print kinematics(x, y, t, dt=1E-5)

"""
Sample run:
python kinematics2.py
((6.283185307179586, -2.4492935982947064e-16), (0.0, 6.283185303064565), (-248.05022036389343, 8.88164867172969e-06))
"""
