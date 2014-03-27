from numpy import *
import matplotlib.pyplot as plt
import sys
from scitools.StringFunction import StringFunction

f = StringFunction(sys.argv[1])
f.vectorize(globals())

if len(sys.argv) == 5:
    n = sys.argv[4]
else:
    n = 501

x = linspace(eval(sys.argv[2]), eval(sys.argv[3]), n)

plt.plot(x, f(x))
plt.show()

raw_input()
