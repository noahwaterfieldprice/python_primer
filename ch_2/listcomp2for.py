# Exercise 2.20
# Author: Noah Waterfield Price

r_list = []
for i in range(5):
    r_list.append(10 ** i)
q1 = []
for r in r_list:
    q1.append(r ** 2)

q2 = [r ** 2 for r in [10 ** i for i in range(5)]]

print q1 == q2

"""
Sample run:
python listcomp2for.py
True
"""
