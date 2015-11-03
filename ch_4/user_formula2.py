# Exercise 4.13
# Author: Noah Waterfield Price

from scitools.StringFunction import StringFunction
from math import *

formula = raw_input('Write a formula involving x: ')
f = StringFunction(formula)
x = 0
while x is not None:
    x = eval(raw_input('Give x (None to quit): '))
    if x is not None:
        print 'f(%g)=%g' % (x, f(x))

"""
Sample run:
python user_formula2.py
Write a formula involving x: sin(x)
Give x (None to quit): pi/2
f(1.5708)=1
Give x (None to quit): pi
f(3.14159)=1.22465e-16
Give x (None to quit): 3*pi/2
f(4.71239)=-1
"""
