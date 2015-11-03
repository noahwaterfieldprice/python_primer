# Exercise 5.33
# Author: Noah Waterfield Price

from numpy import *
import matplotlib.pyplot as plt
import sys
from scitools.StringFunction import StringFunction

f = StringFunction(sys.argv[1])
f.vectorize(globals())
x = linspace(eval(sys.argv[2]), eval(sys.argv[3]), 501)

plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['f(x) = %s' % sys.argv[1]])
plt.show()

raw_input()
