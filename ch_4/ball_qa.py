# Exercise 4.6
# Author: Noah Waterfield Price

g = 9.81
v0 = float(raw_input('v0 = ?\n'))
t = float(raw_input('t = ?\n'))
y = v0 * t - 0.5 * g * t ** 2
print y

"""
Sample run:
python ball_qa.py
v0 = ?
10
t = ?
4
-38.48
"""
